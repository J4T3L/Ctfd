import React, { useState, useEffect } from 'react';
import { KeyRound, ShieldAlert } from 'lucide-react';

export default function JwtPage() {
  const [content, setContent] = useState('');

  const fetchJwtPage = async () => {
    try {
      const res = await fetch('/jwt_lab/');
      const text = await res.text();
      setContent(text);
    } catch (err) {
      setContent('JWT Error');
    }
  };

  useEffect(() => {
    fetchJwtPage();
  }, []);

  return (
    <div className="page-container">
      <div style={{ marginBottom: '2rem' }}>
        <span className="badge badge-hard">HARD • 400 PTS • JWT WEAK SECRET</span>
        <h1 style={{ fontSize: '2rem', fontWeight: '800', color: '#fff', marginTop: '0.5rem' }}>
          OAuth Session & JWT Token Inspector
        </h1>
        <p style={{ color: 'var(--text-muted)' }}>
          Session token inspector. Manipulate <code>jwt_auth</code> cookie using weak secret <code>secret123</code> or algorithm <code>none</code>.
        </p>
      </div>

      <div className="glass-card">
        <div className="code-block" dangerouslySetInnerHTML={{ __html: content }} />
      </div>
    </div>
  );
}
