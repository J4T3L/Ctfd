import os
import sqlite3
from flask import Blueprint, request, render_template, redirect, url_for, flash, g

sqli_bp = Blueprint('sqli', __name__, template_folder='../templates/sqli', url_prefix='/sqli')

DATABASE = 'sqli_database.db'

def get_db():
    db = getattr(g, '_sqli_database', None)
    if db is None:
        db = g._sqli_database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db

def init_sqli_db():
    flag_val = "CTF{34sy_sql_1nj3ct10n_byp4ss_2026}"
    for path in ['/flag_sqli.txt', 'flag_sqli.txt', 'flag.txt', '/flag.txt']:
        if os.path.exists(path):
            try:
                with open(path, 'r') as f:
                    content = f.read().strip()
                    if '34sy' in content or 'sqli' in content:
                        flag_val = content
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
        cursor.execute("""
            INSERT INTO users (username, password, role, flag) 
            VALUES ('admin', 'SuperComplexPassword987!#$', 'Administrator', ?)
        """, (flag_val,))
        conn.commit()

@sqli_bp.route('/')
def index():
    return render_template('sqli/login.html')

@sqli_bp.route('/login', methods=['POST'])
def login():
    username = request.form.get('username', '')
    password = request.form.get('password', '')

    if not username or not password:
        flash("Username and password are required!", "error")
        return redirect(url_for('sqli.index'))

    # VULNERABLE SQL QUERY
    query = f"SELECT id, username, role, flag FROM users WHERE username = '{username}' AND password = '{password}'"
    
    try:
        db = get_db()
        cursor = db.cursor()
        user = cursor.execute(query).fetchone()

        if user:
            return render_template('sqli/dashboard.html', user=user, query_used=query)
        else:
            flash("Invalid credentials! Username or password incorrect.", "error")
            return render_template('sqli/login.html', query_used=query)
    except sqlite3.Error as e:
        flash(f"Database SQL Error: {str(e)}", "error")
        return render_template('sqli/login.html', query_used=query)
