import React, { useState } from 'react';
import { KeyRound, Lock, ShieldAlert, CheckCircle2 } from 'lucide-react';

export default function SqliPage() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setResult(null);

    try {
      const bodyData = new URLSearchParams();
      bodyData.append('username', username);
      bodyData.append('password', password);

      const res = await fetch('/sqli/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        body: bodyData
      });

      const text = await res.text();
      if (text.includes('CTF{')) {
        const flagMatch = text.match(/CTF\{[A-Za-z0-9_]+\}/);
        setResult({ success: true, flag: flagMatch ? flagMatch[0] : 'Flag Revealed!' });
      } else {
        setResult({ success: false, message: 'Invalid Staff Credentials. Authentication Denied.' });
      }
    } catch (err) {
      setResult({ success: false, message: 'Server Connection Error.' });
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="page-container">
      <div style={{ marginBottom: '2rem' }}>
        <span className="badge badge-easy">EASY • 100 PTS • SQL INJECTION</span>
        <h1 style={{ fontSize: '2rem', fontWeight: '800', color: '#fff', marginTop: '0.5rem' }}>
          Staff Portal Authentication
        </h1>
        <p style={{ color: 'var(--text-muted)' }}>
          DevNotes internal staff authentication gateway. Audit the username input field for SQL Injection authentication bypass.
        </p>
      </div>

      <div className="glass-card" style={{ maxWidth: '540px' }}>
        <form onSubmit={handleSubmit}>
          <div className="form-group">
            <label className="form-label">Username / Staff ID</label>
            <input 
              type="text" 
              className="form-input" 
              placeholder="e.g. admin' --" 
              value={username} 
              onChange={(e) => setUsername(e.target.value)} 
              required 
            />
          </div>

          <div className="form-group">
            <label className="form-label">Password</label>
            <input 
              type="password" 
              className="form-input" 
              placeholder="••••••••" 
              value={password} 
              onChange={(e) => setPassword(e.target.value)} 
            />
          </div>

          <button type="submit" className="btn-primary" style={{ width: '100%', justifyContent: 'center' }} disabled={loading}>
            {loading ? 'Authenticating...' : 'Authenticate Staff Account 🔒'}
          </button>
        </form>

        {result && (
          <div style={{ marginTop: '1.5rem' }}>
            {result.success ? (
              <div className="alert-box alert-success">
                <CheckCircle2 size={20} />
                <div>
                  <div style={{ fontWeight: '700' }}>Authentication Bypass Successful!</div>
                  <div style={{ fontFamily: 'var(--font-code)', fontSize: '1.1rem', marginTop: '0.4rem', background: '#040711', padding: '0.6rem', borderRadius: '6px' }}>
                    {result.flag}
                  </div>
                </div>
              </div>
            ) : (
              <div className="alert-box alert-danger">
                <ShieldAlert size={20} />
                <div>{result.message}</div>
              </div>
            )}
          </div>
        )}
      </div>
    </div>
  );
}
