"""Biimaal archive dockets + 404."""
import ui
from ui import (H, label, btn, plate, section_head, card, kv, accordion,
                numlist, statrow, filters, tabs, notice, quote, cta_band, crumbs)


def sub_crumbs(name):
    return crumbs([("Home", H("index.html")), ("Archive", H("archive.html")), (name, None)])


def archive_hero(name, lbl, title, lead, plate_name, note, meta, actions=None):
    acts = actions or (btn(H('archive/method.html'), 'Editorial method', 'light'))
    meta_html = "".join(
        f'<div><span>{k}</span><b>{v}</b></div>' for k, v in meta
    )
    return f'''<section class="pagehero">
  <div class="wrap">
    {sub_crumbs(name)}
    <div class="pagehero-inner mt-3">
      <div>
        <span class="label label--dark">{lbl}</span>
        <h1 class="display mt-2">{title}</h1>
        <p class="lede soft mt-3">{lead}</p>
        <div class="btn-row mt-4">{acts}</div>
        <div class="meta-strip mt-4">{meta_html}</div>
      </div>
      <div>
        {plate(plate_name, note, tag='Context plate', cls='plate--wide', note='Illustrative plate — not archival evidence.')}
      </div>
    </div>
  </div>
</section>'''


# ======================================================== CHRONOLOGY
def chronology():
    hero = archive_hero(
        "Chronology", "Chronology · working framework",
        'A map of questions <em>across time</em>.',
        'These broad markers are research prompts, not confirmed events or a complete periodisation. Entries will expand only as documentation and community review allow.',
        'contour.svg', 'Layers of context, not a sequence',
        [("Entries", "06"), ("Periods", "Framework"), ("Status", "Placeholder"), ("Claims", "None")],
        btn(H('archive/places.html'), 'Places in relation', 'primary') + btn(H('archive/method.html'), 'Method', 'light'))

    intro = f'''<section class="section band">
  <div class="wrap grid g-1-2 align-center">
    <div>
      {label("How to read this docket")}
      <h2 class="display h2 mt-2">Periods are prompts, <em>not proof</em>.</h2>
      <p class="body mt-3">A period heading helps a reader locate a question. It does not establish that something happened in that period, that the period is agreed, or that the category is locally meaningful.</p>
      <p class="body mt-2">Where a date appears in future entries, it will carry its own status: documented, inferred, contested, or approximate.</p>
    </div>
    <div class="card card--flat">
      <span class="label">Entry states</span>
      {kv([("Context", "Broad orientation. No specific claim."), ("Under review", "Material identified; description not yet ready."), ("Consent-led", "Living accounts; access conditions apply."), ("Restricted", "Existence acknowledged; contents withheld.")])}
    </div>
  </div>
</section>'''

    entries = f'''<section class="section band band--ink">
  <div class="wrap">
    {section_head("Perioscope", 'Six entries, each with <em>evidence fields</em>.',
                  'Expand an entry to see what would be needed before any public historical claim could be responsibly described.', dark=True)}
    <div class="grid g2">
      {card("Earlier contexts", "A space for orienting readers to broad regional contexts before connecting any source to a particular community history. No periodisation is asserted.", num="01 · Context only", dark=True, link=("Evidence fields", H("#ea")))}
      {card("Regional reference points", "Comparative material from neighbouring areas may help frame questions, but difference must not be smoothed into resemblance.", num="02 · Context", dark=True)}
      {card("Twentieth-century materials", "Records requiring comparison: catalogues, correspondence, registers, and reports whose provenance, language, and relationship to scope are assessed.", num="03 · Under review", dark=True)}
      {card("Potential records", "May be catalogued as leads while provenance, language, and relationship to the archive’s scope are assessed.", num="04 · Leads", dark=True)}
      {card("Contemporary memory", "Living accounts and stewardship, described by access conditions rather than displayed where consent review remains active.", num="05 · Consent-led", dark=True)}
      {card("Protected holdings", "Material that exists but is not available for browsing, quotation, or inference from the public description.", num="06 · Restricted", dark=True)}
    </div>
  </div>
</section>'''

    detail = f'''<section class="section band band--cream" id="ea">
  <div class="wrap">
    {section_head("Evidence fields", 'What a future entry would need.',
                  'These are the fields that turn a prompt into a record. They are shown empty here so the gap is visible rather than hidden.')}
    <div class="grid g-1-2 align-start">
      <div>
        {tabs("chron", [
            ("Context 01", kv([("Period label", "Earlier contexts — broad orientation"), ("What it can support", "Locating a question, not answering it"), ("Provenance", "No source attached in this placeholder state"), ("Status", "Open research question")])),
            ("Record 03", kv([("Period label", "Twentieth-century materials — under review"), ("What it can support", "Comparative reading once provenance is documented"), ("Provenance", "Repository, creator, date range, language: not yet supplied"), ("Status", "Leads only; not a public claim")])),
            ("Memory 05", kv([("Period label", "Contemporary memory — consent-led"), ("What it can support", "Context and language, where consent allows"), ("Provenance", "Contributor conditions; review ongoing"), ("Status", "Described by access, not content")])),
        ])}
      </div>
      <div class="notice">
        <span class="label">Verification rule</span>
        <p>A period entry can be published before its supporting material is fully documented — but only when it is labelled as a prompt. The label is not a formality; it is the condition that makes publication honest.</p>
      </div>
    </div>
  </div>
</section>'''

    return hero + intro + entries + detail + cta_band(
        "Next docket", "Places in relation.",
        "Place labels carry their own conditions: orientation, connection, movement, and naming. The places docket explains how each is used.",
        btn(H('archive/places.html'), 'Places in relation', 'primary') + btn(H('timeline.html'), 'Timeline framework', 'light'))


