from pathlib import Path


def replace_exact(text: str, old: str, new: str, label: str, expected: int = 1) -> str:
    count = text.count(old)
    if count != expected:
        raise RuntimeError(f"Expected {expected} occurrence(s) of {label}, found {count}")
    return text.replace(old, new)


# Homepage: sharpen the primary identity and add a path to the focused positioning page.
index_path = Path("index.html")
index = index_path.read_text(encoding="utf-8")

old_home_description = "Senior infrastructure, automation, platform, cybersecurity, and technology operations leader in Central Ohio, open to remote, hybrid, contract, and consulting roles."
new_home_description = "Senior infrastructure automation and security modernization leader serving regulated and mission-critical organizations; open to employment, contract, and consulting roles."
index = replace_exact(index, old_home_description, new_home_description, "homepage description", expected=4)
index = replace_exact(index, '"dateModified":"2026-08-04"', '"dateModified":"2026-08-05"', "homepage dateModified")
index = replace_exact(index, '"jobTitle":"Senior Technology, Infrastructure and Automation Leader"', '"jobTitle":"Senior Infrastructure Automation and Security Modernization Leader"', "homepage structured-data job title")
index = replace_exact(
    index,
    '<p class="lede">Senior technology and operations leader with 35+ years of hands-on experience designing, securing, automating, modernizing, and operating mission-critical environments across financial services, government, defense, healthcare, critical infrastructure, consulting, and small business.</p>',
    '<p class="lede">Senior infrastructure automation and security modernization leader with 35+ years of hands-on experience designing, securing, automating, modernizing, and operating mission-critical environments across financial services, government, defense, healthcare, critical infrastructure, consulting, and small business.</p>',
    "homepage hero positioning",
)
index = replace_exact(
    index,
    '<div class="actions"><a class="btn primary" href="recruiter-brief.html">60-second recruiter brief</a><a class="btn" href="case-studies.html">Review case studies</a><a class="btn" href="#resumes">View current resumes</a><a class="btn" href="#contact">Discuss an opportunity</a></div>',
    '<div class="actions"><a class="btn primary" href="recruiter-brief.html">60-second recruiter brief</a><a class="btn" href="infrastructure-automation-security-modernization.html">Primary market focus</a><a class="btn" href="case-studies.html">Review case studies</a><a class="btn" href="#resumes">View current resumes</a><a class="btn" href="#contact">Discuss an opportunity</a></div>',
    "homepage action buttons",
)
index = replace_exact(
    index,
    '<div class="muted">Senior Technology, Infrastructure & Automation Leader</div>',
    '<div class="muted">Infrastructure Automation & Security Modernization Leader</div>',
    "homepage identity subtitle",
)
index_path.write_text(index, encoding="utf-8")


# Recruiter brief: narrow the message around the strongest market intersection.
brief_path = Path("recruiter-brief.html")
brief = brief_path.read_text(encoding="utf-8")

