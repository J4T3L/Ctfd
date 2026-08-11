import React, { useState } from 'react';
import { FileText, ShieldAlert } from 'lucide-react';

export default function XxePage() {
  const [xmlData, setXmlData] = useState('<?xml version="1.0"?>\n<!DOCTYPE test [ <!ENTITY xxe SYSTEM "file:///flag.txt"> ]>\n<data>&xxe;</data>');
  const [output, setOutput] = useState('');
  const [loading, setLoading] = useState(false);

  const handleParse = async (e) => {
    e.preventDefault();
    setLoading(true);
    try {
      const bodyData = new URLSearchParams();
      bodyData.append('xml_data', xmlData);

      const res = await fetch('/xxe_lab/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        body: bodyData
      });

      const text = await res.text();
      setOutput(text);
    } catch (err) {
      setOutput('XXE Execution Error');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="page-container">
      <div style={{ marginBottom: '2rem' }}>
        <span className="badge badge-hard">HARD • 450 PTS • XXE INJECTION</span>
        <h1 style={{ fontSize: '2rem', fontWeight: '800', color: '#fff', marginTop: '0.5rem' }}>
          XML External Entity (XXE) Parser
        </h1>
        <p style={{ color: 'var(--text-muted)' }}>
          Submit raw XML payload with external entity definitions to read system <code>/flag.txt</code>.
        </p>
      </div>

      <div className="glass-card">
        <form onSubmit={handleParse}>
          <div className="form-group">
            <label className="form-label">Raw XML Payload Input</label>
            <textarea 
              className="form-textarea" 
              value={xmlData} 
              onChange={(e) => setXmlData(e.target.value)} 
              required 
            />
          </div>

          <button type="submit" className="btn-primary" disabled={loading}>
            {loading ? 'Parsing...' : 'Parse XML Payload 📄'}
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
