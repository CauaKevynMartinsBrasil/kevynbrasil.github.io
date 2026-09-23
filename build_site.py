"""Build the static portfolio pages. Run `python3 build_site.py` in this folder."""
from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parent
NAME = "Caua Kevyn Martins Brasil"
EMAIL = "cm2080@scarletmail.rutgers.edu"
LINKEDIN = "https://www.linkedin.com/in/kevin-brasil-6b93032a8/"

NAV = [
    ("Overview", "index.html"),
    ("About", "about.html"),
    ("Projects", "projects.html"),
    ("Experience", "experience.html"),
    ("Highlights", "highlights.html"),
    ("Résumé", "resume.html"),
    ("Contact", "contact.html"),
]


def page(title: str, description: str, current: str, content: str) -> str:
    links = "\n".join(
        f'<li><a href="{href}"' + (' aria-current="page"' if current == href else '') + f'>{label}</a></li>'
        for label, href in NAV
    )
    return f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="{escape(description, quote=True)}">
  <meta name="theme-color" content="#cc0033">
  <title>{escape(title)} | {NAME}</title>
  <link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' fill='%23cc0033'/%3E%3Ctext x='32' y='42' text-anchor='middle' font-family='Arial,sans-serif' font-weight='bold' font-size='23' fill='white'%3ECK%3C/text%3E%3C/svg%3E">
  <link rel="stylesheet" href="site.css?v=2">
</head>
<body>
  <a class="skip-link" href="#main">Skip to content</a>
  <header class="site-header">
    <a class="brand" href="index.html" aria-label="{NAME}, home"><span class="brand-mark" aria-hidden="true">KB<span>↗</span></span><span class="brand-name">Caua Kevyn<br>Martins Brasil</span></a>
    <p class="nav-caption">Personal portfolio</p>
    <nav aria-label="Primary"><ul class="nav-list">{links}</ul></nav>
    <div class="sidebar-school"><span class="school-rule"></span><strong>Rutgers<br>Business School</strong><span>BS in Finance · 2028</span></div>
    <a class="sidebar-contact" href="mailto:{EMAIL}">Start a conversation <span>↗</span></a>
  </header>
  <div class="site-content"><div class="topline"><span>FINANCE &amp; BUSINESS</span><span>Based in New Jersey <span class="status-dot" aria-hidden="true"></span></span></div>
  <main id="main">{content}</main>
  <footer class="site-footer"><div class="wrap footer-top"><div><strong>{NAME}</strong><p>Finance student. Curious about what comes next.</p></div><nav class="footer-links" aria-label="Footer"><a href="contact.html">Contact</a><a href="{LINKEDIN}" target="_blank" rel="noopener noreferrer">LinkedIn ↗</a><a href="#main">Back to top ↑</a></nav><span class="copyright">© 2026</span></div></footer></div>
