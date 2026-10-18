document.addEventListener("DOMContentLoaded", () => {
  const spotlightCards = document.querySelectorAll(".card");
  const finePointer = window.matchMedia("(hover: hover) and (pointer: fine)");
  const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)");

  if (finePointer.matches && !reducedMotion.matches) {
    spotlightCards.forEach((card) => {
      card.addEventListener("pointermove", (event) => {
        const bounds = card.getBoundingClientRect();
        card.style.setProperty("--spotlight-x", `${event.clientX - bounds.left}px`);
        card.style.setProperty("--spotlight-y", `${event.clientY - bounds.top}px`);
        card.classList.add("spotlight-active");
      });

      card.addEventListener("pointerleave", () => {
        card.classList.remove("spotlight-active");
      });
    });
  }

  const header = document.querySelector("header.site-header");
  if (!header) return;

  header.className = "site-header home-header";
  header.innerHTML = `
    <div class="header-inner">
      <a class="brand home-brand" href="/" aria-label="Biimaal History Archive home">
        <img class="home-brand-image home-brand-image-redesigned" src="https://i.postimg.cc/vBbrShJx/calan.png" alt="Biimaal / Bimal archive emblem">
        <span class="home-brand-copy">
          <span class="brand-name" style="font-size: 10px; color: transparent; background-image: linear-gradient(90deg, var(--color-primary), var(--color-text)); background-clip: text; -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-family: Poppins, &quot;Trebuchet MS&quot;, Arial, sans-serif; font-weight: 700;">KOONFUR-BARI INITIATIVES</span>
          <span class="brand-subtitle" style="color: rgb(192, 192, 192);">HISTORY ARCHIVE</span>
        </span>
      </a>
      <details class="home-mobile-menu">
        <summary aria-label="Open archive navigation" style="color: var(--color-text); background-color: var(--color-surface);"><span class="home-menu-icon" aria-hidden="true">☰</span><span>Explore</span></summary>
        <nav class="header-nav home-navigation home-mobile-link-row" aria-label="Main navigation">
          <a href="/">Home</a><a href="/about">About</a><a href="/resistance">Resistance</a><a href="/timeline">Timeline</a><a href="/library">Sources</a>
          <a class="home-nav-cta" href="/research">Research Library<span aria-hidden="true">↗</span></a>
          <details class="nav-menu home-nav-menu">
            <summary>More<span aria-hidden="true">⌄</span></summary>
            <div class="nav-menu-panel">
              <p>Biimaal history · research pathways</p>
              <div class="nav-grid nav-grid-buttons">
                <a href="/resistance">Biimaal resistance</a><a href="/communities">Communities</a><a href="/resources">Learning resources</a><a href="/map">Map &amp; land research</a><a href="/contact">Contact guidance</a><a href="/timeline">Historical timeline</a><a href="/atrocities">Violence &amp; accountability</a><a href="/oral-histories">Oral histories</a><a href="/people">People &amp; biography</a><a href="/places">Places &amp; geography</a><a href="/documents">Documents</a><a href="/library">Research library</a><a href="/search">Search &amp; discovery</a><a href="/sources">Sources &amp; methods</a><a href="/archive">Evidence labels</a><a href="/contribute">Contribute</a><a href="/blog">Corrections &amp; reply</a><a href="/submit">Prepare a submission</a>
              </div>
            </div>
          </details>
        </nav>
      </details>
      <nav class="header-nav home-navigation home-desktop-navigation" aria-label="Main navigation">
        <a href="/">Home</a>
        <a href="/about">About</a>
        <a href="/resistance">Resistance</a>
        <a href="/timeline">Timeline</a>
        <a href="/library">Sources</a>
        <a class="home-nav-cta" href="/research">Documents <span aria-hidden="true">↗</span></a>
        <details class="nav-menu home-nav-menu">
          <summary>Explore history <span aria-hidden="true">⌄</span></summary>
          <div class="nav-menu-panel">
            <p>Biimaal history · research pathways</p>
            <div class="nav-grid nav-grid-buttons">
                              <a href="/resistance">Biimaal resistance</a>
                <a href="/communities">Communities</a>
                <a href="/resources">Learning resources</a>
                <a href="/map">Map &amp; land research</a>
                <a href="/contact">Contact guidance</a>
                
              <a href="/timeline">Historical timeline</a>
              <a href="/atrocities">Violence &amp; accountability</a>
              <a href="/oral-histories">Oral histories</a>
              <a href="/people">People &amp; biography</a>
              <a href="/places">Places &amp; geography</a>
              <a href="/documents">Documents</a>
              <a href="/library">Research library</a>
              <a href="/search">Search &amp; discovery</a>
              <a href="/sources">Sources &amp; methods</a>
              
              <a href="/archive">Evidence labels</a>
              
              
              
              <a href="/contribute">Contribute</a>
              <a href="/civic-advocacy">Civic advocacy &amp; memory</a>
              <a href="/blog">Corrections &amp; reply</a>
              <a href="/submit">Prepare a submission</a>
            </div>
          </div>
        </details>
      </nav>
    </div>
  `;
});

document.addEventListener("DOMContentLoaded", () => {
  const path = window.location.pathname.replace(/\/+$/, "") || "/";
  if (path === "/" || path === "/home") return;

  const header = document.querySelector("header.site-header");
  const main = document.querySelector("main");
  if (!header || !main || document.querySelector(".site-breadcrumb")) return;

  const pageHeading = main.querySelector("h1");
  const currentPage = pageHeading?.textContent.trim() || document.title;
  const breadcrumb = document.createElement("nav");
  breadcrumb.className = "site-breadcrumb";
  breadcrumb.setAttribute("aria-label", "Breadcrumb");
  breadcrumb.innerHTML = `
    <a href="/">Home</a>
    <span aria-hidden="true">/</span>
    <span aria-current="page"></span>
  `;
  breadcrumb.querySelector('[aria-current="page"]').textContent = currentPage;
  header.insertAdjacentElement("afterend", breadcrumb);

  const battleHero = document.querySelector(".battle-hero");
  if (battleHero && main.parentNode) {
    main.parentNode.insertBefore(battleHero, main);
  }
});

document.addEventListener("DOMContentLoaded", () => {
  if (document.querySelector(".back-to-top-wrap")) return;

  const topAnchor = document.createElement("span");
  topAnchor.id = "page-top";
  topAnchor.setAttribute("aria-hidden", "true");
  document.body.prepend(topAnchor);

  const backToTop = document.createElement("div");
  backToTop.className = "back-to-top-wrap";
  backToTop.innerHTML = `
    <a class="back-to-top" href="#page-top" aria-label="Back to top of page">
      <span aria-hidden="true">↑</span>
      <span>Back to top</span>
    </a>
  `;

  const footer = document.querySelector("footer.site-footer");
  const main = document.querySelector("main");
  if (footer) {
    footer.insertAdjacentElement("beforebegin", backToTop);
  } else if (main) {
    main.append(backToTop);
  } else {
    document.body.append(backToTop);
  }
});

document.addEventListener("DOMContentLoaded", () => {
  if (window.location.pathname.replace(/\/+$/, "") !== "/about") return;

  const autoplayControls = document.querySelector("#research-pathways .pathways-autoplay");
  const autoplayButton = document.querySelector("#research-pathways #autoplay-toggle");

  autoplayControls?.remove();

  window.setTimeout(() => {
    if (autoplayButton?.getAttribute("aria-pressed") === "false") {
      autoplayButton.click();
    }
  }, 0);
});