# ============================================================ PLACES
def places():
    hero = archive_hero(
        "Places", "Places · orientation and connection",
        'Place is a relationship, <em>not a boundary line</em>.',
        'The archive begins with Benadir as a point of orientation while remaining attentive to wider coastal, inland, urban, rural, and diasporic connections.',
        'mapgrid.svg', 'Orientation, not enclosure',
        [("Starting point", "Benadir"), ("Connection types", "04"), ("Boundary claims", "None"), ("Access", "Open")],
        btn(H('map.html'), 'See the orientation diagram', 'primary') + btn(H('archive/chronology.html'), 'Chronology', 'light'))

    cards = f'''<section class="section band">
  <div class="wrap">
    {section_head("Connected places", 'Four kinds of connection, <em>each conditional</em>.',
                  'Place labels may be historical, contemporary, approximate, translated, or contested, and should be read with their stated limits.')}
    <div class="grid g4">
      {card("Benadir orientation", "A starting point for locating a context, without defining the full reach of community ties or historical movement.", num="01")}
      {card("Coastal connections", "Ports, fishing, trade, and travel link settlements in ways registers rarely capture. These are questions, not routes.", num="02")}
      {card("Inland relations", "Kinship, grazing, and markets connect inland and riverine communities. Naming may differ between records and local usage.", num="03")}
      {card("Diasporic pathways", "Remittance, correspondence, and return shape how histories are remembered — and may preserve material absent locally.", num="04")}
    </div>
  </div>
</section>'''

    naming = f'''<section class="section band band--ink">
  <div class="wrap grid g2 align-start">
    <div>
      {label("Identity and terminology", dark=True)}
      <h2 class="display h2 mt-2">Names are living terms, <em>not fixed labels</em>.</h2>
      <p class="lede soft mt-3">This archive uses “Biimaal / Bimal” as an inclusive working form. Terminology can vary across language, family, place, period, source type, and personal preference.</p>
      <p class="body soft mt-2">The archive records variation with care rather than treating one spelling as universally final. Where terminology is translated, abbreviated, inherited from a catalogue, or supplied by a researcher, that condition should be visible.</p>
    </div>
    <div class="grid" style="gap:1rem">
      {card("Working term", "“Biimaal” — used here as one visible archive term. Its appearance does not establish a single pronunciation, boundary, lineage, or meaning across every source.", dark=True, num="Term A")}
      {card("Variant usage", "“Bimal” — included as a variant that may appear in conversation, memory, scholarship, catalogues, or other records. Similar spelling is not assumed to mean identical context.", dark=True, num="Term B")}
      {card("Terminology note", "Community preference and self-description take priority over convenient archival shorthand.", dark=True, num="Note")}
    </div>
  </div>
</section>'''

    limits = f'''<section class="section band band--cream">
  <div class="wrap">
    {section_head("Reading place labels", 'What a place name can and <em>cannot</em> do.',
                  'A place name locates a description; it does not establish a boundary, a population, or a political claim.')}
    <div class="card card--flat" style="padding:clamp(.8rem,2vw,1.4rem);overflow-x:auto">
      <table class="table">
        <caption>Place label conditions</caption>
        <thead><tr><th>Label type</th><th>What it supports</th><th>What it does not support</th></tr></thead>
        <tbody>
          <tr><td>Historical name</td><td>Locating a period-specific description</td><td>A claim that the name is current or exclusive</td></tr>
          <tr><td>Administrative name</td><td>Reading a record by its own categories</td><td>A claim about local self-description</td></tr>
          <tr><td>Approximate location</td><td>Orientation for a reader</td><td>Precision about a boundary or site</td></tr>
          <tr><td>Contested name</td><td>Showing that naming is disputed</td><td>Adjudicating which name is correct</td></tr>
          <tr><td>Withheld location</td><td>Protecting people or sites at risk</td><td>Inferring a location from description</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</section>'''

    return hero + cards + naming + limits + cta_band(
        "Next docket", "Oral histories.",
        "Testimony is held with context, consent, and the right to remain unfinished. The oral histories docket explains the conditions.",
        btn(H('archive/oral-histories.html'), 'Oral histories', 'primary') + btn(H('archive/method.html'), 'Method', 'light'))


