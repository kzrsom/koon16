"""Core pages: home, about, mission, principles, history."""
import ui
from ui import (H, label, btn, plate, section_head, card, kv, accordion,
                numlist, statrow, filters, tabs, notice, quote, cta_band, crumbs)


# =============================================================== 01 · HOME
def home():
    hero = f'''<section class="hero">
  <div class="wrap hero-inner">
    <div class="hero-copy">
      <span class="label label--dark" data-so="U-doodid rayid oo nabad ah oo loogu talagalay is-goosasho">Peaceful civic advocacy for self-determination</span>
      <h1 class="display mt-3"><span data-so="Mustaqbal ">A future of </span><em data-so="sharaf, cadaalad, iyo is-maamul maxalli ah.">dignity, justice, and local self-rule.</em></h1>
      <p class="lede" data-so="Koonfur Bari waa madal rayid iyo taariikh oo taageerta soo-jeedinta gobolka inuu maamulo arrimihiisa isagoo ah dowlad federaal oo madax-banaan oo ka tirsan Soomaaliya, iyadoo loo marayo hab sharci ah, nabad ah, oo dimuqraadi ah.">Koonfur Bari is a civic and historical platform supporting the Southeast region’s proposal to manage its own affairs as an independent federal state within Somalia through lawful, peaceful, and democratic means.</p>
      <div class="btn-row mt-3">
        {btn(H('mission.html'), 'Explore the mission', 'primary')}
        {btn(H('history.html'), 'Read the history', 'light')}
      </div>
      <div class="hero-principles">
        <div><span class="n">01</span><span class="t">Lawful</span><span class="small soft">Constitutional dialogue</span></div>
        <div><span class="n">02</span><span class="t">Peaceful</span><span class="small soft">Nonviolent participation</span></div>
        <div><span class="n">03</span><span class="t">Inclusive</span><span class="small soft">Equal dignity for all</span></div>
      </div>
    </div>
    <div class="hero-side">
      <a class="cardlink" href="{H('archive/history-resistance.html')}">
        <article class="card--dark card" style="padding:1rem">
          <div class="plate plate--wide">
            <img src="{H('assets/plates/weave.svg')}" alt="Abstract woven plate representing collective memory" loading="eager">
            <span class="plate__tag">Archive docket</span>
            <figcaption class="plate__cap">Representative plate — verify provenance before use</figcaption>
          </div>
          <div style="padding-top:1.1rem">
            <span class="chip chip--ghost-light">Community memory</span>
            <h2 class="display h3 mt-2" style="font-size:1.5rem">Biimaal revolt: 1824–2004, a hundred years remembered</h2>
            <p class="small mt-1" style="color:#cfdedb">History should be documented, verified, and remembered responsibly. The anniversary is treated here as a research question, not a settled narrative.</p>
            <span class="link-arrow mt-2" style="display:inline-flex">Open the history &amp; resistance docket <span class="hover-arrow">→</span></span>
          </div>
        </article>
      </a>
      <div class="hero-strip">
        <span class="label label--dark">Our common purpose</span>
        <p class="small mt-1">Local decisions. Shared responsibility. People closest to the land, livelihoods, and daily challenges should have a meaningful voice in the decisions that shape their future.</p>
        <a class="link-arrow mt-2" href="{H('mission.html')}">Learn more about our vision →</a>
      </div>
    </div>
  </div>
</section>
<div class="band band--cream band--edge">
  <div class="wrap">
    {ui.statrow([("04", "Civic commitments"), ("07", "Archive dockets"), ("06", "Research priorities"), ("100%", "Status labelled")])}
  </div>
</div>'''

    mission = f'''<section class="section band">
  <div class="wrap">
    {section_head("Our mission",
                  'A peaceful platform for <em>dignity and representation</em>.',
                  'Our work is grounded in peaceful advocacy, community consent, historical truth, and the belief that every community deserves safety, representation, and the power to shape its own future.')}
    <div class="grid g4">
      {card("Rights and representation", "Community voices should be reflected in decisions that affect their lives, land, and future.", num="01")}
      {card("Land and environment", "We support the protection of land, water, natural resources, and community livelihoods.", num="02")}
      {card("Self-rule and justice", "We support inclusive governance, accountability, and the rule of law.", num="03")}
      {card("Education and memory", "Documentation, education, and dialogue help new generations understand what happened.", num="04")}
    </div>
    <div class="btn-row mt-4">{btn(H('mission.html'), 'Read the full mission', 'outline')}</div>
  </div>
</section>'''

    research = f'''<section class="section band band--ink">
  <div class="wrap">
    {section_head("Research and evidence",
                  'A careful record for a shared future.',
                  'Our research brings together historical records, community testimony, visual archives, and open questions. We distinguish documented evidence from reported experience so every contribution can be read with care.',
                  dark=True)}
    <div class="grid g-1-2 align-center">
      <div class="grid g2">
        {card("Read the record critically", "Colonial documents, public records, scholarship, and oral histories each carry context, perspective, and limits.", num="01", dark=True)}
        {card("Keep community voice central", "Family memory and local knowledge help restore histories that have been overlooked while honouring consent and privacy.", num="02", dark=True)}
        {card("Label the uncertainty", "A status label describes the present editorial state of a record. It does not decide truth, rank lived knowledge, or replace contextual review.", num="03", dark=True)}
        {card("Invite correction", "Descriptions can be challenged, clarified, contextualised, restricted, or withdrawn. Right of reply is a route, not an afterthought.", num="04", dark=True)}
      </div>
      <div>
        {plate('ledger.svg', 'The archive reads records for what they say and how they were made', tag='Research plate', cls='plate--tall', note='Illustrative plate — not a document, not archival evidence.')}
        <div class="btn-row mt-3">
          {btn(H('research.html'), 'Explore the research', 'primary')}
          {btn(H('archive/method.html'), 'Read the archive guide', 'light')}
        </div>
      </div>
    </div>
  </div>
</section>'''

    principles = f'''<section class="section band band--paper2">
  <div class="wrap">
    {section_head("What guides us", 'Four commitments. <em>One peaceful path.</em>',
                  'The platform’s civic and research work is guided by lawful participation, accountability, equal dignity, and shared peace.')}
    <div class="grid g4">
      {card("Lawful recognition", "A democratic path toward recognised local self-rule within a constitutional framework.", num="I")}
      {card("Accountable administration", "Institutions that protect public resources and answer to the people they serve.", num="II")}
      {card("Equal dignity", "Equal protection and political agency for indigenous and marginalised communities.", num="III")}
      {card("Shared peace", "Reconciliation, lawful negotiation, and nonviolent participation as the foundation for change.", num="IV")}
    </div>
    <div class="btn-row mt-4">{btn(H('principles.html'), 'How these commitments are applied', 'outline')}</div>
  </div>
</section>'''

    priorities = f'''<section class="section band band--cream">
  <div class="wrap">
    {section_head("Our priorities", 'From advocacy to <em>action</em>.',
                  'We focus on practical, peaceful campaigns that protect people, place, memory, and the possibility of self-rule. Each priority names who it serves and what progress looks like.')}
    <div class="grid g3">
      {card("Human rights", "Support documentation and advocate for equal rights, safety, and accountability — including for indigenous and marginalised communities whose concerns are least often recorded.", num="Priority 01")}
      {card("Political dialogue", "Bring community priorities to policymakers, civil society, media, and partners through briefings, public explanation, and calm, evidence-led argument.", num="Priority 02")}
      {card("Self-rule campaigns", "Build informed, peaceful campaigns for representation and local decision-making, with clear legal framing and public reasoning at every step.", num="Priority 03")}
      {card("Land protection", "Promote transparent, consent-based decisions about land and development, especially where tenure, water access, or displacement are contested.", num="Priority 04")}
      {card("Resources and environment", "Protect natural resources, livelihoods, and the environment for future generations, with attention to water, grazing, farming, and coastal life.", num="Priority 05")}
      {card("Youth leadership", "Create pathways for young people to lead research, advocacy, enterprise, and renewal — including training in documentation and public communication.", num="Priority 06")}
    </div>
  </div>
</section>'''

    gallery = f'''<section class="section band band--ink2">
  <div class="wrap">
    {section_head("Visual archive", 'Place, memory, and <em>community</em>.',
                  'Representative plates for educational and storytelling purposes. Every plate is labelled as context, never as proof, and historical materials must be verified before publication.',
                  dark=True)}
    <div class="grid g3">
      <div>{plate('coast.svg', 'Coastal orientation', tag='Context plate', cls='plate--wide', note='Illustrative only — no named place or event.')}</div>
      <div>{plate('contour.svg', 'Lower Shabelle terrain', tag='Context plate', cls='plate--wide', note='Illustrative only — not a navigational map.')}</div>
      <div>{plate('weave.svg', 'Shared heritage', tag='Context plate', cls='plate--wide', note='Illustrative only — symbolic, not documentary.')}</div>
    </div>
    <div class="btn-row mt-4">{btn(H('archive.html'), 'Enter the visual archive', 'light')}</div>
  </div>
</section>'''

    history_feature = f'''<section class="section band">
  <div class="wrap grid g-2-1 align-center">
    <div>
      {label("History")}
      <h2 class="display h2 mt-2">Document, verify, <em>remember responsibly</em>.</h2>
      <p class="lede soft mt-3">History is strongest when evidence, testimony, and uncertainty can be held together with care. This platform publishes frameworks and conditions, not conclusions it cannot support.</p>
      <div class="btn-row mt-4">
        {btn(H('history.html'), 'Read history', 'dark')}
        {btn(H('timeline.html'), 'Timeline framework', 'outline')}
      </div>
    </div>
    <div>
      {quote("A label describes the present editorial state of a record. It does not settle its meaning, establish certainty, or remove the need for contextual review.", "Editorial method · Biimaal archive")}
      <div class="chips mt-4">
        <span class="chip chip--orange">Documented evidence</span>
        <span class="chip chip--amber">Community memory</span>
        <span class="chip">Interpretation</span>
        <span class="chip">Open question</span>
      </div>
    </div>
  </div>
</section>'''

    pathways = f'''<section class="section band band--paper2 band--edge">
  <div class="wrap">
    {section_head("The Biimaal archive", 'Three ways into <em>the record</em>.',
                  'The archive offers pathways rather than a final account. Each pathway makes its limits visible, and each record carries the conditions under which it may be read.')}
    <div class="grid g3">
      {card("Broad chronology", "A navigational timeline for locating periods, themes, and questions without claiming a complete historical sequence.", num="01", link=("Open chronology", H("archive/chronology.html")))}
      {card("Places in relation", "Benadir and connected places are considered through movement, language, kinship, work, and changing local relationships.", num="02", link=("Open places", H("archive/places.html")))}
      {card("Protected testimony", "A consent-first pathway for testimony that may require restricted access, community review, or a decision not to publish.", num="03", link=("Open oral histories", H("archive/oral-histories.html")))}
    </div>
    <div class="grid g3 mt-3">
      {card("History & resistance", "A framework for researching late nineteenth-century context, colonial-period records, and wider resistance questions.", tag="Cautious framework", link=("Read the framework", H("archive/history-resistance.html")))}
      {card("Sensitive records", "An editorial frame for material that requires harm minimisation, minimal metadata, and a clear takedown pathway.", tag="Restricted", link=("Read the notice", H("archive/sensitive-records.html")))}
      {card("Editorial method", "How labels, review, consent, translation, and correction actually work inside this archive.", tag="Method", link=("Read the method", H("archive/method.html")))}
    </div>
  </div>
</section>'''

    involved = f'''<section class="section band band--ink">
  <div class="wrap grid g-1-2 align-center">
    <div>
      {label("Get involved", dark=True)}
      <h2 class="display h2 mt-2">Help make the record <em>more accountable</em>.</h2>
      <p class="lede soft mt-3">Share a story, source, correction, or support message in a way that protects your privacy and respects community care. Contributions are reviewed before any public use.</p>
      <div class="btn-row mt-4">
        {btn(H('get-involved.html'), 'Contribute with care', 'primary')}
        {btn(H('questions.html'), 'See open questions', 'light')}
      </div>
    </div>
    <div class="grid g2">
      {card("Share a source", "Point us to a document, photograph, map, or publication with enough context to trace it responsibly.", dark=True)}
      {card("Flag a correction", "Naming, translation, framing, access, and consent are all legitimate grounds for correction.", dark=True)}
      {card("Suggest a question", "A good research lead is a question with context, not a demand for a conclusion.", dark=True)}
      {card("Offer support", "Time, translation, review, or partnership — described plainly, with no obligation attached.", dark=True)}
    </div>
  </div>
</section>'''

    legend = f'''<section class="section section--tight band band--cream">
  <div class="wrap">
    <div class="grid g-1-2 align-center">
      <div>{label("Reading the labels")}<h2 class="display h3 mt-2">Status is part of the record.</h2></div>
      <div>
        <div class="chips">
          <span class="chip chip--orange"><span class="dot dot--open"></span>Verified evidence</span>
          <span class="chip chip--amber">Community memory</span>
          <span class="chip chip--amber">Scholarly interpretation</span>
          <span class="chip">Placeholder</span>
          <span class="chip">Unresolved claim</span>
          <span class="chip chip--ink">Restricted</span>
        </div>
        <p class="small soft mt-2">No label ranks lived knowledge, and none decides truth by itself. <a class="link-arrow" href="{H('archive/method.html')}">Read the full legend →</a></p>
      </div>
    </div>
  </div>
</section>'''

    return hero + mission + research + principles + priorities + gallery + history_feature + pathways + involved + legend


