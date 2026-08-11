import React from 'react';
import { Shield, Bell, Search, User, ChevronDown, Activity } from 'lucide-react';

export default function Navbar() {
  return (
    <header className="top-header">
      <div style={{ display: 'flex', alignItems: 'center', gap: '1.5rem' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '0.6rem', background: 'rgba(255,255,255,0.04)', padding: '0.4rem 0.9rem', borderRadius: '8px', border: '1px solid var(--border-color)' }}>
          <Activity size={16} color="var(--accent-emerald)" />
          <span style={{ fontSize: '0.82rem', fontWeight: '600', color: 'var(--text-muted)' }}>Tenant:</span>
          <span style={{ fontSize: '0.85rem', fontWeight: '700', color: '#fff' }}>Apex-Production-US-East</span>
          <ChevronDown size={14} color="var(--text-sub)" />
        </div>
      </div>

      <div style={{ display: 'flex', alignItems: 'center', gap: '1.2rem' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', background: 'rgba(16, 185, 129, 0.1)', padding: '0.35rem 0.8rem', borderRadius: '20px', border: '1px solid rgba(16, 185, 129, 0.3)' }}>
          <div style={{ width: '8px', height: '8px', borderRadius: '50%', background: 'var(--accent-emerald)', boxShadow: '0 0 10px var(--accent-emerald)' }}></div>
          <span style={{ fontSize: '0.78rem', fontWeight: '700', color: 'var(--accent-emerald)' }}>SOC Cluster Active</span>
        </div>

        <button style={{ background: 'rgba(255,255,255,0.05)', border: '1px solid var(--border-color)', width: '38px', height: '38px', borderRadius: '10px', display: 'flex', alignItems: 'center', justifyContent: 'center', color: 'var(--text-muted)', cursor: 'pointer' }}>
          <Bell size={18} />
        </button>

        <div style={{ display: 'flex', alignItems: 'center', gap: '0.8rem', paddingLeft: '0.8rem', borderLeft: '1px solid var(--border-color)' }}>
          <div style={{ width: '36px', height: '36px', borderRadius: '50%', background: 'linear-gradient(135deg, var(--accent-cyan), var(--accent-purple))', display: 'flex', alignItems: 'center', justifyContent: 'center', fontWeight: '700', color: '#fff', fontSize: '0.9rem' }}>
            AD
          </div>
          <div>
            <div style={{ fontSize: '0.85rem', fontWeight: '700', color: '#fff' }}>Admin Administrator</div>
            <div style={{ fontSize: '0.72rem', color: 'var(--text-sub)' }}>SecOps Team Lead</div>
          </div>
        </div>
      </div>
    </header>
  );
}