# ==================================================== ORAL HISTORIES
def oral_histories():
    hero = archive_hero(
        "Oral histories", "Oral histories · consent-led description",
        'Oral testimony is held with context, consent, and <em>the right to remain unfinished</em>.',
        'This docket models a careful oral-history archive. It contains no recordings, names, quotations, dates, places, or claims. The placeholders show how access, consent, identity, language, safeguarding, and uncertainty can remain visible together.',
        'portrait.svg', 'Atmospheric plate — not documentary evidence',
        [("Holdings", "03 placeholders"), ("Recordings", "None"), ("Access", "Varies"), ("Withdrawal", "Always available")],
        btn(H('#placeholders'), 'View testimony placeholders', 'primary') + btn(H('#care'), 'Read the care statement', 'light'))

    care = f'''<section class="section band" id="care">
  <div class="wrap grid g-1-2 align-start">
    <div>
      {label("Before engaging")}
      <h2 class="display h2 mt-2">Listening is not a licence to <em>circulate</em>.</h2>
      <p class="body mt-3">Oral testimony may include personal experience, community memory, inherited knowledge, uncertainty, grief, or disagreement. A responsible archive does not treat spoken material as automatically public, final, representative, or independently verified.</p>
      <p class="body mt-2">Access and description should follow informed consent, speaker wishes, safeguarding review, relevant community protocol, and a clear route for revision or withdrawal.</p>
    </div>
    <div class="grid" style="gap:1rem">
      {card("Consent is ongoing", "A contributor may set access conditions, revisit them, limit future use, ask for contextual changes, or seek withdrawal. Consent should be understandable, documented appropriately, and reviewed when circumstances change.", num="01")}
      {card("Identity is a protected decision", "Names, voices, kinship details, locations, accents, occupations, and contextual clues can identify a person. Attribution is used only where permission and safety review support it.", num="02")}
      {card("Labels stay distinct", "Oral testimony, community memory, scholarly interpretation, allegation, unresolved claim, and verified evidence are not interchangeable.", num="03")}
    </div>
  </div>
</section>'''

    placeholders = f'''<section class="section band band--ink" id="placeholders">
  <div class="wrap">
    {section_head("Testimony index", 'Three access conditions, <em>no exposed speaker</em>.',
                  'These are deliberately non-specific placeholders. Their purpose is to make archive decisions legible: whether a transcript exists, how language is described, who may review material, and why an item may remain closed.', dark=True)}
    <div class="grid g3">
      <article class="card card--dark">
        <span class="chip chip--ghost-light">Restricted access</span>
        <h3 class="h4 mt-2">Testimony placeholder A</h3>
        <p class="mt-1">A placeholder for oral testimony held under restricted conditions. The record is not available for browsing, quotation, download, or inference from this page.</p>
        {kv([("Consent status", "Safeguarded"), ("Transcript", "Not publicly available"), ("Review", "Required before any description")], dark=True)}
      </article>
      <article class="card card--dark">
        <span class="chip chip--ghost-light">Private access</span>
        <h3 class="h4 mt-2">Testimony placeholder B</h3>
        <p class="mt-1">A placeholder for testimony retained privately. It may be held for a contributor, designated custodians, or a defined care process rather than for public research access.</p>
        {kv([("Consent status", "Private"), ("Transcript", "Access not assigned"), ("Custody", "Contributor-nominated")], dark=True)}
      </article>
      <article class="card card--dark">
        <span class="chip chip--ghost-light">Community review</span>
        <h3 class="h4 mt-2">Testimony placeholder C</h3>
        <p class="mt-1">A placeholder for testimony awaiting or requiring community review. Access, wording, context, translation, and publication remain open questions.</p>
        {kv([("Consent status", "Review-led"), ("Transcript", "Review-dependent"), ("Translation", "Not yet agreed")], dark=True)}
      </article>
    </div>
    <h3 class="display h3 mt-5">Placeholder A · what may be described</h3>
    <div class="mt-3">
      {tabs("testimony", [
          ("Transcript preview", '<p class="small soft">No transcript text is displayed. A restricted transcript preview should state only that access is controlled and should never reveal identifying wording, voice detail, or sensitive content through excerpts.</p>'),
          ("Metadata", kv([("Language", "Language information is intentionally withheld where it could contribute to identification or bypass an agreed access boundary."), ("Recording", "No recording date, format, duration, location, equipment detail, or custody history is supplied."), ("Safeguarding", "A documented safety, consent, and access review is required before any description or sharing decision.")])),
          ("Privacy guidance", '<p class="small soft">Restricted means access is not assumed. The archive should minimise metadata, protect speaker identification, respect agreed conditions, and avoid creating discoverability through description alone.</p>'),
      ])}
    </div>
  </div>
</section>'''

    withdrawal = f'''<section class="section band band--cream">
  <div class="wrap">
    {section_head("Withdrawal and revision", 'A contributor can change their mind. <em>That is the system working</em>.',
                  'Withdrawal is not treated as a problem to be managed, but as a condition of participation. The archive records the decision without exposing the contributor.')}
    <div class="grid g4">
      {card("Revise", "Ask for context, wording, translation, or framing to be changed.", num="A")}
      {card("Restrict", "Move material from open to review-led, restricted, or private.", num="B")}
      {card("Withdraw", "Ask that material be removed from public description entirely.", num="C")}
      {card("Silence", "Ask that nothing further be published or said about the item.", num="D")}
    </div>
    <div class="notice mt-4">
      <span class="label">Practical note</span>
      <p>Withdrawal from a public description is straightforward. Withdrawal from third-party circulation is not always possible — which is why minimisation and consent come before publication, not after.</p>
    </div>
  </div>
</section>'''

    return hero + care + placeholders + withdrawal + cta_band(
        "Next docket", "History and resistance research.",
        "A cautious framework for approaching late nineteenth-century context, colonial-period records, and wider resistance questions.",
        btn(H('archive/history-resistance.html'), 'History &amp; resistance', 'primary') + btn(H('archive/sensitive-records.html'), 'Sensitive records', 'light'))