# ============================================================== 02 · ABOUT
def about():
    hero = f'''<section class="pagehero">
  <div class="wrap">
    {crumbs([("Home", H("index.html")), ("About", None)])}
    <div class="pagehero-inner mt-3">
      <div>
        <span class="label label--dark">About Koonfur Bari</span>
        <h1 class="display mt-2">A civic platform rooted in <em>accountability</em>.</h1>
        <p class="lede soft mt-3">Koonfur Bari brings civic advocacy and historical inquiry together without treating either as a finished record. This page explains the platform’s scope, its limits, and the checks that sit between a contribution and a published page.</p>
        <div class="btn-row mt-4">
          {btn(H('mission.html'), 'Our mission', 'primary')}
          {btn(H('archive/method.html'), 'Editorial method', 'light')}
        </div>
      </div>
      <div class="meta-list">
        <div><span>Status</span><b>Active programme</b></div>
        <div><span>Scope</span><b>Southeast Somalia</b></div>
        <div><span>Type</span><b>Civic &amp; research</b></div>
        <div><span>Claims published</span><b>None unverified</b></div>
        <div><span>Review</span><b>Pre-publication</b></div>
      </div>
    </div>
  </div>
</section>'''

    scope = f'''<section class="section band">
  <div class="wrap grid g-1-2 align-start">
    <div>
      {label("Scope and responsibility")}
      <h2 class="display h2 mt-2">What this platform does — and deliberately does not do.</h2>
    </div>
    <div class="body">
      <p class="lead-in">Koonfur Bari supports peaceful discussion of local representation, shared governance, historical memory, land, and community wellbeing. It does not replace legal process, community consent, or independent verification.</p>
      <p class="mt-2">That distinction matters. A civic platform can explain a proposal, document a process, and host careful research. It cannot certify a historical event, settle a land dispute, or speak for a community. Where those tasks belong to courts, assemblies, elders, or families, this platform says so and steps back.</p>
      <p class="mt-2">The programme is designed to support informed civic participation, respectful dialogue, and responsible historical documentation. Every public page is therefore written to be readable by someone who disagrees with it.</p>
    </div>
  </div>
  <div class="wrap mt-5">
    <div class="grid g2">
      <div class="card card--flat">
        <span class="card__num">This platform is</span>
        <ul class="ticks">
          <li>A civic and historical information resource</li>
          <li>A record of frameworks, conditions, and open questions</li>
          <li>A route for corrections, right of reply, and contribution</li>
          <li>Explicit about the limits of every source it describes</li>
          <li>Independent of any armed actor or electoral campaign</li>
        </ul>
      </div>
      <div class="card card--flat">
        <span class="card__num">This platform is not</span>
        <ul class="crosses">
          <li>A legal authority, court, or arbitration body</li>
          <li>A representative body speaking for a community</li>
          <li>A publisher of unverified accusations against named people</li>
          <li>A substitute for consent, safeguarding, or independent peer review</li>
          <li>A complete or final archive of any history</li>
        </ul>
      </div>
    </div>
  </div>
</section>'''

    practice = f'''<section class="section band band--ink">
  <div class="wrap">
    {section_head("Accountability in practice", 'Four checks between a contribution and <em>a public page</em>.',
                  'We aim to identify uncertainty, distinguish evidence from interpretation, welcome correction, and handle personal testimony with care. Contributions are reviewed before any public use.', dark=True)}
    <div class="grid g-1-2 align-start">
      <div>
        {numlist([
          ("Intake", "A source, question, correction, or testimony is received with its context: who supplied it, how it was obtained, and what conditions attach to it."),
          ("Context review", "Wording, attribution, provenance, language, and access conditions are checked before anything is described publicly."),
          ("Editorial decision", "The item may be published, published with limits, held for community review, restricted, or declined. Each outcome is recorded."),
          ("Correction loop", "Published descriptions remain open to challenge, clarification, contextualisation, restriction, or withdrawal."),
        ])}
      </div>
      <div class="grid" style="gap:1rem">
        {card("Editorial review", "A named reviewer checks provenance, framing, translation, and the difference between record and interpretation.", dark=True, num="A")}
        {card("Community review", "Where material concerns a living community, review sits with people who hold the relationships — not only with researchers.", dark=True, num="B")}
        {card("Safeguarding", "Personal testimony, minors, and sensitive accounts are assessed for risk before any description exists.", dark=True, num="C")}
        {card("Right of reply", "A person or family named in a contested account can respond before publication, revision, or further circulation.", dark=True, num="D")}
      </div>
    </div>
  </div>
</section>'''

    programme = f'''<section class="section band band--paper2">
  <div class="wrap">
    {section_head("Programme shape", 'How the work is organised.',
                  'The programme is arranged in four connected tracks so that advocacy, research, archive work, and community care do not drift apart.')}
    <div class="grid g4">
      {card("Civic advocacy", "Public explanation of the proposal, briefings, and peaceful campaigns for representation and local decision-making.", num="Track 01")}
      {card("Research", "Themes, methods, question registers, and reading pathways that can be audited rather than simply believed.", num="Track 02")}
      {card("Archive", "A patient index of periods, places, testimony conditions, and protected records with visible access limits.", num="Track 03")}
      {card("Community care", "Consent, safeguarding, translation, and correction — treated as core work, not as administration.", num="Track 04")}
    </div>
  </div>
</section>'''

    public = f'''<section class="section band">
  <div class="wrap grid g-2-1 align-center">
    <div>
      {label("Public purpose")}
      <h2 class="display h2 mt-2">Written to be useful to people who are <em>not specialists</em>.</h2>
      <p class="body mt-3">Public purpose means plain explanation: what a proposal says, what a record can support, what remains unknown, and how a reader can respond. It also means refusing the pressure to turn a difficult question into a confident slogan.</p>
      <ul class="ticks mt-3">
        <li>Every page states what it can and cannot establish</li>
        <li>Frameworks are published before conclusions</li>
        <li>Corrections are described as a normal editorial outcome</li>
        <li>Language and translation decisions are made visible</li>
      </ul>
    </div>
    <div>{plate('columns.svg', 'Institutions answer to the people they serve', tag='Context plate', cls='plate--wide', note='Illustrative plate — not a named institution or place.')}</div>
  </div>
</section>'''

    funding = f'''<section class="section band band--cream band--edge">
  <div class="wrap grid g2">
    <div>
      {label("Independence")}
      <h3 class="h3 mt-2">No hidden sponsorship.</h3>
      <p class="mt-2">The platform does not accept funding that carries editorial conditions, and it does not accept support from armed actors or electoral campaigns. Where support exists in future, it will be described on this page with its scope and any restrictions attached.</p>
    </div>
    <div id="contact">
      {label("Contact pathways")}
      <h3 class="h3 mt-2">Reach the right desk.</h3>
      {kv([
        ("General", "Use the contribution route on Get involved and select “Support message”."),
        ("Corrections", "Select “Correction” and describe the page, the wording, and the reason."),
        ("Right of reply", "Select “Correction”, mark it as a reply request, and state the urgency."),
        ("Research leads", "Use the research form so the topic and source type stay attached."),
        ("Access requests", "Describe the material by its public description only — never send sensitive content."),
      ])}
      <div class="btn-row mt-3">{btn(H('get-involved.html'), 'Open the contribution route', 'dark')}</div>
    </div>
  </div>
</section>'''

    return hero + scope + practice + programme + public + funding + cta_band(
        "Continue", "Read the mission in full.",
        "The mission page sets out the lawful civic path, the shared-future argument, and the objectives the programme holds itself to.",
        btn(H('mission.html'), 'Our mission', 'primary') + btn(H('principles.html'), 'What guides us', 'light'),
        dark=True)


