from pathlib import Path

path = Path("index.html")
content = path.read_text(encoding="utf-8")

old_huntington = '''<article class="timeline-item"><div class="meta">August 2020–September 2024 · Huntington National Bank</div><h3>Senior Automation Engineer / Network Engineer III</h3><p>Supported secure 24x7 enterprise infrastructure and delivered network, firewall, incident-management, monitoring, and service-request automation.</p><ul><li>Used Python, Ansible/AWX, Terraform, Azure DevOps, Git, ServiceNow, PagerDuty, Rundeck, APIs, Docker, and Kubernetes-related tooling.</li><li>Built automation supporting more than half of incoming ticket volume and 10,000+ incidents and requests annually.</li><li>Developed Palo Alto policy analysis that evaluated hundreds of thousands of objects and rules in minutes.</li></ul></article>'''

new_huntington = '''<article class="timeline-item"><div class="meta">February 2018–September 2024 · Apex Systems / Huntington National Bank</div><h3>Network &amp; Security Engineer Consultant → Senior Automation Engineer / Network Engineer III</h3><p>Progressed from an Apex Systems consulting engagement supporting Huntington into direct Huntington employment and senior automation engineering responsibilities.</p><ul><li>Began in Huntington’s security and network operations environment, supporting network, cybersecurity, remote access, branches, ATMs, WAN, VoIP, proxies, and vendor-connected services.</li><li>Advanced into enterprise automation using Python, Ansible/AWX, Terraform, Azure DevOps, Git, ServiceNow, PagerDuty, Rundeck, APIs, Docker, and Kubernetes-related tooling.</li><li>Built automation supporting more than half of incoming ticket volume and 10,000+ incidents and requests annually.</li><li>Developed Palo Alto policy analysis that evaluated hundreds of thousands of objects and rules in minutes.</li></ul></article>'''

old_earlier = '''<article class="timeline-item"><div class="meta">1994–2009 · Earlier enterprise, government, defense, consulting, and instruction</div><h3>Network, Systems, Security & Architecture Roles</h3><p>Progressed through EDS, ACS Defense at Wright-Patterson Air Force Base, Cisco Systems, The Longaberger Company, Ohio Department of Job and Family Services, Plannet Group, and part-time Cisco/security instruction. Work included enterprise routing and switching, Unix and Windows systems, firewalls, security architecture, managed infrastructure, NERC CIP-aligned utility environments, manufacturing systems, technical consulting, and adult education.</p></article>'''

new_earlier = '''<article class="timeline-item"><div class="meta">1991–2009 · Earlier enterprise, government, defense, consulting, and instruction</div><h3>Network, Systems, Security &amp; Architecture Roles</h3><p>The documented full-time enterprise chronology begins in August 1991 at Freudenberg Spunweb Company and progresses through EDS, ACS Defense at Wright-Patterson Air Force Base, Cisco Systems, The Longaberger Company, Ohio Department of Job and Family Services, Plannet Group, and part-time Cisco/security instruction. Work included enterprise routing and switching, Unix and Windows systems, firewalls, security architecture, managed infrastructure, NERC CIP-aligned utility environments, manufacturing systems, technical consulting, and adult education.</p></article>'''

for label, old, new in (
    ("Huntington timeline", old_huntington, new_huntington),
    ("early-career timeline", old_earlier, new_earlier),
):
    count = content.count(old)
    if count != 1:
        raise RuntimeError(f"Expected exactly one {label} block, found {count}")
    content = content.replace(old, new)

path.write_text(content, encoding="utf-8")
print("Updated homepage chronology successfully.")
