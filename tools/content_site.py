"""Site pages: research, archive, timeline, map, field notes, get involved, questions, document."""
import ui
from ui import (H, label, btn, plate, section_head, card, kv, accordion,
                numlist, statrow, filters, tabs, notice, quote, cta_band, crumbs)


# ============================================================ RESEARCH
def research():
    hero = f'''<section class="pagehero">
  <div class="wrap">
    {crumbs([("Home", H("index.html")), ("Research", None)])}
    <div class="pagehero-inner mt-3">
      <div>
        <span class="label label--dark">Research and evidence</span>
        <h1 class="display mt-2">Questions held <em>with care</em>.</h1>
        <p class="lede soft mt-3">Research themes are active inquiries, not final claims. Each is approached through source awareness, consent, context, and review.</p>
        <div class="btn-row mt-4">
          {btn(H('#lead'), 'Propose a research lead', 'primary')}
          {btn(H('archive/method.html'), 'Read the method', 'light')}
        </div>
      </div>
      <div class="meta-list">
        <div><span>Themes</span><b>03 active</b></div>
        <div><span>Method</span><b>Source-aware</b></div>
        <div><span>Review</span><b>Editorial + community</b></div>
        <div><span>Output</span><b>Framework, not verdict</b></div>
      </div>
    </div>
  </div>
</section>'''

    themes = f'''<section class="section band">
  <div class="wrap">
    {section_head("Research themes", 'Three inquiries, each with <em>visible limits</em>.',
                  'Filter the themes to see how each is framed. Every theme states what is being asked, how it would be answered, and what would not count as an answer.')}
    {filters("themes", [("all", "All themes", "3"), ("land", "Land", ""), ("memory", "Memory", ""), ("water", "Water", "")])}
    <div class="grid g3">
      <article class="card" data-cat="land" data-scope="themes">
        <span class="chip chip--amber">Open question</span>
        <h3 class="h4 mt-2">Land, livelihoods, and administration</h3>
        <p class="mt-1">How are land access, livelihoods, local administration, and displacement represented across records and community knowledge?</p>
        {kv([("Answered by", "Registers, agreements, local testimony, and comparable accounts"), ("Not enough", "A single document read without context")], stack=True)}
      </article>
      <article class="card" data-cat="memory" data-scope="themes">
        <span class="chip chip--ink">In review</span>
        <h3 class="h4 mt-2">Memory, resistance, and oral history</h3>
        <p class="mt-1">How can oral accounts be gathered without extracting them from people, place, relationship, consent, or privacy?</p>
        {kv([("Answered by", "Consent-led interviews and community-reviewed description"), ("Not enough", "Unattributed quotation or paraphrase")], stack=True)}
      </article>
      <article class="card" data-cat="water" data-scope="themes">
        <span class="chip chip--amber">Forthcoming</span>
        <h3 class="h4 mt-2">Water, environment, and future stewardship</h3>
        <p class="mt-1">A continuing inquiry into water, environmental change, agricultural livelihoods, and locally grounded stewardship.</p>
        {kv([("Answered by", "Hydrological records, farming knowledge, and land-use history"), ("Not enough", "Projection presented as measurement")], stack=True)}
      </article>
    </div>
    <p class="is-hidden small soft mt-3" data-empty="themes">No themes match this filter yet.</p>
  </div>
</section>'''

    method = f'''<section class="section band band--ink">
  <div class="wrap grid g-2-1 align-start">
    <div>
      {label("Methods", dark=True)}
      <h2 class="display h2 mt-2">How a question becomes <em>a record</em>.</h2>
      <p class="lede soft mt-3">Four stages, each of which can stop the process. Nothing advances simply because it is interesting.</p>
      <div class="mt-4">
        {numlist([
          ("Scope the question", "Define what is being asked, for whom, and what an answer would look like. Record what is out of scope."),
          ("Map the sources", "Identify records, testimony, scholarship, and visual material — with their access conditions and known gaps."),
          ("Review with others", "Subject, language, and where relevant community review. Disagreement is recorded rather than averaged."),
          ("Publish the frame", "Release the question, the method, and the limits. Conclusions follow only where support exists."),
        ])}
      </div>
    </div>
    <div>{plate('ledger.svg', 'A record is also an argument', tag='Method plate', cls='plate--tall', note='Illustrative plate — not a document.')}</div>
  </div>
</section>'''

    ethics = f'''<section class="section band band--cream">
  <div class="wrap">
    {section_head("Research ethics", 'Consent, privacy, and <em>the right to remain unfinished</em>.',
                  'Ethical research is slower. These are the conditions the programme accepts as non-negotiable, even where they reduce the amount that can be published.')}
    <div class="grid g3">
      {card("Informed consent", "Contributors know how material may be used, who may read it, and how to revisit or withdraw permission later.", num="01")}
      {card("Minimisation", "Collect the least identifying detail required. Do not create discoverability through description alone.", num="02")}
      {card("Attribution choice", "Names, voices, and locations can identify a person. Attribution is used only where permission and safety review support it.", num="03")}
      {card("No extraction", "Community knowledge is not a resource to be harvested. Participation does not require disclosure.", num="04")}
      {card("Language care", "Translation is an editorial act. Meaning, register, and possible loss of context should be visible.", num="05")}
      {card("Open correction", "Findings remain revisable. A published frame can be narrowed, contextualised, or withdrawn.", num="06")}
    </div>
  </div>
</section>'''

    lead = f'''<section class="section band" id="lead">
  <div class="wrap grid g-1-2 align-start">
    <div>
      {label("Propose a research lead")}
      <h2 class="display h2 mt-2">Bring a question, <em>not a demand</em>.</h2>
      <p class="body mt-3">Submissions are reviewed as research leads and are not automatically published. A useful lead names a source type, a rough context, and what you think it might help explain.</p>
      <div class="notice mt-3">
        <span class="label">Before you submit</span>
        <p>Do not send sensitive material, personal data about others, or anything that could put you or another person at risk. A description is enough to start.</p>
      </div>
    </div>
    <form class="form card" data-validate data-form-kind="research lead">
      <div class="field">
        <label for="rq-topic">Topic <span aria-hidden="true">*</span></label>
        <input class="input" id="rq-topic" name="topic" type="text" required placeholder="e.g. water access and farming practice">
        <span class="field-error">Please add a short topic.</span>
      </div>
      <div class="field">
        <label for="rq-source">Source type</label>
        <select class="select" id="rq-source" name="source">
          <option>Oral history</option><option>Document</option><option>Photograph</option>
          <option>Map</option><option>Publication</option><option>Other</option>
        </select>
      </div>
      <div class="field">
        <label for="rq-context">Context <span aria-hidden="true">*</span></label>
        <textarea class="textarea" id="rq-context" name="context" required placeholder="What does this help explain, and what are its limits?"></textarea>
        <span class="field-error">A short context note is required.</span>
      </div>
      <div class="field">
        <label for="rq-contact">Contact (optional)</label>
        <input class="input" id="rq-contact" name="contact" type="email" placeholder="you@example.com">
      </div>
      <label class="checkline"><input type="checkbox" required> I understand leads are reviewed and may not be published.</label>
      <div class="form-status" data-form-status role="status" aria-live="polite"></div>
      <button class="btn btn--primary" type="submit">Submit research lead</button>
      <p class="form-note">This demonstration stores nothing. In a live system you would receive a reference number.</p>
    </form>
  </div>
</section>'''

    questions = f'''<section class="section band band--paper2 band--edge">
  <div class="wrap">
    {section_head("Current question register", 'What we are asking <em>right now</em>.',
                  'A register keeps the inquiry visible between publications. Items move between states as evidence and review allow.')}
    <div class="card card--flat" style="padding:clamp(.8rem,2vw,1.4rem);overflow-x:auto">
      <table class="table">
        <caption>Extract · research question register</caption>
        <thead><tr><th>Question</th><th>Theme</th><th>Status</th></tr></thead>
        <tbody>
          <tr><td>How is land access described across administrative records and family knowledge?</td><td>Land</td><td><span class="chip chip--amber">Open</span></td></tr>
          <tr><td>Which villages appear in records under names that differ from local usage?</td><td>Place</td><td><span class="chip chip--amber">Open</span></td></tr>
          <tr><td>What conditions did families set when sharing testimony in earlier projects?</td><td>Memory</td><td><span class="chip chip--ink">In review</span></td></tr>
          <tr><td>How is water access described by farmers and by administrators?</td><td>Water</td><td><span class="chip chip--amber">Open</span></td></tr>
          <tr><td>Where do published accounts of resistance derive from the same small set of sources?</td><td>History</td><td><span class="chip">Forthcoming</span></td></tr>
        </tbody>
      </table>
    </div>
    <div class="btn-row mt-4">{btn(H('questions.html'), 'Full question register', 'dark')}</div>
  </div>
</section>'''

    return hero + themes + method + ethics + lead + questions + cta_band(
        "Next", "Enter the archive itself.",
        "The archive applies these methods to periods, places, testimony, and protected material — with a visible status for every record.",
        btn(H('archive.html'), 'Open the archive', 'primary') + btn(H('timeline.html'), 'Timeline framework', 'light'))


