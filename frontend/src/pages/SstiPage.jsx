import React, { useState } from 'react';
import { FileText, Zap, ShieldAlert, CheckCircle2 } from 'lucide-react';

export default function SstiPage() {
  const [template, setTemplate] = useState("{{ self.__init__.__globals__.__builtins__.open('/flag.txt').read() }}");
  const [output, setOutput] = useState('');
  const [loading, setLoading] = useState(false);

  const handlePreview = async (e) => {
    e.preventDefault();
    setLoading(true);
    setOutput('');

    try {
      const bodyData = new URLSearchParams();
      bodyData.append('template', template);
      bodyData.append('report_name', 'Security Audit');
      bodyData.append('auditor', 'SecOps');
      bodyData.append('status', 'PASSED');

      const res = await fetch('/ssti/preview', {
        method: 'POST',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        body: bodyData
      });

      const text = await res.text();
      setOutput(text);
    } catch (err) {
      setOutput('Render Error');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="page-container">
      <div style={{ marginBottom: '2rem' }}>
        <span className="badge badge-hard">HARD • 500 PTS • JINJA2 SSTI</span>
        <h1 style={{ fontSize: '2rem', fontWeight: '800', color: '#fff', marginTop: '0.5rem' }}>
          CyberVault Audit Report Generator
        </h1>
        <p style={{ color: 'var(--text-muted)' }}>
          Custom Jinja2 Template Engine. Bypass WAF keyword restrictions to execute Server-Side Template Injection and read <code>/flag.txt</code>.
        </p>
      </div>

      <div className="glass-card">
        <form onSubmit={handlePreview}>
          <div className="form-group">
            <label className="form-label">Jinja2 Template Definition</label>
            <textarea 
              className="form-textarea" 
              value={template} 
              onChange={(e) => setTemplate(e.target.value)} 
              required 
            />
          </div>

          <button type="submit" className="btn-primary" disabled={loading}>
            {loading ? 'Rendering...' : 'Render Audit Report Preview ⚡'}
          </button>
        </form>

        {output && (
          <div style={{ marginTop: '2rem' }}>
            <h4 style={{ color: 'var(--text-muted)', marginBottom: '0.8rem', fontSize: '0.85rem', textTransform: 'uppercase' }}>Rendered Output Preview</h4>
            <div className="code-block" dangerouslySetInnerHTML={{ __html: output }} />
          </div>
        )}
      </div>
    </div>
  );
}