old_brief_title = "Recruiter Brief | David C. Fields, M.S."
new_brief_title = "Recruiter Brief | Infrastructure Automation & Security Modernization"
brief = replace_exact(brief, old_brief_title, new_brief_title, "recruiter brief title", expected=3)
old_brief_description = "A concise recruiter brief covering David C. Fields&#x27; strongest technology leadership, infrastructure, automation, cybersecurity, consulting, and engineering qualifications."
new_brief_description = "Recruiter brief for David C. Fields: infrastructure automation, security modernization, platform operations, public-sector technology, and technical leadership."
brief = replace_exact(brief, old_brief_description, new_brief_description, "recruiter brief description", expected=3)
brief = replace_exact(
    brief,
    '<h1>Senior technology leadership with deep infrastructure and automation roots.</h1>\n  <p class="lede">David C. Fields, M.S., is a senior technology and operations professional whose background combines enterprise infrastructure, networking, cybersecurity, automation, architecture, consulting, managed services, business operations, and people leadership.</p>',
    '<h1>Infrastructure automation, security modernization, and technology leadership for mission-critical environments.</h1>\n  <p class="lede">David C. Fields, M.S., combines enterprise infrastructure, networking, cybersecurity, automation, architecture, platform operations, consulting, managed services, and people leadership. His strongest fit is where regulated or operationally critical systems must become more secure, observable, repeatable, resilient, and supportable.</p>',
    "recruiter brief hero",
)
brief = replace_exact(
    brief,
    '  <div class="actions">\n    <a class="btn primary" href="resume-leadership.html">Leadership resume</a>\n    <a class="btn" href="resume-tech.html">Engineering resume</a>\n    <a class="btn" href="case-studies.html">Review case studies</a>\n    <a class="btn" href="index.html#contact">Contact David</a>\n  </div>',
    '  <div class="actions">\n    <a class="btn primary" href="infrastructure-automation-security-modernization.html">View primary market focus</a>\n    <a class="btn" href="resume-leadership.html">Leadership resume</a>\n    <a class="btn" href="resume-tech.html">Engineering resume</a>\n    <a class="btn" href="case-studies.html">Review case studies</a>\n    <a class="btn" href="index.html#contact">Contact David</a>\n  </div>',
    "recruiter brief actions",
)
old_best_fit = '''<section class="section">
  <div class="intro"><p class="eyebrow">Best-fit opportunities</p><h2>Where the background is strongest.</h2></div>
  <div class="grid3">
    <article class="card"><h3>Infrastructure & Platform Leadership</h3><p>Infrastructure manager, technology manager, platform engineering lead, infrastructure director, architecture lead, and operations leadership roles.</p></article>
    <article class="card"><h3>Senior Technical Roles</h3><p>Infrastructure automation, platform engineering, DevOps, network automation, Linux and systems engineering, cybersecurity, and technical architecture.</p></article>
    <article class="card"><h3>Consulting & Contract Work</h3><p>Appropriate W-2, contract, contract-to-hire, and carefully scoped consulting engagements through Lighthouse Digital Logistix.</p></article>
  </div>
</section>'''
new_best_fit = '''<section class="section">
  <div class="intro"><p class="eyebrow">Best-fit opportunities</p><h2>A focused intersection of engineering, security, operations, and leadership.</h2></div>
  <div class="grid3">
    <article class="card"><h3>Infrastructure Automation & Security Modernization</h3><p>Principal or senior automation engineering, infrastructure modernization, network-security automation, architecture, and technical-lead roles in regulated or mission-critical environments.</p></article>
    <article class="card"><h3>Platform, DevSecOps & Operations Leadership</h3><p>Platform engineering lead, infrastructure manager, technology manager, director, architecture lead, and senior operations roles requiring both technical credibility and service-delivery judgment.</p></article>
    <article class="card"><h3>Public Sector, Critical Infrastructure & Consulting</h3><p>Government, defense, utility, healthcare, financial-services, transportation, and consulting work involving modernization, resilience, cybersecurity, automation, continuity, and operational risk.</p></article>
  </div>
</section>'''
brief = replace_exact(brief, old_best_fit, new_best_fit, "recruiter brief best-fit section")

strongest_marker = '''<section class="section">
  <div class="intro"><p class="eyebrow">Strongest evidence</p><h2>What differentiates David.</h2></div>'''
market_section = '''<section class="section">
  <article class="panel">
    <p class="eyebrow">Primary market position</p>
    <h2>Senior Infrastructure Automation & Security Modernization Leader</h2>
    <p>This position concentrates David’s broad background into one practical value proposition: modernize complex infrastructure by connecting automation, cybersecurity, platform operations, resilience, documentation, service management, and leadership rather than treating them as separate disciplines.</p>
    <div class="actions"><a class="btn primary" href="infrastructure-automation-security-modernization.html">Review the focused positioning</a></div>
  </article>
</section>

'''
brief = replace_exact(brief, strongest_marker, market_section + strongest_marker, "recruiter brief market-focus insertion")
brief_path.write_text(brief, encoding="utf-8")