</body>
</html>
'''


def project_row(number: str, type_: str, title: str, blurb: str, url: str, style: str, symbol: str, foot: str, small: bool = False) -> str:
    icons = {"01": "<path d='M8 32V14h12v18M20 32V8h12v24M32 32V20h8v12M5 36h38'/>", "02": "<rect x='8' y='7' width='32' height='34' rx='3'/><path d='M15 16h18M15 24h6m6 0h6M15 32h6m6 0h6'/>", "03": "<path d='M8 15h30l-7-7M38 33H8l7 7'/><circle cx='24' cy='24' r='7'/>"}
    return f'''<article class="project-card"><div class="project-visual {style}"><svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true">{icons[number]}</svg><span>{foot}</span></div>
      <div class="project-copy"><span class="eyebrow">{type_}</span><h3><a href="{url}">{title}</a></h3><p>{blurb}</p><a class="text-link" href="{url}">Read the story <span aria-hidden="true">→</span></a></div></article>'''



projects = [
    project_row("01", "Winning team · consulting", "The Bergen 250",
        "Tourism, seasonal events, and a museum fundraising proposal for the Bergen County Historical Society. Member of the winning Team Two.",
        "project-bergecco.html", "", "B—P", "Tourism strategy / 2023", True),
    project_row("02", "Operations · analysis", "A closer look at store performance",
        "Working across cash reconciliation, delivery commissions, payroll, pricing, and marketing spend in a high-volume restaurant environment.",
        "project-operations.html", "rose", "01—03", "Operations / 2025–26", True),
    project_row("03", "Finance · client discovery", "Understanding funding fit",
        "Qualifying small-business needs and explaining working-capital options, repayment structures, and tradeoffs during a finance internship.",
        "project-funding.html", "navy", "$25–100k", "Finance / 2026", True),
]


PAGES = {
"index.html": page("Overview", "Finance, business experience, and campus involvement from Caua Kevyn Martins Brasil.", "index.html", f'''
  <div class="wrap"><section class="profile-hero" aria-labelledby="hero-title">
    <div class="profile-scarlet"><span class="profile-label">THE NEXT CHAPTER</span><div class="profile-word">Finance.<br>People.<br>Possibility.</div><div class="profile-school">Rutgers Business School<span>Finance undergraduate<br>Class of 2028</span></div></div>
    <div class="profile-intro"><span class="eyebrow">Hello, I’m</span><h1 id="hero-title">Caua Kevyn<br>Martins Brasil</h1><p class="lead">Learning how businesses work.<br>Finding where I can make a difference.</p><p class="intro-detail">I study finance at Rutgers and bring hands-on experience in business operations, small-business funding, and legal research.</p><div class="button-row"><a class="button" href="projects.html">Explore my work <span aria-hidden="true">→</span></a><a class="button secondary" href="resume.html">View résumé</a></div></div>
  </section>
  <div class="focus-strip"><span>My focus</span><strong>Financial analysis</strong><strong>Business operations</strong><strong>Clear communication</strong></div>
  <section class="section"><div class="section-head"><div><span class="eyebrow">Experience in action</span><h2>Work worth a closer look.</h2></div><a class="text-link" href="projects.html">All work →</a></div><div class="project-list">{''.join(projects)}</div></section>
  <section class="highlight-section"><div class="section-head"><div><span class="eyebrow">Beyond the job titles</span><h2>A few milestones.</h2></div><a class="text-link" href="highlights.html">Explore highlights →</a></div>
    <div class="milestone-grid"><article class="milestone academic"><span class="eyebrow">Bergen Community College</span><strong class="big-stat">3.89<span>GPA</span></strong><h3>A strong foundation.</h3><p>AS in Business Administration · May 2026<br>Dean’s List recognition</p></article><article class="milestone"><span class="tile-icon" aria-hidden="true">↗</span><span class="eyebrow">Leadership</span><h3>From member<br>to president.</h3><p>Legal Studies Club president at Bergen, organizing programming and member engagement.</p><a class="text-link" href="highlights.html#leadership">Leadership &amp; involvement →</a></article><article class="milestone"><span class="tile-icon" aria-hidden="true">✳</span><span class="eyebrow">Recognition</span><h3>Supported<br>along the way.</h3><p>Moses Family Endowed Scholarship and LEO Foundation Endowed Scholarship.</p><a class="text-link" href="highlights.html#recognition">Academic highlights →</a></article></div>
  </section>
  <section class="section journey-section"><div><span class="eyebrow">The journey so far</span><h2>Building on<br>each experience.</h2><p class="body-copy">Work, education, and community have each added something to the way I approach business.</p><a class="text-link" href="about.html">Get to know me →</a></div><div class="journey-list"><a href="highlights.html#leadership"><span>2026</span><div><h3>A new chapter at Rutgers</h3><p>Studying finance and joining ALPFA.</p></div><span aria-hidden="true">↗</span></a><a href="experience.html"><span>2025–26</span><div><h3>Business from the inside</h3><p>Operations at Master Pizza; finance at High Rise Capital.</p></div><span aria-hidden="true">↗</span></a><a href="project-bergecco.html"><span>2023</span><div><h3>A winning team proposal</h3><p>The Bergen 250: tourism strategy for the Bergen County Historical Society.</p></div><span aria-hidden="true">↗</span></a></div></section>
  <section class="connect-banner"><div><span class="eyebrow">Let’s connect</span><h2>Have an opportunity in mind?</h2><p>I’d be glad to talk about finance internships, analytical projects, and business operations.</p></div><a class="button" href="contact.html">Get in touch ↗</a></section></div>'''),

"highlights.html": page("Highlights", "Academic recognition, leadership, and campus involvement.", "highlights.html", '''<div class="wrap"><header class="page-intro"><span class="eyebrow">Beyond the résumé</span><h1>Milestones &amp;<br>meaningful involvement.</h1><p class="lead">The communities, achievements, and experiences that are shaping my path.</p></header>
<section id="recognition" class="highlight-section"><div class="section-head"><div><span class="eyebrow">Academic recognition</span><h2>A foundation to build on.</h2></div></div><div class="milestone-grid"><article class="milestone academic"><span class="eyebrow">Bergen Community College</span><strong class="big-stat">3.89<span>GPA</span></strong><h3>Business Administration</h3><p>Associate in Science · May 2026<br>Dean’s List recognition</p></article><article class="milestone"><span class="tile-icon" aria-hidden="true">✳</span><span class="eyebrow">Scholarship</span><h3>Moses Family<br>Endowed Scholarship</h3><p>Academic support received while studying at Bergen Community College.</p></article><article class="milestone"><span class="tile-icon" aria-hidden="true">✳</span><span class="eyebrow">Scholarship</span><h3>LEO Foundation<br>Endowed Scholarship</h3><p>Recognition received during my time at Bergen Community College.</p></article></div></section>
<section class="connect-banner"><div><span class="eyebrow">Team achievement · December 2023</span><h2>The Bergen 250: winning team.</h2><p>Member of Team Two in Bergen Community College’s tourism consulting competition for the Bergen County Historical Society. The instructor’s published recap identifies Team Two as the winner.</p></div><a class="button" href="project-bergecco.html">Explore the project →</a></section>
<section id="leadership" class="section"><div class="section-head"><div><span class="eyebrow">Leadership &amp; involvement</span><h2>Growing with a community.</h2></div></div><div class="involvement-grid"><article class="involvement-card"><span class="eyebrow">President · 2024–2025</span><h3>Legal Studies Club</h3><p class="organization">Bergen Community College</p><p>Organized programming and member engagement around law, business, and professional development.</p></article><article class="involvement-card"><span class="eyebrow">Member · 2026–present</span><h3>ALPFA</h3><p class="organization">Rutgers University</p><p>Association of Latino Professionals For America. Continuing my campus involvement as I study finance at Rutgers.</p></article><article class="involvement-card wide"><span class="eyebrow">Additional involvement</span><h3>More ways to take part.</h3><ul class="chip-list"><li>Student Government Association</li><li>Latin American Student Association</li><li>Motion: Student Achievement Club</li></ul></article></div></section>
<section class="connect-banner"><div><span class="eyebrow">Put it in context</span><h2>See the experience behind the highlights.</h2><p>Explore my work in operations, finance, and research.</p></div><a class="button" href="experience.html">My experience →</a></section></div>'''),

"about.html": page("About", "Learn about Caua Kevyn Martins Brasil's education, leadership, and interest in finance.", "about.html", f'''
  <div class="wrap"><header class="page-intro"><span class="eyebrow">The person behind the work</span><h1>About me</h1>
    <p class="lead">I’m a finance student interested in how careful analysis, clear communication, and practical judgment help a business move forward.</p></header>
    <section class="split-section"><div><span class="eyebrow">Perspective</span><h2>Where I’m coming from</h2></div><div class="body-copy">
      <p>My interest in finance grew from being close to the decisions businesses make every day. At a busy restaurant, I’ve worked with the details behind operations: cash and deposits, delivery commissions, payroll, pricing, and marketing spend. That gave me a concrete sense of how small changes can affect performance.</p>
      <p>In a finance internship, I learned to listen for what small-business owners actually needed before discussing funding options. Earlier legal work taught me to research carefully and present information in a way someone else can use. Together, those experiences shaped how I think: understand the context, look closely at the evidence, and communicate the next step clearly.</p>
    </div></section>
    <section class="split-section"><div><span class="eyebrow">Education</span><h2>Learning by doing</h2></div><div class="body-copy">
      <p>I’m pursuing a Bachelor of Science in Finance at Rutgers Business School, with an expected graduation in May 2028. I earned an Associate in Science in Business Administration from Bergen Community College in May 2026, graduating with a 3.89 GPA and Dean’s List recognition.</p>
      <p>Accounting, statistics, economics, Python, and hands-on work with spreadsheets have helped me connect classroom ideas to business questions. I received the Moses Family Endowed Scholarship and the LEO Foundation Endowed Scholarship at Bergen.</p>
    </div></section>
    <section class="split-section"><div><span class="eyebrow">Community</span><h2>Beyond coursework</h2></div><div class="body-copy">
      <p>As president of Bergen’s Legal Studies Club, I organized programming and member engagement around law, business, and professional development. At Rutgers, I’m a member of the Association of Latino Professionals For America (ALPFA).</p>
      <p>I have also participated in student government, the Latin American Student Association, and Motion: Student Achievement Club. I speak Portuguese natively and am proficient in Spanish—skills that help me connect with people across backgrounds.</p>
    </div></section>
    <section class="section"><div class="section-head"><div><span class="eyebrow">How I work</span><h2>What I bring to a team</h2></div></div>
      <div class="card-grid"><div class="info-card"><span class="eyebrow">01</span><h3>Attention to detail</h3><p>Careful with records, numbers, and research that others rely on.</p></div><div class="info-card"><span class="eyebrow">02</span><h3>Clear communication</h3><p>Comfortable explaining unfamiliar information and listening first.</p></div><div class="info-card"><span class="eyebrow">03</span><h3>Operational perspective</h3><p>Interested in how analysis connects to real people and daily decisions.</p></div></div>
    </section></div>'''),

"projects.html": page("Projects", "Consulting, operational analysis, and finance work from Caua Kevyn Martins Brasil.", "projects.html", f'''
  <div class="wrap"><header class="page-intro compact"><span class="eyebrow">Selected work</span><h1>Ideas put into practice.</h1>
    <p class="lead">Three settings, one approach: understand the problem, examine the details, and make the information useful to someone making a decision.</p></header>
    <div class="project-list">{''.join(projects)}</div>
    <section class="statement"><h2>Good analysis should lead somewhere</h2><div class="body-copy"><p>Each story explains the context, my contribution, and what the work taught me. The operations and funding entries describe professional experience rather than separate client deliverables.</p><a class="text-link" href="experience.html">View professional experience <span aria-hidden="true">↗</span></a></div></section>
  </div>'''),

"experience.html": page("Experience", "Professional experience in operations, finance, and legal research.", "experience.html", f'''
  <div class="wrap"><header class="page-intro compact"><span class="eyebrow">Professional experience</span><h1>Work that shaped<br>how I think</h1>
    <p class="lead">From a high-volume business to financing conversations and legal research, I’ve learned to work with both data and people.</p></header>
    <section class="timeline" aria-label="Professional experience">
      <article class="timeline-entry"><span class="timeline-date">June 2025 — present<br>Carlstadt, NJ</span><div><h2>Master Pizza</h2><p class="role-name">Operations intern &amp; team lead</p>
        <ul><li>Reconcile roughly $1,000–$3,000 in daily cash and deposits, checking end-of-day totals and maintaining deposit records.</li><li>Review delivery commissions, payroll, marketing budgets, and pricing in a location processing more than 200 orders on a typical day.</li><li>Lead counter and delivery staff through busy shifts, and train new teammates on POS systems, order processing, and front-of-house procedures.</li></ul>
        <ul class="chip-list"><li>Cash reconciliation</li><li>Margin awareness</li><li>Team leadership</li></ul></div></article>
      <article class="timeline-entry"><span class="timeline-date">May — June 2026<br>Manhattan, NY</span><div><h2>High Rise Capital</h2><p class="role-name">Finance intern</p>
        <ul><li>Prospected and qualified small-business owners through high-volume daily outreach.</li><li>Asked about funding needs and explained working-capital options such as merchant cash advances, lines of credit, and business loans.</li><li>Discussed financing structures in the $25,000–$100,000 range, including repayment terms and product fit.</li></ul>
        <ul class="chip-list"><li>Client discovery</li><li>Working capital</li><li>Financial communication</li></ul></div></article>
      <article class="timeline-entry"><span class="timeline-date">October 2023 — October 2024<br>Lyndhurst, NJ</span><div><h2>Gencarelli’s &amp; Ramasa Law Firm</h2><p class="role-name">Legal intern</p>
        <ul><li>Researched more than 16 active matters and organized findings into structured briefs and case-preparation materials for attorneys.</li><li>Practiced synthesizing dense information accurately and handling sensitive records with care.</li></ul>
        <ul class="chip-list"><li>Research</li><li>Written synthesis</li><li>Confidentiality</li></ul></div></article>
    </section>
    <section class="section"><div class="section-head"><div><span class="eyebrow">What connects these roles</span><h2>Analysis in context</h2></div></div>
      <div class="card-grid"><div class="info-card"><span class="eyebrow">Operations</span><h3>Know the process</h3><p>The numbers make more sense when you know how the work happens.</p></div><div class="info-card"><span class="eyebrow">Finance</span><h3>Ask first</h3><p>Understanding someone’s needs is part of evaluating an option.</p></div><div class="info-card"><span class="eyebrow">Research</span><h3>Make it usable</h3><p>Good findings are organized for the person who acts on them.</p></div></div>
    </section></div>'''),

"resume.html": page("Résumé", "Résumé overview for Caua Kevyn Martins Brasil, finance student at Rutgers Business School.", "resume.html", f'''
  <div class="wrap"><header class="page-intro compact"><span class="eyebrow">At a glance</span><h1>Résumé</h1>
    <p class="lead">Finance student with experience in operations, small-business funding, legal research, and team leadership.</p>
    <div class="button-row" style="margin-top:27px"><a class="button" href="mailto:{EMAIL}?subject=R%C3%A9sum%C3%A9%20request">Request full résumé <span aria-hidden="true">↗</span></a><a class="text-link" href="{LINKEDIN}" target="_blank" rel="noopener noreferrer">LinkedIn profile <span aria-hidden="true">↗</span></a></div>
  </header><section class="resume-block"><h2>Education</h2><div>
    <div class="resume-item"><h3>Rutgers Business School</h3><span class="date">Expected May 2028</span><p>Bachelor of Science in Finance · Newark, New Jersey</p></div>
    <div class="resume-item"><h3>Bergen Community College</h3><span class="date">May 2026</span><p>Associate in Science, Business Administration · 3.89 GPA · Dean’s List</p><p>Moses Family Endowed Scholarship · LEO Foundation Endowed Scholarship</p></div>
  </div></section><section class="resume-block"><h2>Experience</h2><div>
    <div class="resume-item"><h3>Master Pizza</h3><span class="date">2025 — present</span><p>Operations Intern &amp; Team Lead · Cash reconciliation, operating expenses, high-volume team coordination.</p></div>
    <div class="resume-item"><h3>High Rise Capital</h3><span class="date">2026</span><p>Finance Intern · Small-business qualification, working-capital products, client communication.</p></div>
    <div class="resume-item"><h3>Gencarelli’s &amp; Ramasa Law Firm</h3><span class="date">2023 — 2024</span><p>Legal Intern · Research, structured briefs, case preparation.</p></div>
  </div></section><section class="resume-block"><h2>Projects</h2><div><div class="resume-item"><h3>Bergecco-Parc Consulting</h3><span class="date">Fall 2023</span><p>Member of the winning Team Two: tourism strategy, seasonal programming, and a museum fundraising proposal for the Bergen County Historical Society. <a href="project-bergecco.html">Read the case study ↗</a></p></div></div></section>
  <section class="resume-block"><h2>Leadership</h2><div>
    <div class="resume-item"><h3>Legal Studies Club</h3><span class="date">2024 — 2025</span><p>President · Bergen Community College</p></div>
    <div class="resume-item"><h3>ALPFA</h3><span class="date">2026 — present</span><p>Member · Rutgers University</p></div>
    <div class="resume-item"><h3>Additional campus involvement</h3><p>Student Government Association · Latin American Student Association · Motion: Student Achievement Club</p></div>
  </div></section><section class="resume-block"><h2>Skills</h2><div>
    <div class="resume-item"><h3>Tools &amp; methods</h3><p>Excel (PivotTables and formulas), QuickBooks, Google Sheets, Python, PowerPoint; financial accounting and business analysis.</p></div>
    <div class="resume-item"><h3>Languages</h3><p>Portuguese (native) · Spanish (proficient) · English</p></div>
  </div></section></div>'''),

"contact.html": page("Contact", "Contact Caua Kevyn Martins Brasil about finance internships and professional opportunities.", "contact.html", f'''
  <div class="wrap"><header class="page-intro compact"><span class="eyebrow">Contact / New Jersey</span><h1>Let’s connect</h1>
    <p class="lead">I’m looking for opportunities to learn and contribute in finance, operations, and business analysis. I’m also glad to talk about the work on this site.</p></header>
    <section class="contact-panel"><div><span class="eyebrow">Start here</span><h2>Have something in mind?</h2><p class="body-copy">The easiest way to reach me is by email. Tell me a little about the role, team, or project, and I’ll get back to you.</p>
      <a class="button" href="mailto:{EMAIL}?subject=Portfolio%20inquiry">Email me <span aria-hidden="true">↗</span></a>
      <div class="contact-note"><span class="eyebrow">Currently interested in</span><p>Finance internships · corporate finance · business operations · analytical projects</p></div></div>
      <div class="contact-methods"><a class="contact-method" href="mailto:{EMAIL}"><span class="eyebrow">01 / Email</span><strong>{EMAIL}</strong><small>Start a conversation <span aria-hidden="true">↗</span></small></a>
        <a class="contact-method" href="{LINKEDIN}" target="_blank" rel="noopener noreferrer"><span class="eyebrow">02 / LinkedIn</span><strong>Connect professionally</strong><small>View my profile <span aria-hidden="true">↗</span></small></a>
        <a class="contact-method" href="resume.html"><span class="eyebrow">03 / Background</span><strong>See my résumé</strong><small>Education and experience <span aria-hidden="true">↗</span></small></a></div>
    </section><section class="contact-next"><div><span class="eyebrow">Before you go</span><h2>Explore the work behind the résumé.</h2><p>Take a look at how I approached a consulting project, operational questions, and funding conversations.</p></div><a class="text-link" href="projects.html">Browse projects <span aria-hidden="true">↗</span></a></section>
  </div>'''),

"project-bergecco.html": page("The Bergen 250", "A winning team tourism proposal for the Bergen County Historical Society, presented December 7, 2023.", "projects.html", '''
<div class="wrap"><header class="page-intro"><a class="text-link back-link" href="projects.html">← All projects</a><span class="eyebrow">Bergecco-Parc Consulting · Academic team project</span><h1>The Bergen 250</h1><p class="lead">Tourism strategy for the Bergen County Historical Society at Historic New Bridge Landing.</p><div class="button-row" style="margin-top:24px"><a class="button" href="https://www.youtube.com/watch?v=j1y3mVapkkw" target="_blank" rel="noopener noreferrer">Watch our presentation ↗</a><a class="button secondary" href="https://visitingamuseum.com/2024/01/09/bergecco-parc-consulting-inc-presents-tourism-at-the-bergen-county-historical-society-december-7th-2023/" target="_blank" rel="noopener noreferrer">Read the project coverage ↗</a></div></header>
<div class="card-grid" style="margin-bottom:28px"><article class="info-card"><span class="eyebrow">Recognition</span><h3>Winning Team Two</h3><p>Identified as the competition winner in the instructor’s published recap.</p></article><article class="info-card"><span class="eyebrow">The brief</span><h3>2 seasonal events</h3><p>Historically grounded Halloween and Spring/Easter programming.</p></article><article class="info-card"><span class="eyebrow">Proposed fundraising</span><h3>$25,000 target</h3><p>A planning goal for the new museum, not an amount reported as raised.</p></article></div>
<div class="case-layout"><div>
<section><h2>The challenge</h2><p>How could a local historical site attract more visitors while keeping its programming connected to its history? In fall 2023, our Introduction to Business class at Bergen Community College developed tourism proposals under the simulated consulting company Bergecco-Parc Consulting Inc.</p><p>The assignment focused on the Bergen County Historical Society at New Bridge Landing in River Edge, New Jersey. Teams were asked to combine event concepts, cost planning, advertising, and fundraising into a presentation.</p></section>
<section><h2>My part in the team</h2><p>I participated as a member of Team Two. Our team’s proposal brought together tourism marketing, event concepts, ticket pricing, and a fundraising model for the historical site. The presentation and competition recognition belong to the team.</p></section>
<section><h2>Our event concepts</h2><p>Team Two’s section of the final presentation developed four proposed events, supported by visitor activities, promotion, and cost estimates.</p><ul><li><strong>Haunted Halloween:</strong> a haunted maze, historical buildings staged as haunted houses, a costume contest, food trucks, and family activities. The visitor plan included parking signs, a brochure with an event map, and membership tables.</li><li><strong>The Easter Spectacular:</strong> a golden-egg hunt with a membership prize, a petting zoo, puppet shows, inflatable attractions, and a brunch buffet.</li><li><strong>Museum fundraiser:</strong> a family event combining food trucks, carnival games, horse rides, and a raffle, with different ticket tiers to support the $25,000 goal.</li><li><strong>Revolutionary Dance:</strong> an additional outdoor event concept for 100 guests, featuring period-inspired dress, catering, music, and $35 tickets.</li></ul><p>Source: Team Two’s presentation, slides 51–89. These concepts were proposals presented for the class project.</p></section>
<section><h2>The fundraising model</h2><p>The team modeled a 700-attendee fundraiser using three ticket tiers and additional raffle sales. The projected revenue and expense figures below come from slides 75–77 and 86–87.</p>
<div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;font-size:13px;text-align:left"><caption style="text-align:left;font-weight:700;margin-bottom:12px">Original proposal assumptions</caption><thead><tr><th scope="col" style="padding:10px;border-bottom:2px solid #dfe4e9">Revenue source</th><th scope="col" style="padding:10px;border-bottom:2px solid #dfe4e9">Assumption</th><th scope="col" style="padding:10px;border-bottom:2px solid #dfe4e9;text-align:right">Projected total</th></tr></thead><tbody>
<tr><th scope="row" style="padding:10px;border-bottom:1px solid #dfe4e9;font-weight:400">All-inclusive tickets</th><td style="padding:10px;border-bottom:1px solid #dfe4e9">200 × $100</td><td style="padding:10px;border-bottom:1px solid #dfe4e9;text-align:right">$20,000</td></tr>
<tr><th scope="row" style="padding:10px;border-bottom:1px solid #dfe4e9;font-weight:400">Regular tickets</th><td style="padding:10px;border-bottom:1px solid #dfe4e9">400 × $30</td><td style="padding:10px;border-bottom:1px solid #dfe4e9;text-align:right">$12,000</td></tr>
<tr><th scope="row" style="padding:10px;border-bottom:1px solid #dfe4e9;font-weight:400">Children’s tickets</th><td style="padding:10px;border-bottom:1px solid #dfe4e9">100 × $10</td><td style="padding:10px;border-bottom:1px solid #dfe4e9;text-align:right">$1,000</td></tr>
<tr><th scope="row" style="padding:10px;border-bottom:1px solid #dfe4e9;font-weight:400">Additional raffle sales</th><td style="padding:10px;border-bottom:1px solid #dfe4e9">100 × $5</td><td style="padding:10px;border-bottom:1px solid #dfe4e9;text-align:right">$500</td></tr>
</tbody></table></div><p style="margin-top:20px"><strong>Projected revenue: $33,500<br>Listed event costs: $8,458<br>Projected net proceeds: $25,042</strong></p><p>The listed costs cover food trucks, horses, an obstacle course, a water slide, and carnival games. The projection clears the $25,000 target by $42, leaving little room for lower attendance or additional expenses. These figures describe the team’s original planning scenario; they are not actual funds raised.</p></section>
<section><h2>Marketing &amp; visitor engagement</h2><p>The team proposed logo concepts, billboard advertising, brochures, QR codes, flyers, and a broader social media presence. Direct outreach included sending first-visit offers to Bergen County residents. On-site membership tables and event maps connected the promotion plan to the visitor experience.</p><p>The deck includes English and Spanish content for the event proposals, supporting the assignment’s bilingual communication requirement. Source: slides 43–49 and 52–67.</p></section>
<section><h2>Presentation &amp; recognition</h2><p>The class presented on December 7, 2023. The instructor’s article names Team Two as the competition winner. The video linked here is the group presentation supplied with this project.</p><p><a class="text-link" href="https://visitingamuseum.com/2024/01/09/bergecco-parc-consulting-inc-presents-tourism-at-the-bergen-county-historical-society-december-7th-2023/" target="_blank" rel="noopener noreferrer">Read the instructor’s recap ↗</a></p></section>
<section><h2>What this work connects</h2><p>The proposal shows how visitor assumptions and ticket prices connect to a fundraising goal. Its narrow projected surplus also makes the effect of cost changes and attendance shortfalls visible. The broader work combined that financial model with event planning and bilingual marketing in a shared team presentation.</p></section>
</div><aside class="case-aside"><dl><dt>Organization studied</dt><dd>Bergen County Historical Society</dd><dt>Location</dt><dd>Historic New Bridge Landing<br>River Edge, New Jersey</dd><dt>Course</dt><dd>Introduction to Business<br>Bergen Community College</dd><dt>My role</dt><dd>Team Two member</dd><dt>Presented</dt><dd>December 7, 2023</dd><dt>Focus</dt><dd>Tourism · event planning · budgeting · bilingual promotion</dd></dl></aside></div>
<section class="highlight-section" style="padding:0 0 60px"><div class="section-head"><div><span class="eyebrow">Explore the original work</span><h2>Presentation &amp; coverage.</h2></div></div><div class="involvement-grid"><article class="involvement-card"><span class="tile-icon" aria-hidden="true">▶</span><span class="eyebrow">Presentation video</span><h3>Team Two’s presentation</h3><p>Watch the group’s presentation on YouTube.</p><a class="text-link" href="https://www.youtube.com/watch?v=j1y3mVapkkw" target="_blank" rel="noopener noreferrer">Watch on YouTube ↗</a></article><article class="involvement-card"><span class="eyebrow">Published January 9, 2024</span><h3>The instructor’s project recap</h3><p>Coverage of the class project, its tourism brief, and the winning team on Visiting a Museum.</p><a class="text-link" href="https://visitingamuseum.com/2024/01/09/bergecco-parc-consulting-inc-presents-tourism-at-the-bergen-county-historical-society-december-7th-2023/" target="_blank" rel="noopener noreferrer">Read the article ↗</a></article></div></section></div>'''),

"project-operations.html": page("Operational Analysis", "An experience note on store operations, reconciliation, and business drivers.", "projects.html", '''
  <div class="wrap"><header class="page-intro compact"><a class="text-link back-link" href="projects.html">← All projects</a><span class="eyebrow">02 / Operations · analysis</span><h1>A closer look at<br>store performance</h1>
    <p class="lead">Seeing how everyday numbers connect to the way a high-volume business actually runs.</p></header>
    <div class="case-layout"><div>
      <section><h2>The setting</h2><p>At Master Pizza, I work across operations and team leadership in a location that processes more than 200 orders on a typical day. The pace makes accuracy matter: cash totals, deposits, staffing, and customer service all need attention at once.</p></section>
      <section><h2>My work</h2><p>Part of my role involves reconciling around $1,000–$3,000 in daily cash and deposits, checking end-of-day totals, and maintaining records. I also examine delivery commissions, payroll, marketing budgets, and pricing to understand the factors that affect margins and operating performance.</p>
        <ul><li>Check that recorded cash and deposits agree with end-of-day activity.</li><li>Look at operating costs alongside the volume and pace of the location.</li><li>Coordinate counter and delivery staff during peak shifts.</li><li>Train new teammates on systems and procedures that support accuracy.</li></ul></section>
      <section><h2>Why it matters</h2><p>Financial performance is built from small, repeated decisions. Understanding the workflow behind the numbers has made me more careful about interpreting them, and more interested in roles that connect analysis to operations.</p><p><em>This is an overview of professional responsibilities, not a client report or a claim of a separate proprietary deliverable.</em></p></section>
      <section><a class="text-link" href="experience.html">See professional experience <span aria-hidden="true">↗</span></a></section>
    </div><aside class="case-aside"><dl><dt>Setting</dt><dd>Master Pizza · Carlstadt, NJ</dd><dt>When</dt><dd>2025 — present</dd><dt>Focus</dt><dd>Reconciliation · costs · pricing · leadership</dd><dt>Tools</dt><dd>POS systems · Excel · operating records</dd></dl></aside></div>
  </div>'''),

"project-funding.html": page("Understanding Funding Fit", "An experience note on client discovery and small-business working-capital options.", "projects.html", '''
  <div class="wrap"><header class="page-intro compact"><a class="text-link back-link" href="projects.html">← All projects</a><span class="eyebrow">03 / Finance · client discovery</span><h1>Understanding<br>funding fit</h1>
    <p class="lead">Learning to match a financing conversation to the needs and circumstances of a small business.</p></header>
    <div class="case-layout"><div>
      <section><h2>The context</h2><p>During my finance internship at High Rise Capital, I reached out to small-business owners and helped qualify their interest in working-capital solutions. Those conversations required more than describing a product: I needed to understand the business need before discussing a possible fit.</p></section>
      <section><h2>My approach</h2><p>I asked about funding needs and discussed options including merchant cash advances, lines of credit, and business loans. For financing discussions in the $25,000–$100,000 range, I explained repayment terms and product structures in plain language so owners could understand the differences.</p>
        <ul><li>Use discovery questions to understand the reason for seeking capital.</li><li>Explain how different funding structures work and what repayment involves.</li><li>Keep prospect information and follow-up organized in a high-volume outreach environment.</li></ul></section>
      <section><h2>What I learned</h2><p>Clear financial communication matters as much as the numbers. A useful conversation gives someone the information to evaluate a choice in the context of their own business.</p><p><em>This is an overview of internship responsibilities, not a recommendation for any specific financial product.</em></p></section>
      <section><a class="text-link" href="experience.html">See professional experience <span aria-hidden="true">↗</span></a></section>
    </div><aside class="case-aside"><dl><dt>Setting</dt><dd>High Rise Capital · Manhattan, NY</dd><dt>When</dt><dd>May — June 2026</dd><dt>Focus</dt><dd>Working capital · discovery · communication</dd><dt>Product context</dt><dd>Merchant cash advances · lines of credit · business loans</dd></dl></aside></div>
  </div>'''),
}


if __name__ == "__main__":
    for filename, markup in PAGES.items():
        (ROOT / filename).write_text(markup, encoding="utf-8")
        print(filename)
