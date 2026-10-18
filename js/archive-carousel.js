document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll("[data-archive-carousel]").forEach((carousel) => {
    const track = carousel.querySelector(".archive-carousel-track");
    const slides = [...carousel.querySelectorAll(".archive-slide")];
    const section = carousel.closest(".archive-carousel-content");
    const previousButton = section?.querySelector(".archive-carousel-prev");
    const nextButton = section?.querySelector(".archive-carousel-next");
    const pagination = carousel.querySelector(".archive-carousel-pagination");
    const isMobile = window.matchMedia("(max-width: 760px)");
    const prefersReducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)");

    if (!track || slides.length === 0) return;

    let autoAdvanceTimer;
    let resumeTimer;
    let isHovered = false;
    let isTouched = false;

    const getStep = () => {
      const firstSlide = slides[0];
      const gap = Number.parseFloat(window.getComputedStyle(track).columnGap) || 0;
      return firstSlide.getBoundingClientRect().width + gap;
    };

    const getActiveIndex = () => {
      const step = getStep();
      return step ? Math.round(track.scrollLeft / step) : 0;
    };

    const goToSlide = (index, behavior = "smooth") => {
      const boundedIndex = (index + slides.length) % slides.length;
      track.scrollTo({
        left: boundedIndex * getStep(),
        behavior
      });
    };

    const paginationButtons = slides.map((slide, index) => {
      const button = document.createElement("button");
      button.type = "button";
      button.setAttribute("aria-label", `Go to topic ${index + 1}`);
      button.addEventListener("click", () => {
        goToSlide(index);
        restartAfterManualInteraction();
      });
      pagination?.append(button);
      return button;
    });

    const updatePagination = () => {
      const activeIndex = Math.min(getActiveIndex(), slides.length - 1);
      paginationButtons.forEach((button, index) => {
        if (index === activeIndex) {
          button.setAttribute("aria-current", "true");
        } else {
          button.removeAttribute("aria-current");
        }
      });
    };

    const stopAutoAdvance = () => {
      window.clearInterval(autoAdvanceTimer);
      autoAdvanceTimer = undefined;
    };

    const canAutoAdvance = () => (
      isMobile.matches &&
      !prefersReducedMotion.matches &&
      !isHovered &&
      !isTouched
    );

    const startAutoAdvance = () => {
      stopAutoAdvance();
      if (!canAutoAdvance()) return;

      autoAdvanceTimer = window.setInterval(() => {
        goToSlide(getActiveIndex() + 1);
      }, 2500);
    };

    function restartAfterManualInteraction() {
      stopAutoAdvance();
      window.clearTimeout(resumeTimer);
      resumeTimer = window.setTimeout(startAutoAdvance, 2500);
    }

    previousButton?.addEventListener("click", () => {
      goToSlide(getActiveIndex() - 1);
      restartAfterManualInteraction();
    });

    nextButton?.addEventListener("click", () => {
      goToSlide(getActiveIndex() + 1);
      restartAfterManualInteraction();
    });

        track.addEventListener("scroll", updatePagination, { passive: true });


    carousel.addEventListener("mouseenter", () => {
      isHovered = true;
      stopAutoAdvance();
    });

    carousel.addEventListener("mouseleave", () => {
      isHovered = false;
      startAutoAdvance();
    });

    carousel.addEventListener("touchstart", () => {
      isTouched = true;
      stopAutoAdvance();
    }, {
      passive: true
    });

    carousel.addEventListener("touchend", () => {
      isTouched = false;
      restartAfterManualInteraction();
    }, {
      passive: true
    });

    carousel.addEventListener("touchcancel", () => {
      isTouched = false;
      startAutoAdvance();
    }, {
      passive: true
    });

    window.addEventListener("resize", () => {
      updatePagination();
      startAutoAdvance();
    });

    isMobile.addEventListener?.("change", startAutoAdvance);
    prefersReducedMotion.addEventListener?.("change", startAutoAdvance);

    updatePagination();
    startAutoAdvance();
  });
});