# New focused market-positioning page.
market_page = '''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Infrastructure Automation & Security Modernization | David C. Fields, M.S.</title>
  <meta name="description" content="Infrastructure automation, cybersecurity, platform operations, public-sector modernization, resilience, and AI operations leadership for regulated and mission-critical organizations.">
  <link rel="canonical" href="https://davidcfields.com/infrastructure-automation-security-modernization.html">
  <meta property="og:title" content="Infrastructure Automation & Security Modernization | David C. Fields, M.S.">
  <meta property="og:description" content="Infrastructure automation, cybersecurity, platform operations, public-sector modernization, resilience, and AI operations leadership for regulated and mission-critical organizations.">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://davidcfields.com/infrastructure-automation-security-modernization.html">
  <link rel="stylesheet" href="assets/css/portfolio-pages.css">
  <meta name="robots" content="index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1">
  <meta name="author" content="David C. Fields, M.S.">
  <meta name="theme-color" content="#07111f">
  <meta property="og:site_name" content="David C. Fields, M.S.">
  <meta property="og:locale" content="en_US">
  <meta property="og:image" content="https://davidcfields.com/images/davidfields.jpg">
  <meta property="og:image:alt" content="Professional headshot of David C. Fields, M.S.">
  <meta name="twitter:card" content="summary">
  <meta name="twitter:title" content="Infrastructure Automation & Security Modernization | David C. Fields, M.S.">
  <meta name="twitter:description" content="Infrastructure automation, cybersecurity, platform operations, public-sector modernization, resilience, and AI operations leadership for regulated and mission-critical organizations.">
  <meta name="twitter:image" content="https://davidcfields.com/images/davidfields.jpg">
  <link rel="icon" href="/favicon.svg" type="image/svg+xml">
  <link rel="manifest" href="/site.webmanifest">
  <link rel="me" href="https://www.linkedin.com/in/david-c-fields">
  <link rel="me" href="https://github.com/davidcfields">
  <script type="application/ld+json">{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":"https://davidcfields.com/"},{"@type":"ListItem","position":2,"name":"Infrastructure Automation & Security Modernization","item":"https://davidcfields.com/infrastructure-automation-security-modernization.html"}]}</script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="header">
  <nav class="nav shell" aria-label="Primary navigation">
    <a class="brand" href="index.html">David C. Fields, <span>M.S.</span></a>
    <div class="links"><a href="index.html#about">About</a><a href="index.html#experience">Experience</a><a href="case-studies.html">Case Studies</a><a href="index.html#resumes">Resumes</a><a href="faq.html">FAQ</a><a href="index.html#contact">Contact</a><a class="nav-cta" href="recruiter-brief.html">Recruiter Brief</a></div>
  </nav>
</header>
<main id="main" class="shell">
<div class="breadcrumb"><a href="index.html">Home</a> / Infrastructure Automation &amp; Security Modernization</div>
<section class="hero">
  <p class="eyebrow">Primary market focus</p>
  <h1>Infrastructure automation and security modernization for regulated, mission-critical environments.</h1>
  <p class="lede">I help connect infrastructure engineering, automation, cybersecurity, platform operations, resilience, service management, and leadership so complex environments become more secure, observable, repeatable, and supportable.</p>
  <div class="actions">
    <a class="btn primary" href="recruiter-brief.html">Read recruiter brief</a>
    <a class="btn" href="case-studies.html">Review case studies</a>
    <a class="btn" href="resume-tech.html">Engineering resume</a>
    <a class="btn" href="resume-leadership.html">Leadership resume</a>
    <a class="btn" href="index.html#contact">Discuss an opportunity</a>
  </div>
</section>

<section aria-label="Career evidence" class="grid4">
  <div class="metric"><b>35+</b><span>years across infrastructure, security, automation, operations, consulting, and leadership</span></div>
  <div class="metric"><b>10,000+</b><span>annual incidents and requests supported by enterprise automation</span></div>
  <div class="metric"><b>10+</b><span>engineers and technicians recruited, developed, and led</span></div>
  <div class="metric"><b>$1M+</b><span>managed-services and engineering practice directed</span></div>
</section>

<section class="section">
  <div class="intro"><p class="eyebrow">Why this focus</p><h2>A scarce combination is more valuable than a list of unrelated specialties.</h2><p>The strongest professional value is not any one tool or title. It is the ability to connect deep infrastructure and network experience with cybersecurity, automation, architecture, operational accountability, business continuity, consulting, and people leadership.</p></div>
  <div class="grid3">
    <article class="card"><h3>Engineering depth</h3><p>Enterprise networking, Linux and Unix, Windows, virtualization, firewalls, remote access, monitoring, incident response, cloud-capable platforms, APIs, containers, and automation.</p></article>
    <article class="card"><h3>Operational judgment</h3><p>24x7 support, service management, incident and change coordination, disaster recovery, business continuity, documentation, escalation, vendor management, and executive visibility.</p></article>
    <article class="card"><h3>Leadership range</h3><p>Architecture, consulting, team building, managed services, technical mentoring, roadmaps, stakeholder communication, product development, and ownership of business-critical technology.</p></article>
  </div>
</section>

<section class="section">
  <div class="intro"><p class="eyebrow">Three focused solution areas</p><h2>Where the background can create the most practical value.</h2></div>
  <div class="grid3">
    <article class="card"><h3>Secure Platform & Infrastructure Automation</h3><p>Automate repetitive infrastructure and security operations, improve observability, integrate service workflows, strengthen repeatability, and reduce manual dependence across network, firewall, Linux, cloud, and platform environments.</p><ul class="tags"><li>Python</li><li>Ansible/AWX</li><li>Terraform</li><li>APIs</li><li>ServiceNow</li><li>Linux</li></ul></article>
    <article class="card"><h3>Regulated & Public-Sector Technology Modernization</h3><p>Support modernization, resilience, cybersecurity, continuity, standards, and operational improvement in financial services, government, defense, healthcare, utilities, transportation, and other risk-sensitive environments.</p><ul class="tags"><li>Cybersecurity</li><li>Architecture</li><li>DR/BCP</li><li>Monitoring</li><li>Risk</li><li>ITIL</li></ul></article>
    <article class="card"><h3>AI Infrastructure, Governance & Operational Automation</h3><p>Design controlled AI-enabled workflows, agent infrastructure, integrations, logging, secrets isolation, testing, and human approval gates. Current work is consulting, product development, lab, and technical validation—not represented as long-term enterprise production ML ownership.</p><ul class="tags"><li>AI agents</li><li>Docker</li><li>Kubernetes/K3s</li><li>Logging</li><li>Secrets</li><li>Human review</li></ul></article>
  </div>
</section>

<section class="section">
  <div class="intro"><p class="eyebrow">Evidence</p><h2>Documented outcomes and operating context.</h2></div>
  <div class="evidence">
    <div class="evidence-row"><strong>Enterprise automation</strong><div>Designed, implemented, maintained, and supported Python, Ansible/AWX, Terraform, Azure DevOps, ServiceNow, PagerDuty, Rundeck, API, Docker, and Kubernetes-related automation in a regulated 24x7 financial-services environment. Automation accounted for more than half of incoming ticket volume and supported 10,000+ incidents and requests annually.</div></div>
    <div class="evidence-row"><strong>Security and resilience analysis</strong><div>Developed Palo Alto firewall analysis that evaluated hundreds of thousands of objects and rules in minutes, identified missing or incorrect recovery policies, and generated structured reporting for disaster-recovery and site-recovery readiness.</div></div>
    <div class="evidence-row"><strong>Leadership and managed services</strong><div>Helped build and direct a $1M+ managed-services and engineering practice, recruited and led more than 10 engineers and technicians, and established centralized monitoring, ticketing, escalation, documentation, service-desk, and reporting capabilities.</div></div>
    <div class="evidence-row"><strong>Regulated and mission-critical sectors</strong><div>Experience spans financial services, Ohio state government, federal and Department of Defense settings, healthcare, critical infrastructure, utilities, manufacturing, consulting, and regulated transportation operations.</div></div>
    <div class="evidence-row"><strong>Current modernization work</strong><div>Through Lighthouse Digital Logistix, CharterVantage, public repositories, and a clearly labeled technical-validation lab, current work includes Linux, containers, Kubernetes/K3s, automation, AI-enabled workflows, SaaS architecture, APIs, documentation, deployment planning, secrets isolation, and human-approval controls.</div></div>
  </div>
</section>

<section class="section">
  <div class="intro"><p class="eyebrow">Experience classification</p><h2>Credibility depends on describing work in the right context.</h2></div>
  <div class="grid2">
    <article class="panel"><h3>Enterprise production experience</h3><p>Financial-services automation, enterprise networking, network security, firewalls, monitoring, incident response, service workflows, architecture, government and defense systems, managed services, disaster recovery, and business continuity.</p></article>
    <article class="panel"><h3>Consulting and operating-company work</h3><p>Infrastructure modernization, cybersecurity controls, identity, cloud and SaaS systems, APIs, websites, endpoints, backups, business applications, automation, documentation, vendor management, and operational risk.</p></article>
    <article class="panel"><h3>Product development</h3><p>CharterVantage requirements, workflow and database design, architecture, integrations, testing, documentation, deployment planning, AI-assisted capabilities, and human approval for customer-facing and financial actions.</p></article>
    <article class="panel"><h3>Lab and technical validation</h3><p>Current RHEL and Ubuntu, KVM/QEMU, Docker, Kubernetes/K3s, ARM64 and x86-64 nodes, GitHub Container Registry, AI-agent infrastructure, logging, configuration management, and secrets isolation are labeled as lab, development, and validation work.</p></article>
  </div>
</section>

<section class="section">
  <div class="intro"><p class="eyebrow">Best-fit roles and engagements</p><h2>Focused enough to be distinctive; broad enough to support multiple income paths.</h2></div>
  <div class="grid3">
    <article class="card"><h3>Senior and principal technical roles</h3><ul class="list-clean"><li>Principal Infrastructure Automation Engineer</li><li>Senior Platform or DevSecOps Engineer</li><li>Security or Infrastructure Architect</li><li>Network Security Automation Engineer</li><li>Senior Linux or Systems Automation Engineer</li></ul></article>
    <article class="card"><h3>Leadership roles</h3><ul class="list-clean"><li>Platform Engineering Lead</li><li>Infrastructure or Technology Manager</li><li>Director of Infrastructure or Automation</li><li>Architecture or Consulting Lead</li><li>Senior Manager, Platform or Infrastructure Operations</li></ul></article>
    <article class="card"><h3>Consulting engagements</h3><ul class="list-clean"><li>Infrastructure and automation assessment</li><li>Security and resilience modernization roadmap</li><li>Operational workflow and incident automation</li><li>AI operations and governance design</li><li>Architecture, documentation, and transition planning</li></ul></article>
  </div>
  <div class="callout"><strong>Work arrangements:</strong> Appropriate full-time employment, contract, contract-to-hire, and carefully scoped consulting engagements. Remote opportunities are preferred, with suitable hybrid or selected onsite work in Central Ohio.</div>
</section>
</main>
<footer class="footer"><div class="shell footer-row"><div>© 2026 David C. Fields. Professional biography, portfolio, and resumes.</div><div class="footer-links"><a href="index.html">Home</a><a href="recruiter-brief.html">Recruiter Brief</a><a href="case-studies.html">Case Studies</a><a href="index.html#resumes">Resumes</a><a href="faq.html">FAQ</a><a href="index.html#contact">Contact</a></div></div></footer>
</body>
</html>
'''
Path("infrastructure-automation-security-modernization.html").write_text(market_page, encoding="utf-8")


