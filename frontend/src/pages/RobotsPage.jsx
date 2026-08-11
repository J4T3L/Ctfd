import React, { useState, useEffect } from 'react';
import { Bot } from 'lucide-react';

export default function RobotsPage() {
  const [content, setContent] = useState('');

  const fetchRobotsPage = async () => {
    try {
      const res = await fetch('/robots_secret/');
      const text = await res.text();
      setContent(text);
    } catch (err) {
      setContent('Robots Error');
    }
  };

  useEffect(() => {
    fetchRobotsPage();
  }, []);

  return (
    <div className="page-container">
      <div style={{ marginBottom: '2rem' }}>
        <span className="badge badge-easy">EASY • 50 PTS • ROBOTS RECON</span>
        <h1 style={{ fontSize: '2rem', fontWeight: '800', color: '#fff', marginTop: '0.5rem' }}>
          Crawler Robots Directive Recon
        </h1>
        <p style={{ color: 'var(--text-muted)' }}>
          Inspect <code>/robots_secret/robots.txt</code> to discover disallowed crawler directory paths.
        </p>
      </div>

      <div className="glass-card">
        <div className="code-block" dangerouslySetInnerHTML={{ __html: content }} />
      </div>
    </div>
  );
}
