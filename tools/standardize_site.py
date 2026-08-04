from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


def page_header(current: str, homepage: bool = False) -> str:
    def link(label: str, href: str, key: str, cta: bool = False) -> str:
        attrs = []
        if current == key:
            attrs.append('aria-current="page"')
        cls = ' class="nav-cta"' if cta else ''
        extra = (' ' + ' '.join(attrs)) if attrs else ''
        return f'<a{cls} href="{href}"{extra}>{label}</a>'

    about = '#about' if homepage else 'index.html#about'
    experience = '#experience' if homepage else 'index.html#experience'
    resumes = '#resumes' if homepage else 'index.html#resumes'
    contact = '#contact' if homepage else ('contact.html' if current == 'contact' else 'index.html#contact')
    brand = '#home' if homepage else 'index.html'

    links = ''.join([
        link('About', about, 'about'),
        link('Experience', experience, 'experience'),
        link('Case Studies', 'case-studies.html', 'case-studies'),
        link('Resumes', resumes, 'resumes'),
        link('FAQ', 'faq.html', 'faq'),
        link('Contact', contact, 'contact'),
        link('Recruiter Brief', 'recruiter-brief.html', 'recruiter', cta=True),
    ])
    return f'''<header class="header">
  <nav class="nav shell" aria-label="Primary navigation">
    <a class="brand" href="{brand}">David C. Fields, <span>M.S.</span></a>
    <div class="links">{links}</div>
  </nav>
</header>'''


def page_footer(homepage: bool = False) -> str:
    home = '#home' if homepage else 'index.html'
    resumes = '#resumes' if homepage else 'index.html#resumes'
    contact = '#contact' if homepage else 'index.html#contact'
    return f'''<footer class="footer"><div class="shell footer-row"><div>© 2026 David C. Fields. Professional biography, portfolio, and resumes.</div><div class="footer-links"><a href="{home}">Home</a><a href="recruiter-brief.html">Recruiter Brief</a><a href="case-studies.html">Case Studies</a><a href="{resumes}">Resumes</a><a href="faq.html">FAQ</a><a href="{contact}">Contact</a></div></div></footer>'''


def replace_header_footer(path: Path, current: str, homepage: bool = False) -> None:
    text = path.read_text(encoding='utf-8')
    text, header_count = re.subn(r'<header class="header">.*?</header>', page_header(current, homepage), text, count=1, flags=re.S)
    if header_count != 1:
        raise RuntimeError(f'Could not replace header in {path.name}')
    text, footer_count = re.subn(r'<footer class="footer">.*?</footer>', page_footer(homepage), text, count=1, flags=re.S)
    if footer_count != 1:
        raise RuntimeError(f'Could not replace footer in {path.name}')
    path.write_text(text, encoding='utf-8')


def resume_bar(current_label: str) -> str:
    links = ''.join([
        '<a href="index.html#about">About</a>',
        '<a href="index.html#experience">Experience</a>',
        '<a href="case-studies.html">Case Studies</a>',
        '<a href="index.html#resumes" aria-current="page">Resumes</a>',
        '<a href="faq.html">FAQ</a>',
        '<a href="index.html#contact">Contact</a>',
        '<a class="bar-cta" href="recruiter-brief.html">Recruiter Brief</a>',
    ])
    return f'''<div class="bar">
  <a class="bar-brand" href="index.html">David C. Fields, M.S.</a>
  <nav class="bar-nav" aria-label="Primary navigation">{links}</nav>
  <button type="button" onclick="window.print()">Print / Save PDF</button>
  <span class="bar-page">{current_label}</span>
</div>'''


