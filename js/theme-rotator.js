(() => {
  const themeLabels = [
    "Community memory",
    "Historical inquiry",
    "Land and place",
    "Source-aware research",
    "Peaceful dialogue"
  ];
  const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)");

  document.querySelectorAll("[data-theme-rotator]").forEach((label) => {
    let currentIndex = 0;
    if (reducedMotion.matches) return;

    window.setInterval(() => {
      label.classList.add("is-changing");
      window.setTimeout(() => {
        currentIndex = (currentIndex + 1) % themeLabels.length;
        label.textContent = themeLabels[currentIndex];
        label.classList.remove("is-changing");
      }, 220);
    }, 3000);
  });
})();
