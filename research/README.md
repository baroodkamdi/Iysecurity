# IY SECURITY Research Library

Add published HTML reports to this directory (or its subdirectories).

The GitHub Action scans `research/**/*.html` and generates `research/index.json`.
The homepage reads that JSON and automatically displays the reports.

Recommended metadata in each report:

```html
<meta name="iy-category" content="Malware Analysis">
<meta name="iy-type" content="Static Analysis">
<meta name="iy-tags" content="Malware, YARA, MITRE ATT&CK">
<meta name="description" content="Short public description of the research.">
<title>Report title | IY SECURITY</title>
```

Do not commit live malware samples, credentials, API keys, private logs, or other sensitive material to a public repository.
