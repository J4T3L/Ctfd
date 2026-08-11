import React, { useState } from 'react';
import { FolderOpen, FileText } from 'lucide-react';

export default function LfiPage() {
  const [filename, setFilename] = useState('welcome.txt');
  const [content, setContent] = useState('');

  const fetchFile = async (fn) => {
    try {
      const res = await fetch(`/lfi/?page=${encodeURIComponent(fn)}`);
      const text = await res.text();
      setContent(text);
    } catch (err) {
      setContent('Error reading file');
    }
  };

  return (
    <div className="page-container">
      <div style={{ marginBottom: '2rem' }}>
        <span className="badge badge-medium">MEDIUM • 250 PTS • LFI</span>
        <h1 style={{ fontSize: '2rem', fontWeight: '800', color: '#fff', marginTop: '0.5rem' }}>
          File Viewer Pro & Compliance Logs
        </h1>
        <p style={{ color: 'var(--text-muted)' }}>
          Audit file viewer utility. Perform path traversal via <code>?page=</code> parameter to read <code>flag.txt</code>.
        </p>
      </div>

      <div className="glass-card">
        <div style={{ display: 'flex', gap: '1rem', marginBottom: '1.5rem', maxWidth: '500px' }}>
          <input 
            type="text" 
            className="form-input" 
            placeholder="page=flag.txt or ../../../../flag.txt" 
            value={filename} 
            onChange={(e) => setFilename(e.target.value)} 
          />
          <button className="btn-primary" onClick={() => fetchFile(filename)}>
            Read Document 📄
          </button>
        </div>

        {content && (
          <div className="code-block" dangerouslySetInnerHTML={{ __html: content }} />
        )}
      </div>
    </div>
  );
}
