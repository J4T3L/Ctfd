import React, { useState } from 'react';
import { NavLink } from 'react-router-dom';
import { 
  Shield, LayoutDashboard, KeyRound, FileText, UserCheck, 
  FolderOpen, Terminal, Globe, Search, Ticket, ShoppingCart, Cpu, Bot, Hash, Code, Wrench,
  Lock, HardDrive, Wifi, Binary
} from 'lucide-react';

export default function Sidebar() {
  const [activeTab, setActiveTab] = useState('web');

  const categories = [
    { id: 'web', name: 'Web Exploit (15)', icon: Globe },
    { id: 'crypto', name: 'Crypto (10)', icon: Lock },
    { id: 'forensics', name: 'Forensics (10)', icon: HardDrive },
    { id: 'network', name: 'Network (8)', icon: Wifi },
    { id: 'reverse', name: 'Reverse (7)', icon: Binary },
  ];

  const modules = {
    web: [
      { label: 'Staff Login Portal', path: '/app/sqli', icon: KeyRound, vuln: 'SQLi' },
      { label: 'Hidden Comments', path: '/app/comment', icon: Code, vuln: 'Comment' },
      { label: 'Robots Directive Recon', path: '/app/robots', icon: Bot, vuln: 'Robots' },
      { label: 'Threat SIEM Search', path: '/app/xss', icon: Search, vuln: 'XSS' },
      { label: 'Cookie Session Manager', path: '/app/cookie', icon: Ticket, vuln: 'Cookie' },
      { label: 'User Profile Directory', path: '/app/idor', icon: UserCheck, vuln: 'IDOR' },
      { label: 'System Compliance Logs', path: '/app/lfi', icon: FolderOpen, vuln: 'LFI' },
      { label: 'Host Latency Diagnostics', path: '/app/rce', icon: Terminal, vuln: 'RCE' },
      { label: 'Cloud Credits Store', path: '/app/logic', icon: ShoppingCart, vuln: 'Logic' },
      { label: 'Webhook Content Fetcher', path: '/app/ssrf', icon: Globe, vuln: 'SSRF' },
      { label: 'OAuth Token Inspector', path: '/app/jwt', icon: KeyRound, vuln: 'JWT' },
      { label: 'XXE XML Parser Engine', path: '/app/xxe', icon: Code, vuln: 'XXE' },
      { label: 'Audit Report Generator', path: '/app/ssti', icon: FileText, vuln: 'SSTI' },
      { label: 'Microservice State Cache', path: '/app/pickle', icon: Cpu, vuln: 'Pickle' },
      { label: 'Exposed .git Directory', path: '/app/git', icon: FolderOpen, vuln: 'Git' }
    ],
    crypto: [
      { label: 'Caesar Cipher ROT13', path: '/app/tools', icon: Lock, vuln: 'ROT13' },
      { label: 'Nested Encoding Base64', path: '/app/tools', icon: Lock, vuln: 'Base64' },
      { label: 'Legacy MD5 Hash Crack', path: '/app/weak_hash', icon: Hash, vuln: 'MD5' },
      { label: 'RSA Small Exponent e=3', path: '/app/tools', icon: Lock, vuln: 'RSA' },
      { label: 'RSA Prime Factorization', path: '/app/tools', icon: Lock, vuln: 'Factor' },
      { label: 'Single-Byte XOR Stream', path: '/app/tools', icon: Lock, vuln: 'XOR' },
      { label: 'Vigenère Frequency', path: '/app/tools', icon: Lock, vuln: 'Vigenère' },
      { label: 'AES-128 ECB Pattern', path: '/app/tools', icon: Lock, vuln: 'AES' },
      { label: 'Insecure Custom Hash', path: '/app/tools', icon: Lock, vuln: 'Hash' },
      { label: 'Diffie-Hellman Weak Mod', path: '/app/tools', icon: Lock, vuln: 'DH' }
    ],
    forensics: [
      { label: 'Image EXIF Metadata', path: '/app/tools', icon: HardDrive, vuln: 'EXIF' },
      { label: 'PNG LSB Steganography', path: '/app/tools', icon: HardDrive, vuln: 'LSB' },
      { label: 'Corrupted File Header Fix', path: '/app/tools', icon: HardDrive, vuln: 'Header' },
      { label: 'Disk Partition Carving', path: '/app/tools', icon: HardDrive, vuln: 'Carve' },
      { label: 'Memory Dump Volatility', path: '/app/tools', icon: HardDrive, vuln: 'Memory' },
      { label: 'Layered PDF Hidden Stream', path: '/app/tools', icon: HardDrive, vuln: 'PDF' },
      { label: 'Encrypted ZIP Cracking', path: '/app/tools', icon: HardDrive, vuln: 'ZIP' },
      { label: 'Audio Spectrogram Signal', path: '/app/tools', icon: HardDrive, vuln: 'Audio' },
      { label: 'Browser History SQLite', path: '/app/tools', icon: HardDrive, vuln: 'SQLite' },
      { label: 'USB HID Keyboard Packet', path: '/app/tools', icon: HardDrive, vuln: 'USB' }
    ],
    network: [
      { label: 'HTTP Cleartext Inspection', path: '/app/tools', icon: Wifi, vuln: 'HTTP' },
      { label: 'DNS Tunneling Exfil', path: '/app/tools', icon: Wifi, vuln: 'DNS' },
      { label: 'Anonymous FTP Capture', path: '/app/tools', icon: Wifi, vuln: 'FTP' },
      { label: 'ICMP Echo Covert Channel', path: '/app/tools', icon: Wifi, vuln: 'ICMP' },
      { label: 'SSL/TLS Decryption Key', path: '/app/tools', icon: Wifi, vuln: 'TLS' },
      { label: 'ARP Cache Poisoning MITM', path: '/app/tools', icon: Wifi, vuln: 'ARP' },
      { label: 'Unencrypted Telnet Login', path: '/app/tools', icon: Wifi, vuln: 'Telnet' },
      { label: 'IoT MQTT Packet Sniffing', path: '/app/tools', icon: Wifi, vuln: 'MQTT' }
    ],
    reverse: [
      { label: 'ELF Compiled Strings', path: '/app/tools', icon: Binary, vuln: 'Strings' },
      { label: 'Python Bytecode (.pyc)', path: '/app/tools', icon: Binary, vuln: 'PYC' },
      { label: 'Java Class Decompile', path: '/app/tools', icon: Binary, vuln: 'Java' },
      { label: 'C ELF Crackme Logic', path: '/app/tools', icon: Binary, vuln: 'Crackme' },
      { label: 'Android APK Smali Logic', path: '/app/tools', icon: Binary, vuln: 'APK' },
      { label: 'x86 Buffer Overflow ret2win', path: '/app/tools', icon: Binary, vuln: 'BOF' },
      { label: 'UPX Packed Unpacking', path: '/app/tools', icon: Binary, vuln: 'UPX' }
    ]
  };

  return (
    <aside className="sidebar">
      <NavLink to="/" className="brand-logo" style={{ marginBottom: '1.2rem', paddingLeft: '0.5rem' }}>
        <div className="brand-logo-icon">
          <Shield size={22} color="#040711" />
        </div>
        <div>
          <div className="brand-logo-text">ApexCloud</div>
          <div style={{ fontSize: '0.7rem', color: 'var(--accent-cyan)', letterSpacing: '0.5px' }}>50 CTF SUITE</div>
        </div>
      </NavLink>

      {/* Main Links */}
      <div style={{ paddingBottom: '0.8rem', borderBottom: '1px solid var(--border-color)', marginBottom: '0.8rem' }}>
        <NavLink to="/" className={({ isActive }) => `nav-item ${isActive ? 'active' : ''}`}>
          <Shield size={18} />
          <span>Platform Overview</span>
        </NavLink>
        <NavLink to="/dashboard" className={({ isActive }) => `nav-item ${isActive ? 'active' : ''}`}>
          <LayoutDashboard size={18} />
          <span>SOC Dashboard</span>
        </NavLink>
        <NavLink to="/app/tools" className={({ isActive }) => `nav-item ${isActive ? 'active' : ''}`}>
          <Wrench size={18} color="var(--accent-purple)" />
          <span style={{ color: 'var(--accent-purple)', fontWeight: '700' }}>Tools & Arsenal</span>
        </NavLink>
      </div>

      {/* Category Tabs Switcher */}
      <div style={{ display: 'flex', gap: '0.3rem', flexWrap: 'wrap', marginBottom: '0.8rem', padding: '0 0.3rem' }}>
        {categories.map((c) => {
          const Icon = c.icon;
          const isActive = activeTab === c.id;
          return (
            <button
              key={c.id}
              onClick={() => setActiveTab(c.id)}
              style={{
                background: isActive ? 'var(--accent-cyan)' : 'rgba(255, 255, 255, 0.05)',
                color: isActive ? '#040711' : 'var(--text-muted)',
                border: 'none',
                padding: '0.35rem 0.6rem',
                borderRadius: '6px',
                fontSize: '0.72rem',
                fontWeight: '700',
                cursor: 'pointer',
                display: 'flex',
                alignItems: 'center',
                gap: '0.3rem',
                transition: 'all 0.2s ease'
              }}
            >
              <Icon size={12} />
              {c.name}
            </button>
          );
        })}
      </div>

      {/* Module List per Active Tab */}
      <div style={{ overflowY: 'auto', flex: 1, paddingRight: '0.3rem' }}>
        {modules[activeTab].map((mod, idx) => {
          const Icon = mod.icon;
          return (
            <NavLink key={idx} to={mod.path} className={({ isActive }) => `nav-item ${isActive ? 'active' : ''}`}>
              <Icon size={16} />
              <span style={{ flex: 1, whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis', fontSize: '0.85rem' }}>{mod.label}</span>
              <span style={{ 
                fontSize: '0.65rem', 
                fontWeight: '700', 
                padding: '0.1rem 0.4rem', 
                borderRadius: '4px', 
                background: 'rgba(6, 182, 212, 0.15)',
                color: 'var(--accent-cyan)'
              }}>
                {mod.vuln}
              </span>
            </NavLink>
          );
        })}
      </div>

      <div style={{ marginTop: 'auto', paddingTop: '0.8rem', borderTop: '1px solid var(--border-color)', paddingLeft: '0.5rem' }}>
        <div style={{ fontSize: '0.75rem', color: 'var(--text-sub)' }}>50 CTF Suite • v5.0-PROD</div>
        <div style={{ fontSize: '0.7rem', color: 'var(--accent-emerald)', marginTop: '0.2rem' }}>All 50 Labs Online</div>
      </div>
    </aside>
  );
}