# ============================================================= ARCHIVE
def archive():
    hero = f'''<section class="pagehero">
  <div class="wrap">
    {crumbs([("Home", H("index.html")), ("Archive", None)])}
    <div class="pagehero-inner mt-3">
      <div>
        <span class="label label--dark">Biimaal archive · living index</span>
        <h1 class="display mt-2">A living archive, <em>read in context</em>.</h1>
        <p class="lede soft mt-3">Archive entries carry source-status labels. Images and records can support inquiry without being treated as proof on their own. This index shows pathways, conditions, and what remains unfinished.</p>
        <div class="btn-row mt-4">
          {btn(H('archive/method.html'), 'Read the method', 'primary')}
          {btn(H('archive/chronology.html'), 'Enter by chronology', 'light')}
        </div>
      </div>
      <div>{plate('ledger.svg', 'Holding space for evidence and memory', tag='Archive plate', cls='plate--wide', note='Illustrative plate — not a document.')}</div>
    </div>
  </div>
</section>'''

    pathways = f'''<section class="section band">
  <div class="wrap">
    {section_head("Purpose", 'Three ways into <em>the archive</em>.',
                  'The archive offers pathways rather than a final account. Each pathway makes its limits visible, and none of them is a shortcut to certainty.')}
    <div class="grid g3">
      {card("Broad chronology", "A navigational timeline for locating periods, themes, and questions without claiming a complete historical sequence.", num="01", link=("Open chronology", H("archive/chronology.html")))}
      {card("Places in relation", "Benadir and connected places are considered through movement, language, kinship, work, and changing local relationships.", num="02", link=("Open places", H("archive/places.html")))}
      {card("Protected testimony", "A consent-first pathway for testimony that may require restricted access, community review, or a decision not to publish.", num="03", link=("Open oral histories", H("archive/oral-histories.html")))}
    </div>
  </div>
</section>'''

    legend = f'''<section class="section band band--ink">
  <div class="wrap">
    {section_head("Status legend", 'Labels make uncertainty <em>readable</em>.',
                  'Evidence labels describe the present editorial status of material. They do not rank lived knowledge, decide truth by themselves, or replace careful reading of provenance, consent, language, and context.', dark=True)}
    <div class="grid g3">
      {card("Placeholder", "Signals that a record, topic, or pathway may be anticipated but is not yet described with public supporting detail.", dark=True, num="Status")}
      {card("Community memory", "Identifies recollection, oral knowledge, or community-held context that should not be presented as independently verified evidence.", dark=True, num="Status")}
      {card("Scholarly interpretation", "Marks an analytical reading or research position. Interpretation is distinct from a primary record and may be revisited.", dark=True, num="Status")}
      {card("Allegation", "Marks a claim that is attributed rather than adopted by the archive. Publication requires contextual and right-of-reply review.", dark=True, num="Status")}
      {card("Unresolved claim", "Signals that available accounts do not yet support a responsible conclusion, or that the matter remains actively contested.", dark=True, num="Status")}
      {card("Restricted", "Indicates that material exists but is not available for browsing, quotation, or inference from the public description.", dark=True, num="Status")}
    </div>
  </div>
</section>'''

    catalogue = f'''<section class="section band band--cream">
  <div class="wrap">
    {section_head("Catalogue preview", 'Six entry types, each with its <em>conditions</em>.',
                  'These cards model how a future entry would appear. They contain no names, quotations, dates, or figures, because those require source review before publication.')}
    {filters("cat", [("all", "All records", "6"), ("photo", "Photograph", ""), ("note", "Research note", ""), ("doc", "Document", "")])}
    <div class="grid g3">
      <article class="card" data-cat="photo" data-scope="cat">
        <div class="plate plate--wide" style="margin:-1.2rem -1.2rem 1.1rem">
          <img src="{H('assets/plates/coast.svg')}" alt="Illustrative coastal plate" loading="lazy">
          <span class="plate__tag">Photograph</span>
        </div>
        <span class="chip chip--amber">Representative/context image</span>
        <h3 class="h4 mt-2">Shared heritage visual</h3>
        <p class="mt-1">A contextual visual entry for discussing collective memory and heritage. Provenance, caption history, and permission review are required before use.</p>
      </article>
      <article class="card" data-cat="note" data-scope="cat">
        <div class="plate plate--wide" style="margin:-1.2rem -1.2rem 1.1rem">
          <img src="{H('assets/plates/columns.svg')}" alt="Illustrative institutional plate" loading="lazy">
          <span class="plate__tag">Research note</span>
        </div>
        <span class="chip chip--ink">Interpretation</span>
        <h3 class="h4 mt-2">Institutional context note</h3>
        <p class="mt-1">A note that accompanies questions about documentation, administration, and how institutional records were produced and kept.</p>
      </article>
      <article class="card" data-cat="note" data-scope="cat">
        <div class="plate plate--wide" style="margin:-1.2rem -1.2rem 1.1rem">
          <img src="{H('assets/plates/portrait.svg')}" alt="Illustrative portrait plate" loading="lazy">
          <span class="plate__tag">Community memory</span>
        </div>
        <span class="chip chip--amber">Consent-led</span>
        <h3 class="h4 mt-2">Memory reference</h3>
        <p class="mt-1">An entry point for thinking about memory, captions, evidence, and provenance — without displaying or paraphrasing restricted material.</p>
      </article>
      <article class="card" data-cat="doc" data-scope="cat">
        <div class="plate plate--wide" style="margin:-1.2rem -1.2rem 1.1rem">
          <img src="{H('assets/plates/ledger.svg')}" alt="Illustrative document plate" loading="lazy">
          <span class="plate__tag">Document</span>
        </div>
        <span class="chip">Placeholder</span>
        <h3 class="h4 mt-2">Administrative paper</h3>
        <p class="mt-1">A record awaiting repository, creator, date range, language notes, and access conditions before any public description can be responsibly written.</p>
      </article>
      <article class="card" data-cat="photo" data-scope="cat">
        <div class="plate plate--wide" style="margin:-1.2rem -1.2rem 1.1rem">
          <img src="{H('assets/plates/delta.svg')}" alt="Illustrative terrain plate" loading="lazy">
          <span class="plate__tag">Map</span>
        </div>
        <span class="chip">Unresolved claim</span>
        <h3 class="h4 mt-2">Place reference</h3>
        <p class="mt-1">A spatial reference requiring scale, date, naming history, production context, and explicit limits on what the image can establish.</p>
      </article>
      <article class="card" data-cat="doc" data-scope="cat">
        <div class="plate plate--wide" style="margin:-1.2rem -1.2rem 1.1rem">
          <img src="{H('assets/plates/weave.svg')}" alt="Illustrative woven plate" loading="lazy">
          <span class="plate__tag">Restricted</span>
        </div>
        <span class="chip chip--ink">Access controlled</span>
        <h3 class="h4 mt-2">Protected holding</h3>
        <p class="mt-1">A public description may indicate that a protected item exists without exposing its contents, source, identifying details, or the reason it is restricted.</p>
      </article>
    </div>
    <p class="is-hidden small soft mt-3" data-empty="cat">No records of this type are described yet.</p>
  </div>
</section>'''

    scope = f'''<section class="section band">
  <div class="wrap grid g-1-2 align-start">
    <div>
      {label("Archive scope")}
      <h2 class="display h2 mt-2">A working index with <em>visible limits</em>.</h2>
      <p class="body mt-3">The archive is designed to make pathways and conditions legible. It can describe materials, questions, and access notes while refusing the pressure to turn every lead into a public conclusion.</p>
    </div>
    <div>
      {numlist([
        ("What may appear", "Context notes, descriptive records, research questions, controlled vocabulary, access conditions, and carefully labelled pathways between materials."),
        ("What it does not claim", "Completeness, final authority, universal representation, or a settled account of questions that remain disputed, private, undocumented, or unresolved."),
        ("Access is contextual", "Not every material should be public, searchable, excerpted, or reproduced. Access may depend on consent, sensitivity, provenance, and ongoing review."),
        ("Status remains visible", "Records may remain provisional, contextual, restricted, corrected, withdrawn, or unresolved. These conditions are part of the record, not a failure of it."),
      ])}
    </div>
  </div>
</section>'''

    access = f'''<section class="section band band--paper2 band--edge">
  <div class="wrap">
    {section_head("Access conditions", 'Four levels, described <em>before</em> content.',
                  'Access is decided before description, not after. Where an item cannot be read, the archive still records that a decision was made — and who made it.')}
    <div class="grid g4">
      {card("Open", "Publicly described and readable, with status labels and context attached.", num="A")}
      {card("Review-led", "Description exists; quotation and circulation await community or expert review.", num="B")}
      {card("Restricted", "Existence is acknowledged; contents, source, and identifying detail are withheld.", num="C")}
      {card("Private", "Held for a contributor, custodians, or a care process — not for research access.", num="D")}
    </div>
    <div class="notice mt-4">
      <span class="label">Important</span>
      <p>Absence from the archive should never be read as absence from lived history. Silence may indicate privacy, danger, loss, or a decision not to publish — and it is not evidence of anything else.</p>
    </div>
    <div class="btn-row mt-4">
      {btn(H('archive/sensitive-records.html'), 'Sensitive records notice', 'dark')}
      {btn(H('archive/oral-histories.html'), 'Oral histories', 'outline')}
    </div>
  </div>
</section>'''

    return hero + pathways + legend + catalogue + scope + access + cta_band(
        "Continue", "Go deeper into the archive.",
        "Six dockets set out periods, places, testimony conditions, resistance research, sensitive material, and the editorial method itself.",
        btn(H('archive/chronology.html'), 'Chronology', 'primary') + btn(H('archive/method.html'), 'Method', 'light'))