# Add the new canonical page to the sitemap and update modified pages.
sitemap_path = Path("sitemap.xml")
sitemap = sitemap_path.read_text(encoding="utf-8")
sitemap = replace_exact(sitemap, '<url><loc>https://davidcfields.com/</loc><lastmod>2026-08-04</lastmod></url>', '<url><loc>https://davidcfields.com/</loc><lastmod>2026-08-05</lastmod></url>', "homepage sitemap date")
sitemap = replace_exact(sitemap, '<url><loc>https://davidcfields.com/recruiter-brief.html</loc><lastmod>2026-08-04</lastmod></url>', '<url><loc>https://davidcfields.com/recruiter-brief.html</loc><lastmod>2026-08-05</lastmod></url>\n  <url><loc>https://davidcfields.com/infrastructure-automation-security-modernization.html</loc><lastmod>2026-08-05</lastmod></url>', "recruiter sitemap entry")
sitemap_path.write_text(sitemap, encoding="utf-8")


# Extend the quality validator to require the new page.
validator_path = Path(".github/scripts/validate_site.py")
validator = validator_path.read_text(encoding="utf-8")
validator = replace_exact(
    validator,
    '    "recruiter-brief.html": "/recruiter-brief.html",\n',
    '    "recruiter-brief.html": "/recruiter-brief.html",\n    "infrastructure-automation-security-modernization.html": "/infrastructure-automation-security-modernization.html",\n',
    "validator route insertion",
)
validator_path.write_text(validator, encoding="utf-8")

print("Scarcity positioning package applied successfully.")