# ============================================================ 03 · MISSION
def mission():
    hero = f'''<section class="pagehero">
  <div class="wrap">
    {crumbs([("Home", H("index.html")), ("Mission", None)])}
    <div class="pagehero-inner mt-3">
      <div>
        <span class="label label--dark">Our mission</span>
        <h1 class="display mt-2">A peaceful platform for <em>dignity and representation</em>.</h1>
        <p class="lede soft mt-3">Our work is grounded in peaceful advocacy, community consent, historical truth, and the belief that every community deserves safety, representation, and the power to shape its own future.</p>
        <div class="btn-row mt-4">
          {btn(H('principles.html'), 'Our commitments', 'primary')}
          {btn(H('research.html'), 'Research &amp; evidence', 'light')}
        </div>
      </div>
      <div>{plate('delta.svg', 'Livelihoods, water, and connection', tag='Context plate', cls='plate--wide', note='Illustrative plate — not a navigational map.')}</div>
    </div>
  </div>
</section>'''

    pillars = f'''<section class="section band">
  <div class="wrap">
    {section_head("Four pillars", 'What the mission actually asks for.',
                  'The mission is not a single demand. It is a set of connected commitments about voice, land, law, and memory — each of which can be explained, tested, and argued with.')}
    <div class="grid g4">
      {card("Rights and representation", "Community voices should be reflected in decisions that affect their lives, land, and future — through institutions that are accessible to ordinary residents.", num="01")}
      {card("Land and environment", "We support the protection of land, water, natural resources, and community livelihoods, with transparent and consent-based decisions about development.", num="02")}
      {card("Self-rule and justice", "We support inclusive governance, accountability, and the rule of law, including the right to question those who hold office.", num="03")}
      {card("Education and memory", "Documentation, education, and dialogue help new generations understand what happened — and what remains disputed.", num="04")}
    </div>
  </div>
</section>'''

    path = f'''<section class="section band band--ink">
  <div class="wrap grid g2 align-start">
    <div class="card card--dark">
      <span class="label label--dark">A lawful civic path</span>
      <h3 class="display h3 mt-2">Persuasion, not pressure.</h3>
      <p class="mt-2">We support democratic participation, constitutional dialogue, accountable administration, and nonviolent civic action. That means working through public argument, lawful institutions, and negotiated agreement — even when the process is slow, uneven, or incomplete.</p>
      <ul class="ticks mt-3">
        <li>Engage institutions that exist rather than inventing parallel authority</li>
        <li>Publish reasoning so it can be examined and answered</li>
        <li>Refuse violence, coercion, and mobilisation by threat</li>
        <li>Accept that lawful outcomes may differ from preferred outcomes</li>
      </ul>
    </div>
    <div class="card card--dark">
      <span class="label label--dark">A shared future</span>
      <h3 class="display h3 mt-2">Self-rule as responsibility.</h3>
      <p class="mt-2">Local self-rule is discussed here as a framework for responsibility, inclusion, and constructive relationships with wider Somali society. It is argued as a route to better services, clearer accountability, and durable peace — not as a rejection of neighbours.</p>
      <ul class="ticks mt-3">
        <li>Guarantees for minorities and marginalised communities</li>
        <li>Continued cooperation on trade, water, and mobility</li>
        <li>Transparent revenue and public spending</li>
        <li>Negotiated, lawful relationships with federal institutions</li>
      </ul>
    </div>
  </div>
</section>'''

    objectives = f'''<section class="section band band--cream">
  <div class="wrap">
    {section_head("Objectives", 'Six practical objectives, each with a <em>visible test</em>.',
                  'Objectives are written so progress can be seen from outside the programme. Where an objective cannot yet be measured, that is stated rather than hidden.')}
    <div class="grid g3">
      {card("Explain the proposal", "Produce plain-language explanations of what local self-rule would change, in Somali and English, reviewed for accuracy and accessibility.", tag="In progress")}
      {card("Document carefully", "Maintain a labelled archive of periods, places, and testimony conditions that other researchers can audit.", tag="In progress")}
      {card("Protect consent", "Operate a consent-first route for testimony, including restricted and private holdings with a withdrawal path.", tag="Operating")}
      {card("Open the record", "Publish a visible corrections and right-of-reply route, and report how requests were resolved.", tag="Operating")}
      {card("Build local capacity", "Create training and paid pathways for community researchers, translators, and reviewers.", tag="Forthcoming")}
      {card("Advance dialogue", "Convene lawful, non-partisan discussion between communities, civil society, and institutions.", tag="Forthcoming")}
    </div>
    <div class="notice mt-4">
      <span class="label">How to read these labels</span>
      <p>“Operating” means the mechanism exists and is used. “In progress” means it exists in partial form. “Forthcoming” means it is designed but not yet available — and should not be described as if it were.</p>
    </div>
  </div>
</section>'''

    approach = f'''<section class="section band">
  <div class="wrap grid g-2-1 align-start">
    <div>
      {label("How change is pursued")}
      <h2 class="display h2 mt-2">Five steps, repeated.</h2>
      <p class="body mt-3">Advocacy here is iterative. Each cycle produces a public artefact — a briefing, a page, a record, a correction — so that the work can be followed rather than assumed.</p>
      <div class="mt-3">
        {numlist([
          ("Listen", "Meet residents, elders, women’s groups, youth networks, and local institutions. Record priorities and conditions of participation."),
          ("Document", "Gather sources and context. Separate what is documented from what is remembered, interpreted, or alleged."),
          ("Explain", "Write the argument plainly, in both working languages, and say what would change our mind."),
          ("Engage", "Bring the argument to institutions, media, partners, and critics — calmly, repeatedly, and in public."),
          ("Review", "Publish what happened, including objections, corrections, and unresolved questions."),
        ])}
      </div>
    </div>
    <div>{plate('mapgrid.svg', 'Relationship, not boundary', tag='Orientation plate', cls='plate--sq', note='Illustrative only — no legal or navigational claim.')}</div>
  </div>
</section>'''

    partners = f'''<section class="section band band--paper2 band--edge">
  <div class="wrap">
    {section_head("Who this is for", 'Four audiences, four different <em>needs</em>.',
                  'The same proposal has to be legible to a resident, a researcher, an official, and a sceptic. Writing for one of them alone is how civic arguments fail.')}
    <div class="grid g4">
      {card("Residents", "Clear information about services, land, representation, and how to raise a concern without risk.", num="01")}
      {card("Researchers", "Frameworks, labels, source conditions, and citation guidance that make limits visible.", num="02")}
      {card("Institutions", "Briefings that state the argument, the evidence, and the specific ask.", num="03")}
      {card("Diaspora &amp; partners", "A way to follow the work, contribute sources, and support documentation responsibly.", num="04")}
    </div>
  </div>
</section>'''

    return hero + pillars + path + objectives + approach + partners + cta_band(
        "Next", "See how the commitments are applied.",
        "Principles matter when they constrain something. The principles page shows where the programme refuses shortcuts and how each commitment is tested in practice.",
        btn(H('principles.html'), 'What guides us', 'primary') + btn(H('get-involved.html'), 'Get involved', 'light'))