def update_resume(path: Path, label: str) -> None:
    text = path.read_text(encoding='utf-8')
    text, count = re.subn(r'<div class="bar">.*?</div>\s*<main', resume_bar(label) + '\n<main', text, count=1, flags=re.S)
    if count != 1:
        raise RuntimeError(f'Could not replace resume bar in {path.name}')
    css = '''
.bar{flex-wrap:wrap}.bar-brand{color:#fff!important;font-weight:800;text-decoration:none;white-space:nowrap}.bar-nav{display:flex;flex-wrap:wrap;align-items:center;justify-content:center;gap:8px 13px;flex:1}.bar-nav a{font-size:12px;font-weight:700;text-decoration:none;white-space:nowrap}.bar-nav a[aria-current="page"]{color:#fff;text-decoration:underline}.bar-nav .bar-cta{padding:6px 9px;border:1px solid rgba(157,230,255,.55);border-radius:8px}.bar-page{width:100%;text-align:center;font-size:12px;color:#c6d3e2}@media(max-width:860px){.bar{justify-content:center}.bar-brand{width:100%;text-align:center}.bar-nav{order:3;width:100%}.bar-page{order:4}}'''
    if '.bar-nav{' not in text:
        text = text.replace('</style>', css + '\n</style>', 1)
    path.write_text(text, encoding='utf-8')


shared_css = ROOT / 'assets/css/portfolio-pages.css'
css = shared_css.read_text(encoding='utf-8')
if '.links .nav-cta' not in css:
    css += '''
.links .nav-cta{padding:7px 11px;border:1px solid rgba(101,216,255,.45);border-radius:10px;color:var(--text);background:rgba(101,216,255,.08)}
.links .nav-cta:hover{background:rgba(101,216,255,.15)}
'''
shared_css.write_text(css, encoding='utf-8')

# Homepage uses embedded CSS.
index = ROOT / 'index.html'
text = index.read_text(encoding='utf-8')
if '.links .nav-cta' not in text:
    text = text.replace('</style>', '.links .nav-cta{padding:7px 11px;border:1px solid rgba(101,216,255,.45);border-radius:10px;color:var(--text);background:rgba(101,216,255,.08)}.links .nav-cta:hover{background:rgba(101,216,255,.15)}\n</style>', 1)
index.write_text(text, encoding='utf-8')

replace_header_footer(index, current='home', homepage=True)

for filename, current in {
    'recruiter-brief.html': 'recruiter',
    'case-studies.html': 'case-studies',
    'case-study-enterprise-automation.html': 'case-studies',
    'case-study-ai-agent-lab.html': 'case-studies',
    'contact.html': 'contact',
    'contact-success.html': 'contact',
}.items():
    replace_header_footer(ROOT / filename, current=current)

update_resume(ROOT / 'resume-tech.html', 'Engineering ATS Resume')
update_resume(ROOT / 'resume-leadership.html', 'Leadership ATS Resume')

