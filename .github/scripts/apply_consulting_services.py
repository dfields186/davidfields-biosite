from __future__ import annotations

from pathlib import Path


def replace_once(path: str, old: str, new: str) -> None:
    file_path = Path(path)
    text = file_path.read_text(encoding="utf-8")
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"Expected one match in {path}, found {count}: {old[:100]!r}")
    file_path.write_text(text.replace(old, new, 1), encoding="utf-8")


consulting_page = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Consulting & Contract Services | David C. Fields, M.S.</title>
  <meta name="description" content="Selective consulting and contract services through Lighthouse Digital Logistix for infrastructure modernization, automation, cybersecurity, resilience, AI-enabled workflows, and technology leadership.">
  <link rel="canonical" href="https://davidcfields.com/consulting-services.html">
  <meta property="og:title" content="Consulting & Contract Services | David C. Fields, M.S.">
  <meta property="og:description" content="Infrastructure modernization, automation, cybersecurity, resilience, AI-enabled workflows, and technology leadership through Lighthouse Digital Logistix.">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://davidcfields.com/consulting-services.html">
  <link rel="stylesheet" href="assets/css/portfolio-pages.css">
  <meta name="robots" content="index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1">
  <meta name="author" content="David C. Fields, M.S.">
  <meta name="theme-color" content="#07111f">
  <meta property="og:site_name" content="David C. Fields, M.S.">
  <meta property="og:locale" content="en_US">
  <meta property="og:image" content="https://davidcfields.com/images/davidfields.jpg">
  <meta property="og:image:alt" content="Professional headshot of David C. Fields, M.S.">
  <meta name="twitter:card" content="summary">
  <meta name="twitter:title" content="Consulting & Contract Services | David C. Fields, M.S.">
  <meta name="twitter:description" content="Infrastructure modernization, automation, cybersecurity, resilience, AI-enabled workflows, and technology leadership through Lighthouse Digital Logistix.">
  <meta name="twitter:image" content="https://davidcfields.com/images/davidfields.jpg">
  <link rel="icon" href="/favicon.svg" type="image/svg+xml">
  <link rel="manifest" href="/site.webmanifest">
  <link rel="me" href="https://www.linkedin.com/in/david-c-fields">
  <link rel="me" href="https://github.com/davidcfields">
  <script type="application/ld+json">{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":"https://davidcfields.com/"},{"@type":"ListItem","position":2,"name":"Consulting & Contract Services","item":"https://davidcfields.com/consulting-services.html"}]}</script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="header">
  <nav class="nav shell" aria-label="Primary navigation">
    <a class="brand" href="index.html">David C. Fields, <span>M.S.</span></a>
    <div class="links"><a href="index.html#about">About</a><a href="index.html#experience">Experience</a><a href="case-studies.html">Case Studies</a><a href="index.html#resumes">Resumes</a><a href="faq.html">FAQ</a><a href="contact.html">Contact</a><a class="nav-cta" href="recruiter-brief.html">Recruiter Brief</a></div>
  </nav>
</header>
<main id="main" class="shell">
<div class="breadcrumb"><a href="index.html">Home</a> / Consulting &amp; Contract Services</div>
<section class="hero">
  <p class="eyebrow">Selective engagements through Lighthouse Digital Logistix</p>
  <h1>Practical technology modernization with senior-level engineering and operating judgment.</h1>
  <p class="lede">I provide carefully scoped consulting, contract, and advisory services where infrastructure, cybersecurity, automation, resilience, service operations, and business requirements must be addressed together rather than as isolated technical tasks.</p>
  <div class="actions">
    <a class="btn primary" href="contact.html">Discuss an engagement</a>
    <a class="btn" href="infrastructure-automation-security-modernization.html">Primary market focus</a>
    <a class="btn" href="case-studies.html">Review case studies</a>
    <a class="btn" href="resume-tech.html">Engineering resume</a>
    <a class="btn" href="resume-leadership.html">Leadership resume</a>
  </div>
</section>

<section class="section">
  <div class="intro"><p class="eyebrow">Who this serves</p><h2>Organizations that need experienced help without adding unnecessary complexity.</h2><p>Engagements are best suited to situations where the technology problem also affects security, workflow, cost, staffing, maintainability, customer experience, continuity, or operational risk.</p></div>
  <div class="grid4">
    <article class="card"><h3>Small and owner-operated businesses</h3><p>Organizations that need senior guidance, stabilization, modernization, automation, or project delivery but do not maintain a full internal technology organization.</p></article>
    <article class="card"><h3>Regulated and mission-critical organizations</h3><p>Teams in financial services, government, defense, healthcare, utilities, transportation, manufacturing, and other risk-sensitive environments.</p></article>
    <article class="card"><h3>Technology and operations leaders</h3><p>Leaders who need an independent architecture review, modernization roadmap, automation plan, transition strategy, or experienced technical sounding board.</p></article>
    <article class="card"><h3>Teams with a temporary capability gap</h3><p>Organizations that need senior engineering, architecture, automation, documentation, or leadership support for a defined period or outcome.</p></article>
  </div>
</section>

<section class="section">
  <div class="intro"><p class="eyebrow">Engagement areas</p><h2>Focused services tied to practical business and operational outcomes.</h2></div>
  <div class="grid3">
    <article class="card"><h3>Infrastructure & Automation Assessment</h3><p>Review infrastructure, recurring operational work, service dependencies, failure points, documentation, and automation opportunities across network, Linux, Windows, cloud, SaaS, identity, backup, monitoring, and business systems.</p><ul class="list-clean"><li>Current-state findings</li><li>Prioritized risk and improvement backlog</li><li>Automation candidates and dependencies</li><li>Practical implementation roadmap</li></ul></article>
    <article class="card"><h3>Security, Resilience & Continuity Review</h3><p>Evaluate cybersecurity controls, identity, backup, recovery, monitoring, incident readiness, vendor dependencies, operational continuity, and recovery assumptions.</p><ul class="list-clean"><li>Risk and control observations</li><li>Recovery and continuity gaps</li><li>Prioritized modernization actions</li><li>Documentation and testing recommendations</li></ul></article>
    <article class="card"><h3>Platform & DevSecOps Architecture Review</h3><p>Assess platform design, Linux and cloud foundations, infrastructure as code, CI/CD, containers, observability, secrets, service workflows, and supportability.</p><ul class="list-clean"><li>Architecture and operating-model review</li><li>Security and supportability concerns</li><li>Tooling and integration recommendations</li><li>Phased adoption plan</li></ul></article>
    <article class="card"><h3>Workflow & Incident Automation Design</h3><p>Identify repetitive work and design controlled automation using Python, Ansible/AWX, Terraform, APIs, ServiceNow-related workflows, notifications, reporting, and human approval where required.</p><ul class="list-clean"><li>Workflow mapping</li><li>Automation design and controls</li><li>Exception and approval handling</li><li>Implementation backlog or prototype</li></ul></article>
    <article class="card"><h3>AI Operations & Governance Design</h3><p>Design practical AI-enabled workflows, agent infrastructure, integrations, logging, secrets isolation, testing, decision boundaries, and human-review controls for operational use.</p><ul class="list-clean"><li>Use-case and risk assessment</li><li>Human-in-the-loop control design</li><li>Architecture and integration plan</li><li>Testing, logging, and governance requirements</li></ul></article>
    <article class="card"><h3>Fractional Technology Leadership & Advisory</h3><p>Provide temporary or part-time senior guidance for roadmaps, architecture, vendor selection, standards, documentation, project recovery, technical mentoring, transition planning, and executive communication.</p><ul class="list-clean"><li>Decision support and prioritization</li><li>Roadmaps and operating standards</li><li>Vendor and solution evaluation</li><li>Leadership and transition support</li></ul></article>
  </div>
</section>

<section class="section">
  <div class="intro"><p class="eyebrow">Typical outputs</p><h2>Usable work products rather than generic recommendations.</h2></div>
  <div class="grid3">
    <article class="panel"><h3>Decision materials</h3><p>Executive findings, prioritized options, risk summaries, cost and dependency considerations, implementation sequencing, and approval points.</p></article>
    <article class="panel"><h3>Technical artifacts</h3><p>Architecture diagrams, automation designs, workflow maps, configuration standards, runbooks, implementation backlogs, test plans, and sanitized reusable patterns.</p></article>
    <article class="panel"><h3>Operational handoff</h3><p>Documentation, ownership assignments, support procedures, training, transition notes, review checkpoints, and follow-on recommendations.</p></article>
  </div>
</section>

<section class="section">
  <div class="intro"><p class="eyebrow">How an engagement starts</p><h2>Controlled scope before commitment.</h2></div>
  <div class="steps">
    <article class="step"><h3>Initial fit conversation</h3><p>Clarify the objective, urgency, operating environment, decision process, access constraints, expected outcomes, and whether the engagement is an appropriate fit.</p></article>
    <article class="step"><h3>Written scope and assumptions</h3><p>Define deliverables, responsibilities, exclusions, timeline assumptions, access needs, fees, payment terms, review points, and approval controls before work begins.</p></article>
    <article class="step"><h3>Discovery and evidence review</h3><p>Gather the minimum information required, interview stakeholders, review existing systems and documentation, and validate assumptions without requesting unnecessary sensitive data.</p></article>
    <article class="step"><h3>Delivery with review checkpoints</h3><p>Provide findings, designs, prototypes, documentation, or implementation work in controlled increments so decisions and risks remain visible.</p></article>
    <article class="step"><h3>Handoff and next-step decision</h3><p>Complete documentation and knowledge transfer, identify unresolved risks, and agree whether implementation, ongoing advisory support, or closure is appropriate.</p></article>
  </div>
</section>

<section class="section">
  <div class="grid2">
    <article class="panel">
      <p class="eyebrow">Experience classification</p>
      <h2>Claims remain tied to the correct context.</h2>
      <p>Enterprise automation, networking, cybersecurity, managed services, incident response, disaster recovery, and leadership experience are distinguished from current Lighthouse consulting, CharterVantage product development, and Linux, container, Kubernetes/K3s, and AI-agent lab or technical-validation work.</p>
    </article>
    <article class="panel">
      <p class="eyebrow">Work arrangements</p>
      <h2>Remote-first with selected Central Ohio work.</h2>
      <p>Engagements may include remote advisory or delivery, selected onsite work in Central Ohio, defined contract assignments, fractional leadership, architecture reviews, assessments, automation design, implementation, or transition support.</p>
    </article>
  </div>
  <div class="callout warn"><strong>Important boundaries:</strong> Website contact does not create a contract, price commitment, employment acceptance, compliance attestation, legal opinion, penetration-test authorization, managed 24x7 support obligation, or emergency-response commitment. Scope, access, professional responsibilities, and fees require a separate written agreement. Qualified legal, tax, accounting, compliance, or specialist security advice should be obtained when required.</div>
  <div class="actions"><a class="btn primary" href="contact.html">Start with a professional inquiry</a><a class="btn" href="recruiter-brief.html">Review recruiter brief</a></div>
</section>
</main>
<footer class="footer"><div class="shell footer-row"><div>© 2026 David C. Fields. Professional biography, portfolio, resumes, and consulting information.</div><div class="footer-links"><a href="index.html">Home</a><a href="consulting-services.html">Consulting</a><a href="recruiter-brief.html">Recruiter Brief</a><a href="case-studies.html">Case Studies</a><a href="index.html#resumes">Resumes</a><a href="faq.html">FAQ</a><a href="contact.html">Contact</a></div></div></footer>
</body>
</html>
"""

Path("consulting-services.html").write_text(consulting_page, encoding="utf-8")

replace_once(
    "index.html",
    '<a class="btn" href="infrastructure-automation-security-modernization.html">Primary market focus</a><a class="btn" href="case-studies.html">Review case studies</a>',
    '<a class="btn" href="infrastructure-automation-security-modernization.html">Primary market focus</a><a class="btn" href="consulting-services.html">Consulting services</a><a class="btn" href="case-studies.html">Review case studies</a>',
)

replace_once(
    "recruiter-brief.html",
    '    <a class="btn primary" href="infrastructure-automation-security-modernization.html">View primary market focus</a>\n    <a class="btn" href="resume-leadership.html">Leadership resume</a>',
    '    <a class="btn primary" href="infrastructure-automation-security-modernization.html">View primary market focus</a>\n    <a class="btn" href="consulting-services.html">Consulting services</a>\n    <a class="btn" href="resume-leadership.html">Leadership resume</a>',
)

replace_once(
    "infrastructure-automation-security-modernization.html",
    '    <a class="btn primary" href="recruiter-brief.html">Read recruiter brief</a>\n    <a class="btn" href="case-studies.html">Review case studies</a>',
    '    <a class="btn primary" href="recruiter-brief.html">Read recruiter brief</a>\n    <a class="btn" href="consulting-services.html">Consulting services</a>\n    <a class="btn" href="case-studies.html">Review case studies</a>',
)

contact_card = '''      <article class="card" style="margin-top:18px">
        <p class="kicker">Consulting and contract services</p>
        <h3>Need a defined assessment, roadmap, or modernization engagement?</h3>
        <p>Review the selective services available through Lighthouse Digital Logistix before submitting an inquiry.</p>
        <div class="card-actions"><a class="btn" href="consulting-services.html">View consulting services</a></div>
      </article>
'''
replace_once(
    "contact.html",
    '      <div class="privacy"><strong>Privacy:</strong>',
    contact_card + '      <div class="privacy"><strong>Privacy:</strong>',
)

replace_once(
    "sitemap.xml",
    '  <url><loc>https://davidcfields.com/infrastructure-automation-security-modernization.html</loc><lastmod>2026-08-05</lastmod></url>\n',
    '  <url><loc>https://davidcfields.com/infrastructure-automation-security-modernization.html</loc><lastmod>2026-08-05</lastmod></url>\n  <url><loc>https://davidcfields.com/consulting-services.html</loc><lastmod>2026-08-05</lastmod></url>\n',
)
replace_once(
    "sitemap.xml",
    '  <url><loc>https://davidcfields.com/contact.html</loc><lastmod>2026-08-04</lastmod></url>',
    '  <url><loc>https://davidcfields.com/contact.html</loc><lastmod>2026-08-05</lastmod></url>',
)

replace_once(
    ".github/scripts/validate_site.py",
    '    "infrastructure-automation-security-modernization.html": "/infrastructure-automation-security-modernization.html",\n',
    '    "infrastructure-automation-security-modernization.html": "/infrastructure-automation-security-modernization.html",\n    "consulting-services.html": "/consulting-services.html",\n',
)

print("Consulting services package applied successfully.")
