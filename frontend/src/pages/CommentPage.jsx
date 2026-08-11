import React, { useState, useEffect } from 'react';
import { Search } from 'lucide-react';

export default function CommentPage() {
  const [content, setContent] = useState('');

  const fetchCommentPage = async () => {
    try {
      const res = await fetch('/hidden_comment/');
      const text = await res.text();
      setContent(text);
    } catch (err) {
      setContent('Error loading page');
    }
  };

  useEffect(() => {
    fetchCommentPage();
  }, []);

  return (
    <div className="page-container">
      <div style={{ marginBottom: '2rem' }}>
        <span className="badge badge-easy">EASY • 50 PTS • HTML COMMENT RECON</span>
        <h1 style={{ fontSize: '2rem', fontWeight: '800', color: '#fff', marginTop: '0.5rem' }}>
          DevCompany Internal Employee Portal
        </h1>
        <p style={{ color: 'var(--text-muted)' }}>
          Public company update portal. Inspect page HTML source code to discover developer comments and hidden admin endpoint.
        </p>
      </div>

      <div className="glass-card">
        {/* 
            TODO FOR DEVELOPER TEAM:
            Uncomment hidden administrative endpoint after security audit completes:
            Secret Admin Endpoint: /hidden_comment/secret_admin_dashboard_99
        */}
        <div className="code-block" dangerouslySetInnerHTML={{ __html: content }} />
      </div>
    </div>
  );
}