# ================================================ HISTORY & RESISTANCE
def history_resistance():
    hero = archive_hero(
        "History &amp; resistance", "History &amp; resistance · cautious working framework",
        'A framework for researching history, power, and <em>resistance with care</em>.',
        'This docket gathers questions and research pathways for approaching late nineteenth-century context, colonial-period records, and wider Benadir resistance research. It does not present a settled narrative or treat incomplete evidence as proof.',
        'weave.svg', 'A visual atmosphere only',
        [("Entries", "04 routes"), ("Claims", "None"), ("Labels", "Visible"), ("Status", "Framework")],
        btn(H('#routes'), 'Explore the framework', 'primary') + btn(H('#caution'), 'Read the caution', 'light'))

    how = f'''<section class="section band">
  <div class="wrap grid g-1-2 align-start">
    <div>
      {label("How to use this page")}
      <h2 class="display h2 mt-2">A research scaffold, not a <em>chronology</em>.</h2>
      <p class="body mt-3">The entries here are research routes. Labels distinguish archival record, scholarly interpretation, eyewitness account, community memory, allegation, and unresolved claim. A label describes current editorial status; it does not settle meaning or certainty.</p>
      <p class="body mt-2">Readers looking for a narrative account will not find one here. That is a deliberate editorial decision: a narrative requires decisions this archive has not yet evidenced.</p>
    </div>
    <div class="notice">
      <span class="label">Caution</span>
      <p>Historians of the region disagree — about periodisation, causality, the reliability of particular series, and the language used to describe events. Presenting agreement where none exists would be a form of invention.</p>
    </div>
  </div>
</section>'''

    routes = f'''<section class="section band band--paper2" id="routes">
  <div class="wrap">
    {section_head("Evidence routes", 'Four routes, four <em>different kinds of support</em>.',
                  'Each route names what it could support and what it could not. None of them is a finding.')}
    {filters("hr", [("all", "All entries", "4"), ("record", "Archival record", ""), ("interp", "Interpretation", ""), ("memory", "Community memory", "")])}
    <div class="grid g2">
      <article class="card" data-cat="record" data-scope="hr">
        <span class="chip">Archival record placeholder</span>
        <h3 class="h4 mt-2">Colonial-period documents</h3>
        <p class="mt-1">Catalogues, correspondence, reports, maps, and registers may be relevant to research, but they may also contain institutional vocabulary, omissions, and uneven points of view. Their existence alone does not verify the account they appear to offer.</p>
        {kv([("Provenance", "Repository, creator, date, collection history, and access conditions remain to be documented."), ("Corroboration", "Needs contextual reading alongside other records and, where welcomed, community knowledge."), ("Confidence", "Unrated until an actual record and its context are reviewed.")])}
      </article>
      <article class="card" data-cat="interp" data-scope="hr">
        <span class="chip chip--ink">Scholarly interpretation</span>
        <h3 class="h4 mt-2">Wider Benadir resistance research</h3>
        <p class="mt-1">Researchers may ask how refusal, negotiation, survival, mobility, labour, language, care, or public action are framed in different sources. This archive does not use the term as an automatic description of any particular event or person.</p>
        {kv([("Interpretive basis", "No publication, author, or citation is supplied in this framework."), ("Analytical limits", "Interpretation should remain separate from primary records and memory."), ("Verification status", "Interpretive prompt only — not a verified conclusion.")])}
      </article>
      <article class="card" data-cat="memory" data-scope="hr">
        <span class="chip chip--amber">Community memory</span>
        <h3 class="h4 mt-2">Intergenerational remembrance</h3>
        <p class="mt-1">Community-held knowledge may preserve language, questions, relationships, and interpretive context. It should be described as memory unless separately supported and shared for that purpose under agreed conditions.</p>
        {kv([("Care conditions", "No testimony is included here; consent, attribution, and circulation preferences would be required first."), ("Status", "Community memory — not independently verified."), ("Publication", "Depends on an agreed access context.")])}
      </article>
      <article class="card" data-cat="record" data-scope="hr">
        <span class="chip chip--orange">Context only</span>
        <h3 class="h4 mt-2">Late nineteenth-century conditions</h3>
        <p class="mt-1">Regional change requires locally grounded reading. Research may examine changing political, commercial, religious, environmental, and social conditions across the wider region. This placeholder assigns no single cause, date, actor, or outcome.</p>
        {kv([("Provenance", "No specific source has been attached in this placeholder state."), ("Corroboration", "Requires comparison across independently situated materials."), ("Verification status", "Open research question.")])}
      </article>
    </div>
    <p class="is-hidden small soft mt-3" data-empty="hr">No routes in this category yet.</p>
  </div>
</section>'''

    language = f'''<section class="section band band--ink">
  <div class="wrap grid g-2-1 align-start">
    <div>
      {label("Language and framing", dark=True)}
      <h2 class="display h2 mt-2">Words carry the argument.</h2>
      <p class="lede soft mt-3">“Resistance”, “revolt”, “rebellion”, “uprising”, and “struggle” are not synonyms. Each frames a different relationship between people, power, and legitimacy.</p>
      <p class="body soft mt-2">This archive does not adopt a term on behalf of a community. Where a source uses one, the term is quoted with its context. Where a working term is used by the archive, it is described as a working term.</p>
    </div>
    <div class="grid" style="gap:.8rem">
      {card("Language is evidence of position", "Cataloguing terms and translations may reflect a record-maker’s framework rather than a community’s self-description.", dark=True, num="01")}
      {card("Absence is not proof", "A missing name, account, or file may indicate many conditions and should not be turned into a conclusion without careful review.", dark=True, num="02")}
      {card("Interpretation is labelled", "Analytical framing is visible as framing. It is not blended into narration so that it reads as fact.", dark=True, num="03")}
    </div>
  </div>
</section>'''

    caution = f'''<section class="section band band--cream" id="caution">
  <div class="wrap grid g2 align-start">
    <div>
      {label("What this page does not do")}
      <h2 class="display h2 mt-2">No events, names, figures, or citations.</h2>
      <ul class="crosses mt-3">
        <li>It does not describe a specific event as established</li>
        <li>It does not name participants or leaders</li>
        <li>It does not give casualty numbers or dates</li>
        <li>It does not reproduce quotations or documents</li>
        <li>It does not resolve disagreements between historians</li>
      </ul>
      <p class="small soft mt-3">Future additions should visibly distinguish evidence type, provenance, confidence, corroboration, and current verification status.</p>
    </div>
    <div>
      {label("Reading discipline")}
      <h2 class="display h2 mt-2">Four questions before you cite.</h2>
      <div class="mt-3">
        {accordion([
          ("What kind of material am I looking at?", "A framework page, a docket, a status label — none of these is a primary source. Citing them as one misrepresents the archive."),
          ("What does the label actually say?", "“Under review” means not ready. “Community memory” means not independently verified. Quoting out of context reverses the meaning."),
          ("Has corroboration been done?", "If the archive has not compared independently situated materials, a reader should not assume comparison has happened elsewhere."),
          ("Who might be affected by my use?", "Re-circulating a claim about a named person changes its consequences, even if its wording stays the same."),
        ])}
      </div>
    </div>
  </div>
</section>'''

    return hero + how + routes + language + caution + cta_band(
        "Next docket", "Sensitive and protected records.",
        "Some material should be described minimally, if at all. That docket sets out harm minimisation, minimal metadata, and the takedown pathway.",
        btn(H('archive/sensitive-records.html'), 'Sensitive records', 'primary') + btn(H('archive/method.html'), 'Editorial method', 'light'))


