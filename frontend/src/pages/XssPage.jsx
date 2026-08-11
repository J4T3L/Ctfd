import React, { useState } from 'react';
import { Search } from 'lucide-react';

export default function XssPage() {
  const [query, setQuery] = useState('<script>alert(1)</script>');
  const [result, setResult] = useState('');

  const handleSearch = async (e) => {
    e.preventDefault();
    try {
      const res = await fetch(`/xss_reflected/?q=${encodeURIComponent(query)}`);
      const text = await res.text();
      setResult(text);
    } catch (err) {
      setResult('Search Error');
    }
  };

  return (
    <div className="page-container">
      <div style={{ marginBottom: '2rem' }}>
        <span className="badge badge-easy">EASY • 100 PTS • REFLECTED XSS</span>
        <h1 style={{ fontSize: '2rem', fontWeight: '800', color: '#fff', marginTop: '0.5rem' }}>
          SIEM Threat Search Engine
        </h1>
        <p style={{ color: 'var(--text-muted)' }}>
          Real-time threat log query engine. Reflected parameter input without HTML sanitization.
        </p>
      </div>

      <div className="glass-card">
        <form onSubmit={handleSearch}>
          <div className="form-group">
            <label className="form-label">Search Query Payload</label>
            <input 
              type="text" 
              className="form-input" 
              value={query} 
              onChange={(e) => setQuery(e.target.value)} 
              required 
            />
          </div>

          <button type="submit" className="btn-primary">
            Execute Search Query 🔍
          </button>
        </form>

        {result && (
          <div style={{ marginTop: '1.5rem' }}>
            <div className="code-block" dangerouslySetInnerHTML={{ __html: result }} />
          </div>
        )}
      </div>
    </div>
  );
}
