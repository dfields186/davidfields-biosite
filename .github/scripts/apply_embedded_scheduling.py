from __future__ import annotations

import re
from pathlib import Path

SCHEDULE_HTML = r'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Schedule a Conversation | David C. Fields, M.S.</title>
  <meta name="description" content="Schedule a recruiter introduction, HR screening, formal interview, technical discussion, or Lighthouse Digital Logistix consultation with David C. Fields, M.S.">
  <link rel="canonical" href="https://davidcfields.com/schedule.html">
  <meta property="og:title" content="Schedule a Conversation | David C. Fields, M.S.">
  <meta property="og:description" content="Choose an appropriate professional meeting type and book from David C. Fields’ current real-time availability.">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://davidcfields.com/schedule.html">
  <link rel="stylesheet" href="assets/css/portfolio-pages.css">
  <style>
    .meeting-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:18px}
    .meeting-card{display:flex;flex-direction:column}.meeting-card .actions{margin-top:auto;padding-top:9px}
    .duration{display:inline-flex;width:max-content;margin:3px 0 11px;padding:5px 9px;border:1px solid var(--line);border-radius:999px;color:var(--accent);font-size:.82rem;font-weight:850}
    .embed-shell{margin-top:25px;border:1px solid var(--line);border-radius:22px;overflow:hidden;background:#fff;box-shadow:var(--shadow)}
    .calendly-inline-widget{min-width:320px;height:960px}
    .privacy-note{margin-top:20px;padding:18px 20px;border:1px solid var(--line);border-radius:16px;background:rgba(255,255,255,.03);color:var(--muted)}
    @media(max-width:920px){.meeting-grid{grid-template-columns:1fr 1fr}.calendly-inline-widget{height:1040px}}
    @media(max-width:680px){.meeting-grid{grid-template-columns:1fr}.calendly-inline-widget{height:1160px}}
  </style>
  <meta name="robots" content="index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1">
  <meta name="author" content="David C. Fields, M.S.">
  <meta name="theme-color" content="#07111f">
  <meta property="og:site_name" content="David C. Fields, M.S.">
  <meta property="og:locale" content="en_US">
  <meta property="og:image" content="https://davidcfields.com/images/davidfields.jpg">
  <meta property="og:image:alt" content="Professional headshot of David C. Fields, M.S.">
  <meta name="twitter:card" content="summary">
  <meta name="twitter:title" content="Schedule a Conversation | David C. Fields, M.S.">
  <meta name="twitter:description" content="Choose an appropriate professional meeting type and book from current real-time availability.">
  <meta name="twitter:image" content="https://davidcfields.com/images/davidfields.jpg">
  <link rel="icon" href="/favicon.svg" type="image/svg+xml">
  <link rel="manifest" href="/site.webmanifest">
  <link rel="me" href="https://www.linkedin.com/in/david-c-fields">
  <link rel="me" href="https://github.com/davidcfields">
  <script type="application/ld+json" data-seo="breadcrumb">{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":"https://davidcfields.com/"},{"@type":"ListItem","position":2,"name":"Schedule","item":"https://davidcfields.com/schedule.html"}]}</script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="header">
  <nav class="nav shell" aria-label="Primary navigation">
    <a class="brand" href="index.html">David C. Fields, <span>M.S.</span></a>
    <div class="links"><a href="index.html#about">About</a><a href="index.html#experience">Experience</a><a href="case-studies.html">Case Studies</a><a href="consulting-services.html">Consulting</a><a href="index.html#resumes">Resumes</a><a href="faq.html">FAQ</a><a href="contact.html">Contact</a><a href="schedule.html" aria-current="page">Schedule</a><a class="nav-cta" href="recruiter-brief.html">Recruiter Brief</a></div>
  </nav>
</header>
<main id="main" class="shell">
  <section class="hero">
    <div class="breadcrumb"><a href="index.html">Home</a> / Schedule</div>
    <p class="eyebrow">Real-time professional scheduling</p>
    <h1>Choose the conversation that fits the objective.</h1>
    <p class="lede">Select an appropriate meeting type, then choose from current available dates and times. Availability reflects existing calendar commitments, configured buffers, scheduling notice, holidays, and daily meeting limits without revealing private calendar details.</p>
  </section>

  <section class="section">
    <div class="intro"><p class="eyebrow">Meeting options</p><h2>Five focused paths—without an open-ended booking menu.</h2><p>All meetings use Google Meet unless another arrangement is agreed separately. Times are shown in the visitor’s local time zone; David’s scheduling rules are maintained in America/New_York.</p></div>
    <div class="meeting-grid">
      <article class="card meeting-card"><p class="kicker">Recruiting</p><h3>Recruiter or Hiring Manager Introduction</h3><span class="duration">20 minutes</span><p>Initial conversation about a role, organization, hiring need, project, work arrangement, or mutual fit.</p><div class="actions"><a class="btn" target="_blank" rel="noopener" href="https://calendly.com/fieldsventures/recruiter-or-hiring-manager-introduction?utm_source=davidcfields.com&amp;utm_medium=website&amp;utm_campaign=professional_scheduling">Open direct booking page</a></div></article>
      <article class="card meeting-card"><p class="kicker">Recruiting</p><h3>Recruiter or HR Screening</h3><span class="duration">30 minutes</span><p>Structured screening covering role alignment, work arrangement, compensation range, timing, process, and next steps.</p><div class="actions"><a class="btn" target="_blank" rel="noopener" href="https://calendly.com/fieldsventures/recruiter-or-hr-screening?utm_source=davidcfields.com&amp;utm_medium=website&amp;utm_campaign=professional_scheduling">Open direct booking page</a></div></article>
      <article class="card meeting-card"><p class="kicker">Employment</p><h3>Formal Job Interview</h3><span class="duration">60 minutes</span><p>Detailed interview with a hiring manager, technical leader, panel, or prospective team.</p><div class="actions"><a class="btn" target="_blank" rel="noopener" href="https://calendly.com/fieldsventures/formal-job-interview?utm_source=davidcfields.com&amp;utm_medium=website&amp;utm_campaign=professional_scheduling">Open direct booking page</a></div></article>
      <article class="card meeting-card"><p class="kicker">Technical</p><h3>Technical or Architecture Discussion</h3><span class="duration">45 minutes</span><p>Infrastructure, automation, cybersecurity, platform engineering, architecture, modernization, operations, or technical leadership.</p><div class="actions"><a class="btn" target="_blank" rel="noopener" href="https://calendly.com/fieldsventures/technical-or-architecture-discussion?utm_source=davidcfields.com&amp;utm_medium=website&amp;utm_campaign=professional_scheduling">Open direct booking page</a></div></article>
      <article class="card meeting-card"><p class="kicker">Consulting</p><h3>Lighthouse Digital Logistix Strategic Consultation</h3><span class="duration">30 minutes</span><p>Exploratory discussion about a business or technology objective, operating challenge, modernization need, or potential engagement.</p><div class="actions"><a class="btn" target="_blank" rel="noopener" href="https://calendly.com/fieldsventures/lhdl-consult?utm_source=davidcfields.com&amp;utm_medium=website&amp;utm_campaign=professional_scheduling">Open direct booking page</a></div></article>
    </div>
  </section>

  <section class="section" id="book">
    <div class="intro"><p class="eyebrow">Book in real time</p><h2>Select a meeting type, date, and available time.</h2><p>The embedded scheduler displays only bookable availability. Calendar event titles, attendees, descriptions, and private details are not displayed.</p></div>
    <div class="embed-shell">
      <div class="calendly-inline-widget" data-url="https://calendly.com/fieldsventures?utm_source=davidcfields.com&amp;utm_medium=website&amp;utm_campaign=professional_scheduling"></div>
    </div>
    <script src="https://assets.calendly.com/assets/external/widget.js" type="text/javascript"></script>
    <noscript><p class="callout">JavaScript is required for the embedded scheduler. Use the <a href="https://calendly.com/fieldsventures" target="_blank" rel="noopener">direct Calendly scheduling page</a> instead.</p></noscript>
    <div class="privacy-note"><strong>Scheduling privacy:</strong> Booking information is processed by Calendly and the connected Google Calendar and Google Meet services. Do not submit passwords, account numbers, protected health information, confidential customer data, authentication details, or other unnecessary sensitive information.</div>
    <div class="callout warn"><strong>Important boundary:</strong> Scheduling a meeting does not create an employment acceptance, consulting contract, scope, pricing agreement, legal or compliance opinion, emergency-support obligation, or commitment by either party. Any consequential arrangement requires separate written confirmation and, where appropriate, qualified professional review.</div>
  </section>
</main>
<footer class="footer"><div class="shell footer-row"><div>© 2026 David C. Fields. Professional biography, portfolio, resumes, consulting, and scheduling information.</div><div class="footer-links"><a href="index.html">Home</a><a href="consulting-services.html">Consulting</a><a href="case-studies.html">Case Studies</a><a href="index.html#resumes">Resumes</a><a href="faq.html">FAQ</a><a href="contact.html">Contact</a><a href="schedule.html">Schedule</a><a href="recruiter-brief.html">Recruiter Brief</a></div></div></footer>
</body>
</html>
'''


def update_primary_nav(text: str, filename: str) -> str:
    def repl(match: re.Match[str]) -> str:
        nav = match.group(0)
        if 'href="schedule.html"' in nav:
            return nav
        contact = re.search(r'(<a[^>]+href="(?:contact\.html|index\.html#contact|#contact)"[^>]*>Contact</a>)', nav)
        if not contact:
            raise RuntimeError(f'Primary navigation Contact link not found in {filename}')
        return nav[:contact.end()] + '<a href="schedule.html">Schedule</a>' + nav[contact.end():]

    updated, count = re.subn(r'<nav[^>]*aria-label="Primary navigation".*?</nav>', repl, text, flags=re.S)
    if count == 0 and 'aria-label="Primary navigation"' in text:
        raise RuntimeError(f'Could not parse primary navigation in {filename}')
    return updated


def update_footer(text: str) -> str:
    def repl(match: re.Match[str]) -> str:
        footer = match.group(0)
        if 'href="schedule.html"' in footer:
            return footer
        contact = re.search(r'(<a[^>]+href="(?:contact\.html|index\.html#contact|#contact)"[^>]*>Contact</a>)', footer)
        if not contact:
            return footer
        return footer[:contact.end()] + '<a href="schedule.html">Schedule</a>' + footer[contact.end():]

    return re.sub(r'<div class="footer-links">.*?</div>', repl, text, flags=re.S)


Path('schedule.html').write_text(SCHEDULE_HTML, encoding='utf-8')

for page in Path('.').glob('*.html'):
    text = page.read_text(encoding='utf-8')
    text = update_primary_nav(text, page.name)
    text = update_footer(text)
    page.write_text(text, encoding='utf-8')

path = Path('index.html')
text = path.read_text(encoding='utf-8')
if '>Schedule a conversation</a>' not in text:
    needle = '<a class="btn" href="#contact">Discuss an opportunity</a>'
    if needle not in text:
        raise RuntimeError('Homepage opportunity CTA not found')
    text = text.replace(needle, '<a class="btn" href="schedule.html">Schedule a conversation</a>' + needle, 1)
path.write_text(text, encoding='utf-8')

for filename in ('recruiter-brief.html', 'infrastructure-automation-security-modernization.html', 'consulting-services.html'):
    path = Path(filename)
    text = path.read_text(encoding='utf-8')
    if '>Schedule a conversation</a>' not in text:
        pattern = r'(<a class="btn(?: primary)?" href="contact\.html">[^<]+</a>)'
        text, count = re.subn(pattern, r'\1<a class="btn" href="schedule.html">Schedule a conversation</a>', text, count=1)
        if count == 0:
            raise RuntimeError(f'Contact CTA not found in {filename}')
    path.write_text(text, encoding='utf-8')

path = Path('contact.html')
text = path.read_text(encoding='utf-8')
if 'Schedule directly from real-time availability' not in text:
    needle = '    <aside>\n      <article class="card">'
    card = '''    <aside>
      <article class="card" style="margin-bottom:18px">
        <p class="kicker">Real-time scheduling</p>
        <h3>Prefer to choose an available time now?</h3>
        <p>Select a recruiter introduction, screening, formal interview, technical discussion, or Lighthouse consultation from current availability.</p>
        <div class="actions"><a class="btn primary" href="schedule.html">Schedule directly from real-time availability</a></div>
      </article>
      <article class="card">'''
    if needle not in text:
        raise RuntimeError('Contact page aside insertion point not found')
    text = text.replace(needle, card, 1)
path.write_text(text, encoding='utf-8')

path = Path('sitemap.xml')
sitemap = path.read_text(encoding='utf-8')
if 'https://davidcfields.com/schedule.html' not in sitemap:
    needle = '  <url><loc>https://davidcfields.com/consulting-services.html</loc><lastmod>2026-08-05</lastmod></url>\n'
    if needle not in sitemap:
        raise RuntimeError('Sitemap consulting entry not found')
    sitemap = sitemap.replace(needle, needle + '  <url><loc>https://davidcfields.com/schedule.html</loc><lastmod>2026-08-05</lastmod></url>\n', 1)
path.write_text(sitemap, encoding='utf-8')

path = Path('.github/scripts/validate_site.py')
validator = path.read_text(encoding='utf-8')
if '"schedule.html": "/schedule.html",' not in validator:
    validator = validator.replace(
        '    "consulting-services.html": "/consulting-services.html",\n',
        '    "consulting-services.html": "/consulting-services.html",\n    "schedule.html": "/schedule.html",\n',
        1,
    )

schedule_checks = '''
for path in Path(".").glob("*.html"):
    text = path.read_text(encoding="utf-8")
    if 'aria-label="Primary navigation"' not in text:
        continue
    if not re.search(r'href="schedule\\.html"[^>]*>Schedule</a>', text):
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
'''
if 'Primary navigation missing Schedule link' not in validator:
    validator = validator.replace('\n\nif errors:\n', '\n' + schedule_checks + '\nif errors:\n', 1)
path.write_text(validator, encoding='utf-8')
