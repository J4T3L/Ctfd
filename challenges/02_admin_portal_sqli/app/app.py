import os
import sqlite3
from flask import Flask, request, render_template, redirect, url_for, flash, g

app = Flask(__name__)
app.secret_key = "easy_sqli_portal_secret_key_2026"

DATABASE = 'database.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def init_db():
    # Read flag from flag.txt or /flag.txt
    flag_val = "CTF{34sy_sql_1nj3ct10n_byp4ss_2026}"
    for path in ['/flag.txt', 'flag.txt', '../flag.txt']:
        if os.path.exists(path):
            try:
                with open(path, 'r') as f:
                    flag_val = f.read().strip()
                break
            except Exception:
                pass

    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("DROP TABLE IF EXISTS users")
        cursor.execute("""
            CREATE TABLE users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                password TEXT NOT NULL,
                role TEXT NOT NULL,
                flag TEXT NOT NULL
            )
        """)
        # Insert admin user with strong random password
        cursor.execute("""
            INSERT INTO users (username, password, role, flag) 
            VALUES ('admin', 'SuperComplexPassword987!#$', 'Administrator', ?)
        """, (flag_val,))
        conn.commit()

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username', '')
    password = request.form.get('password', '')

    if not username or not password:
        flash("Username and password are required!", "error")
        return redirect(url_for('index'))

    # VULNERABLE SQL QUERY (Direct string formatting without parameterization)
    query = f"SELECT id, username, role, flag FROM users WHERE username = '{username}' AND password = '{password}'"
    
    try:
        db = get_db()
        cursor = db.cursor()
        user = cursor.execute(query).fetchone()

        if user:
            return render_template('dashboard.html', user=user, query_used=query)
        else:
            flash("Invalid credentials! Username or password incorrect.", "error")
            return render_template('login.html', query_used=query)
    except sqlite3.Error as e:
        flash(f"Database SQL Error: {str(e)}", "error")
        return render_template('login.html', query_used=query)

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=8000, debug=False)
else:
    init_db()
