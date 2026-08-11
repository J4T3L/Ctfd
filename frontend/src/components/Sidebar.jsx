import React from 'react';
import { NavLink } from 'react-router-dom';
import { 
  Shield, LayoutDashboard, KeyRound, FileText, UserCheck, 
  FolderOpen, Terminal, Globe, Search, Ticket, ShoppingCart, Cpu, Bot, Hash, Code
} from 'lucide-react';

export default function Sidebar() {
  const modules = [
    { label: 'SaaS Platform Home', path: '/', icon: Shield },
    { label: 'SOC Dashboard', path: '/dashboard', icon: LayoutDashboard },
    
    // Easy Modules (5)
    { label: 'Staff Login Portal', path: '/app/sqli', icon: KeyRound, category: 'EASY', vuln: 'SQLi' },
    { label: 'Hidden Comments', path: '/app/comment', icon: Code, category: 'EASY', vuln: 'Comment' },
    { label: 'Robots Directive Recon', path: '/app/robots', icon: Bot, category: 'EASY', vuln: 'Robots' },
    { label: 'Threat SIEM Search', path: '/app/xss', icon: Search, category: 'EASY', vuln: 'XSS' },
    { label: 'Cookie Session Manager', path: '/app/cookie', icon: Ticket, category: 'EASY', vuln: 'Cookie' },
    
    // Medium Modules (5)
    { label: 'User Profile Directory', path: '/app/idor', icon: UserCheck, category: 'MEDIUM', vuln: 'IDOR' },
    { label: 'MD5 Password Hash', path: '/app/weak_hash', icon: Hash, category: 'MEDIUM', vuln: 'Hash' },
    { label: 'System Compliance Logs', path: '/app/lfi', icon: FolderOpen, category: 'MEDIUM', vuln: 'LFI' },
    { label: 'Host Latency Diagnostics', path: '/app/rce', icon: Terminal, category: 'MEDIUM', vuln: 'RCE' },
    { label: 'Cloud Credits Store', path: '/app/logic', icon: ShoppingCart, category: 'MEDIUM', vuln: 'Logic' },
    
    // Hard Modules (5)
    { label: 'Webhook Content Fetcher', path: '/app/ssrf', icon: Globe, category: 'HARD', vuln: 'SSRF' },
    { label: 'OAuth Token Inspector', path: '/app/jwt', icon: KeyRound, category: 'HARD', vuln: 'JWT' },
    { label: 'XXE XML Parser Engine', path: '/app/xxe', icon: Code, category: 'HARD', vuln: 'XXE' },
    { label: 'Audit Report Generator', path: '/app/ssti', icon: FileText, category: 'HARD', vuln: 'SSTI' },
    { label: 'Microservice State Cache', path: '/app/pickle', icon: Cpu, category: 'HARD', vuln: 'Pickle' }
  ];

  return (
    <aside className="sidebar">
      <NavLink to="/" className="brand-logo" style={{ marginBottom: '1.5rem', paddingLeft: '0.5rem' }}>
        <div className="brand-logo-icon">
          <Shield size={22} color="#040711" />
        </div>
        <div>
          <div className="brand-logo-text">ApexCloud</div>
          <div style={{ fontSize: '0.7rem', color: 'var(--accent-cyan)', letterSpacing: '0.5px' }}>ENTERPRISE SEC</div>
        </div>
      </NavLink>

      <div style={{ overflowY: 'auto', flex: 1, paddingRight: '0.3rem' }}>
        <div className="nav-section-label">Main Overview</div>
        <NavLink to="/" className={({ isActive }) => `nav-item ${isActive ? 'active' : ''}`}>
          <Shield size={18} />
          <span>Platform Overview</span>
        </NavLink>
        <NavLink to="/dashboard" className={({ isActive }) => `nav-item ${isActive ? 'active' : ''}`}>
          <LayoutDashboard size={18} />
          <span>SOC Dashboard</span>
        </NavLink>

        <div className="nav-section-label">Enterprise Modules (15 Labs)</div>
        {modules.slice(2).map((mod) => {
          const Icon = mod.icon;
          return (
            <NavLink key={mod.path} to={mod.path} className={({ isActive }) => `nav-item ${isActive ? 'active' : ''}`}>
              <Icon size={18} />
              <span style={{ flex: 1, whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis' }}>{mod.label}</span>
              <span style={{ 
                fontSize: '0.68rem', 
                fontWeight: '700', 
                padding: '0.15rem 0.45rem', 
                borderRadius: '4px', 
                background: mod.category === 'EASY' ? 'rgba(16, 185, 129, 0.15)' : mod.category === 'MEDIUM' ? 'rgba(6, 182, 212, 0.15)' : 'rgba(168, 85, 247, 0.15)',
                color: mod.category === 'EASY' ? 'var(--accent-emerald)' : mod.category === 'MEDIUM' ? 'var(--accent-cyan)' : 'var(--accent-purple)'
              }}>
                {mod.vuln}
              </span>
            </NavLink>
          );
        })}
      </div>

      <div style={{ marginTop: 'auto', paddingTop: '1rem', borderTop: '1px solid var(--border-color)', paddingLeft: '0.5rem' }}>
        <div style={{ fontSize: '0.75rem', color: 'var(--text-sub)' }}>ApexCloud v4.2.0-PROD</div>
        <div style={{ fontSize: '0.7rem', color: 'var(--accent-emerald)', marginTop: '0.2rem' }}>All Systems Nominal</div>
      </div>
    </aside>
  );
}
