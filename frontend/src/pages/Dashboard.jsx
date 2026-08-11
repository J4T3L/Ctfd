import React from 'react';
import { NavLink } from 'react-router-dom';
import { Shield, AlertTriangle, CheckCircle2, Cpu, HardDrive, Globe, Terminal, Users, ArrowUpRight } from 'lucide-react';

export default function Dashboard() {
  return (
    <div className="page-container">
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '2rem' }}>
        <div>
          <h1 style={{ fontSize: '2rem', fontWeight: '800', color: '#fff' }}>SOC Operations Control Center</h1>
          <p style={{ color: 'var(--text-muted)', fontSize: '0.95rem' }}>Real-time telemetry and vulnerable enterprise endpoint audit overview.</p>
        </div>
        <div style={{ display: 'flex', gap: '0.8rem' }}>
          <span className="badge badge-easy">System Online</span>
        </div>
      </div>

      {/* Main Grid */}
      <div className="grid-cols-2" style={{ marginBottom: '2.5rem' }}>
        <div className="glass-card">
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1.2rem' }}>
            <h3 style={{ fontSize: '1.1rem', fontWeight: '700', color: '#fff' }}>Active Security Alerts</h3>
            <span style={{ fontSize: '0.75rem', color: 'var(--accent-cyan)', fontWeight: '700' }}>LIVE AUDIT</span>
          </div>

          <div style={{ display: 'flex', flexDirection: 'column', gap: '0.8rem' }}>
            <div style={{ background: 'rgba(239, 68, 68, 0.1)', border: '1px solid rgba(239, 68, 68, 0.3)', padding: '0.8rem 1rem', borderRadius: '8px', display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: '0.8rem' }}>
                <AlertTriangle size={18} color="var(--accent-red)" />
                <div>
                  <div style={{ fontSize: '0.9rem', fontWeight: '700', color: '#fff' }}>Authentication Bypass Vulnerability</div>
                  <div style={{ fontSize: '0.78rem', color: 'var(--text-sub)' }}>Module: Staff Login (/app/sqli)</div>
                </div>
              </div>
              <NavLink to="/app/sqli" className="btn-secondary" style={{ padding: '0.4rem 0.8rem', fontSize: '0.8rem' }}>
                Audit <ArrowUpRight size={14} />
              </NavLink>
            </div>

            <div style={{ background: 'rgba(168, 85, 247, 0.1)', border: '1px solid rgba(168, 85, 247, 0.3)', padding: '0.8rem 1rem', borderRadius: '8px', display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: '0.8rem' }}>
                <AlertTriangle size={18} color="var(--accent-purple)" />
                <div>
                  <div style={{ fontSize: '0.9rem', fontWeight: '700', color: '#fff' }}>Jinja2 SSTI Template Injection</div>
                  <div style={{ fontSize: '0.78rem', color: 'var(--text-sub)' }}>Module: Report Generator (/app/ssti)</div>
                </div>
              </div>
              <NavLink to="/app/ssti" className="btn-secondary" style={{ padding: '0.4rem 0.8rem', fontSize: '0.8rem' }}>
                Audit <ArrowUpRight size={14} />
              </NavLink>
            </div>
          </div>
        </div>

        <div className="glass-card">
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1.2rem' }}>
            <h3 style={{ fontSize: '1.1rem', fontWeight: '700', color: '#fff' }}>Cluster Resource Telemetry</h3>
            <span style={{ fontSize: '0.75rem', color: 'var(--accent-emerald)', fontWeight: '700' }}>HEALTHY</span>
          </div>

          <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '1rem' }}>
            <div style={{ background: '#040711', padding: '1rem', borderRadius: '8px', border: '1px solid var(--border-color)' }}>
              <div style={{ fontSize: '0.8rem', color: 'var(--text-muted)' }}>CPU Cluster Load</div>
              <div style={{ fontSize: '1.5rem', fontWeight: '800', color: 'var(--accent-cyan)', marginTop: '0.3rem' }}>14.2%</div>
            </div>
            <div style={{ background: '#040711', padding: '1rem', borderRadius: '8px', border: '1px solid var(--border-color)' }}>
              <div style={{ fontSize: '0.8rem', color: 'var(--text-muted)' }}>Memory Allocation</div>
              <div style={{ fontSize: '1.5rem', fontWeight: '800', color: 'var(--accent-purple)', marginTop: '0.3rem' }}>512 MB</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
