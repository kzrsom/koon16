document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll("[data-archive-slideshow]").forEach((slideshow) => {
    const slides = Array.from(slideshow.querySelectorAll(".archive-guide-slide"));
    const dots = Array.from(slideshow.querySelectorAll(".archive-guide-dots button"));
    const previousButton = slideshow.querySelector(".archive-guide-prev");
    const nextButton = slideshow.querySelector(".archive-guide-next");
    const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)");
    const interval = 3000;
    let activeIndex = slides.findIndex((slide) => slide.classList.contains("is-active"));
    let timer;
    let resumeTimer;

    if (slides.length < 2) {
      return;
    }

    if (activeIndex < 0) {
      activeIndex = 0;
    }

    const showSlide = (index) => {
      activeIndex = (index + slides.length) % slides.length;

      slides.forEach((slide, slideIndex) => {
        const isActive = slideIndex === activeIndex;
        slide.classList.toggle("is-active", isActive);
        slide.setAttribute("aria-hidden", String(!isActive));

        if (isActive) {
          slide.removeAttribute("inert");
        } else {
          slide.setAttribute("inert", "");
        }
      });

      dots.forEach((dot, dotIndex) => {
        if (dotIndex === activeIndex) {
          dot.setAttribute("aria-current", "true");
        } else {
          dot.removeAttribute("aria-current");
        }
      });
    };

    const stopAutoplay = () => {
      window.clearInterval(timer);
      window.clearTimeout(resumeTimer);
    };

    const startAutoplay = () => {
      stopAutoplay();

      if (!document.hidden && !reducedMotion.matches) {
        timer = window.setInterval(() => showSlide(activeIndex + 1), interval);
      }
    };

    const pauseThenResume = () => {
      stopAutoplay();

      if (!document.hidden && !reducedMotion.matches) {
        resumeTimer = window.setTimeout(startAutoplay, 5000);
      }
    };

    previousButton?.addEventListener("click", () => {
      showSlide(activeIndex - 1);
      pauseThenResume();
    });

    nextButton?.addEventListener("click", () => {
      showSlide(activeIndex + 1);
      pauseThenResume();
    });

    dots.forEach((dot, index) => {
      dot.addEventListener("click", () => {
        showSlide(index);
        pauseThenResume();
      });
    });

    slideshow.addEventListener("pointerenter", pauseThenResume);
    slideshow.addEventListener("focusin", pauseThenResume);
    slideshow.addEventListener("pointerleave", startAutoplay);
    document.addEventListener("visibilitychange", startAutoplay);
    reducedMotion.addEventListener("change", startAutoplay);

    showSlide(activeIndex);
    startAutoplay();
  });
});