# ===================================================== SENSITIVE RECORDS
def sensitive_records():
    gate = '''<div class="gate" data-gate role="dialog" aria-modal="true" aria-labelledby="gate-title">
  <div class="gate-card">
    <span class="label">Safe-open acknowledgement</span>
    <h2 class="display h3" id="gate-title">Open metadata with care.</h2>
    <p>The fields on this page remain non-specific placeholder metadata. By continuing, you acknowledge that sensitive archival description should minimise harm, protect affected people, preserve uncertainty, and avoid sharing beyond an appropriate access context.</p>
    <div class="btn-row mt-3">
      <button class="btn btn--primary" type="button" data-gate-accept>Continue to fields</button>
      <button class="btn btn--outline" type="button" data-gate-cancel>Cancel</button>
    </div>
  </div>
</div>'''

    hero = archive_hero(
        "Sensitive records", "Sensitive &amp; protected records · editorial frame",
        'Some material should be described <em>minimally, if at all</em>.',
        'This docket is an editorial framework. It contains exactly three non-specific placeholders pending source review and does not assert any incident, name, date, place, casualty figure, quotation, or citation as fact.',
        'ledger.svg', 'Restricted description',
        [("Placeholders", "03"), ("Content", "Withheld"), ("Assertions", "None"), ("Takedown", "Available")],
        btn(H('#principles'), 'Harm minimisation', 'primary') + btn(H('#takedown'), 'Takedown pathway', 'light'))

    principles = f'''<section class="section band" id="principles">
  <div class="wrap">
    {section_head("Harm minimisation", 'Five rules that come <em>before</em> description.',
                  'Sensitive material is not a harder version of ordinary material. It requires a different order of decisions: minimise, protect, withhold, and only then consider describing.')}
    <div class="grid g3">
      {card("Describe less", "A public description may indicate that a protected item exists without exposing contents, source, identifying details, or the reason it is restricted.", num="01")}
      {card("Do not create discoverability", "Wording, tags, and metadata can make material findable even when content is withheld. Searchability is a form of publication.", num="02")}
      {card("Preserve uncertainty", "Where accounts conflict or context is missing, retain the uncertainty. Certainty is not a neutral default.", num="03")}
      {card("Right of reply first", "Where a living person, family, or community is concerned, a response should be invited before publication or revision.", num="04")}
      {card("Record the decision", "Note what was withheld, by whom, and why — so that the choice can be reviewed later without re-exposing anyone.", num="05")}
      {card("Make withdrawal possible", "A clear takedown route should exist, and using it should not be treated as an admission of error.", num="06")}
    </div>
  </div>
</section>'''

    holders = f'''<section class="section band band--ink">
  <div class="wrap">
    {section_head("Placeholder index", 'Three holdings, <em>minimum metadata</em>.',
                  'Each placeholder records only what is needed to make the access decision legible. Nothing here identifies a person, place, or event.', dark=True)}
    <div class="grid g3">
      <article class="card card--dark">
        <span class="chip chip--ghost-light">Restricted</span>
        <h3 class="h4 mt-2">Holding A</h3>
        <p class="mt-1">A protected record exists in this archive’s scope. Contents, creator, language, and dating are withheld pending review.</p>
        {kv([("Status", "Restricted"), ("Description", "Existence only"), ("Review", "Safeguarding required")], dark=True)}
      </article>
      <article class="card card--dark">
        <span class="chip chip--ghost-light">Sealed</span>
        <h3 class="h4 mt-2">Holding B</h3>
        <p class="mt-1">A record subject to a time-limited closure. The closure period and its reason are recorded privately, not publicly.</p>
        {kv([("Status", "Sealed"), ("Description", "Existence only"), ("Review", "Custodian review")], dark=True)}
      </article>
      <article class="card card--dark">
        <span class="chip chip--ghost-light">Under review</span>
        <h3 class="h4 mt-2">Holding C</h3>
        <p class="mt-1">A lead awaiting provenance and harm review. No description exists yet because none could be written responsibly at this stage.</p>
        {kv([("Status", "Under review"), ("Description", "None"), ("Review", "Pending")], dark=True)}
      </article>
    </div>
    <div class="notice notice--dark mt-4">
      <span class="label label--dark">Local-only placeholder status</span>
      <p>No records, personal details, acknowledgements, search terms, or requests are collected, stored, transmitted, or published from this page.</p>
    </div>
  </div>
</section>'''

    takedown = f'''<section class="section band band--cream" id="takedown">
  <div class="wrap grid g2 align-start">
    <div>
      {label("Takedown and correction")}
      <h2 class="display h2 mt-2">Removal is a legitimate <em>editorial outcome</em>.</h2>
      <p class="body mt-3">Where material is inaccurate, harmful, improperly attributed, or missing necessary context, the archive should provide a route for review. Corrections are not limited to factual error: they can address naming, translation, access, framing, consent, and whether a public record should remain available at all.</p>
      <div class="btn-row mt-4">
        {btn(H('get-involved.html#corrections'), 'Request a correction', 'dark')}
        {btn(H('get-involved.html'), 'Contribute with care', 'outline')}
      </div>
    </div>
    <div>
      {numlist([
        ("Receive", "A concern, correction, or request for reply is received without assuming the existing description is complete or correct."),
        ("Review context", "The wording, attribution, access conditions, provenance, and additional context are reviewed with appropriate care."),
        ("Revise responsibly", "The archive may correct, contextualise, restrict, remove, or leave a record unresolved while making its editorial status visible."),
        ("Record the outcome", "The decision and its reason are retained so that later readers can see that a change was made and why."),
      ])}
    </div>
  </div>
</section>'''

    return gate + hero + principles + holders + takedown + cta_band(
        "Next docket", "How the archive is governed.",
        "The method docket sets out labels, review roles, translation policy, correction, and the limits of this framework.",
        btn(H('archive/method.html'), 'Editorial method', 'primary') + btn(H('questions.html'), 'Open questions', 'light'))


