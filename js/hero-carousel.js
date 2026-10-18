/* Accessible six-slide hero controls. */
(() => {
  document.querySelectorAll('[data-hero-carousel]').forEach((carousel) => {
    const slides = Array.from(carousel.querySelectorAll('[data-hero-slide]'));
    const dots = Array.from(carousel.querySelectorAll('[data-hero-dot]'));
    const previous = carousel.querySelector('[data-hero-prev]');
    const next = carousel.querySelector('[data-hero-next]');
    const count = carousel.querySelector('[data-hero-count]');
    if (slides.length < 2) return;

    const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
    let autoplay;

    let active = Math.max(0, slides.findIndex((slide) => slide.classList.contains('is-active')));

    carousel.querySelectorAll('.hero-carousel-slide h1, .hero-carousel-slide h2').forEach((heading) => {
      if (heading.dataset.waveReady === 'true') return;
      const text = heading.textContent.trim();
      heading.setAttribute('aria-label', text);
      heading.dataset.waveReady = 'true';
      heading.replaceChildren(...Array.from(text, (character, index) => {
        const span = document.createElement('span');
        span.className = 'hero-wave-letter';
        span.setAttribute('aria-hidden', 'true');
        span.style.setProperty('--wave-index', index);
        span.textContent = character === ' ' ? '\u00a0' : character;
        return span;
      }));
    });

    const show = (index) => {
      active = (index + slides.length) % slides.length;
      slides.forEach((slide, position) => {
        const selected = position === active;
        slide.classList.toggle('is-active', selected);
        slide.setAttribute('aria-hidden', String(!selected));
        if (selected) slide.removeAttribute('inert');
        else slide.setAttribute('inert', '');
      });
      dots.forEach((dot, position) => {
        if (position === active) dot.setAttribute('aria-current', 'true');
        else dot.removeAttribute('aria-current');
      });
      if (count) count.innerHTML = `${String(active + 1).padStart(2, '0')} <span>/ ${String(slides.length).padStart(2, '0')}</span>`;
    };

    const startAutoplay = () => {
      window.clearInterval(autoplay);
      if (!document.hidden && !reducedMotion.matches) {
        autoplay = window.setInterval(() => show(active + 1), 3000);
      }
    };

    previous?.addEventListener('click', () => {
      show(active - 1);
      startAutoplay();
    });
    next?.addEventListener('click', () => {
      show(active + 1);
      startAutoplay();
    });
    dots.forEach((dot, index) => dot.addEventListener('click', () => {
      show(index);
      startAutoplay();
    }));

    carousel.addEventListener('keydown', (event) => {
      if (event.key === 'ArrowLeft') {
        event.preventDefault();
        show(active - 1);
        startAutoplay();
      } else if (event.key === 'ArrowRight') {
        event.preventDefault();
        show(active + 1);
        startAutoplay();
      }
    });

    carousel.addEventListener('pointerenter', () => {
      window.clearInterval(autoplay);
    });
    carousel.addEventListener('pointerleave', startAutoplay);
    document.addEventListener('visibilitychange', startAutoplay);
    reducedMotion.addEventListener('change', startAutoplay);
    show(active);
    startAutoplay();
  });
})();
