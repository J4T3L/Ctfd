import React, { useState, useEffect } from 'react';
import { Ticket } from 'lucide-react';

export default function CookiePage() {
  const [content, setContent] = useState('');

  const fetchCookiePage = async () => {
    try {
      const res = await fetch('/cookie_lab/');
      const text = await res.text();
      setContent(text);
    } catch (err) {
      setContent('Cookie Error');
    }
  };

  useEffect(() => {
    fetchCookiePage();
  }, []);

  return (
    <div className="page-container">
      <div style={{ marginBottom: '2rem' }}>
        <span className="badge badge-easy">EASY • 100 PTS • COOKIE MANIPULATION</span>
        <h1 style={{ fontSize: '2rem', fontWeight: '800', color: '#fff', marginTop: '0.5rem' }}>
          Cookie Session Manager
        </h1>
        <p style={{ color: 'var(--text-muted)' }}>
          Session role determined by <code>user_session</code> HTTP Cookie. Change Base64 value from <code>role=guest</code> to <code>role=admin</code> (<code>cm9sZT1hZG1pbg==</code>).
        </p>
      </div>

      <div className="glass-card">
        <div className="code-block" dangerouslySetInnerHTML={{ __html: content }} />
      </div>
    </div>
  );
}
