from __future__ import annotations

import html
import json
import re
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(".")
SITE = "https://davidcfields.com"
LASTMOD = "2026-08-04"
IMAGE = f"{SITE}/images/davidfields.jpg"

INDEXABLE = {
    "index.html": "/",
    "recruiter-brief.html": "/recruiter-brief.html",
    "case-studies.html": "/case-studies.html",
    "case-study-enterprise-automation.html": "/case-study-enterprise-automation.html",
    "case-study-ai-agent-lab.html": "/case-study-ai-agent-lab.html",
    "faq.html": "/faq.html",
    "contact.html": "/contact.html",
    "resume-tech.html": "/resume-tech.html",
    "resume-leadership.html": "/resume-leadership.html",
}

NOINDEX = {"about.html", "resume.html", "contact-success.html", "404.html"}

BREADCRUMBS = {
    "recruiter-brief.html": [("Home", "/"), ("Recruiter Brief", "/recruiter-brief.html")],
    "case-studies.html": [("Home", "/"), ("Case Studies", "/case-studies.html")],
    "case-study-enterprise-automation.html": [
        ("Home", "/"),
        ("Case Studies", "/case-studies.html"),
        ("Enterprise Infrastructure Automation", "/case-study-enterprise-automation.html"),
    ],
    "case-study-ai-agent-lab.html": [
        ("Home", "/"),
        ("Case Studies", "/case-studies.html"),
        ("Distributed AI-Agent Lab", "/case-study-ai-agent-lab.html"),
    ],
    "faq.html": [("Home", "/"), ("Professional FAQ", "/faq.html")],
    "contact.html": [("Home", "/"), ("Contact", "/contact.html")],
    "resume-tech.html": [("Home", "/"), ("Engineering ATS Resume", "/resume-tech.html")],
    "resume-leadership.html": [("Home", "/"), ("Leadership ATS Resume", "/resume-leadership.html")],
}

COMMON_TAG_PATTERNS = [
    r'\s*<meta name="robots"[^>]*>',
    r'\s*<meta name="author"[^>]*>',
    r'\s*<meta name="theme-color"[^>]*>',
    r'\s*<meta property="og:site_name"[^>]*>',
    r'\s*<meta property="og:locale"[^>]*>',
    r'\s*<meta property="og:image"[^>]*>',
    r'\s*<meta property="og:image:alt"[^>]*>',
    r'\s*<meta name="twitter:card"[^>]*>',
    r'\s*<meta name="twitter:title"[^>]*>',
    r'\s*<meta name="twitter:description"[^>]*>',
    r'\s*<meta name="twitter:image"[^>]*>',
    r'\s*<link rel="icon"[^>]*>',
    r'\s*<link rel="manifest"[^>]*>',
    r'\s*<link rel="me"[^>]*>',
]


def extract(pattern: str, text: str, label: str) -> str:
    match = re.search(pattern, text, flags=re.I | re.S)
    if not match:
        raise RuntimeError(f"Missing {label}")
    return match.group(1).strip()


def remove_generated_tags(text: str) -> str:
    for pattern in COMMON_TAG_PATTERNS:
        text = re.sub(pattern, "", text, flags=re.I)
    text = re.sub(
        r'\s*<script type="application/ld\+json" data-seo="breadcrumb">.*?</script>',
        "",
        text,
        flags=re.I | re.S,
    )
    return text


def breadcrumb_script(items: list[tuple[str, str]]) -> str:
    payload = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {
                "@type": "ListItem",
                "position": position,
                "name": name,
                "item": SITE + path,
            }
            for position, (name, path) in enumerate(items, start=1)
        ],
    }
    return (
        '<script type="application/ld+json" data-seo="breadcrumb">'
        + json.dumps(payload, separators=(",", ":"), ensure_ascii=False)
        + "</script>"
    )


