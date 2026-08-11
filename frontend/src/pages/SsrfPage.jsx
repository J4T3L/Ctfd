import React, { useState } from 'react';
import { Globe, ShieldAlert } from 'lucide-react';

export default function SsrfPage() {
  const [url, setUrl] = useState('http://127.0.0.1:8000/ssrf/internal/admin/secret');
  const [content, setContent] = useState('');
  const [loading, setLoading] = useState(false);

  const handleFetch = async (e) => {
    e.preventDefault();
    setLoading(true);
    try {
      const bodyData = new URLSearchParams();
      bodyData.append('url', url);

      const res = await fetch('/ssrf/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        body: bodyData
      });

      const text = await res.text();
      setContent(text);
    } catch (err) {
      setContent('SSRF Fetch Error');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="page-container">
      <div style={{ marginBottom: '2rem' }}>
        <span className="badge badge-hard">HARD • 350 PTS • SSRF</span>
        <h1 style={{ fontSize: '2rem', fontWeight: '800', color: '#fff', marginTop: '0.5rem' }}>
          URL Content Fetcher & Webhook Engine
        </h1>
        <p style={{ color: 'var(--text-muted)' }}>
          Server-side asset ingestion engine. Exploit SSRF to access the internal admin endpoint <code>http://127.0.0.1:8000/ssrf/internal/admin/secret</code>.
        </p>
      </div>

      <div className="glass-card">
        <form onSubmit={handleFetch}>
          <div className="form-group">
            <label className="form-label">Target URL to Fetch</label>
            <input 
              type="text" 
              className="form-input" 
              value={url} 
              onChange={(e) => setUrl(e.target.value)} 
              required 
            />
          </div>

          <button type="submit" className="btn-primary" disabled={loading}>
            {loading ? 'Fetching...' : 'Fetch Remote URL 🌐'}
          </button>
        </form>

        {content && (
          <div style={{ marginTop: '1.5rem' }}>
            <div className="code-block" dangerouslySetInnerHTML={{ __html: content }} />
          </div>
        )}
      </div>
    </div>
  );
}
