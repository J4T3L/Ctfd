import React from 'react';
import { NavLink } from 'react-router-dom';
import { Shield, Zap, Lock, Server, Cpu, Activity, ArrowRight, CheckCircle } from 'lucide-react';

export default function Home() {
  return (
    <div className="page-container">
      {/* Hero Section */}
      <div className="glass-card" style={{ padding: '3.5rem 2.5rem', marginBottom: '2.5rem', background: 'linear-gradient(135deg, rgba(15,23,42,0.9), rgba(6,182,212,0.08))', border: '1px solid rgba(6, 182, 212, 0.3)' }}>
        <div style={{ display: 'inline-flex', alignItems: 'center', gap: '0.6rem', padding: '0.4rem 1rem', borderRadius: '30px', background: 'rgba(6, 182, 212, 0.12)', border: '1px solid var(--border-cyan)', marginBottom: '1.2rem' }}>
          <Zap size={16} color="var(--accent-cyan)" />
          <span style={{ fontSize: '0.82rem', fontWeight: '700', color: 'var(--accent-cyan)', letterSpacing: '0.5px' }}>APEXCLOUD ENTERPRISE PLATFORM v4.2</span>
        </div>
        <h1 style={{ fontSize: '2.8rem', fontWeight: '800', lineHeight: 1.15, marginBottom: '1rem', background: 'linear-gradient(90deg, #ffffff, #94a3b8)', WebkitBackgroundClip: 'text', WebkitTextFillColor: 'transparent' }}>
          Next-Generation Cloud Defense & SOC Analytics
        </h1>
        <p style={{ fontSize: '1.1rem', color: 'var(--text-muted)', maxWidth: '750px', lineHeight: 1.6, marginBottom: '2rem' }}>
          Unified security orchestration, real-time threat intelligence, and zero-trust asset compliance for enterprise infrastructure.
        </p>

        <div style={{ display: 'flex', gap: '1rem', flexWrap: 'wrap' }}>
          <NavLink to="/dashboard" className="btn-primary">
            Launch SOC Dashboard <ArrowRight size={18} />
          </NavLink>
          <NavLink to="/app/sqli" className="btn-secondary">
            Access Staff Portal
          </NavLink>
        </div>
      </div>

      {/* Metrics Row */}
      <div className="grid-cols-3" style={{ marginBottom: '2.5rem' }}>
        <div className="glass-card" style={{ display: 'flex', alignItems: 'center', gap: '1.2rem' }}>
          <div style={{ width: '50px', height: '50px', borderRadius: '12px', background: 'rgba(16, 185, 129, 0.12)', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
            <Activity size={26} color="var(--accent-emerald)" />
          </div>
          <div>
            <div style={{ fontSize: '1.8rem', fontWeight: '800', color: '#fff' }}>99.99%</div>
            <div style={{ fontSize: '0.85rem', color: 'var(--text-muted)' }}>Infrastructure Uptime SLA</div>
          </div>
        </div>

        <div className="glass-card" style={{ display: 'flex', alignItems: 'center', gap: '1.2rem' }}>
          <div style={{ width: '50px', height: '50px', borderRadius: '12px', background: 'rgba(6, 182, 212, 0.12)', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
            <Server size={26} color="var(--accent-cyan)" />
          </div>
          <div>
            <div style={{ fontSize: '1.8rem', fontWeight: '800', color: '#fff' }}>14,280+</div>
            <div style={{ fontSize: '0.85rem', color: 'var(--text-muted)' }}>Protected Cloud Nodes</div>
          </div>
        </div>

        <div className="glass-card" style={{ display: 'flex', alignItems: 'center', gap: '1.2rem' }}>
          <div style={{ width: '50px', height: '50px', borderRadius: '12px', background: 'rgba(168, 85, 247, 0.12)', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
            <Lock size={26} color="var(--accent-purple)" />
          </div>
          <div>
            <div style={{ fontSize: '1.8rem', fontWeight: '800', color: '#fff' }}>Zero-Trust</div>
            <div style={{ fontSize: '0.85rem', color: 'var(--text-muted)' }}>Continuous Identity Validation</div>
          </div>
        </div>
      </div>
    </div>
  );
}