# ============================================================ TIMELINE
def timeline():
    hero = f'''<section class="pagehero">
  <div class="wrap">
    {crumbs([("Home", H("index.html")), ("Timeline", None)])}
    <div class="pagehero-inner mt-3">
      <div>
        <span class="label label--dark">Timeline</span>
        <h1 class="display mt-2">Time is not a <em>straight line</em>.</h1>
        <p class="lede soft mt-3">This route is a guide to reading historical material, not a comprehensive chronology or a set of final historical claims.</p>
        <div class="btn-row mt-4">
          {btn(H('archive/chronology.html'), 'Archive chronology', 'primary')}
          {btn(H('history.html'), 'How we read history', 'light')}
        </div>
      </div>
      <div>{plate('contour.svg', 'Layers, not a line', tag='Framework plate', cls='plate--wide', note='Illustrative plate — not a chronology.')}</div>
    </div>
  </div>
</section>'''

    keys = f'''<section class="section band">
  <div class="wrap">
    {section_head("Reading key", 'Three kinds of entry, <em>never merged</em>.',
                  'Each item below carries a type. The type tells you what kind of support an entry has, and therefore how much it can carry in an argument.')}
    <div class="grid g3">
      {card("Documented evidence", "Materials with identifiable sources can still require context, interpretation, and corroboration.", num="Type A")}
      {card("Testimony", "Community testimony carries knowledge, relationship, and obligations of consent that must be respected.", num="Type B")}
      {card("Interpretation and open questions", "Interpretation should be labelled, and uncertainty should remain visible where evidence is incomplete.", num="Type C")}
    </div>
  </div>
</section>'''

    entries = f'''<section class="section band band--paper2">
  <div class="wrap">
    {section_head("Framework", 'Periods, records, and questions kept <em>distinct</em>.',
                  'Each entry identifies a possible research route rather than supplying an unverified event. Expand an entry to see the fields that would be needed before a public historical claim could be responsibly described.')}
    {filters("tl", [("all", "All entries", "6"), ("context", "Period context", ""), ("record", "Archival record", ""), ("interp", "Interpretation", ""), ("memory", "Community memory", "")])}
    <div class="tl">
      <div class="tl-item is-open" data-cat="context" data-scope="tl">
        <span class="tl-period">Context 01 · Late nineteenth century</span>
        <h3 class="h4">Regional change requires locally grounded reading</h3>
        <p class="small soft">Research may examine changing political, commercial, religious, environmental, and social conditions across the wider region. This placeholder assigns no single cause, date, actor, or outcome to any community history.</p>
        {accordion([("View evidence fields", kv([("Provenance", "No specific source has been attached in this placeholder state."), ("Corroboration", "Requires comparison across independently situated materials where appropriate."), ("Verification status", "Open research question — not a verified historical claim.")]))])}
      </div>
      <div class="tl-item" data-cat="record" data-scope="tl">
        <span class="tl-period">Record 02 · Colonial-period documents</span>
        <h3 class="h4">Administrative documents can preserve purpose as well as information</h3>
        <p class="small soft">Catalogues, correspondence, reports, maps, and registers may be relevant to research, but they may also contain institutional vocabulary, omissions, and uneven points of view. Their existence alone does not verify the account they appear to offer.</p>
        {accordion([("View evidence fields", kv([("Provenance", "Repository, creator, date, collection history, and access conditions remain to be documented."), ("Corroboration", "Needs contextual reading alongside other records and, where welcomed, community knowledge."), ("Confidence", "Unrated until an actual record and its context are reviewed.")]))])}
      </div>
      <div class="tl-item" data-cat="interp" data-scope="tl">
        <span class="tl-period">Interpretation 03 · Wider Benadir resistance research</span>
        <h3 class="h4">Resistance may be researched without reducing it to one form or story</h3>
        <p class="small soft">Researchers may ask how refusal, negotiation, survival, mobility, labour, language, care, or public action are framed in different sources. This archive does not use the term as an automatic description of any particular event or person.</p>
        {accordion([("View evidence fields", kv([("Interpretive basis", "No publication, author, or citation is supplied in this framework."), ("Analytical limits", "Interpretation should remain separate from primary records and memory."), ("Verification status", "Interpretive prompt only — not a verified conclusion.")]))])}
      </div>
      <div class="tl-item" data-cat="memory" data-scope="tl">
        <span class="tl-period">Memory 04 · Intergenerational remembrance</span>
        <h3 class="h4">Memory can guide research while retaining its own conditions of care</h3>
        <p class="small soft">Community-held knowledge may preserve language, questions, relationships, and interpretive context. It should be described as memory unless separately supported and shared for that purpose under agreed conditions.</p>
        {accordion([("View evidence fields", kv([("Care conditions", "No testimony is included here; consent, attribution, and circulation preferences would be required first."), ("Status", "Community memory — not independently verified."), ("Publication", "Depends on an agreed access context and continued consent.")]))])}
      </div>
      <div class="tl-item" data-cat="context" data-scope="tl">
        <span class="tl-period">Context 05 · Twentieth-century institutions</span>
        <h3 class="h4">Institutional records reveal procedures and their makers</h3>
        <p class="small soft">Registers, minutes, and correspondence can show how categories were applied and who was counted. They rarely record how those categories were experienced.</p>
        {accordion([("View evidence fields", kv([("Provenance", "Not yet supplied."), ("Corroboration", "Compare with independent materials and, where welcomed, community accounts."), ("Verification status", "Framework placeholder.")]))])}
      </div>
      <div class="tl-item" data-cat="memory" data-scope="tl">
        <span class="tl-period">Memory 06 · Contemporary stewardship</span>
        <h3 class="h4">Living knowledge may be described by access rather than displayed</h3>
        <p class="small soft">Where consent, safety, or community review is active, a record can exist publicly without its contents being reproduced.</p>
        {accordion([("View evidence fields", kv([("Access", "Review-led or restricted; contents not reproduced."), ("Consent", "Ongoing and revisitable."), ("Verification status", "Not applicable to protected material.")]))])}
      </div>
    </div>
    <p class="is-hidden small soft mt-3" data-empty="tl">No entries match this filter yet.</p>
  </div>
</section>'''

    return hero + keys + entries + cta_band(
        "Continue", "Questions remain part of the record.",
        "The question register holds open, in-review, and forthcoming inquiries so that what is unknown stays visible between publications.",
        btn(H('questions.html'), 'Question register', 'primary') + btn(H('archive/chronology.html'), 'Archive chronology', 'light'))


