document.addEventListener('DOMContentLoaded', () => {
    const templateSelect = document.getElementById('template_preset');
    const templateTextarea = document.getElementById('template');

    if (templateSelect && templateTextarea) {
        const presets = {
            standard: `<div class="report-card">
    <h2>Audit Report: {{ report_name }}</h2>
    <p>Auditor: <strong>{{ auditor }}</strong></p>
    <div class="status-badge status-passed">Status: {{ status }}</div>
    <hr class="divider"/>
    <p class="summary-text">{{ summary }}</p>
</div>`,
            compact: `<div class="report-card" style="padding: 1.5rem;">
    <h3>{{ report_name }} [{{ status }}]</h3>
    <small>Prepared by {{ auditor }}</small>
    <p style="margin-top: 1rem;">{{ summary }}</p>
</div>`,
            minimal: `[REPORT] {{ report_name }} | Auditor: {{ auditor }} | Status: {{ status }} | Summary: {{ summary }}`
        };

        templateSelect.addEventListener('change', (e) => {
            const val = e.target.value;
            if (presets[val]) {
                templateTextarea.value = presets[val];
            }
        });
    }
});