# ============================================================ METHOD
def method():
    hero = archive_hero(
        "Method", "Method · editorial governance",
        'Labels, review, and <em>correction</em> made visible.',
        'This docket explains how the archive decides what may be published, in what form, and under which conditions. It is the page that governs every other page.',
        'columns.svg', 'Procedures precede conclusions',
        [("Labels", "06"), ("Review roles", "03"), ("Glossary", "08"), ("Version", "Working")],
        btn(H('#labels'), 'Label legend', 'primary') + btn(H('#workflow'), 'Review workflow', 'light'))

    labels = f'''<section class="section band" id="labels">
  <div class="wrap">
    {section_head("Label legend", 'Six labels, one <em>discipline</em>.',
                  'A label describes the present editorial state of material. It does not rank lived knowledge, decide truth by itself, or replace careful reading of provenance, consent, language, and context.')}
    <div class="grid g3">
      {card("Verified evidence", "Assessed within stated limits, with sources, provenance, and date of review recorded. Still open to correction.", num="L1")}
      {card("Documented record", "A source exists and is described, but its interpretation may still be contested or incomplete.", num="L2")}
      {card("Community memory", "Recollection or inherited knowledge, shared under agreed conditions. Not independently verified.", num="L3")}
      {card("Scholarly interpretation", "An analytical reading situated in its methods, language, evidence base, and publication moment.", num="L4")}
      {card("Allegation", "Attributed rather than adopted. Publication requires contextual and right-of-reply review.", num="L5")}
      {card("Unresolved / restricted", "Sources conflict, context is missing, or access is withheld. Uncertainty is retained rather than filled in.", num="L6")}
    </div>
  </div>
</section>'''

    workflow = f'''<section class="section band band--ink" id="workflow">
  <div class="wrap grid g-1-2 align-start">
    <div>
      {label("Review workflow", dark=True)}
      <h2 class="display h2 mt-2">Five gates before <em>publication</em>.</h2>
      <p class="lede soft mt-3">Any gate can stop or narrow a description. A record that cannot pass is not published with a warning attached — it is held.</p>
      <div class="mt-4">
        {numlist([
          ("Provenance", "Can we trace this material to a repository, contributor, or collection with stated conditions?"),
          ("Context", "Do we understand why it was made, for whom, and what it cannot establish?"),
          ("Language", "Are original terms preserved, translations described, and meaning shifts visible?"),
          ("Harm", "Could description, naming, or circulation expose or stigmatise anyone now?"),
          ("Consent and reply", "Have contributors and those named had a genuine opportunity to set conditions or respond?"),
        ])}
      </div>
    </div>
    <div class="grid" style="gap:1rem">
      {card("Subject review", "Checks provenance, framing, and the difference between record and interpretation.", dark=True, num="Role A")}
      {card("Language review", "Checks terminology, translation, register, and possible loss of meaning.", dark=True, num="Role B")}
      {card("Safeguarding review", "Assesses risk to living people, including identification through metadata.", dark=True, num="Role C")}
      {card("Community review", "Sits with people who hold the relationships, not only with researchers.", dark=True, num="Role D")}
    </div>
  </div>
</section>'''

    glossary = f'''<section class="section band band--cream" id="glossary">
  <div class="wrap">
    {section_head("Glossary", 'Eight working terms, <em>plainly defined</em>.',
                  'Terminology in this archive is a working instrument, not a claim about the world. Definitions are revisable — and where a term is contested, that is stated.')}
    <div class="grid g2">
      <div>{accordion([
          ("Provenance", "The history of a record’s creation, custody, and description — who made it, when, where it has been, and who has described it since."),
          ("Corroboration", "Support from independently situated material. A second copy of the same claim is not corroboration."),
          ("Status label", "A visible statement of a record’s present editorial condition. It is not a truth score."),
          ("Access condition", "The terms under which material may be read, quoted, or circulated — including review-led, restricted, and private."),
        ])}</div>
      <div>{accordion([
          ("Minimisation", "Collecting and publishing the least identifying detail required for the purpose."),
          ("Right of reply", "A structured opportunity for a person, family, or community to respond to a contested account before or after publication."),
          ("Periodisation", "How time is divided into periods. In this archive it is treated as an argument, not a fact."),
          ("Withdrawal", "A contributor’s request that material no longer be published, quoted, or described. Honoured as a condition, not negotiated as a favour."),
        ])}</div>
    </div>
  </div>
</section>'''

    limits = f'''<section class="section band band--paper2 band--edge">
  <div class="wrap grid g-2-1 align-start">
    <div>
      {label("Limits of this framework")}
      <h2 class="display h2 mt-2">What the method cannot fix.</h2>
      <p class="body mt-3">A method reduces harm; it does not eliminate it. Some material should never be published, some questions may never be answerable, and some disagreements are older and larger than this archive.</p>
      <ul class="ticks mt-3">
        <li>A label cannot make an unreliable source reliable</li>
        <li>Consent cannot be obtained retroactively for everyone affected</li>
        <li>Translation always loses something, and the loss is not always visible</li>
        <li>An archive cannot adjudicate a land or political dispute</li>
        <li>Absence from the record is not evidence of absence in history</li>
      </ul>
    </div>
    <div class="card card--flat">
      <span class="label">Version note</span>
      {kv([("Version", "Working framework, revision 1"), ("Changes", "Amendments are dated and kept visible alongside previous wording."), ("Review cycle", "Reviewed when material, consent, or context changes."), ("Contact", "Use the correction route for methodological objections.")])}
      <div class="btn-row mt-3">{btn(H('get-involved.html'), 'Raise an objection', 'dark')}</div>
    </div>
  </div>
</section>'''

    return hero + labels + workflow + glossary + limits + cta_band(
        "Continue", "Read the history this method serves.",
        "The history page applies these labels to the archive’s approach to makers, silences, and interpretation.",
        btn(H('history.html'), 'History', 'primary') + btn(H('archive.html'), 'Archive overview', 'light'))