# ========================================================= 04 · PRINCIPLES
def principles():
    hero = f'''<section class="pagehero">
  <div class="wrap">
    {crumbs([("Home", H("index.html")), ("Principles", None)])}
    <div class="pagehero-inner mt-3">
      <div>
        <span class="label label--dark">What guides us</span>
        <h1 class="display mt-2">Four commitments. <em>One peaceful path.</em></h1>
        <p class="lede soft mt-3">The platform’s civic and research work is guided by lawful participation, accountability, equal dignity, and shared peace. This page sets out what each commitment requires — and where it forbids something we might otherwise be tempted to do.</p>
      </div>
      <div class="meta-list">
        <div><span>Commitment</span><b>01 Lawful</b></div>
        <div><span>Commitment</span><b>02 Accountable</b></div>
        <div><span>Commitment</span><b>03 Equal dignity</b></div>
        <div><span>Commitment</span><b>04 Shared peace</b></div>
      </div>
    </div>
  </div>
</section>'''

    blocks = ""
    data = [
        ("I", "Lawful recognition",
         "A democratic path toward recognised local self-rule within a constitutional framework.",
         ["Argue through institutions that exist, including courts and assemblies",
          "Publish the legal reasoning behind any proposal",
          "Accept that lawful decisions may not be the ones we prefer",
          "Refuse any route that depends on coercion or force"],
         "Lawfulness is not a formality. It is what makes a claim durable after the current argument is over."),
        ("II", "Accountable administration",
         "Institutions that protect public resources and answer to the people they serve.",
         ["Describe how revenue, land, and appointments would be transparent",
          "Support audit, public reporting, and access to information",
          "Name the mechanism by which an official can be questioned",
          "Oppose impunity, including where it is politically convenient"],
         "Accountability is only real if it applies to allies as well as opponents."),
        ("III", "Equal dignity",
         "Equal protection and political agency for indigenous and marginalised communities.",
         ["Ensure minority representation is structural, not symbolic",
          "Treat consent as a condition, not a consultation step",
          "Make language and access decisions with affected communities",
          "Refuse accounts that erase or instrumentalise marginalised people"],
         "A majority claim cannot substitute for the consent of those who would be governed by it."),
        ("IV", "Shared peace",
         "Reconciliation, lawful negotiation, and nonviolent participation as the foundation for change.",
         ["Reject incitement, dehumanising language, and mobilisation by threat",
          "Keep channels open to those who disagree",
          "Separate disagreement from enmity",
          "Support processes that repair relationships, not only settle disputes"],
         "Peace is not the absence of argument. It is the condition that lets argument remain lawful."),
    ]
    for num, title, lead, bullets, note in data:
        blocks += f'''<div class="grid g-1-3 align-start" style="padding-block:clamp(1.8rem,3.4vw,2.8rem);border-top:1px solid var(--line)">
  <div>
    <span class="display" style="font-size:clamp(2.6rem,4vw,3.6rem);color:#7d5f10;line-height:1">{num}</span>
    <h2 class="display h3 mt-2">{title}</h2>
  </div>
  <div>
    <p class="lead-in">{lead}</p>
    <ul class="ticks mt-2">{"".join(f"<li>{b}</li>" for b in bullets)}</ul>
    <p class="aside-note mt-3">{note}</p>
  </div>
</div>'''

    applied = f'''<section class="section band">
  <div class="wrap">
    {section_head("Application", 'Where a principle has to <em>constrain</em> us.',
                  'A commitment that never rules anything out is decoration. The table below names situations where the programme accepts a slower or less satisfying course.')}
    <div class="card card--flat" style="padding:clamp(.8rem,2vw,1.4rem);overflow-x:auto">
      <table class="table">
        <caption>Principle in tension with pressure</caption>
        <thead><tr><th>Pressure</th><th>What the principle requires</th><th>Commitment</th></tr></thead>
        <tbody>
          <tr><td>A story is compelling but unverified</td><td>Publish the question and the label, not the conclusion.</td><td>Accountable</td></tr>
          <tr><td>A source asks for anonymity</td><td>Honour it, describe the condition, and accept a thinner record.</td><td>Equal dignity</td></tr>
          <tr><td>A claim would mobilise support quickly</td><td>Check whether it hardens division before it informs.</td><td>Shared peace</td></tr>
          <tr><td>A partner wants favourable framing</td><td>Decline the condition, or describe it publicly.</td><td>Lawful</td></tr>
          <tr><td>A named person disputes a record</td><td>Offer reply, review context, revise or restrict if warranted.</td><td>Equal dignity</td></tr>
          <tr><td>An institution is slow to respond</td><td>Keep engaging lawfully; document the delay.</td><td>Lawful</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</section>'''

    limits = f'''<section class="section band band--paper2">
  <div class="wrap grid g2 align-start">
    <div>
      {label("Red lines")}
      <h2 class="display h2 mt-2">What the programme will not do.</h2>
      <ul class="crosses mt-3">
        <li>Publish unverified accusations against named individuals</li>
        <li>Describe allegation as established fact, or memory as proof</li>
        <li>Publish testimony without consent, or after consent is withdrawn</li>
        <li>Accept funding that carries editorial conditions</li>
        <li>Coordinate with armed actors or electoral campaigns</li>
        <li>Use translation to smooth over disagreement</li>
        <li>Present a navigational or legal claim as settled when it is contested</li>
      </ul>
    </div>
    <div>
      {label("Review")}
      <h2 class="display h2 mt-2">How compliance is checked.</h2>
      <div class="mt-3">
        {accordion([
          ("Who reviews a page before publication?",
           "A subject reviewer checks provenance and framing; a language reviewer checks translation and terminology; a safeguarding reviewer is consulted where living people, minors, or sensitive accounts are involved."),
          ("What happens when a red line is crossed?",
           "The item is restricted or withdrawn, the reason is recorded internally, and a public note is added where the withdrawal itself is significant."),
          ("Can the principles be changed?",
           "Yes, but only in public. Amendments are dated, explained, and kept visible alongside the previous wording."),
          ("How are partner relationships governed?",
           "Written terms state that no partner reviews or approves editorial content, and any support received is described on the About page."),
        ])}
      </div>
    </div>
  </div>
</section>'''

    return hero + f'<section class="section band"><div class="wrap">{blocks}</div></section>' + applied + limits + cta_band(
        "Continue", "Read the mission these commitments serve.",
        "The mission page sets out the lawful civic path and the six objectives the programme measures itself against.",
        btn(H('mission.html'), 'Our mission', 'primary') + btn(H('archive/method.html'), 'Editorial method', 'light'))


