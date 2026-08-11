import React, { useState, useEffect } from 'react';
import { UserCheck, Search, ShieldAlert } from 'lucide-react';

export default function IdorPage() {
  const [userId, setUserId] = useState('102');
  const [profile, setProfile] = useState(null);
  const [loading, setLoading] = useState(false);

  const fetchProfile = async (id) => {
    setLoading(true);
    try {
      const res = await fetch(`/idor/?user_id=${id}`);
      const text = await res.text();
      setProfile(text);
    } catch (err) {
      setProfile('Error loading profile');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchProfile(userId);
  }, []);

  return (
    <div className="page-container">
      <div style={{ marginBottom: '2rem' }}>
        <span className="badge badge-medium">MEDIUM • 150 PTS • IDOR</span>
        <h1 style={{ fontSize: '2rem', fontWeight: '800', color: '#fff', marginTop: '0.5rem' }}>
          UserProfile Directory
        </h1>
        <p style={{ color: 'var(--text-muted)' }}>
          Organization directory inspector. Modify the <code>user_id</code> URL parameter to view Administrator ID 100 profile.
        </p>
      </div>

      <div className="glass-card">
        <div style={{ display: 'flex', gap: '1rem', marginBottom: '1.5rem', maxWidth: '400px' }}>
          <input 
            type="text" 
            className="form-input" 
            placeholder="User ID (e.g. 100)" 
            value={userId} 
            onChange={(e) => setUserId(e.target.value)} 
          />
          <button className="btn-primary" onClick={() => fetchProfile(userId)} disabled={loading}>
            Inspect
          </button>
        </div>

        {profile && (
          <div className="code-block" dangerouslySetInnerHTML={{ __html: profile }} />
        )}
      </div>
    </div>
  );
}
