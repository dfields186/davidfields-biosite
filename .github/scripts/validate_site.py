from __future__ import annotations

import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import urlparse

SITE = "https://davidcfields.com"
INDEXABLE = {
    "index.html": "/",
    "recruiter-brief.html": "/recruiter-brief.html",
    "infrastructure-automation-security-modernization.html": "/infrastructure-automation-security-modernization.html",
    "consulting-services.html": "/consulting-services.html",
    "schedule.html": "/schedule.html",
    "case-studies.html": "/case-studies.html",
    "case-study-enterprise-automation.html": "/case-study-enterprise-automation.html",
    "case-study-ai-agent-lab.html": "/case-study-ai-agent-lab.html",
    "faq.html": "/faq.html",
    "contact.html": "/contact.html",
    "resume-tech.html": "/resume-tech.html",
    "resume-leadership.html": "/resume-leadership.html",
}
NOINDEX = {"about.html", "resume.html", "contact-success.html", "404.html"}
errors: list[str] = []

for filename, route in INDEXABLE.items():
    path = Path(filename)
    if not path.exists():
        errors.append(f"Missing indexable page: {filename}")
        continue
    text = path.read_text(encoding="utf-8")
    expected = SITE + route
    if filename == "index.html":
        expected = SITE + "/"
    if f'<link rel="canonical" href="{expected}">' not in text:
        errors.append(f"Wrong or missing canonical in {filename}: expected {expected}")
    for token in ('<title>', 'name="description"', 'name="robots"', 'property="og:image"', 'name="twitter:card"'):
        if token not in text:
            errors.append(f"Missing {token} in {filename}")
    if "www.davidcfields.com" in text:
        errors.append(f"Legacy www host remains in {filename}")

for filename in NOINDEX:
    path = Path(filename)
    if not path.exists():
        errors.append(f"Missing noindex page: {filename}")
        continue
    text = path.read_text(encoding="utf-8")
    if 'name="robots" content="noindex,follow"' not in text:
        errors.append(f"Missing noindex,follow in {filename}")

if not Path("robots.txt").exists():
    errors.append("Missing robots.txt")
else:
    robots = Path("robots.txt").read_text(encoding="utf-8")
    if f"Sitemap: {SITE}/sitemap.xml" not in robots:
        errors.append("robots.txt does not declare the canonical sitemap")

if not Path("sitemap.xml").exists():
    errors.append("Missing sitemap.xml")
else:
    root = ET.parse("sitemap.xml").getroot()
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    found = {node.text for node in root.findall("sm:url/sm:loc", ns)}
    expected = {SITE + route for route in INDEXABLE.values()}
    if found != expected:
        errors.append(f"Sitemap URL mismatch. Missing={sorted(expected-found)} Extra={sorted(found-expected)}")

for path in Path(".").glob("*.html"):
    text = path.read_text(encoding="utf-8")
    for href in re.findall(r'href="([^"]+)"', text):
        if href.startswith(("http://", "https://", "mailto:", "tel:", "#", "/")):
            continue
        target = href.split("#", 1)[0].split("?", 1)[0]
        if not target:
            continue
        parsed = urlparse(target)
        if parsed.path.endswith(".html") and not Path(parsed.path).exists():
            errors.append(f"Broken internal link in {path.name}: {href}")

for required in ("favicon.svg", "site.webmanifest", "404.html"):
    if not Path(required).exists():
        errors.append(f"Missing {required}")

for path in Path(".").glob("*.html"):
    text = path.read_text(encoding="utf-8")
    if 'aria-label="Primary navigation"' not in text:
        continue
    if not re.search(r'href="consulting-services\.html"[^>]*>Consulting</a>', text):
        errors.append(f"Primary navigation missing Consulting link in {path.name}")


for path in Path(".").glob("*.html"):
    text = path.read_text(encoding="utf-8")
    if 'aria-label="Primary navigation"' not in text:
        continue
    if not re.search(r'href="schedule\.html"[^>]*>Schedule</a>', text):
        errors.append(f"Primary navigation missing Schedule link in {path.name}")

schedule_text = Path("schedule.html").read_text(encoding="utf-8") if Path("schedule.html").exists() else ""
for token in (
    'class="calendly-inline-widget"',
    'https://assets.calendly.com/assets/external/widget.js',
    'https://calendly.com/fieldsventures',
    'recruiter-or-hiring-manager-introduction',
    'recruiter-or-hr-screening',
    'formal-job-interview',
    'technical-or-architecture-discussion',
    'lhdl-consult',
    '<noscript>',
):
    if token not in schedule_text:
        errors.append(f"Scheduling page missing required integration token: {token}")

if errors:
    print("Site quality validation failed:")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)
print("Site quality validation passed.")