# ============================================================== 404
def not_found():
    return f'''<section class="hero" style="min-height:72vh;display:flex;align-items:center">
  <div class="wrap" style="padding-block:clamp(3rem,8vw,6rem)">
    <span class="label label--dark">404 / route not found</span>
    <h1 class="display mt-3" style="font-size:clamp(2.6rem,7vw,5.6rem);max-width:20ch">This page is not in <em>the archive</em>.</h1>
    <p class="lede soft mt-3" style="max-width:52ch">The route you requested could not be found. It may never have existed, or it may have been withdrawn, restricted, or renamed. Those are all legitimate outcomes in an archive.</p>
    <div class="btn-row mt-4">
      {btn(H('index.html'), 'Return home', 'primary')}
      {btn(H('archive.html'), 'Open the archive', 'light')}
      {btn(H('questions.html'), 'Ask a question', 'light')}
    </div>
    <div class="grid g4 mt-6">
      {card("Archive overview", "Pathways, labels, and access conditions.", dark=True, link=("Open", H("archive.html")))}
      {card("Chronology", "Research prompts across time, not events.", dark=True, link=("Open", H("archive/chronology.html")))}
      {card("Editorial method", "How publication decisions are made.", dark=True, link=("Open", H("archive/method.html")))}
      {card("Get involved", "Corrections, sources, and right of reply.", dark=True, link=("Open", H("get-involved.html")))}
    </div>
  </div>
</section>'''


