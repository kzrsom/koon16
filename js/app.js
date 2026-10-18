document.addEventListener("DOMContentLoaded", () => {
  if (document.body.dataset.archiveInitialized === "true") return;
  document.body.dataset.archiveInitialized = "true";

  const prefersReducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)");

  // Remove any previously rendered backdrop markup so pages never accumulate layers.
  document.querySelectorAll(".weather-rain, .weather-lightning").forEach((layer) => layer.remove());

  const rainLayer = document.createElement("div");
  rainLayer.className = "weather-rain";
  rainLayer.setAttribute("aria-hidden", "true");

  if (!prefersReducedMotion.matches) {
    for (let index = 0; index < 90; index += 1) {
      const drop = document.createElement("span");
      drop.className = "weather-drop";
      drop.style.left = `${Math.random() * 100}%`;
      drop.style.setProperty("--drop-height", `${14 + Math.random() * 28}px`);
      drop.style.setProperty("--drop-duration", `${0.7 + Math.random() * 1.1}s`);
      drop.style.setProperty("--drop-delay", `${Math.random() * -2}s`);
      rainLayer.append(drop);
    }
  }

  document.body.append(rainLayer);

  const lightning = document.createElement("div");
  lightning.className = "weather-lightning";
  lightning.setAttribute("aria-hidden", "true");
  document.body.append(lightning);

  if (!prefersReducedMotion.matches) {
    let flashTimer;

    window.addEventListener("pointermove", (event) => {
      const windAngle = ((event.clientX / window.innerWidth) - 0.5) * 24;
      rainLayer.style.setProperty("--wind-angle", `${windAngle}deg`);
    }, {
      passive: true
    });

    const flash = () => {
      lightning.classList.remove("is-flashing");
      void lightning.offsetWidth;
      lightning.classList.add("is-flashing");
    };

    window.addEventListener("pointerdown", () => {
      flash();
      window.clearInterval(flashTimer);
      flashTimer = window.setInterval(flash, 900);
    });

    ["pointerup", "pointercancel", "blur"].forEach((eventName) => {
      window.addEventListener(eventName, () => window.clearInterval(flashTimer));
    });
  }

  const homeFeatureSection = document.querySelector(".home-feature-section");
  if (homeFeatureSection && window.location.pathname === "/") {
    homeFeatureSection.remove();
  }

  const historicalFeatureCards = document.querySelector("#home-historical-feature-cards");
  const researchProgram = document.querySelector(".home-context-research");
  if (historicalFeatureCards && researchProgram) {
    researchProgram.insertAdjacentElement("beforebegin", historicalFeatureCards);
  }

  const copyHeaderButton = document.querySelector("[data-copy-header]");
  if (copyHeaderButton) {
    copyHeaderButton.addEventListener("click", async () => {
      const buttonCode = copyHeaderButton.cloneNode(true);

      try {
        await navigator.clipboard.writeText(buttonCode.outerHTML.trim());
        copyHeaderButton.textContent = "Button code copied";
      } catch {
        copyHeaderButton.textContent = "Clipboard unavailable";
      }
    });
  }

  const mobileMenu = document.querySelector(".home-mobile-menu");
  if (mobileMenu) {
    let closeTimer;

    const scheduleClose = () => {
      window.clearTimeout(closeTimer);
      if (!mobileMenu.open) return;

      closeTimer = window.setTimeout(() => {
        const focusWasInside = mobileMenu.contains(document.activeElement);
        mobileMenu.querySelectorAll("details[open]").forEach((menu) => {
          menu.open = false;
        });
        mobileMenu.open = false;

        if (focusWasInside) {
          mobileMenu.querySelector("summary")?.focus();
        }
      }, 10000);
    };

    mobileMenu.addEventListener("toggle", scheduleClose);
    mobileMenu.addEventListener("pointerdown", scheduleClose);
    mobileMenu.addEventListener("keydown", scheduleClose);
    mobileMenu.addEventListener("focusin", scheduleClose);
  }

  const copyButton = document.querySelector("[data-copy]");
  if (copyButton) {
    copyButton.addEventListener("click", async () => {
      const source = document.querySelector("[data-copy-source]");
      const status = document.querySelector("[data-copy-status]");
      if (!source || !status) return;

      try {
        await navigator.clipboard.writeText(source.textContent.trim());
        status.textContent = "Placeholder copied. Confirm every field, source, access note, and permission before use.";
      } catch {
        status.textContent = "Clipboard access is unavailable. Select and copy the placeholder text manually.";
      }
    });
  }

  const filterInput = document.querySelector("[data-filter-input]");
  if (filterInput) {
    filterInput.addEventListener("input", () => {
      const query = filterInput.value.trim().toLowerCase();
      document.querySelectorAll("[data-filter-item]").forEach((item) => {
        item.hidden = !item.textContent.toLowerCase().includes(query);
      });
    });
  }

  document.querySelectorAll("[data-auto-slide]").forEach((carousel) => {
    const cards = [...carousel.querySelectorAll(":scope > li")];
    if (cards.length < 2 || prefersReducedMotion.matches) return;

    let timer;
    const step = () => {
      const maxScroll = carousel.scrollWidth - carousel.clientWidth;
      const gap = Number.parseFloat(window.getComputedStyle(carousel).columnGap) || 0;
      const nextPosition = carousel.scrollLeft + cards[0].getBoundingClientRect().width + gap;

      carousel.scrollTo({
        left: nextPosition >= maxScroll - 8 ? 0 : nextPosition,
        behavior: "smooth"
      });
    };
    const stop = () => window.clearInterval(timer);
    const start = () => {
      stop();
      timer = window.setInterval(step, 4000);
    };

    carousel.addEventListener("mouseenter", stop);
    carousel.addEventListener("mouseleave", start);
    carousel.addEventListener("focusin", stop);
    carousel.addEventListener("focusout", start);
    carousel.addEventListener("touchstart", stop, {
      passive: true
    });
    carousel.addEventListener("touchend", start, {
      passive: true
    });
    start();
  });

  const localForm = document.querySelector("[data-local-form]");
  if (localForm) {
    localForm.addEventListener("submit", (event) => {
      event.preventDefault();
      if (!localForm.reportValidity()) return;

      const message = document.querySelector("[data-form-status]");
      if (message) {
        message.textContent = "Your draft passed local field checks. Nothing was sent or stored.";
      }
      localForm.reset();
    });
  }
});

document.addEventListener("DOMContentLoaded", () => {
  if (window.location.pathname !== "/") return;

  const mission = document.querySelector("#mission");
  if (!mission) return;

  const findSectionByHeading = (headingText) => {
    return [...document.querySelectorAll("main section")].find((section) => {
      const heading = section.querySelector("h2");
      return heading?.textContent.trim() === headingText;
    });
  };

  const sectionsToMove = [
    findSectionByHeading("Local decisions. Shared responsibility."),
    findSectionByHeading("A community-led call for justice and dignity."),
    findSectionByHeading("Read across periods")
  ].filter(Boolean);

  let insertionPoint = mission;
  sectionsToMove.forEach((section) => {
    insertionPoint.insertAdjacentElement("afterend", section);
    insertionPoint = section;
  });
});