# ================================================================= MAP
MAP_SVG = '''<svg viewBox="0 0 820 540" role="group" aria-label="Schematic orientation diagram with selectable places">
  <defs>
    <linearGradient id="sea" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#0c2a33"/><stop offset="1" stop-color="#04141a"/>
    </linearGradient>
    <linearGradient id="land" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#12333c"/><stop offset="1" stop-color="#0c242c"/>
    </linearGradient>
    <pattern id="gr" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M40 0H0v40" fill="none" stroke="#c9a227" stroke-opacity=".13"/>
    </pattern>
  </defs>
  <rect width="820" height="540" fill="url(#sea)"/>
  <rect width="820" height="540" fill="url(#gr)"/>
  <path d="M0 0 L118 0 C 214 118, 296 222, 356 320 C 396 388, 436 470, 466 540 L0 540 Z" fill="url(#land)"/>
  <g fill="none" stroke="#c9a227" stroke-opacity=".22">
    <path d="M0 60 C 96 160, 178 250, 238 348 C 272 404, 306 476, 330 540"/>
    <path d="M0 130 C 70 214, 140 292, 196 380 C 228 430, 258 490, 276 540"/>
    <path d="M0 210 C 44 274, 100 340, 148 412 C 176 452, 200 500, 214 540"/>
    <path d="M0 300 C 30 344, 62 392, 96 448 C 114 478, 132 512, 146 540"/>
  </g>
  <path d="M118 0 C 214 118, 296 222, 356 320 C 396 388, 436 470, 466 540"
        fill="none" stroke="#ffb866" stroke-opacity=".85" stroke-width="2.2"/>
  <path d="M134 0 C 230 116, 312 220, 372 318 C 412 386, 452 468, 482 540"
        fill="none" stroke="#ffb866" stroke-opacity=".22" stroke-width="1"/>
  <path d="M246 138 C 274 206, 296 268, 316 318 C 332 352, 358 374, 390 384"
        fill="none" stroke="#8fd0d8" stroke-opacity=".6" stroke-width="2.2" stroke-linecap="round"/>
  <path d="M262 132 C 290 200, 312 262, 332 312 C 348 346, 374 368, 404 378"
        fill="none" stroke="#8fd0d8" stroke-opacity=".2" stroke-width="1"/>
  <g stroke="#c9a227" stroke-opacity=".5" stroke-dasharray="6 7" fill="none">
    <path d="M358 392 L 470 402"/>
    <path d="M358 392 L 300 300"/>
    <path d="M358 392 L 560 340"/>
    <path d="M300 300 L 190 358"/>
    <path d="M358 392 L 650 262"/>
  </g>
  <g class="map-node is-active" data-place="1" data-kind="Orientation" data-title="Benadir orientation"
     data-body="A starting point for locating a context, not a definition of the reach of community ties, movement, or historical relationship."
     data-note="Orientation, not enclosure.">
    <circle cx="358" cy="392" r="19" fill="#ff8000" fill-opacity=".16"/>
    <circle cx="358" cy="392" r="7" fill="#ff8000"/>
    <text x="358" y="366" text-anchor="middle" fill="#ffd7ae" font-family="IBM Plex Mono, monospace" font-size="11" letter-spacing="1.4">BENADIR</text>
  </g>
  <g class="map-node" data-place="2" data-kind="Coastal connection" data-title="Coastal connections"
     data-body="Ports, fishing, trade, and travel link coastal settlements in ways that registers rarely capture. These connections are research questions, not fixed routes."
     data-note="Illustrative diagram — not a navigational or legal map.">
    <circle cx="470" cy="402" r="6.5" fill="#0a2028" stroke="#ffb866" stroke-width="1.8"/>
    <text x="482" y="406" fill="#cfe0dc" font-family="IBM Plex Mono, monospace" font-size="10" letter-spacing="1.2">COASTAL</text>
  </g>
  <g class="map-node" data-place="3" data-kind="Inland relation" data-title="Inland relations"
     data-body="Kinship, grazing, and markets connect inland and riverine communities. Naming and boundaries may differ between administrative records and local usage."
     data-note="Relationship, not boundary.">
    <circle cx="190" cy="358" r="6.5" fill="#0a2028" stroke="#ffb866" stroke-width="1.8"/>
    <text x="202" y="362" fill="#cfe0dc" font-family="IBM Plex Mono, monospace" font-size="10" letter-spacing="1.2">INLAND</text>
  </g>
  <g class="map-node" data-place="4" data-kind="Diasporic pathway" data-title="Diasporic pathways"
     data-body="Remittance, correspondence, and return shape how histories are remembered and funded. Diaspora memory may preserve material absent from local collections."
     data-note="Movement across contexts, not a single route.">
    <circle cx="650" cy="262" r="6.5" fill="#0a2028" stroke="#ffb866" stroke-width="1.8"/>
    <text x="662" y="266" fill="#cfe0dc" font-family="IBM Plex Mono, monospace" font-size="10" letter-spacing="1.2">DIASPORA</text>
  </g>
  <g class="map-node" data-place="5" data-kind="River &amp; farmland" data-title="River corridor and farmland"
     data-body="Water access, irrigation, and tenure are entangled. Claims about land often depend on how water is described, and by whom."
     data-note="Context for land questions — no claim about tenure.">
    <circle cx="316" cy="318" r="6.5" fill="#0a2028" stroke="#8fd0d8" stroke-width="1.8"/>
    <text x="328" y="314" fill="#bfe3e6" font-family="IBM Plex Mono, monospace" font-size="10" letter-spacing="1.2">RIVER</text>
  </g>
  <text x="640" y="330" text-anchor="middle" fill="#6f8b87" font-family="IBM Plex Mono, monospace" font-size="9" letter-spacing="2.4">INDIAN OCEAN</text>
  <text x="560" y="500" text-anchor="middle" fill="#6f8b87" font-family="IBM Plex Mono, monospace" font-size="8.5" letter-spacing="1.8">SCHEMATIC · NOT TO SCALE</text>
</svg>'''