# ============================================================ 05 · HISTORY
def history():
    hero = f'''<section class="pagehero">
  <div class="wrap">
    {crumbs([("Home", H("index.html")), ("History", None)])}
    <div class="pagehero-inner mt-3">
      <div>
        <span class="label label--dark">History</span>
        <h1 class="display mt-2">A record that asks to be <em>read carefully</em>.</h1>
        <p class="lede soft mt-3">History is not strengthened by certainty alone. It requires attention to records, testimony, context, absence, and the questions that remain open.</p>
        <div class="btn-row mt-4">
          {btn(H('timeline.html'), 'Timeline framework', 'primary')}
          {btn(H('archive/chronology.html'), 'Chronology docket', 'light')}
        </div>
      </div>
      <div>{plate('contour.svg', 'Terrain of memory', tag='Context plate', cls='plate--wide', note='Illustrative plate — not archival evidence.')}</div>
    </div>
  </div>
</section>'''

    approach = f'''<section class="section band">
  <div class="wrap">
    {section_head("How this platform approaches history", 'Three habits before any <em>conclusion</em>.',
                  'Historical images, documents, and oral accounts can inform one another, but none should be detached from its setting. The archive labels contextual materials rather than presenting them as verified proof.')}
    <div class="grid g3">
      {card("Read the maker", "A record is made by someone, for a purpose. Administrative vocabulary, omissions, and categories are part of what the record is, not noise around it.", num="01")}
      {card("Read the silence", "A missing name or an absent file may indicate loss, restriction, danger, or simply a different record-keeping practice. Absence is not proof.", num="02")}
      {card("Read the reader", "Interpretation is situated too. A researcher’s questions, language, and moment shape what becomes visible — so interpretation is labelled as interpretation.", num="03")}
    </div>
    <div class="notice mt-4">
      <span class="label">Care before publication</span>
      <p>Where provenance is incomplete, the platform says so. Where accounts differ, the difference remains visible. Responsible memory leaves room for further research and correction.</p>
    </div>
  </div>
</section>'''

    layers = f'''<section class="section band band--ink">
  <div class="wrap">
    {section_head("Reading layers", 'Four kinds of material, <em>held apart</em>.',
                  'Most historical harm happens when categories collapse: a memory becomes a fact, an allegation becomes a finding, an interpretation becomes a record. These four panels are the basic discipline.', dark=True)}
    <div class="grid g4">
      {card("Documented evidence", "Materials with identifiable sources can still require context, interpretation, and corroboration. Provenance is a starting condition, not a verdict.", num="L1", dark=True, chips='<span class="chip chip--orange">Documented</span>')}
      {card("Testimony", "Community testimony carries knowledge, relationship, and obligations of consent that must be respected — including the right not to be quoted.", num="L2", dark=True, chips='<span class="chip chip--amber">Memory</span>')}
      {card("Interpretation", "Interpretation should be labelled, and uncertainty should remain visible where evidence is incomplete. An argument is not a source.", num="L3", dark=True, chips='<span class="chip chip--ghost-light">Analysis</span>')}
      {card("Open questions", "Not every question requires an immediate answer. Some questions are the most honest thing a record can contain.", num="L4", dark=True, chips='<span class="chip chip--ghost-light">Unresolved</span>')}
    </div>
  </div>
</section>'''

    contexts = f'''<section class="section band band--paper2">
  <div class="wrap">
    {section_head("Contexts", 'Periods are a research scaffold, <em>not a sequence</em>.',
                  'The archive organises material by broad context so that readers can locate questions. No entry in this list asserts a date, actor, or outcome as established.')}
    <div class="grid g2">
      <div class="card card--flat">
        <span class="card__num">Context 01</span>
        <h3 class="h4">Late nineteenth-century conditions</h3>
        <p class="mt-1">Changing political, commercial, religious, environmental, and social conditions across the wider region. Research may ask how these were experienced locally without assuming a single cause or turning context into a claim.</p>
      </div>
      <div class="card card--flat">
        <span class="card__num">Context 02</span>
        <h3 class="h4">Colonial-period records</h3>
        <p class="mt-1">Administrative documents preserve purpose as well as information. Catalogues, correspondence, reports, maps, and registers can be relevant while carrying institutional vocabulary, omissions, and uneven points of view.</p>
      </div>
      <div class="card card--flat">
        <span class="card__num">Context 03</span>
        <h3 class="h4">Resistance and political change</h3>
        <p class="mt-1">Refusal, negotiation, survival, mobility, labour, language, care, and public action appear differently across sources. The archive does not use “resistance” as an automatic description of any person or event.</p>
      </div>
      <div class="card card--flat">
        <span class="card__num">Context 04</span>
        <h3 class="h4">Contemporary memory</h3>
        <p class="mt-1">Living accounts may be described by their access conditions rather than displayed — especially where consent, safeguarding, or community review remains active.</p>
      </div>
    </div>
    <div class="btn-row mt-4">{btn(H('archive/chronology.html'), 'Open the chronology framework', 'dark')}</div>
  </div>
</section>'''

    caution = f'''<section class="section band">
  <div class="wrap grid g-2-1 align-center">
    <div>
      {label("Caution")}
      <h2 class="display h2 mt-2">This page contains no verified historical claims.</h2>
      <p class="body mt-3">It deliberately avoids inventing specific events, names, quotations, casualty figures, or citations. Future additions should visibly distinguish evidence type, provenance, confidence, corroboration, and current verification status.</p>
      <p class="body mt-2">Where a page cannot meet that standard, the honest options are to describe less, label the uncertainty, or wait.</p>
      <div class="btn-row mt-4">
        {btn(H('archive/history-resistance.html'), 'History &amp; resistance framework', 'dark')}
        {btn(H('questions.html'), 'Open questions', 'outline')}
      </div>
    </div>
    <div class="card card--flat">
      <span class="label">Reading checklist</span>
      <ul class="ticks mt-2">
        <li>Who made this, and for whom?</li>
        <li>What kind of material is it?</li>
        <li>What would corroborate it — and has that been done?</li>
        <li>Who might be harmed by circulating it now?</li>
        <li>What would correction look like?</li>
      </ul>
    </div>
  </div>
</section>'''

    return hero + approach + layers + contexts + caution + cta_band(
        "Continue", "Read the record through its labels.",
        "The editorial method explains every status label used across the archive, how review works, and how correction and withdrawal are handled.",
        btn(H('archive/method.html'), 'Editorial method', 'primary') + btn(H('research.html'), 'Research & evidence', 'light'))


