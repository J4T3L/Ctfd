import React, { useState } from 'react';
import { Terminal, Zap } from 'lucide-react';

export default function RcePage() {
  const [ip, setIp] = useState('127.0.0.1; cat flag.txt');
  const [output, setOutput] = useState('');
  const [loading, setLoading] = useState(false);

  const handlePing = async (e) => {
    e.preventDefault();
    setLoading(true);
    try {
      const bodyData = new URLSearchParams();
      bodyData.append('ip', ip);

      const res = await fetch('/rce_ping/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        body: bodyData
      });

      const text = await res.text();
      setOutput(text);
    } catch (err) {
      setOutput('Ping Execution Failed');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="page-container">
      <div style={{ marginBottom: '2rem' }}>
        <span className="badge badge-medium">MEDIUM • 300 PTS • COMMAND INJECTION</span>
        <h1 style={{ fontSize: '2rem', fontWeight: '800', color: '#fff', marginTop: '0.5rem' }}>
          Ping Diagnostic Utility
        </h1>
        <p style={{ color: 'var(--text-muted)' }}>
          Network host diagnostic utility. Inject command separators like <code>;</code> or <code>&&</code> to execute shell commands.
        </p>
      </div>

      <div className="glass-card">
        <form onSubmit={handlePing}>
          <div className="form-group">
            <label className="form-label">Target Host IP / Command Input</label>
            <input 
              type="text" 
              className="form-input" 
              value={ip} 
              onChange={(e) => setIp(e.target.value)} 
              required 
            />
          </div>

          <button type="submit" className="btn-primary" disabled={loading}>
            {loading ? 'Executing Ping...' : 'Execute Ping Diagnostic ⚡'}
          </button>
        </form>

        {output && (
          <div style={{ marginTop: '1.5rem' }}>
            <div className="code-block" dangerouslySetInnerHTML={{ __html: output }} />
          </div>
        )}
      </div>
    </div>
  );
}