def common_head_block(title: str, description: str, indexable: bool) -> str:
    robots = (
        "index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1"
        if indexable
        else "noindex,follow"
    )
    escaped_title = html.escape(html.unescape(title), quote=True)
    escaped_description = html.escape(html.unescape(description), quote=True)
    return f'''  <meta name="robots" content="{robots}">
  <meta name="author" content="David C. Fields, M.S.">
  <meta name="theme-color" content="#07111f">
  <meta property="og:site_name" content="David C. Fields, M.S.">
  <meta property="og:locale" content="en_US">
  <meta property="og:image" content="{IMAGE}">
  <meta property="og:image:alt" content="Professional headshot of David C. Fields, M.S.">
  <meta name="twitter:card" content="summary">
  <meta name="twitter:title" content="{escaped_title}">
  <meta name="twitter:description" content="{escaped_description}">
  <meta name="twitter:image" content="{IMAGE}">
  <link rel="icon" href="/favicon.svg" type="image/svg+xml">
  <link rel="manifest" href="/site.webmanifest">
  <link rel="me" href="https://www.linkedin.com/in/david-c-fields">
  <link rel="me" href="https://github.com/davidcfields">'''


def normalize_homepage(text: str) -> str:
    new_title = "David C. Fields, M.S. | Infrastructure, Automation & Technology Leader"
    new_description = (
        "Senior infrastructure, automation, platform, cybersecurity, and technology operations "
        "leader in Central Ohio, open to remote, hybrid, contract, and consulting roles."
    )
    text = re.sub(r"<title>.*?</title>", f"<title>{new_title}</title>", text, count=1, flags=re.S)
    text = re.sub(
        r'<meta name="description" content="[^"]*">',
        f'<meta name="description" content="{new_description}">',
        text,
        count=1,
    )
    text = re.sub(
        r'<meta property="og:title" content="[^"]*">',
        f'<meta property="og:title" content="{new_title}">',
        text,
        count=1,
    )
    text = re.sub(
        r'<meta property="og:description" content="[^"]*">',
        f'<meta property="og:description" content="{new_description}">',
        text,
        count=1,
    )

    graph = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "WebSite",
                "@id": f"{SITE}/#website",
                "url": f"{SITE}/",
                "name": "David C. Fields, M.S.",
                "inLanguage": "en-US",
                "publisher": {"@id": f"{SITE}/#person"},
            },
            {
                "@type": "ProfilePage",
                "@id": f"{SITE}/#profile",
                "url": f"{SITE}/",
                "name": new_title,
                "description": new_description,
                "isPartOf": {"@id": f"{SITE}/#website"},
                "about": {"@id": f"{SITE}/#person"},
                "mainEntity": {"@id": f"{SITE}/#person"},
                "dateModified": LASTMOD,
                "inLanguage": "en-US",
            },
            {
                "@type": "Person",
                "@id": f"{SITE}/#person",
                "name": "David C. Fields",
                "honorificSuffix": "M.S.",
                "url": f"{SITE}/",
                "image": IMAGE,
                "email": "mailto:david@davidcfields.com",
                "telephone": "+1-740-334-0254",
                "jobTitle": "Senior Technology, Infrastructure and Automation Leader",
                "homeLocation": {"@type": "Place", "name": "Central Ohio, United States"},
                "sameAs": [
                    "https://www.linkedin.com/in/david-c-fields",
                    "https://github.com/davidcfields",
                ],
                "alumniOf": [
                    {"@type": "CollegeOrUniversity", "name": "Norwich University"},
                    {"@type": "CollegeOrUniversity", "name": "DeVry University"},
                ],
            },
        ],
    }
    replacement = (
        '<script type="application/ld+json">'
        + json.dumps(graph, separators=(",", ":"), ensure_ascii=False)
        + "</script>"
    )
    text, count = re.subn(
        r'<script type="application/ld\+json">.*?</script>',
        replacement,
        text,
        count=1,
        flags=re.S,
    )
    if count != 1:
        raise RuntimeError("Homepage JSON-LD block was not found exactly once")
    return text


def update_html(path: Path, indexable: bool) -> None:
    text = path.read_text(encoding="utf-8")
    text = text.replace("https://www.davidcfields.com", SITE)
    text = remove_generated_tags(text)
    if path.name == "index.html":
        text = normalize_homepage(text)

    title = extract(r"<title>(.*?)</title>", text, f"title in {path.name}")
    description = extract(
        r'<meta name="description" content="(.*?)">',
        text,
        f"meta description in {path.name}",
    )
    additions = [common_head_block(title, description, indexable)]
    if path.name in BREADCRUMBS:
        additions.append(breadcrumb_script(BREADCRUMBS[path.name]))
    insertion = "\n" + "\n".join(additions) + "\n"
    if "</head>" not in text:
        raise RuntimeError(f"Missing </head> in {path.name}")
    text = text.replace("</head>", insertion + "</head>", 1)
    path.write_text(text, encoding="utf-8")