def map_page():
    hero = f'''<section class="pagehero">
  <div class="wrap">
    {crumbs([("Home", H("index.html")), ("Map &amp; land", None)])}
    <div class="pagehero-inner mt-3">
      <div>
        <span class="label label--dark">Map &amp; land</span>
        <h1 class="display mt-2">Land is more than <em>a boundary</em>.</h1>
        <p class="lede soft mt-3">Land, water, livelihoods, and consent are interconnected. This route provides a civic research frame, not legal or navigational mapping.</p>
        <div class="btn-row mt-4">
          {btn(H('archive/places.html'), 'Places in relation', 'primary')}
          {btn(H('research.html'), 'Research themes', 'light')}
        </div>
      </div>
      <div class="notice notice--dark">
        <span class="label label--dark">Please note</span>
        <p class="small">Every image and diagram here is a contextual reference. None is a legal, evidentiary, or navigational map, and none defines a boundary.</p>
      </div>
    </div>
  </div>
</section>'''

    interactive = f'''<section class="section band">
  <div class="wrap">
    {section_head("Orientation diagram", 'Select a node to read its <em>conditions</em>.',
                  'The diagram shows relationships the archive treats as research questions: orientation, coastal connection, inland relation, river corridor, and diasporic movement.')}
    <div class="grid g-1-3 align-start">
      <div class="map-shell">{MAP_SVG}</div>
      <div class="map-readout" data-map-readout aria-live="polite">
        <span class="marker">Orientation</span>
        <h3 class="h3 mt-1">Benadir orientation</h3>
        <p class="mt-2 small">Select a node to read how the archive describes it.</p>
      </div>
    </div>
    <p class="img-note">Schematic orientation only — not a navigational, legal, or evidentiary map.</p>
  </div>
</section>'''

    stewardship = f'''<section class="section band band--ink">
  <div class="wrap grid g2 align-start">
    <div>
      {label("Consent and stewardship", dark=True)}
      <h2 class="display h2 mt-2">Decisions about land require the people who live on it.</h2>
      <p class="lede soft mt-3">Decisions about land and development should be transparent, informed by affected communities, and attentive to water, livelihoods, environmental care, and future generations.</p>
      <ul class="ticks mt-3">
        <li>Consent is a condition, not a consultation step</li>
        <li>Water access is treated as part of any land question</li>
        <li>Development claims are read alongside livelihood impact</li>
        <li>Women’s and minority tenure interests are named explicitly</li>
        <li>Displacement is documented as harm, not as data</li>
      </ul>
    </div>
    <div>{plate('delta.svg', 'Water, livelihoods, and connection', tag='Context plate', cls='plate--wide', note='Illustrative plate — no location or tenure claim.')}</div>
  </div>
</section>'''

    questions = f'''<section class="section band band--cream">
  <div class="wrap">
    {section_head("Land questions", 'What the archive asks about <em>land</em>.',
                  'These questions stay open because closing them requires evidence this platform does not hold — and because a wrong answer about land causes immediate harm.')}
    <div class="grid g2">
      <div class="card card--flat">
        <span class="card__num">Q1 — Tenure</span>
        <h3 class="h4">How is access described across records and family knowledge?</h3>
        <p class="mt-1">Registers may record a category where a family records an arrangement. Comparing the two is research, not reconciliation.</p>
      </div>
      <div class="card card--flat">
        <span class="card__num">Q2 — Water</span>
        <h3 class="h4">Who controls irrigation, and how is that described?</h3>
        <p class="mt-1">Water rights are often entangled with land claims. Records of one rarely settle the other.</p>
      </div>
      <div class="card card--flat">
        <span class="card__num">Q3 — Displacement</span>
        <h3 class="h4">How is movement recorded, and who is not counted?</h3>
        <p class="mt-1">Administrative categories may omit people who never registered, or who left before registration existed.</p>
      </div>
      <div class="card card--flat">
        <span class="card__num">Q4 — Naming</span>
        <h3 class="h4">Which places appear under names that differ from local usage?</h3>
        <p class="mt-1">Naming is evidence of position. A catalogue term may reflect a record-maker’s framework rather than local self-description.</p>
      </div>
    </div>
    <div class="btn-row mt-4">{btn(H('archive/places.html'), 'Read places in relation', 'dark')}</div>
  </div>
</section>'''

    plates_row = f'''<section class="section band band--paper2 band--edge">
  <div class="wrap">
    {section_head("Visual references", 'Three plates, three <em>limits</em>.',
                  'Contextual landscape references are labelled by what they cannot establish. Atmosphere is not evidence.')}
    <div class="grid g3">
      <div>{plate('coast.svg', 'Coastal reference', tag='Atmosphere', cls='plate--wide', note='No named place or event.')}</div>
      <div>{plate('delta.svg', 'Riverine reference', tag='Atmosphere', cls='plate--wide', note='No tenure or boundary claim.')}</div>
      <div>{plate('contour.svg', 'Terrain reference', tag='Atmosphere', cls='plate--wide', note='Not a navigational map.')}</div>
    </div>
  </div>
</section>'''

    return hero + interactive + stewardship + questions + plates_row + cta_band(
        "Continue", "Places are relations, not lines.",
        "The archive’s places docket explains how Benadir and connected places are described, and why place labels carry conditions.",
        btn(H('archive/places.html'), 'Places in relation', 'primary') + btn(H('archive/method.html'), 'Editorial method', 'light'))


# ========================================================= FIELD NOTES
def field_notes():
    hero = f'''<section class="pagehero">
  <div class="wrap">
    {crumbs([("Home", H("index.html")), ("Field notes", None)])}
    <div class="pagehero-inner mt-3">
      <div>
        <span class="label label--dark">Field notes</span>
        <h1 class="display mt-2">Notes from an <em>unfinished record</em>.</h1>
        <p class="lede soft mt-3">Field notes keep questions, methods, cautions, and context visible while research remains in progress. They are dated by sequence, not presented as findings.</p>
      </div>
      <div class="meta-list">
        <div><span>Format</span><b>Working note</b></div>
        <div><span>Status</span><b>Provisional</b></div>
        <div><span>Citation</span><b>Not for citation</b></div>
        <div><span>Corrections</span><b>Welcome</b></div>
      </div>
    </div>
  </div>
</section>'''

    notes = f'''<section class="section band">
  <div class="wrap">
    {section_head("Working notes", 'Six notes, each naming its own <em>limit</em>.',
                  'A working note records what was noticed, what remains unclear, and what would change the note. It is written to be challenged.')}
    {filters("notes", [("all", "All notes", "6"), ("method", "Method", ""), ("questions", "Questions", ""), ("review", "Review", "")])}
    <div class="grid g2">
      <article class="card" data-cat="method" data-scope="notes">
        <span class="badge-date">Note 006 · Working</span>
        <h3 class="h4 mt-2">Reading a catalogue against local naming</h3>
        <p class="mt-1">Catalogue entries often use terms that do not match how residents name a place. Recording both — and the difference — is more useful than choosing one. A future note should describe how the comparison was made.</p>
        {kv([("What would change this", "Evidence that the catalogue term and local term describe different things"), ("Owner", "Place research")])}
      </article>
      <article class="card" data-cat="method" data-scope="notes">
        <span class="badge-date">Note 005 · Working</span>
        <h3 class="h4 mt-2">Translation as an editorial decision</h3>
        <p class="mt-1">A translated phrase can sound more certain than the original. Where a term carries obligation or relationship, the note keeps the original and explains the choice rather than settling it.</p>
        {kv([("What would change this", "Community preference for a different working term"), ("Owner", "Language review")])}
      </article>
      <article class="card" data-cat="questions" data-scope="notes">
        <span class="badge-date">Note 004 · Open question</span>
        <h3 class="h4 mt-2">Why so few accounts describe ordinary work</h3>
        <p class="mt-1">Collections tend to preserve conflict and administration. Farming, fishing, weaving, and care appear mainly in the margins. A research route might begin with photographs rather than reports.</p>
        {kv([("What would change this", "A collection with substantial everyday material"), ("Owner", "Livelihoods research")])}
      </article>
      <article class="card" data-cat="review" data-scope="notes">
        <span class="badge-date">Note 003 · Review</span>
        <h3 class="h4 mt-2">Consent that changes over time</h3>
        <p class="mt-1">A contributor may agree to a recording, then ask later that it not be quoted. Treating the later request as final is the only defensible reading of ongoing consent.</p>
        {kv([("What would change this", "Nothing — this is treated as a settled condition"), ("Owner", "Safeguarding")])}
      </article>
      <article class="card" data-cat="questions" data-scope="notes">
        <span class="badge-date">Note 002 · Open question</span>
        <h3 class="h4 mt-2">Maps that show less than they claim</h3>
        <p class="mt-1">A map’s authority often exceeds its evidence. Scale, date, and the purpose of the mapmaker belong beside the image, not in a caption written later.</p>
        {kv([("What would change this", "Production context for a specific map"), ("Owner", "Spatial research")])}
      </article>
      <article class="card" data-cat="method" data-scope="notes">
        <span class="badge-date">Note 001 · Method</span>
        <h3 class="h4 mt-2">Starting the archive with conditions, not content</h3>
        <p class="mt-1">The first publication decision was to publish labels, access levels, and review steps before any descriptive content. That order protects later work from the pressure of an empty page.</p>
        {kv([("What would change this", "A reviewed, consent-led, fully sourced record set"), ("Owner", "Editorial")])}
      </article>
    </div>
    <p class="is-hidden small soft mt-3" data-empty="notes">No notes in this category yet.</p>
  </div>
</section>'''

    method = f'''<section class="section band band--ink">
  <div class="wrap">
    {section_head("Method in the field", 'Three things every note must name.', 'A note that names its own weak point is more useful than a confident summary that hides it.', dark=True)}
    <div class="grid g3">
      {card("What was observed", "Describe the material, the setting, and who was present — without attributing anything that was not agreed to be attributed.", dark=True, num="01")}
      {card("What remains unclear", "Name the gap precisely. “Unknown” is more useful than a plausible reconstruction.", dark=True, num="02")}
      {card("What would change it", "State the evidence that would revise the note. This is what makes a note research rather than opinion.", dark=True, num="03")}
    </div>
  </div>
</section>'''

    reading = f'''<section class="section band band--cream">
  <div class="wrap grid g-2-1 align-start">
    <div>
      {label("Reading list")}
      <h2 class="display h2 mt-2">Where to start.</h2>
      <p class="body mt-3">A short route for readers new to the material. Nothing here substitutes for source review; each item is a starting condition rather than a settled account.</p>
      <div class="mt-3">
        {accordion([
          ("Begin with the method", "The editorial method explains labels, review, consent, and correction. Reading it first makes every other page easier to interpret."),
          ("Then read the chronology framework", "Periods are research prompts, not events. The chronology shows how the archive organises questions across time."),
          ("Then the places docket", "Place labels carry conditions. Learning how they are used prevents a common misreading of maps and registers."),
          ("Then oral histories", "Testimony is the most easily harmed material. Reading the consent conditions first is a form of respect, not paperwork."),
          ("Finally the sensitive records notice", "Some material should be described only minimally. Understanding why is part of understanding the archive."),
        ])}
      </div>
    </div>
    <div class="card card--flat">
      <span class="label">Note conventions</span>
      {kv([("Sequence", "Notes are numbered, not dated, until publication review completes."), ("Status", "Working, review, or open question."), ("Citation", "Not for citation while provisional."), ("Correction", "Send a correction referencing the note number."), ("Attribution", "Contributors are named only with permission.")])}
    </div>
  </div>
</section>'''

    return hero + notes + method + reading + cta_band(
        "Contribute", "A note can start with a question.",
        "If something here is wrong, incomplete, or missing context, the correction route is the fastest way to improve the record.",
        btn(H('get-involved.html'), 'Send a correction', 'primary') + btn(H('questions.html'), 'Question register', 'light'))


