import React, { useState, useEffect } from 'react';
import { Cpu } from 'lucide-react';

export default function PicklePage() {
  const [content, setContent] = useState('');

  const fetchPicklePage = async () => {
    try {
      const res = await fetch('/pickle_rce/');
      const text = await res.text();
      setContent(text);
    } catch (err) {
      setContent('Pickle Error');
    }
  };

  useEffect(() => {
    fetchPicklePage();
  }, []);

  return (
    <div className="page-container">
      <div style={{ marginBottom: '2rem' }}>
        <span className="badge badge-hard">HARD • 500 PTS • PYTHON PICKLE RCE</span>
        <h1 style={{ fontSize: '2rem', fontWeight: '800', color: '#fff', marginTop: '0.5rem' }}>
          Microservice State Cache Deserializer
        </h1>
        <p style={{ color: 'var(--text-muted)' }}>
          Python pickle session cache inspector. Inject base64 encoded pickle object with <code>__reduce__</code> RCE payload into <code>pickle_session</code> cookie.
        </p>
      </div>

      <div className="glass-card">
        <div className="code-block" dangerouslySetInnerHTML={{ __html: content }} />
      </div>
    </div>
  );
}
