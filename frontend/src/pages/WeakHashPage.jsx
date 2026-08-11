import React, { useState } from 'react';
import { KeyRound, Lock, CheckCircle2, ShieldAlert } from 'lucide-react';

export default function WeakHashPage() {
  const [password, setPassword] = useState('password123');
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setResult(null);

    try {
      const bodyData = new URLSearchParams();
      bodyData.append('password', password);

      const res = await fetch('/weak_hash/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        body: bodyData
      });

      const text = await res.text();
      if (text.includes('CTF{')) {
        const flagMatch = text.match(/CTF\{[A-Za-z0-9_]+\}/);
        setResult({ success: true, flag: flagMatch ? flagMatch[0] : 'Flag Revealed!' });
      } else {
        setResult({ success: false, message: 'Invalid Password Hash. Access Denied.' });
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
        <span className="badge badge-medium">MEDIUM • 200 PTS • MD5 HASH CRACKING</span>
        <h1 style={{ fontSize: '2rem', fontWeight: '800', color: '#fff', marginTop: '0.5rem' }}>
          Legacy MD5 Password Cracking
        </h1>
        <p style={{ color: 'var(--text-muted)' }}>
          Admin password is stored as legacy MD5 hash. Crack the MD5 hash <code>e10adc3949ba59abbe56e057f20f883e</code> to authenticate.
        </p>
      </div>

      <div className="glass-card" style={{ maxWidth: '540px' }}>
        <form onSubmit={handleSubmit}>
          <div className="form-group">
            <label className="form-label">Admin Password</label>
            <input 
              type="password" 
              className="form-input" 
              placeholder="e.g. password123" 
              value={password} 
              onChange={(e) => setPassword(e.target.value)} 
              required 
            />
          </div>

          <button type="submit" className="btn-primary" style={{ width: '100%', justifyContent: 'center' }} disabled={loading}>
            {loading ? 'Checking Hash...' : 'Submit & Check MD5 Hash 🔑'}
          </button>
        </form>

        {result && (
          <div style={{ marginTop: '1.5rem' }}>
            {result.success ? (
              <div className="alert-box alert-success">
                <CheckCircle2 size={20} />
                <div>
                  <div style={{ fontWeight: '700' }}>MD5 Hash Cracked Successfully!</div>
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