PAGES = [
    dict(url="index.html", nav_title="Home", section="Program",
         title="Koonfur Bari — Southern Somalia Research Program",
         description="A civic and historical platform supporting the Southeast region’s proposal to manage its own affairs through lawful, peaceful, and democratic means.",
         active="", body=home),
    dict(url="about.html", nav_title="About", section="Program",
         title="About — Koonfur Bari",
         description="Scope, accountability, independence, programme shape, and contact pathways for the Koonfur Bari civic and historical platform.",
         active="about.html", body=about),
    dict(url="mission.html", nav_title="Mission", section="Program",
         title="Our mission — Koonfur Bari",
         description="A peaceful platform for dignity and representation: the lawful civic path, a shared future, and six practical objectives with visible tests.",
         active="mission.html", body=mission),
    dict(url="principles.html", nav_title="Principles", section="Program",
         title="What guides us — Koonfur Bari",
         description="Four commitments — lawful recognition, accountable administration, equal dignity, and shared peace — and where each constrains the programme.",
         active="principles.html", body=principles),
    dict(url="history.html", nav_title="History", section="Program",
         title="History — Koonfur Bari",
         description="How this platform approaches history: makers, silences, interpretation, and the categories that keep evidence, memory, and analysis apart.",
         active="history.html", body=history),
]