def create_support_files() -> None:
    robots = f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n"
    Path("robots.txt").write_text(robots, encoding="utf-8")

    urls = [SITE + path for path in INDEXABLE.values()]
    entries = "\n".join(
        f"  <url><loc>{url}</loc><lastmod>{LASTMOD}</lastmod></url>" for url in urls
    )
    sitemap = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + entries
        + "\n</urlset>\n"
    )
    Path("sitemap.xml").write_text(sitemap, encoding="utf-8")

    favicon = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" role="img" aria-label="DCF">
  <rect width="64" height="64" rx="14" fill="#07111f"/>
  <path d="M9 12h46v40H9z" fill="#10223a" stroke="#65d8ff" stroke-width="2"/>
  <text x="32" y="39" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-size="20" font-weight="700" fill="#eef7ff">DCF</text>
</svg>\n'''
    Path("favicon.svg").write_text(favicon, encoding="utf-8")

    manifest = {
        "name": "David C. Fields, M.S. — Professional Portfolio",
        "short_name": "David Fields",
        "start_url": "/",
        "scope": "/",
        "display": "minimal-ui",
        "background_color": "#07111f",
        "theme_color": "#07111f",
        "icons": [{"src": "/favicon.svg", "sizes": "any", "type": "image/svg+xml"}],
    }
    Path("site.webmanifest").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )

    page404 = f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Page Not Found | David C. Fields, M.S.</title>
  <meta name="description" content="The requested page could not be found on David C. Fields' professional portfolio website.">
  <link rel="stylesheet" href="assets/css/portfolio-pages.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="header"><nav class="nav shell" aria-label="Primary navigation"><a class="brand" href="index.html">David C. Fields, <span>M.S.</span></a><div class="links"><a href="index.html#about">About</a><a href="index.html#experience">Experience</a><a href="case-studies.html">Case Studies</a><a href="index.html#resumes">Resumes</a><a href="faq.html">FAQ</a><a href="index.html#contact">Contact</a><a class="nav-cta" href="recruiter-brief.html">Recruiter Brief</a></div></nav></header>
<main id="main" class="shell"><section class="hero"><p class="eyebrow">404 · Page not found</p><h1>The requested page is not available.</h1><p class="lede">The address may be outdated or mistyped. Use the links below to continue to the professional profile, recruiter brief, case studies, resumes, FAQ, or contact form.</p><div class="actions"><a class="btn primary" href="index.html">Return home</a><a class="btn" href="recruiter-brief.html">Recruiter brief</a><a class="btn" href="case-studies.html">Case studies</a></div></section></main>
<footer class="footer"><div class="shell footer-row"><div>© 2026 David C. Fields.</div><div class="footer-links"><a href="index.html">Home</a><a href="faq.html">FAQ</a><a href="index.html#contact">Contact</a></div></div></footer>
</body>
</html>'''
    Path("404.html").write_text(page404, encoding="utf-8")


def create_validation() -> None:
    Path(".github/scripts").mkdir(parents=True, exist_ok=True)
    validator = r'''from __future__ import annotations

import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import urlparse

SITE = "https://davidcfields.com"
INDEXABLE = {
    "index.html": "/",
    "recruiter-brief.html": "/recruiter-brief.html",
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

if errors:
    print("Site quality validation failed:")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)
print("Site quality validation passed.")
'''
    Path(".github/scripts/validate_site.py").write_text(validator, encoding="utf-8")

    workflow = '''name: Site quality

on:
  pull_request:
  push:
    branches:
      - main

permissions:
  contents: read

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - name: Check out repository
        uses: actions/checkout@v4
      - name: Validate SEO and internal links
        run: python .github/scripts/validate_site.py
'''
    Path(".github/workflows").mkdir(parents=True, exist_ok=True)
    Path(".github/workflows/site-quality.yml").write_text(workflow, encoding="utf-8")


create_support_files()

for filename in INDEXABLE:
    update_html(Path(filename), indexable=True)
for filename in ("about.html", "resume.html", "contact-success.html"):
    update_html(Path(filename), indexable=False)
update_html(Path("404.html"), indexable=False)
create_validation()
print("SEO foundation applied successfully.")
