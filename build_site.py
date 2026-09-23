"""Build the static portfolio pages. Run `python3 build_site.py` in this folder."""
from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parent
NAME = "Caua Kevyn Martins Brasil"
EMAIL = "cm2080@scarletmail.rutgers.edu"
LINKEDIN = "https://www.linkedin.com/in/kevin-brasil-6b93032a8/"

NAV = [
    ("About", "about.html"),
    ("Projects", "projects.html"),
    ("Experience", "experience.html"),
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
  <meta name="theme-color" content="#fcfbf8">
  <title>{escape(title)} | {NAME}</title>
  <link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' fill='%23cc0033'/%3E%3Ctext x='32' y='42' text-anchor='middle' font-family='Arial,sans-serif' font-weight='bold' font-size='23' fill='white'%3ECK%3C/text%3E%3C/svg%3E">
  <link rel="stylesheet" href="site.css">
</head>
<body>
  <a class="skip-link" href="#main">Skip to content</a>
  <header class="site-header"><div class="wrap header-inner">
    <a class="brand" href="index.html" aria-label="{NAME}, home"><span class="brand-mark" aria-hidden="true">CK</span>{NAME}</a>
    <nav aria-label="Primary"><ul class="nav-list">{links}</ul></nav>
  </div></header>
  <main id="main">{content}</main>
  {'' if current == 'contact.html' else '<section class="footer-cta" aria-labelledby="footer-cta-title"><div class="wrap footer-cta-inner"><div><span class="eyebrow">Get in touch</span><h2 id="footer-cta-title">Let’s start a conversation.</h2><p>For internships, projects, and professional conversations in finance and business.</p></div><a class="button button-light" href="contact.html">Contact me <span aria-hidden="true">↗</span></a></div></section>'}
  <footer class="site-footer"><div class="wrap">
    <div class="footer-top"><div><strong>{NAME}</strong><p>Finance · operations · thoughtful analysis</p></div>
      <nav class="footer-links" aria-label="Footer"><a href="projects.html">Projects</a><a href="resume.html">Résumé</a><a href="mailto:{EMAIL}">Email</a><a href="{LINKEDIN}" target="_blank" rel="noopener noreferrer">LinkedIn ↗</a></nav></div>
    <div class="footer-bottom"><span>New Jersey · 2026</span><span>Built with care and clarity.</span></div>
  </div></footer>
</body>
</html>
'''


def art(style: str, label: str, symbol: str, foot: str, href: str, small: bool = False) -> str:
    klass = "art-symbol symbol-small" if small else "art-symbol"
    return f'''<a class="project-art {style}" href="{href}" aria-label="View {escape(label)} case study">
      <span class="art-label">{label}</span><span class="{klass}" aria-hidden="true">{symbol}</span><span class="art-foot">{foot}</span>
    </a>'''


def project_row(number: str, type_: str, title: str, blurb: str, url: str, style: str, symbol: str, foot: str, small: bool = False) -> str:
    return f'''<article class="project-row"><span class="project-number">{number}</span>
      <div class="project-copy"><span class="eyebrow">{type_}</span><h3>{title}</h3><p>{blurb}</p><a class="text-link" href="{url}">Explore the work <span aria-hidden="true">↗</span></a></div>
      {art(style, type_, symbol, foot, url, small)}</article>'''


projects = [
    project_row("01", "Consulting · strategy", "Bergecco-Parc Consulting",
        "A team-built marketing plan for a historic center, connecting audience research, revenue opportunities, and events to a clearer attendance strategy.",
        "project-bergecco.html", "", "B—P", "Strategy / 2023", True),
    project_row("02", "Operations · analysis", "A closer look at store performance",
        "Working across cash reconciliation, delivery commissions, payroll, pricing, and marketing spend in a high-volume restaurant environment.",
        "project-operations.html", "rose", "01—03", "Operations / 2025–26", True),
    project_row("03", "Finance · client discovery", "Understanding funding fit",
        "Qualifying small-business needs and explaining working-capital options, repayment structures, and tradeoffs during a finance internship.",
        "project-funding.html", "navy", "$25–100k", "Finance / 2026", True),
]


PAGES = {
"index.html": page("Portfolio", "Finance portfolio of Caua Kevyn Martins Brasil: projects, experience, résumé, and contact.", "", f'''
  <div class="wrap"><section class="hero" aria-labelledby="hero-title"><div>
    <span class="eyebrow">Finance portfolio / New Jersey</span>
    <h1 id="hero-title">Caua Kevyn<br>Martins Brasil<span class="red">.</span></h1>
    <div class="school-badge"><span class="school-badge-line" aria-hidden="true"></span><span>Rutgers Business School <small>Finance · Class of 2028</small></span></div>
    <p class="lead">I connect numbers, operations, and people to understand how businesses make better decisions.</p>
    <div class="button-row"><a class="button" href="projects.html">Explore projects <span aria-hidden="true">↗</span></a><a class="text-link" href="resume.html">View résumé <span aria-hidden="true">↗</span></a></div>
    <div class="hero-meta"><span>Business operations</span><span>Small-business finance</span><span>Legal research</span></div>
  </div><div class="hero-art" role="img" aria-label="Typographic portrait card featuring the initials CK">
    <span class="art-top"><span>CKMB</span><span>Rutgers / Business School</span></span><span class="art-initials" aria-hidden="true">C<span style="margin-left:-.16em">K</span></span><span class="art-bottom">Finance<br>with perspective.</span>
  </div></section><hr class="rule">
  <section class="about-teaser two-col" aria-labelledby="home-about"><div><span class="eyebrow">01 / Introduction</span><h2 id="home-about">A little about me</h2></div>
    <div class="body-copy"><p>I’m studying finance while building experience in the day-to-day decisions that shape a business: managing operations, evaluating funding needs, and turning research into useful recommendations.</p><a class="text-link" href="about.html">More about my path <span aria-hidden="true">↗</span></a></div>
  </section><hr class="rule">
  <section class="section" aria-labelledby="selected-work"><div class="section-head"><div><span class="eyebrow">02 / Selected work</span><h2 id="selected-work">Projects &amp; practice</h2><p class="body-copy">A closer look at the work behind the résumé.</p></div><span class="count">01 — 03</span></div>
    <div class="project-list">{''.join(projects)}</div>
  </section><section class="statement"><h2>Curious about the story behind the numbers<span class="red">.</span></h2><div class="body-copy"><p>From reconciling daily deposits to asking the right questions about financing, I’m drawn to work that makes complex decisions more understandable.</p><a class="text-link" href="experience.html">See my experience <span aria-hidden="true">↗</span></a></div></section>
  </div>'''),

"about.html": page("About", "Learn about Caua Kevyn Martins Brasil's education, leadership, and interest in finance.", "about.html", f'''
  <div class="wrap"><header class="page-intro"><span class="eyebrow">The person behind the work</span><h1>About me<span class="red">.</span></h1>
    <p class="lead">I’m a finance student interested in how careful analysis, clear communication, and practical judgment help a business move forward.</p></header>
    <section class="split-section"><div><span class="eyebrow">01 / Perspective</span><h2>Where I’m coming from</h2></div><div class="body-copy">
      <p>My interest in finance grew from being close to the decisions businesses make every day. At a busy restaurant, I’ve worked with the details behind operations: cash and deposits, delivery commissions, payroll, pricing, and marketing spend. That gave me a concrete sense of how small changes can affect performance.</p>
      <p>In a finance internship, I learned to listen for what small-business owners actually needed before discussing funding options. Earlier legal work taught me to research carefully and present information in a way someone else can use. Together, those experiences shaped how I think: understand the context, look closely at the evidence, and communicate the next step clearly.</p>
    </div></section>
    <section class="split-section"><div><span class="eyebrow">02 / Education</span><h2>Learning by doing</h2></div><div class="body-copy">
      <p>I’m pursuing a Bachelor of Science in Finance at Rutgers Business School, with an expected graduation in May 2028. I earned an Associate in Science in Business Administration from Bergen Community College in May 2026, graduating with a 3.89 GPA and Dean’s List recognition.</p>
      <p>Accounting, statistics, economics, Python, and hands-on work with spreadsheets have helped me connect classroom ideas to business questions. I received the Moses Family Endowed Scholarship and the LEO Foundation Endowed Scholarship at Bergen.</p>
    </div></section>
    <section class="split-section"><div><span class="eyebrow">03 / Community</span><h2>Beyond coursework</h2></div><div class="body-copy">
      <p>As president of Bergen’s Legal Studies Club, I organized programming and member engagement around law, business, and professional development. At Rutgers, I’m a member of the Association of Latino Professionals For America (ALPFA).</p>
      <p>I have also participated in student government, the Latin American Student Association, and Motion: Student Achievement Club. I speak Portuguese natively and am proficient in Spanish—skills that help me connect with people across backgrounds.</p>
    </div></section>
    <section class="section"><div class="section-head"><div><span class="eyebrow">How I work</span><h2>What I bring to a team</h2></div></div>
      <div class="card-grid"><div class="info-card"><span class="eyebrow">01</span><h3>Attention to detail</h3><p>Careful with records, numbers, and research that others rely on.</p></div><div class="info-card"><span class="eyebrow">02</span><h3>Clear communication</h3><p>Comfortable explaining unfamiliar information and listening first.</p></div><div class="info-card"><span class="eyebrow">03</span><h3>Operational perspective</h3><p>Interested in how analysis connects to real people and daily decisions.</p></div></div>
    </section></div>'''),

"projects.html": page("Projects", "Consulting, operational analysis, and finance work from Caua Kevyn Martins Brasil.", "projects.html", f'''
  <div class="wrap"><header class="page-intro compact"><span class="eyebrow">Selected work / 01 — 03</span><h1>Projects &amp; practice<span class="red">.</span></h1>
    <p class="lead">Three settings, one approach: understand the problem, examine the details, and make the information useful to someone making a decision.</p></header>
    <div class="project-list">{''.join(projects)}</div>
    <section class="statement"><h2>Good analysis should lead somewhere<span class="red">.</span></h2><div class="body-copy"><p>Each story explains the context, my contribution, and what the work taught me. The operations and funding entries describe professional experience rather than separate client deliverables.</p><a class="text-link" href="experience.html">View professional experience <span aria-hidden="true">↗</span></a></div></section>
  </div>'''),

"experience.html": page("Experience", "Professional experience in operations, finance, and legal research.", "experience.html", f'''
  <div class="wrap"><header class="page-intro compact"><span class="eyebrow">Professional experience</span><h1>Work that shaped<br>how I think<span class="red">.</span></h1>
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
  <div class="wrap"><header class="page-intro compact"><span class="eyebrow">At a glance</span><h1>Résumé<span class="red">.</span></h1>
    <p class="lead">Finance student with experience in operations, small-business funding, legal research, and team leadership.</p>
    <div class="button-row" style="margin-top:27px"><a class="button" href="mailto:{EMAIL}?subject=R%C3%A9sum%C3%A9%20request">Request full résumé <span aria-hidden="true">↗</span></a><a class="text-link" href="{LINKEDIN}" target="_blank" rel="noopener noreferrer">LinkedIn profile <span aria-hidden="true">↗</span></a></div>
  </header><section class="resume-block"><h2>Education</h2><div>
    <div class="resume-item"><h3>Rutgers Business School</h3><span class="date">Expected May 2028</span><p>Bachelor of Science in Finance · Newark, New Jersey</p></div>
    <div class="resume-item"><h3>Bergen Community College</h3><span class="date">May 2026</span><p>Associate in Science, Business Administration · 3.89 GPA · Dean’s List</p><p>Moses Family Endowed Scholarship · LEO Foundation Endowed Scholarship</p></div>
  </div></section><section class="resume-block"><h2>Experience</h2><div>
    <div class="resume-item"><h3>Master Pizza</h3><span class="date">2025 — present</span><p>Operations Intern &amp; Team Lead · Cash reconciliation, operating expenses, high-volume team coordination.</p></div>
    <div class="resume-item"><h3>High Rise Capital</h3><span class="date">2026</span><p>Finance Intern · Small-business qualification, working-capital products, client communication.</p></div>
    <div class="resume-item"><h3>Gencarelli’s &amp; Ramasa Law Firm</h3><span class="date">2023 — 2024</span><p>Legal Intern · Research, structured briefs, case preparation.</p></div>
  </div></section><section class="resume-block"><h2>Projects</h2><div><div class="resume-item"><h3>Bergecco-Parc Consulting</h3><span class="date">Fall 2023</span><p>Team marketing strategy for a historic center, including revenue opportunities and event ideas. <a href="project-bergecco.html">Read the case study ↗</a></p></div></div></section>
  <section class="resume-block"><h2>Leadership</h2><div>
    <div class="resume-item"><h3>Legal Studies Club</h3><span class="date">2024 — 2025</span><p>President · Bergen Community College</p></div>
    <div class="resume-item"><h3>ALPFA</h3><span class="date">2026 — present</span><p>Member · Rutgers University</p></div>
    <div class="resume-item"><h3>Additional campus involvement</h3><p>Student Government Association · Latin American Student Association · Motion: Student Achievement Club</p></div>
  </div></section><section class="resume-block"><h2>Skills</h2><div>
    <div class="resume-item"><h3>Tools &amp; methods</h3><p>Excel (PivotTables and formulas), QuickBooks, Google Sheets, Python, PowerPoint; financial accounting and business analysis.</p></div>
    <div class="resume-item"><h3>Languages</h3><p>Portuguese (native) · Spanish (proficient) · English</p></div>
  </div></section></div>'''),

"contact.html": page("Contact", "Contact Caua Kevyn Martins Brasil about finance internships and professional opportunities.", "contact.html", f'''
  <div class="wrap"><header class="page-intro compact"><span class="eyebrow">Contact / New Jersey</span><h1>Let’s connect<span class="red">.</span></h1>
    <p class="lead">I’m looking for opportunities to learn and contribute in finance, operations, and business analysis. I’m also glad to talk about the work on this site.</p></header>
    <section class="contact-panel"><div><span class="eyebrow">Start here</span><h2>Have something in mind?</h2><p class="body-copy">The easiest way to reach me is by email. Tell me a little about the role, team, or project, and I’ll get back to you.</p>
      <a class="button" href="mailto:{EMAIL}?subject=Portfolio%20inquiry">Email me <span aria-hidden="true">↗</span></a>
      <div class="contact-note"><span class="eyebrow">Currently interested in</span><p>Finance internships · corporate finance · business operations · analytical projects</p></div></div>
      <div class="contact-methods"><a class="contact-method" href="mailto:{EMAIL}"><span class="eyebrow">01 / Email</span><strong>{EMAIL}</strong><small>Start a conversation <span aria-hidden="true">↗</span></small></a>
        <a class="contact-method" href="{LINKEDIN}" target="_blank" rel="noopener noreferrer"><span class="eyebrow">02 / LinkedIn</span><strong>Connect professionally</strong><small>View my profile <span aria-hidden="true">↗</span></small></a>
        <a class="contact-method" href="resume.html"><span class="eyebrow">03 / Background</span><strong>See my résumé</strong><small>Education and experience <span aria-hidden="true">↗</span></small></a></div>
    </section><section class="contact-next"><div><span class="eyebrow">Before you go</span><h2>Explore the work behind the résumé.</h2><p>Take a look at how I approached a consulting project, operational questions, and funding conversations.</p></div><a class="text-link" href="projects.html">Browse projects <span aria-hidden="true">↗</span></a></section>
  </div>'''),

"project-bergecco.html": page("Bergecco-Parc Consulting", "A historic-center marketing strategy project by Caua Kevyn Martins Brasil and a consulting team.", "projects.html", '''
  <div class="wrap"><header class="page-intro compact"><a class="text-link back-link" href="projects.html">← All projects</a><span class="eyebrow">01 / Consulting · strategy</span><h1>Bergecco-Parc<br>Consulting<span class="red">.</span></h1>
    <p class="lead">Building a marketing plan to help a historic center attract visitors and strengthen revenue.</p></header>
    <div class="case-layout"><div>
      <section><h2>The brief</h2><p>In fall 2023, I worked with a five-person team on a plan to increase attendance and revenue for a historic center. The challenge was to connect what the center offered with reasons for more people to visit, return, and participate.</p></section>
      <section><h2>Our approach</h2><p>We examined how the center could make better use of its revenue streams, reach relevant audiences through clearer marketing channels and messages, and develop events tailored to the venue. The work required bringing a range of ideas together into one practical recommendation.</p>
        <ul><li>Reviewed existing revenue opportunities and attendance goals.</li><li>Considered messaging and channels that could make the venue more visible.</li><li>Proposed customized events designed to bring people to the center.</li><li>Collaborated across a team of five to organize and present the plan.</li></ul></section>
      <section><h2>What I took from it</h2><p>A recommendation becomes stronger when the financial objective and the audience experience reinforce each other. This project made me think about strategy as a set of choices a real organization can carry out, not simply a collection of ideas.</p></section>
      <section><a class="text-link" href="projects.html">Explore more work <span aria-hidden="true">↗</span></a></section>
    </div><aside class="case-aside"><dl><dt>Type</dt><dd>Team consulting project</dd><dt>When</dt><dd>Fall 2023</dd><dt>Focus</dt><dd>Attendance · revenue · marketing strategy</dd><dt>My contribution</dt><dd>Research, analysis, recommendations, team collaboration</dd></dl></aside></div>
  </div>'''),

"project-operations.html": page("Operational Analysis", "An experience note on store operations, reconciliation, and business drivers.", "projects.html", '''
  <div class="wrap"><header class="page-intro compact"><a class="text-link back-link" href="projects.html">← All projects</a><span class="eyebrow">02 / Operations · analysis</span><h1>A closer look at<br>store performance<span class="red">.</span></h1>
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
  <div class="wrap"><header class="page-intro compact"><a class="text-link back-link" href="projects.html">← All projects</a><span class="eyebrow">03 / Finance · client discovery</span><h1>Understanding<br>funding fit<span class="red">.</span></h1>
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
