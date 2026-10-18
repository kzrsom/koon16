/* Carousel controls: use data-carousel-prev / data-carousel-next buttons. */
(() => {
  document.querySelectorAll('.carousel').forEach((carousel) => {
    const track = carousel.querySelector('.carousel__track');
    if (!track) return;

    const scrollBySlide = (direction) => {
      const slide = track.querySelector('.carousel__slide');
      if (!slide) return;
      const styles = window.getComputedStyle(track);
      const gap = parseFloat(styles.columnGap || styles.gap) || 0;
      track.scrollBy({
        left: direction * (slide.getBoundingClientRect().width + gap),
        behavior: window.matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth'
      });
    };

    carousel.querySelector('[data-carousel-prev]')?.addEventListener('click', () => scrollBySlide(-1));
    carousel.querySelector('[data-carousel-next]')?.addEventListener('click', () => scrollBySlide(1));
  });
})();