PAGES = [
    dict(url="archive/chronology.html", nav_title="Archive chronology", section="Archive",
         title="Chronology framework — Biimaal archive",
         description="A working chronology framework: research prompts across periods, with evidence fields and no settled historical claims.",
         active="archive.html", body=chronology, subnav="archive/chronology.html"),
    dict(url="archive/places.html", nav_title="Places in relation", section="Archive",
         title="Places in relation — Biimaal archive",
         description="Benadir as orientation and connected places as relationships: naming, connection, and the limits of place labels.",
         active="archive.html", body=places, subnav="archive/places.html"),
    dict(url="archive/oral-histories.html", nav_title="Oral histories", section="Archive",
         title="Oral histories — Biimaal archive",
         description="Consent-led description of oral testimony: access conditions, protected identity, safeguards, and withdrawal.",
         active="archive.html", body=oral_histories, subnav="archive/oral-histories.html"),
    dict(url="archive/history-resistance.html", nav_title="History & resistance", section="Archive",
         title="History & resistance — Biimaal archive",
         description="A cautious framework for researching late nineteenth-century context, colonial records, and wider resistance questions.",
         active="archive.html", body=history_resistance, subnav="archive/history-resistance.html"),
    dict(url="archive/sensitive-records.html", nav_title="Sensitive records", section="Archive",
         title="Sensitive records — Biimaal archive",
         description="An editorial frame for protected material: harm minimisation, minimal metadata, and a takedown pathway.",
         active="archive.html", body=sensitive_records, subnav="archive/sensitive-records.html"),
    dict(url="archive/method.html", nav_title="Editorial method", section="Archive",
         title="Editorial method — Biimaal archive",
         description="Label legend, review workflow, glossary, and the limits of the archive’s editorial framework.",
         active="archive.html", body=method, subnav="archive/method.html"),
    dict(url="404.html", nav_title="Page not found", section="System",
         title="Page not found — Koonfur Bari",
         description="This route is not in the archive. Return home or open the archive overview.",
         active="", body=not_found),
]
