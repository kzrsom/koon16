document.addEventListener("DOMContentLoaded", () => {
  const toggle = document.querySelector(".menu-toggle");
  const menu = document.querySelector(".mobile-nav");

  if (toggle && menu) {
    toggle.addEventListener("click", () => {
      const isOpen = menu.classList.toggle("open");
      toggle.setAttribute("aria-expanded", String(isOpen));
      toggle.innerHTML = isOpen ? "✕ <span>Close</span>" : "☰ <span>Menu</span>";
    });

    menu.querySelectorAll("a").forEach((link) => {
      link.addEventListener("click", () => {
        menu.classList.remove("open");
        toggle.setAttribute("aria-expanded", "false");
        toggle.innerHTML = "☰ <span>Menu</span>";
      });
    });
  }

  const pathParts = window.location.pathname.split("/").filter(Boolean);
  const currentPath = pathParts.length ? `/${pathParts.join("/")}` : "/";

  document.querySelectorAll(".desktop-nav .nav-link, .mobile-nav .nav-link").forEach((link) => {
    if (link.getAttribute("href") === currentPath) {
      link.setAttribute("aria-current", "page");
    }
  });
});