# ======================================================== GET INVOLVED
def get_involved():
    hero = f'''<section class="pagehero">
  <div class="wrap">
    {crumbs([("Home", H("index.html")), ("Get involved", None)])}
    <div class="pagehero-inner mt-3">
      <div>
        <span class="label label--dark">Get involved</span>
        <h1 class="display mt-2">Help make the record <em>more accountable</em>.</h1>
        <p class="lede soft mt-3">Share a story, source, correction, or support message in a way that protects your privacy and respects community care.</p>
        <div class="btn-row mt-4">
          {btn(H('#contribute'), 'Contribute with care', 'primary')}
          {btn(H('#guidance'), 'Read the guidance first', 'light')}
        </div>
      </div>
      <div class="notice notice--dark">
        <span class="label label--dark">Before you send anything</span>
        <p class="small">Contributions are saved for review and are not automatically published. Do not submit sensitive material or anything that could put you or another person at risk.</p>
      </div>
    </div>
  </div>
</section>'''

    ways = f'''<section class="section band">
  <div class="wrap">
    {section_head("Ways to help", 'Four useful routes, one of which is <em>enough</em>.',
                  'You do not need a complete record to contribute. You can share a source, flag a correction, suggest a research question, offer general support, or explain relevant context.')}
    <div class="grid g4">
      {card("Story or memory", "Describe what you know and how you came to know it. You decide what may be quoted and whether you are named.", num="01")}
      {card("Source or record", "A document, photograph, map, or publication — plus where it came from and what limits it has.", num="02")}
      {card("Correction", "Naming, translation, framing, access, and consent are all legitimate grounds for correction.", num="03")}
      {card("Support message", "Time, translation, review, partnership, or a note of support. No obligation attached.", num="04")}
    </div>
  </div>
</section>'''

    guidance = f'''<section class="section band band--paper2" id="guidance">
  <div class="wrap grid g2 align-start">
    <div>
      {label("Safeguarding")}
      <h2 class="display h2 mt-2">What not to send.</h2>
      <ul class="crosses mt-3">
        <li>Material that could identify a person who has not agreed to be identified</li>
        <li>Anything about a minor, or about a living person in a contested account</li>
        <li>Information about current disputes, threats, or ongoing risks</li>
        <li>Scans or photographs of documents you do not have permission to share</li>
        <li>Medical, legal, or financial details about yourself or others</li>
      </ul>
      <p class="small soft mt-3">If you are unsure, send a description only. The team can discuss conditions before anything is transmitted.</p>
    </div>
    <div>
      {label("What happens next")}
      <h2 class="display h2 mt-2">Nothing is published automatically.</h2>
      <div class="mt-3">
        {numlist([
          ("Received", "Your contribution is logged with its stated conditions. You receive a reference number in a live system."),
          ("Reviewed", "A reviewer checks context, provenance, consent, and risk. You may be asked for clarification."),
          ("Decided", "The material may be described, held for community review, restricted, or declined — each with a reason."),
          ("Recorded", "The decision, and any later correction, is retained so the record stays auditable."),
        ])}
      </div>
    </div>
  </div>
</section>'''

    form_html = f'''<section class="section band" id="contribute">
  <div class="wrap grid g-1-2 align-start">
    <div>
      {label("Contribute with care")}
      <h2 class="display h2 mt-2">A contribution is a relationship, not a transaction.</h2>
      <p class="body mt-3">This form is a demonstration. It validates your entries and shows the review route, but transmits nothing and stores nothing.</p>
      <div class="card card--flat mt-3">
        <span class="label">Your choices</span>
        {kv([("For review only", "The team may read and consider the material but will not publish it without a further conversation."), ("Contact me first", "Nothing is published, quoted, or paraphrased until you have responded to a specific proposal."), ("Anonymous", "You may contribute without giving a name. A contact is optional and only used to discuss your contribution.")])}
      </div>
      <div class="notice mt-3" id="corrections">
        <span class="label">Corrections &amp; right of reply</span>
        <p>If a page concerns you, your family, or a contested account, select “Correction” and mark it as a reply request. A reply is not treated as an addendum — it can change a record’s description, status, access, or presence.</p>
      </div>
    </div>
    <form class="form card" data-validate data-form-kind="contribution">
      <div class="field">
        <label for="ci-type">Contribution type <span aria-hidden="true">*</span></label>
        <select class="select" id="ci-type" name="type" required>
          <option value="">Choose one…</option>
          <option>Story or memory</option>
          <option>Source or record</option>
          <option>Correction</option>
          <option>Right of reply</option>
          <option>Support message</option>
        </select>
        <span class="field-error">Please choose a contribution type.</span>
      </div>
      <div class="grid g2" style="gap:1.1rem">
        <div class="field">
          <label for="ci-name">Name (optional)</label>
          <input class="input" id="ci-name" name="name" type="text" placeholder="How should we address you?">
        </div>
        <div class="field">
          <label for="ci-contact">Contact (optional)</label>
          <input class="input" id="ci-contact" name="contact" type="email" placeholder="you@example.com">
        </div>
      </div>
      <div class="field">
        <label for="ci-message">Message <span aria-hidden="true">*</span></label>
        <textarea class="textarea" id="ci-message" name="message" required placeholder="What would you like the reviewers to know? Describe conditions and limits where you can."></textarea>
        <span class="field-error">Please add a message.</span>
      </div>
      <div class="field">
        <label for="ci-review">Review preference</label>
        <select class="select" id="ci-review" name="review">
          <option>For review only</option>
          <option>Contact me before using this</option>
          <option>Anonymous — do not contact</option>
        </select>
      </div>
      <label class="checkline"><input type="checkbox" required> I have not included sensitive material about other people, and I understand this is a demonstration form.</label>
      <div class="form-status" data-form-status role="status" aria-live="polite"></div>
      <button class="btn btn--primary" type="submit">Save contribution</button>
      <p class="form-note">No data leaves your browser. Nothing is stored, transmitted, or published.</p>
    </form>
  </div>
</section>'''

    roles = f'''<section class="section band band--ink">
  <div class="wrap">
    {section_head("Other ways to help", 'Roles that make the work <em>possible</em>.',
                  'The archive depends on people who translate, review, catalogue, and question. These are not volunteer “opportunities” so much as necessary functions.', dark=True)}
    <div class="grid g4">
      {card("Translation", "Somali and English review of terminology, register, and meaning. Translation is treated as editorial work, not typing.", dark=True, num="01")}
      {card("Review", "Subject reviewers check provenance and framing. Community reviewers check consent, naming, and care.", dark=True, num="02")}
      {card("Cataloguing", "Describing material with its conditions: repository, creator, date range, language, access.", dark=True, num="03")}
      {card("Questioning", "Readers who disagree publicly and precisely improve the record more than readers who agree quietly.", dark=True, num="04")}
    </div>
    <div class="btn-row mt-4">
      {btn(H('about.html#contact'), 'Contact pathways', 'light')}
      {btn(H('archive/method.html'), 'Read the method', 'primary')}
    </div>
  </div>
</section>'''

    return hero + ways + guidance + form_html + roles + cta_band(
        "Thank you", "Read how contributions are handled.",
        "The editorial method explains review, consent, correction, and withdrawal — the conditions your contribution would enter.",
        btn(H('archive/method.html'), 'Editorial method', 'primary') + btn(H('principles.html'), 'What guides us', 'light'))


