from __future__ import annotations

import re
from pathlib import Path

ORDER = [
    ("about", "About"),
    ("experience", "Experience"),
    ("case-studies", "Case Studies"),
    ("consulting", "Consulting"),
    ("resumes", "Resumes"),
    ("faq", "FAQ"),
    ("contact", "Contact"),
    ("recruiter", "Recruiter Brief"),
]


def active_section(filename: str) -> str | None:
    if filename == "about.html":
        return "about"
    if filename == "case-studies.html" or filename.startswith("case-study-"):
        return "case-studies"
    if filename == "consulting-services.html":
        return "consulting"
    if filename.startswith("resume"):
        return "resumes"
    if filename == "faq.html":
        return "faq"
    if filename.startswith("contact"):
        return "contact"
    if filename == "recruiter-brief.html":
        return "recruiter"
    return None


def hrefs(filename: str) -> dict[str, str]:
    if filename == "index.html":
        return {
            "about": "#about",
            "experience": "#experience",
            "case-studies": "case-studies.html",
            "consulting": "consulting-services.html",
            "resumes": "#resumes",
            "faq": "faq.html",
            "contact": "#contact",
            "recruiter": "recruiter-brief.html",
        }
    return {
        "about": "index.html#about",
        "experience": "index.html#experience",
        "case-studies": "case-studies.html",
        "consulting": "consulting-services.html",
        "resumes": "index.html#resumes",
        "faq": "faq.html",
        "contact": "contact.html",
        "recruiter": "recruiter-brief.html",
    }


def link_html(filename: str, style: str) -> str:
    active = active_section(filename)
    page_hrefs = hrefs(filename)
    links: list[str] = []
    for key, label in ORDER:
        attrs = [f'href="{page_hrefs[key]}"']
        if key == "recruiter":
            attrs.insert(0, f'class="{"bar-cta" if style == "bar" else "nav-cta"}"')
        if key == active:
            attrs.append('aria-current="page"')
        links.append(f'<a {" ".join(attrs)}>{label}</a>')
    return "".join(links)


changed: list[str] = []
for path in sorted(Path(".").glob("*.html")):
    text = path.read_text(encoding="utf-8")
    original = text

    if '<div class="links">' in text:
        replacement = f'<div class="links">{link_html(path.name, "standard")}</div>'
        text, count = re.subn(
            r'<div class="links">.*?</div>',
            replacement,
            text,
            count=1,
            flags=re.DOTALL,
        )
        if count != 1:
            raise SystemExit(f"Could not replace standard navigation in {path.name}")

    if '<nav class="bar-nav" aria-label="Primary navigation">' in text:
        replacement = (
            '<nav class="bar-nav" aria-label="Primary navigation">'
            + link_html(path.name, "bar")
            + '</nav>'
        )
        text, count = re.subn(
            r'<nav class="bar-nav" aria-label="Primary navigation">.*?</nav>',
            replacement,
            text,
            count=1,
            flags=re.DOTALL,
        )
        if count != 1:
            raise SystemExit(f"Could not replace resume navigation in {path.name}")

    if text != original:
        path.write_text(text, encoding="utf-8")
        changed.append(path.name)

if len(changed) < 10:
    raise SystemExit(f"Expected broad site-wide navigation updates, changed only: {changed}")

validator = Path(".github/scripts/validate_site.py")
validator_text = validator.read_text(encoding="utf-8")
marker = "\nif errors:\n"
check = '''\nfor path in Path(".").glob("*.html"):\n    text = path.read_text(encoding="utf-8")\n    if 'aria-label="Primary navigation"' not in text:\n        continue\n    if not re.search(r'href="consulting-services\\.html"[^>]*>Consulting</a>', text):\n        errors.append(f"Primary navigation missing Consulting link in {path.name}")\n\n'''
if check.strip() not in validator_text:
    if marker not in validator_text:
        raise SystemExit("Could not locate validator insertion point")
    validator_text = validator_text.replace(marker, check + marker, 1)
    validator.write_text(validator_text, encoding="utf-8")

print("Updated site-wide navigation in:")
for name in changed:
    print(f"- {name}")