faq = '''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Professional FAQ | David C. Fields, M.S.</title>
  <meta name="description" content="Frequently asked questions for recruiters, hiring leaders, clients, and collaborators evaluating David C. Fields for senior technology, infrastructure, automation, cybersecurity, leadership, contract, and consulting work.">
  <link rel="canonical" href="https://www.davidcfields.com/faq.html">
  <meta property="og:title" content="Professional FAQ | David C. Fields, M.S.">
  <meta property="og:description" content="Role fit, resume selection, experience context, work arrangements, consulting scope, certifications, and contact information.">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://www.davidcfields.com/faq.html">
  <link rel="stylesheet" href="assets/css/portfolio-pages.css">
  <style>
    .faq-list{display:grid;gap:14px}.faq-list details{border:1px solid var(--line);border-radius:18px;background:linear-gradient(180deg,rgba(17,36,59,.95),rgba(11,25,43,.96));box-shadow:var(--shadow);padding:0 22px}.faq-list summary{cursor:pointer;font-weight:850;font-size:1.08rem;padding:20px 34px 20px 0;position:relative;list-style:none}.faq-list summary::-webkit-details-marker{display:none}.faq-list summary:after{content:"+";position:absolute;right:0;top:17px;color:var(--accent);font-size:1.5rem}.faq-list details[open] summary:after{content:"–"}.faq-answer{padding:0 0 21px;color:var(--muted)}.faq-answer p:first-child{margin-top:0}.faq-answer ul{color:#d4e2ef}
  </style>
  <script type="application/ld+json">{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":"What roles are the strongest fit for David C. Fields?","acceptedAnswer":{"@type":"Answer","text":"Strong fits include senior infrastructure automation and platform engineering roles, engineering or architecture lead positions, infrastructure or technology management and director roles, cybersecurity and operations leadership, and carefully scoped consulting or contract engagements."}},{"@type":"Question","name":"Which resume should a recruiter use?","acceptedAnswer":{"@type":"Answer","text":"Use the Engineering ATS resume for technical infrastructure, automation, platform, DevOps, Linux, cloud, network automation, cybersecurity, and architecture roles. Use the Leadership ATS resume for management, director, consulting-lead, architecture-lead, and technology-operations roles."}},{"@type":"Question","name":"How is production experience distinguished from lab or training work?","acceptedAnswer":{"@type":"Answer","text":"Enterprise production work, consulting and operating-company work, product development, transferable experience, and lab or technical-validation work are presented separately. Current Linux, container, Kubernetes, and AI-agent lab work is not represented as primary enterprise production ownership."}},{"@type":"Question","name":"What consulting services are available through Lighthouse Digital Logistix?","acceptedAnswer":{"@type":"Answer","text":"Services include infrastructure modernization, cybersecurity, automation, AI-enabled workflows, software and website solutions, technical support, systems assessment, documentation, and business-systems consulting for appropriate small organizations, owner-operated companies, and individuals."}},{"@type":"Question","name":"What work arrangements are considered?","acceptedAnswer":{"@type":"Answer","text":"Suitable full-time W-2, contract, contract-to-hire, and consulting work may be considered, including remote roles, appropriate hybrid work in Central Ohio, and selected onsite or travel requirements when scope, compensation, workload, and logistics are reasonable."}},{"@type":"Question","name":"Which certifications are current?","acceptedAnswer":{"@type":"Answer","text":"Currently held credentials are CompTIA Security+, ITIL v3 Foundation, and VMware VCP5-DCV. CISSP, CISM, CISA, CCNP Enterprise, CCDP, CCSE, CCNA, and CCDA are identified as previously held rather than current."}}]}</script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
''' + page_header('faq') + '''
<main id="main" class="shell">
  <div class="breadcrumb"><a href="index.html">Home</a> / FAQ</div>
  <section class="hero">
    <p class="eyebrow">Professional FAQ</p>
    <h1>Answers for recruiters, hiring leaders, and prospective clients.</h1>
    <p class="lede">This page explains role fit, resume selection, experience context, work arrangements, consulting scope, certification status, and the most useful next step.</p>
    <div class="actions"><a class="btn primary" href="recruiter-brief.html">Read the recruiter brief</a><a class="btn" href="case-studies.html">Review case studies</a><a class="btn" href="index.html#contact">Start a conversation</a></div>
  </section>

  <section class="section faq-list" aria-label="Frequently asked questions">
    <details open><summary>What roles are the strongest fit?</summary><div class="faq-answer"><p>The strongest matches combine technical depth, operational responsibility, architecture, automation, cybersecurity, and leadership.</p><ul class="list-clean"><li>Senior Infrastructure Automation Engineer or Senior Platform Engineer</li><li>Platform Engineering, Infrastructure, or Architecture Lead</li><li>Infrastructure or Technology Manager</li><li>Director of Infrastructure, Automation, Technology Operations, or Managed Services</li><li>Senior DevOps, reliability-oriented infrastructure, network automation, or cybersecurity roles</li><li>Appropriate consulting and contract engagements through Lighthouse Digital Logistix</li></ul></div></details>

    <details><summary>Which resume should be used?</summary><div class="faq-answer"><p><strong>Engineering ATS Resume:</strong> use for technical infrastructure, automation, platform, DevOps, Linux, cloud, network automation, cybersecurity, and architecture positions.</p><p><strong>Leadership ATS Resume:</strong> use for management, director, consulting-lead, architecture-lead, service-delivery, and technology-operations positions.</p><p>The matching long-form master resume supplies supporting detail for customization, interviews, and qualification review.</p></div></details>

    <details><summary>Is David primarily an engineer or a leader?</summary><div class="faq-answer"><p>Both dimensions are material. The background combines senior hands-on engineering and architecture with team building, managed services, service delivery, vendor management, incident leadership, business operations, executive communication, and technology strategy.</p><p>The appropriate emphasis depends on the role rather than forcing all experience into one label.</p></div></details>

    <details><summary>How is enterprise production experience separated from lab work?</summary><div class="faq-answer"><p>Experience is deliberately classified by context:</p><ul class="list-clean"><li><strong>Enterprise production:</strong> regulated, mission-critical infrastructure, networking, cybersecurity, automation, incident management, and service operations.</li><li><strong>Consulting and operating-company production:</strong> real business systems, support, automation, websites, identity, SaaS applications, integrations, security, and continuity.</li><li><strong>Product development:</strong> CharterVantage requirements, architecture, workflows, databases, integrations, testing, deployment planning, and human-approval controls.</li><li><strong>Lab and technical validation:</strong> current Linux, Docker, Kubernetes/K3s, heterogeneous compute, AI-agent, container-image, logging, and secrets-isolation work.</li></ul><p>Lab experience is not presented as primary enterprise production ownership.</p></div></details>

    <details><summary>What is the context for cloud, containers, Kubernetes, and AI work?</summary><div class="faq-answer"><p>The background includes enterprise automation and cloud-capable infrastructure work, plus current hands-on consulting, software-product, and technical-validation work involving Linux, Docker, Kubernetes/K3s, GitHub Actions, GitHub Container Registry, APIs, AI agents, and human-in-the-loop controls.</p><p>Specific depth and production context should be evaluated from the Engineering Resume and case studies rather than inferred from a keyword list.</p></div></details>

    <details><summary>What consulting work is available through Lighthouse Digital Logistix?</summary><div class="faq-answer"><p>Appropriate engagements may include infrastructure modernization, cybersecurity assessment and improvement, automation, AI-enabled workflows, software and website solutions, technical support, systems integration, documentation, operational process improvement, and practical technology strategy.</p><p>Engagements should be clearly scoped around objectives, deliverables, timing, access requirements, risk, budget, and approval controls.</p></div></details>

    <details><summary>What work arrangements are considered?</summary><div class="faq-answer"><ul class="list-clean"><li>Remote opportunities across the United States</li><li>Appropriate hybrid roles in Central Ohio</li><li>Selected onsite work or travel when requirements are reasonable</li><li>Full-time W-2, contract, contract-to-hire, and consulting</li></ul><p>Current availability is time-sensitive, so recruiters and clients should confirm it through the contact form.</p></div></details>

    <details><summary>Which certifications are current?</summary><div class="faq-answer"><p><strong>Currently held:</strong> CompTIA Security+, ITIL v3 Foundation, and VMware VCP5-DCV.</p><p><strong>Previously held:</strong> CISSP, CISM, CISA, CCNP Enterprise, CCDP, CCSE, CCNA, and CCDA.</p><p>Historical credentials are disclosed as previous credentials and are not represented as active.</p></div></details>

    <details><summary>Can a role-specific resume be provided?</summary><div class="faq-answer"><p>Yes. The appropriate ATS master resume is used as the factual baseline, then tailored to the actual job description without inventing qualifications, changing chronology, or overstating production experience.</p></div></details>

    <details><summary>Are professional references available?</summary><div class="faq-answer"><p>Multiple professional references are available upon request. Reference contact details are shared privately at the appropriate stage rather than posted publicly.</p></div></details>

    <details><summary>What is the best way to make contact?</summary><div class="faq-answer"><p>Use the <a href="index.html#contact">professional inquiry form</a> and include the role or project, work arrangement, compensation or budget when appropriate, expected timing, key requirements, and the desired next step.</p></div></details>
  </section>
</main>
''' + page_footer() + '''
</body>
</html>
'''
(ROOT / 'faq.html').write_text(faq, encoding='utf-8')

print('FAQ created and navigation standardized.')