# ========================================================== QUESTIONS
def questions():
    hero = f'''<section class="pagehero">
  <div class="wrap">
    {crumbs([("Home", H("index.html")), ("Questions", None)])}
    <div class="pagehero-inner mt-3">
      <div>
        <span class="label label--dark">Questions</span>
        <h1 class="display mt-2">Questions remain <em>part of the record</em>.</h1>
        <p class="lede soft mt-3">Not every question requires an immediate answer. The platform distinguishes documented material, interpretation, testimony, and open inquiry.</p>
        <div class="btn-row mt-4">
          {btn(H('#register'), 'Jump to the register', 'primary')}
          {btn(H('#faq'), 'Common questions', 'light')}
        </div>
      </div>
      <div class="meta-list">
        <div><span>Open</span><b>05 questions</b></div>
        <div><span>In review</span><b>02 questions</b></div>
        <div><span>Forthcoming</span><b>03 questions</b></div>
        <div><span>Answered</span><b>Recorded, revisable</b></div>
      </div>
    </div>
  </div>
</section>'''

    register = f'''<section class="section band" id="register">
  <div class="wrap">
    {section_head("Question register", 'A register keeps inquiry <em>visible</em>.',
                  'Each question carries a status. A question does not become an answer because it has been asked often, and an answer does not become final because it has been published.')}
    {filters("q", [("all", "All", "10"), ("open", "Open", ""), ("review", "In review", ""), ("forth", "Forthcoming", "")])}
    <div class="card card--flat" style="padding:clamp(.8rem,2vw,1.4rem);overflow-x:auto">
      <table class="table">
        <caption>Question register · working extract</caption>
        <thead><tr><th>Question</th><th>Theme</th><th>Route</th><th>Status</th></tr></thead>
        <tbody>
          <tr data-cat="open" data-scope="q"><td>How is land access described across records and family knowledge?</td><td>Land</td><td>Research</td><td><span class="chip chip--amber">Open</span></td></tr>
          <tr data-cat="open" data-scope="q"><td>Which places appear under names that differ from local usage?</td><td>Place</td><td>Archive</td><td><span class="chip chip--amber">Open</span></td></tr>
          <tr data-cat="review" data-scope="q"><td>What conditions did families set when sharing testimony previously?</td><td>Memory</td><td>Oral histories</td><td><span class="chip chip--ink">In review</span></td></tr>
          <tr data-cat="open" data-scope="q"><td>How is water access described by farmers and by administrators?</td><td>Water</td><td>Research</td><td><span class="chip chip--amber">Open</span></td></tr>
          <tr data-cat="forth" data-scope="q"><td>Where do published accounts of resistance derive from the same small source set?</td><td>History</td><td>History &amp; resistance</td><td><span class="chip">Forthcoming</span></td></tr>
          <tr data-cat="review" data-scope="q"><td>Which catalogue terms reflect an administrator’s category rather than self-description?</td><td>Language</td><td>Method</td><td><span class="chip chip--ink">In review</span></td></tr>
          <tr data-cat="open" data-scope="q"><td>How should material be described when consent was given for a limited purpose only?</td><td>Ethics</td><td>Method</td><td><span class="chip chip--amber">Open</span></td></tr>
          <tr data-cat="forth" data-scope="q"><td>What would a locally grounded periodisation look like?</td><td>Chronology</td><td>Chronology</td><td><span class="chip">Forthcoming</span></td></tr>
          <tr data-cat="open" data-scope="q"><td>How are ordinary livelihoods documented, if at all?</td><td>Livelihoods</td><td>Field notes</td><td><span class="chip chip--amber">Open</span></td></tr>
          <tr data-cat="forth" data-scope="q"><td>What access conditions should apply to protected holdings?</td><td>Access</td><td>Sensitive records</td><td><span class="chip">Forthcoming</span></td></tr>
        </tbody>
      </table>
    </div>
    <p class="is-hidden small soft mt-3" data-empty="q">No questions in this state yet.</p>
  </div>
</section>'''

    faq = f'''<section class="section band band--ink" id="faq">
  <div class="wrap grid g-1-3 align-start">
    <div>
      {label("Common questions", dark=True)}
      <h2 class="display h2 mt-2">Asked, answered <em>carefully</em>.</h2>
      <p class="body soft mt-3">Short answers to the questions readers ask most often. Where an answer depends on context, the answer says so.</p>
    </div>
    <div>
      {accordion([
        ("Is this an official or government website?",
         "No. This is an independent civic and historical platform. It does not represent a government, an administration, or a community body, and it cannot make legal or administrative decisions."),
        ("Does the archive publish verified historical facts?",
         "It publishes frameworks and conditions, with labels that describe the present editorial status of material. Where support is incomplete, that is stated rather than filled in."),
        ("Why are there no names, dates, or quotations?",
         "Because publishing them responsibly requires source review, consent, and right-of-reply checks that this demonstration build has not completed. The absence is deliberate, not an oversight."),
        ("What does a status label actually mean?",
         "It describes the current editorial state of a record — placeholder, memory, interpretation, allegation, unresolved, or restricted. It is not a truth score and it does not rank lived knowledge."),
        ("Can I contribute anonymously?",
         "Yes. Contact details are optional, and you can ask that nothing be published without a further conversation. Anonymous does not mean unattributed in the internal record."),
        ("How do I request a correction or a right of reply?",
         "Use the contribution form and choose “Correction” or “Right of reply”. A reply can change a record’s description, status, access, or presence — it is not treated as an addendum."),
        ("Is the map a real map?",
         "No. It is a schematic orientation diagram. It is not navigational, not legal, and does not define any boundary."),
        ("Who reviews what?",
         "A subject reviewer checks provenance and framing, a language reviewer checks translation and terminology, and a safeguarding reviewer is involved where living people or sensitive accounts are concerned."),
        ("Can I cite this page?",
         "Cite it as a framework page, not as a historical source. The citation templates on the document guide show the difference."),
      ])}
    </div>
  </div>
</section>'''

    ask = f'''<section class="section band band--cream band--edge">
  <div class="wrap grid g2 align-start">
    <div>
      {label("Ask better")}
      <h2 class="display h2 mt-2">How to ask a question that can be answered.</h2>
      <div class="mt-3">
        {numlist([
          ("Name the material", "A question about “the records” cannot be researched. A question about a specific register, series, or collection can."),
          ("State the condition", "If an answer depends on consent, access, translation, or safety, say so. Conditions are part of the question."),
          ("Say what would count", "Describe what evidence would support or contradict an answer. This prevents the question from becoming rhetoric."),
        ])}
      </div>
    </div>
    <div class="card card--flat">
      <span class="label">Submit a question</span>
      <p class="mt-2">Questions can be sent through the contribution route and are logged in this register when they are specific enough to research.</p>
      <div class="btn-row mt-3">{btn(H('get-involved.html'), 'Send a question', 'dark')}{btn(H('research.html#lead'), 'Propose a lead', 'outline')}</div>
    </div>
  </div>
</section>'''

    return hero + register + faq + ask + cta_band(
        "Continue", "Read the method behind the register.",
        "The editorial method explains how a question moves between open, in review, forthcoming, and recorded states.",
        btn(H('archive/method.html'), 'Editorial method', 'primary') + btn(H('research.html'), 'Research & evidence', 'light'))


