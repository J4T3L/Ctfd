import React, { useState } from 'react';
import { NavLink } from 'react-router-dom';
import { 
  Terminal, Shield, Search, Cpu, Globe, KeyRound, Wrench, 
  ExternalLink, Copy, CheckCircle2, BookOpen, Zap
} from 'lucide-react';

export default function ToolsPage() {
  const [copiedId, setCopiedId] = useState(null);

  const copyCommand = (id, cmd) => {
    navigator.clipboard.writeText(cmd);
    setCopiedId(id);
    setTimeout(() => setCopiedId(null), 2000);
  };

  const toolCategories = [
    {
      category: 'Vulnerability Scanners & Reconnaissance',
      tools: [
        {
          id: 'nuclei',
          name: 'Nuclei',
          author: 'ProjectDiscovery',
          tag: 'Scanner',
          desc: 'Fast and customizable vulnerability scanner based on simple YAML templates. Essential for automated CVE scanning, LFI, RCE, and SSRF detection.',
          cmd: 'nuclei -u https://target.paradick.my.id/app/lfi -t file/lfi/',
          ctfLink: '/app/lfi'
        },
        {
          id: 'nikto',
          name: 'Nikto Web Scanner',
          author: 'CIRT',
          tag: 'Recon',
          desc: 'Web server scanner for dangerous files, outdated server software, and misconfigured HTTP headers.',
          cmd: 'nikto -h https://target.paradick.my.id/',
          ctfLink: '/app/robots'
        }
      ]
    },
    {
      category: 'Directory & Parameter Fuzzers',
      tools: [
        {
          id: 'ffuf',
          name: 'ffuf (Fuzz Faster Fool)',
          author: 'ffuf dev',
          tag: 'Fuzzer',
          desc: 'High-speed web fuzzer written in Go. Used for directory discovery, parameter fuzzing, and IDOR enumerations.',
          cmd: "ffuf -u 'https://target.paradick.my.id/idor/?user_id=FUZZ' -w numbers.txt",
          ctfLink: '/app/idor'
        },
        {
          id: 'gobuster',
          name: 'Gobuster',
          author: 'OJ Reeves',
          tag: 'Directory Brute',
          desc: 'URI/DNS/VHost brute-forcing tool written in Go to discover hidden administrative endpoints.',
          cmd: 'gobuster dir -u https://target.paradick.my.id/ -w /usr/share/wordlists/dirb/common.txt',
          ctfLink: '/app/comment'
        }
      ]
    },
    {
      category: 'Proxy & Request Interceptors',
      tools: [
        {
          id: 'burp',
          name: 'Burp Suite (Community / Pro)',
          author: 'PortSwigger',
          tag: 'Interceptors',
          desc: 'Industry-standard graphical HTTP proxy for inspecting requests, cookie tampering, intruder attacks, and repeater payloads.',
          cmd: 'Set Browser Proxy -> 127.0.0.1:8080 (Burp Interceptor)',
          ctfLink: '/app/sqli'
        }
      ]
    },
    {
      category: 'SQL Injection Automation',
      tools: [
        {
          id: 'sqlmap',
          name: 'sqlmap',
          author: 'Bernardo Damele & Miroslav Stampar',
          tag: 'Exploitation',
          desc: 'Automatic SQL injection and database takeover engine. Detects and exploits SQLi vulnerabilities in forms and parameters.',
          cmd: "sqlmap -u 'https://target.paradick.my.id/sqli/login' --data='username=admin&password=x' --batch",
          ctfLink: '/app/sqli'
        }
      ]
    },
    {
      category: 'JWT & Token Analyzers',
      tools: [
        {
          id: 'jwt_tool',
          name: 'jwt_tool',
          author: 'ticarpi',
          tag: 'Token Analysis',
          desc: 'Toolkit for testing JSON Web Tokens (JWT) for weak secrets, signature spoofing, and algorithm none attacks.',
          cmd: 'python3 jwt_tool.py <JWT_TOKEN_STRING> -X a',
          ctfLink: '/app/jwt'
        }
      ]
    },
    {
      category: 'Template Injection & SSTI',
      tools: [
        {
          id: 'tplmap',
          name: 'tplmap',
          author: 'epinna',
          tag: 'SSTI Exploiter',
          desc: 'Automatic Server-Side Template Injection (SSTI) detection and exploitation tool for Jinja2, Mako, Twig, etc.',
          cmd: "python2 tplmap.py -u 'https://target.paradick.my.id/ssti/preview' -d 'template=*'",
          ctfLink: '/app/ssti'
        }
      ]
    },
    {
      category: 'Hash Cracking & Password Recovery',
      tools: [
        {
          id: 'hashcat',
          name: 'Hashcat',
          author: 'atom',
          tag: 'Password Recovery',
          desc: "World's fastest rule-based password recovery utility. Cracks MD5, SHA-256, bcrypt, and NTLM hashes.",
          cmd: 'hashcat -m 0 e10adc3949ba59abbe56e057f20f883e rockyou.txt',
          ctfLink: '/app/weak_hash'
        }
      ]
    }
  ];

  return (
    <div className="page-container">
      <div style={{ marginBottom: '2.5rem' }}>
        <div style={{ display: 'inline-flex', alignItems: 'center', gap: '0.6rem', padding: '0.4rem 1rem', borderRadius: '30px', background: 'rgba(168, 85, 247, 0.12)', border: '1px solid var(--border-purple)', marginBottom: '0.8rem' }}>
          <Wrench size={16} color="var(--accent-purple)" />
          <span style={{ fontSize: '0.82rem', fontWeight: '700', color: 'var(--accent-purple)', letterSpacing: '0.5px' }}>MODUL AJAR • CTF TOOLSET & ARSENAL GUIDE</span>
        </div>
        <h1 style={{ fontSize: '2.4rem', fontWeight: '800', color: '#fff' }}>
          Recommended Pentesting & CTF Tools
        </h1>
        <p style={{ color: 'var(--text-muted)', fontSize: '1.05rem', maxWidth: '800px', marginTop: '0.4rem' }}>
          Panduan rekomendasi perkakas (*security tools*) standar industri untuk mempraktikkan eksplorasi & pentesting 15 laboratorium CTF Web Exploitation.
        </p>
      </div>

      <div style={{ display: 'flex', flexDirection: 'column', gap: '2.5rem' }}>
        {toolCategories.map((cat, idx) => (
          <div key={idx}>
            <h3 style={{ fontSize: '1.2rem', fontWeight: '700', color: 'var(--accent-cyan)', marginBottom: '1.2rem', borderBottom: '1px solid var(--border-color)', paddingBottom: '0.5rem' }}>
              {cat.category}
            </h3>

            <div className="grid-cols-2">
              {cat.tools.map((t) => (
                <div key={t.id} className="glass-card" style={{ display: 'flex', flexDirection: 'column', justifyContent: 'space-between' }}>
                  <div>
                    <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: '0.8rem' }}>
                      <div>
                        <h4 style={{ fontSize: '1.2rem', fontWeight: '800', color: '#fff' }}>{t.name}</h4>
                        <div style={{ fontSize: '0.78rem', color: 'var(--text-sub)' }}>By {t.author}</div>
                      </div>
                      <span className="badge badge-medium">{t.tag}</span>
                    </div>

                    <p style={{ color: 'var(--text-muted)', fontSize: '0.9rem', lineHeight: 1.5, marginBottom: '1.2rem' }}>
                      {t.desc}
                    </p>
                  </div>

                  <div>
                    <div className="form-label" style={{ fontSize: '0.75rem', marginBottom: '0.4rem' }}>Example Terminal Command:</div>
                    <div style={{ background: '#040711', border: '1px solid var(--border-color)', borderRadius: '8px', padding: '0.7rem 0.9rem', display: 'flex', alignItems: 'center', justifyContent: 'space-between', fontFamily: 'var(--font-code)', fontSize: '0.82rem', color: 'var(--accent-cyan)', marginBottom: '1rem' }}>
                      <span style={{ whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis', paddingRight: '0.5rem' }}>{t.cmd}</span>
                      <button 
                        onClick={() => copyCommand(t.id, t.cmd)} 
                        style={{ background: 'none', border: 'none', color: 'var(--text-muted)', cursor: 'pointer', display: 'flex', alignItems: 'center', gap: '0.3rem' }}
                      >
                        {copiedId === t.id ? <CheckCircle2 size={16} color="var(--accent-emerald)" /> : <Copy size={16} />}
                      </button>
                    </div>

                    <NavLink to={t.ctfLink} className="btn-secondary" style={{ width: '100%', justifyContent: 'center', fontSize: '0.85rem' }}>
                      Practise on CTF Lab Module →
                    </NavLink>
                  </div>
                </div>
              ))}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