# =========================================================== DOCUMENT
def document():
    hero = f'''<section class="pagehero">
  <div class="wrap">
    {crumbs([("Home", H("index.html")), ("Document guide", None)])}
    <div class="pagehero-inner mt-3">
      <div>
        <span class="label label--dark">Document guide</span>
        <h1 class="display mt-2">Documents need <em>context</em>.</h1>
        <p class="lede soft mt-3">A document can clarify one part of a history while leaving other experiences unrecorded. This route supports careful reading, annotation, and source-status review.</p>
        <div class="btn-row mt-4">
          {btn(H('#annotated'), 'See the annotated model', 'primary')}
          {btn(H('#citation'), 'Citation templates', 'light')}
        </div>
      </div>
      <div>{plate('ledger.svg', 'Read the maker, not only the text', tag='Document plate', cls='plate--wide', note='Illustrative plate — a model, not a real document.')}</div>
    </div>
  </div>
</section>'''

    annotated = f'''<section class="section band" id="annotated">
  <div class="wrap">
    {section_head("Annotated model", 'Four questions asked of every <em>paragraph</em>.',
                  'Hover or tap a highlighted phrase to see the editorial note attached to it. The model shows how annotations sit beside a text rather than replacing it.')}
    <div class="grid g-1-2 align-start">
      <div class="doc-frame">
        <p class="marker">Model document · entirely illustrative text</p>
        <h3 class="h3 mt-2" style="max-width:26ch">Administrative description of a district</h3>
        <div class="doc-line mt-3">
          The officer records the population of the district as
          <span class="hl" data-note="1">composed of several communities</span><span class="ref">1</span>,
          noting that enumeration was
          <span class="hl" data-note="2">incomplete in the eastern villages</span><span class="ref">2</span>.
        </div>
        <div class="doc-line">
          Cultivation is described as the principal occupation, with
          <span class="hl" data-note="3">land held according to local custom</span><span class="ref">3</span>.
        </div>
        <div class="doc-line">
          The report concludes that the district is
          <span class="hl" data-note="4">peaceful and orderly</span><span class="ref">4</span>.
        </div>
        <p class="img-note">Illustrative model only. No real document, place, person, or figure is reproduced.</p>
      </div>
      <div class="grid" style="gap:.8rem">
        <div class="note-item" data-note-item="1">
          <span class="n">Note 1 · Category</span>
          <p>“Several communities” is an administrative grouping, not a self-description. The officer’s categories may not match local identity or naming.</p>
        </div>
        <div class="note-item" data-note-item="2">
          <span class="n">Note 2 · Absence</span>
          <p>An incomplete count is not a small count. The missing villages should be treated as undocumented rather than empty.</p>
        </div>
        <div class="note-item" data-note-item="3">
          <span class="n">Note 3 · Translation</span>
          <p>“Local custom” compresses a set of arrangements into a phrase. What those arrangements were, and for whom, is a research question.</p>
        </div>
        <div class="note-item" data-note-item="4">
          <span class="n">Note 4 · Purpose</span>
          <p>“Peaceful and orderly” describes the administrator’s priorities as much as the district. It should not be read as an absence of grievance.</p>
        </div>
      </div>
    </div>
  </div>
</section>'''

    fields = f'''<section class="section band band--ink">
  <div class="wrap">
    {section_head("Required fields", 'Every record needs a <em>traceable condition</em>.',
                  'These fields are not metadata decoration. They are the difference between a source and an assertion.', dark=True)}
    <div class="grid g3">
      {card("Provenance", "Repository, collection, creator, date range, custody history, and access conditions.", dark=True, num="01")}
      {card("Production context", "Why the record was made, for whom, in which language, and under which institutional framework.", dark=True, num="02")}
      {card("Corroboration", "Which independently situated materials support, complicate, or contradict it.", dark=True, num="03")}
      {card("Language notes", "Original terms, translation choices, and where meaning may have shifted.", dark=True, num="04")}
      {card("Harm review", "Whether naming, reproducing, or circulating the record could expose or stigmatise anyone now.", dark=True, num="05")}
      {card("Verification status", "The present editorial state, with the date it was last reviewed.", dark=True, num="06")}
    </div>
  </div>
</section>'''

    citation = f'''<section class="section band band--cream" id="citation">
  <div class="wrap">
    {section_head("Citation templates", 'Cite the frame, not a <em>conclusion</em>.',
                  'These templates describe how to reference framework pages responsibly. They deliberately avoid implying that a claim has been verified.')}
    <div class="grid g2">
      <div class="card card--flat">
        <div class="kicker-row"><span class="label">Framework page</span><button class="copy-btn" data-copy="#cite-a" type="button">Copy</button></div>
        <pre class="code mt-2" id="cite-a">Koonfur Bari. “History — A record that asks to be read
carefully.” Southern Somalia Research Program, framework
page, accessed [DATE]. Not a primary source.</pre>
      </div>
      <div class="card card--flat">
        <div class="kicker-row"><span class="label">Archive docket</span><button class="copy-btn" data-copy="#cite-b" type="button">Copy</button></div>
        <pre class="code mt-2" id="cite-b">Biimaal Archive, Koonfur Bari. “Chronology framework,”
docket, accessed [DATE]. Contains research prompts,
not verified historical claims.</pre>
      </div>
      <div class="card card--flat">
        <div class="kicker-row"><span class="label">Status label</span><button class="copy-btn" data-copy="#cite-c" type="button">Copy</button></div>
        <pre class="code mt-2" id="cite-c">Status: community memory — described as recollection,
not independently verified evidence. Access condition:
review-led. Reviewed [DATE].</pre>
      </div>
      <div class="card card--flat">
        <div class="kicker-row"><span class="label">Restricted holding</span><button class="copy-btn" data-copy="#cite-d" type="button">Copy</button></div>
        <pre class="code mt-2" id="cite-d">A protected holding is recorded in this archive.
Contents, source, and identifying details are withheld.
Do not cite content; cite the existence of the condition
only, with permission.</pre>
      </div>
    </div>
  </div>
</section>'''

    method = f'''<section class="section band band--paper2 band--edge">
  <div class="wrap grid g-2-1 align-start">
    <div>
      {label("Reading procedure")}
      <h2 class="display h2 mt-2">Five passes over a document.</h2>
      <div class="mt-3">
        {numlist([
          ("Material", "What is it physically — paper, ink, form, annotations, damage? Material form is evidence of use."),
          ("Purpose", "Who made it, for what decision, and who was expected to read it?"),
          ("Language", "Which terms are institutional, translated, or inherited? Keep original wording beside any paraphrase."),
          ("Silence", "What is not recorded, and is that absence meaningful or simply structural?"),
          ("Circulation", "Who might be affected by republishing it now — and what conditions should apply?"),
        ])}
      </div>
    </div>
    <div class="card card--flat">
      <span class="label">Common errors</span>
      <ul class="crosses mt-2">
        <li>Treating a count as a population</li>
        <li>Reading a category as an identity</li>
        <li>Using a single record as corroboration for itself</li>
        <li>Quoting a translation as though it were the original</li>
        <li>Assuming a file’s presence proves an event</li>
        <li>Assuming a file’s absence disproves one</li>
      </ul>
    </div>
  </div>
</section>'''

    return hero + annotated + fields + citation + method + cta_band(
        "Continue", "See how the method is applied.",
        "The editorial method shows the labels, review steps, and correction routes that these document practices feed into.",
        btn(H('archive/method.html'), 'Editorial method', 'primary') + btn(H('history.html'), 'How we read history', 'light'))


PAGES = [
    dict(url="research.html", nav_title="Research", section="Research",
         title="Research & evidence — Koonfur Bari",
         description="Active research themes, method, ethics, and a question register for the Southeast region’s civic and historical work.",
         active="research.html", body=research),
    dict(url="archive.html", nav_title="Archive", section="Archive",
         title="Biimaal archive — Koonfur Bari",
         description="A living archive index: pathways, status labels, catalogue previews, scope, and access conditions.",
         active="archive.html", body=archive, subnav="archive.html"),
    dict(url="timeline.html", nav_title="Timeline framework", section="Research",
         title="Timeline framework — Koonfur Bari",
         description="A research scaffold for periods, records, interpretation, and community memory — not a chronology of established events.",
         active="timeline.html", body=timeline),
    dict(url="map.html", nav_title="Map & land", section="Research",
         title="Map & land — Koonfur Bari",
         description="An orientation diagram and land questions: consent, stewardship, water, naming, and tenure as research conditions.",
         active="map.html", body=map_page),
    dict(url="field-notes.html", nav_title="Field notes", section="Program",
         title="Field notes — Koonfur Bari",
         description="Working notes that keep questions, methods, cautions, and context visible while research remains in progress.",
         active="field-notes.html", body=field_notes),
    dict(url="get-involved.html", nav_title="Get involved", section="Program",
         title="Get involved — Koonfur Bari",
         description="Contribute a source, memory, correction, or support message — with safeguarding guidance and a visible review route.",
         active="get-involved.html", body=get_involved),
    dict(url="questions.html", nav_title="Question register", section="Research",
         title="Questions — Koonfur Bari",
         description="A register of open, in-review, and forthcoming questions, plus careful answers to common questions about the platform.",
         active="questions.html", body=questions),
    dict(url="document.html", nav_title="Document guide", section="Archive",
         title="Document guide — Koonfur Bari",
         description="How to read a document with context: annotations, required fields, citation templates, and a five-pass reading procedure.",
         active="document.html", body=document),
]
