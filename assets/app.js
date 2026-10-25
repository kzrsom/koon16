/* ==========================================================================
   Koonfur Bari — interaction layer
   Vanilla JS, no dependencies. All progressive enhancement.
   ========================================================================== */
(function () {
  'use strict';

  var $ = function (s, c) { return (c || document).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };
  var depth = parseInt(document.body.getAttribute('data-depth') || '0', 10);
  var PREFIX = new Array(depth + 1).join('../');

  /* ---------------------------------------------------------- year stamp */
  $$('[data-year]').forEach(function (el) { el.textContent = new Date().getFullYear(); });

  /* ------------------------------------------------------------- header */
  var header = $('#site-header');
  var progress = $('[data-progress]');
  var backtop = $('[data-backtop]');

  function onScroll() {
    var y = window.scrollY || window.pageYOffset;
    var h = document.documentElement.scrollHeight - window.innerHeight;
    if (progress) progress.style.width = (h > 0 ? (y / h) * 100 : 0) + '%';
    if (backtop) backtop.classList.toggle('is-visible', y > 620);
    if (header) header.style.boxShadow = y > 12 ? '0 12px 30px -22px rgba(0,0,0,.9)' : 'none';
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  if (backtop) backtop.addEventListener('click', function () {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });

  /* --------------------------------------------------------- mobile menu */
  var menuBtn = $('[data-menu-toggle]');
  var mobileNav = $('#nav-mobile');
  if (menuBtn && mobileNav) {
    menuBtn.addEventListener('click', function () {
      var open = mobileNav.classList.toggle('is-open');
      menuBtn.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }

  /* -------------------------------------------------------------- reveal */
  var revealables = $$('.card, .section-head, .tl-item, .plate, .statrow, .notice, .quote, .acc, .map-shell, .doc-frame');
  if ('IntersectionObserver' in window) {
    // never hide content that is already on screen
    var fold = window.innerHeight * 0.92;
    revealables = revealables.filter(function (el) {
      if (el.getBoundingClientRect().top < fold) return false;
      el.classList.add('reveal');
      return true;
    });
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) {
          e.target.classList.add('is-in');
          io.unobserve(e.target);
        }
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
    revealables.forEach(function (el) { io.observe(el); });
    // safety net: never leave content hidden (print, deep links, odd viewports)
    window.addEventListener('load', function () {
      revealables.forEach(function (el) {
        var r = el.getBoundingClientRect();
        if (r.top < window.innerHeight * 1.3) el.classList.add('is-in');
      });
    });
    window.addEventListener('beforeprint', function () {
      revealables.forEach(function (el) { el.classList.add('is-in'); });
    });
  }

  /* ------------------------------------------------------------- filters */
  $$('[data-filters]').forEach(function (group) {
    var scope = group.getAttribute('data-filters');
    group.addEventListener('click', function (e) {
      var btn = e.target.closest('[data-filter]');
      if (!btn) return;
      var val = btn.getAttribute('data-filter');
      $$('[data-filter]', group).forEach(function (b) {
        b.classList.toggle('is-active', b === btn);
        b.setAttribute('aria-pressed', b === btn ? 'true' : 'false');
      });
      $$('[data-cat]').forEach(function (item) {
        if (item.getAttribute('data-scope') !== scope) return;
        var cats = (item.getAttribute('data-cat') || '').split(' ');
        var show = val === 'all' || cats.indexOf(val) !== -1;
        item.classList.toggle('is-hidden', !show);
      });
      var empty = $('[data-empty="' + scope + '"]');
      if (empty) {
        var visible = $$('[data-cat][data-scope="' + scope + '"]').filter(function (i) {
          return !i.classList.contains('is-hidden');
        }).length;
        empty.classList.toggle('is-hidden', visible > 0);
      }
    });
  });

  /* ---------------------------------------------------------------- tabs */
  $$('[data-tabs]').forEach(function (bar) {
    var uid = bar.getAttribute('data-tabs');
    bar.addEventListener('click', function (e) {
      var tab = e.target.closest('[data-tab]');
      if (!tab) return;
      $$('[data-tab]', bar).forEach(function (t) {
        t.setAttribute('aria-selected', t === tab ? 'true' : 'false');
      });
      $$('[data-tabpanel="' + uid + '"]').forEach(function (panel) {
        panel.classList.toggle('is-active', panel.id === tab.getAttribute('data-tab').replace('tab-', ''));
      });
    });
  });

  /* -------------------------------------------------------------- search */
  var searchBox = $('[data-search-box]');
  var searchInput = $('[data-search-input]');
  var searchResults = $('[data-search-results]');
  var index = window.KB_INDEX || [];

  function renderSearch(q) {
    if (!searchResults) return;
    var term = (q || '').trim().toLowerCase();
    if (!term) {
      searchResults.innerHTML = index.slice(0, 6).map(function (r) {
        return '<a href="' + PREFIX + r.u + '"><span>' + r.t + '</span><span>' + r.s + '</span></a>';
      }).join('');
      return;
    }
    var hits = index.filter(function (r) {
      return (r.t + ' ' + r.d + ' ' + r.s).toLowerCase().indexOf(term) !== -1;
    }).slice(0, 10);
    if (!hits.length) {
      searchResults.innerHTML = '<p class="small soft" style="padding:.6rem 0">No pages matched “' + q + '”. Try “archive”, “land”, “consent” or “method”.</p>';
      return;
    }
    searchResults.innerHTML = hits.map(function (r) {
      return '<a href="' + PREFIX + r.u + '"><span>' + r.t + '</span><span>' + r.s + '</span></a>';
    }).join('');
  }

  function openSearch() {
    if (!searchBox) return;
    searchBox.classList.add('is-open');
    renderSearch('');
    if (searchInput) { searchInput.value = ''; searchInput.focus(); }
  }
  function closeSearch() { if (searchBox) searchBox.classList.remove('is-open'); }

  $$('[data-search-open]').forEach(function (b) { b.addEventListener('click', openSearch); });
  if (searchBox) {
    searchBox.addEventListener('click', function (e) { if (e.target === searchBox) closeSearch(); });
    var closeBtn = $('[data-search-close]');
    if (closeBtn) closeBtn.addEventListener('click', closeSearch);
  }
  if (searchInput) searchInput.addEventListener('input', function (e) { renderSearch(e.target.value); });

  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') {
      closeSearch();
      if (mobileNav && mobileNav.classList.contains('is-open') && menuBtn) {
        mobileNav.classList.remove('is-open');
        menuBtn.setAttribute('aria-expanded', 'false');
      }
    }
    if ((e.key === 'k' || e.key === 'K') && (e.metaKey || e.ctrlKey)) {
      e.preventDefault(); openSearch();
    }
  });

  /* --------------------------------------------------------------- forms */
  $$('form[data-validate]').forEach(function (form) {
    form.noValidate = true; // use our own, more legible error states
    var status = $('[data-form-status]', form);
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var ok = true;
      $$('[required]', form).forEach(function (field) {
        var wrap = field.closest('.field');
        var val = (field.value || '').trim();
        var bad = !val;
        if (!bad && field.type === 'email') bad = !/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(val);
        if (!bad && field.type === 'checkbox') bad = !field.checked;
        if (wrap) wrap.classList.toggle('has-error', bad);
        field.setAttribute('aria-invalid', bad ? 'true' : 'false');
        if (bad) ok = false;
      });
      if (!ok) {
        var first = $('.has-error', form);
        if (first) first.scrollIntoView({ behavior: 'smooth', block: 'center' });
        return;
      }
      if (status) {
        var kind = form.getAttribute('data-form-kind') || 'contribution';
        status.innerHTML = '<strong>Saved locally — not transmitted.</strong> This demonstration stores nothing. In a live system your ' +
          kind + ' would be queued for editorial review, and you would receive a reference number before any publication decision.';
        status.classList.add('is-visible');
        status.scrollIntoView({ behavior: 'smooth', block: 'center' });
      }
      form.reset();
      $$('.has-error', form).forEach(function (f) { f.classList.remove('has-error'); });
    });
    $$('input, textarea, select', form).forEach(function (f) {
      f.addEventListener('input', function () {
        var wrap = f.closest('.field');
        if (wrap) wrap.classList.remove('has-error');
      });
    });
  });

  /* ------------------------------------------------------------ lanugage */
  var LANG = 'en';
  var langBtn = $('[data-lang-toggle]');
  var langLabel = $('[data-lang-label]');
  function applyLang(lang) {
    LANG = lang;
    $$('[data-so]').forEach(function (el) {
      if (!el.getAttribute('data-en')) el.setAttribute('data-en', el.textContent);
      el.textContent = lang === 'so' ? el.getAttribute('data-so') : el.getAttribute('data-en');
    });
    document.documentElement.lang = lang === 'so' ? 'so' : 'en';
    if (langLabel) langLabel.textContent = lang === 'so' ? 'Soomaali' : 'English';
    if (langBtn) langBtn.textContent = lang === 'so' ? 'SO / EN' : 'EN / SO';
    if (langBtn) langBtn.setAttribute('aria-label', lang === 'so' ? 'Switch to English' : 'Switch to Somali');
    try { localStorage.setItem('kb-lang', lang); } catch (err) {}
  }
  if (langBtn) {
    var saved = null;
    try { saved = localStorage.getItem('kb-lang'); } catch (err) {}
    langBtn.addEventListener('click', function () {
      applyLang(LANG === 'en' ? 'so' : 'en');
      toast(LANG === 'so'
        ? 'Somali: navigation, labels, and key headings switch immediately. Long-form sections remain in English while translation review is completed.'
        : 'English restored.');
    });
    if (saved === 'so') applyLang('so');
  }

  /* ---------------------------------------------------------------- toast */
  var toastEl = $('[data-toast]');
  var toastTimer = null;
  function toast(msg) {
    if (!toastEl) return;
    toastEl.textContent = msg;
    toastEl.classList.add('is-visible');
    clearTimeout(toastTimer);
    toastTimer = setTimeout(function () { toastEl.classList.remove('is-visible'); }, 6000);
  }

  /* ----------------------------------------------------------------- map */
  var mapNodes = $$('[data-place]');
  var mapReadout = $('[data-map-readout]');
  if (mapNodes.length && mapReadout) {
    var showPlace = function (node) {
      mapNodes.forEach(function (n) { n.classList.toggle('is-active', n === node); });
      mapReadout.innerHTML =
        '<span class="marker">' + (node.getAttribute('data-kind') || 'Place') + '</span>' +
        '<h3 class="h3 mt-1">' + node.getAttribute('data-title') + '</h3>' +
        '<p class="mt-2 small">' + node.getAttribute('data-body') + '</p>' +
        '<p class="img-note">' + (node.getAttribute('data-note') || 'Relationship, not boundary.') + '</p>';
    };
    mapNodes.forEach(function (n) {
      n.addEventListener('click', function () { showPlace(n); });
      n.addEventListener('keydown', function (e) {
        if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); showPlace(n); }
      });
      n.setAttribute('tabindex', '0');
      n.setAttribute('role', 'button');
    });
    showPlace(mapNodes[0]);
  }

  /* ------------------------------------------------- document annotations */
  var notes = $$('[data-note-item]');
  var marks = $$('[data-note]');
  function activateNote(id) {
    marks.forEach(function (m) { m.classList.toggle('is-active', m.getAttribute('data-note') === id); });
    notes.forEach(function (n) { n.classList.toggle('is-active', n.getAttribute('data-note-item') === id); });
  }
  marks.forEach(function (m) {
    m.addEventListener('click', function () { activateNote(m.getAttribute('data-note')); });
  });
  notes.forEach(function (n) {
    n.addEventListener('mouseenter', function () { activateNote(n.getAttribute('data-note-item')); });
    n.addEventListener('focus', function () { activateNote(n.getAttribute('data-note-item')); });
  });

  /* --------------------------------------------------------------- gates */
  var gate = $('[data-gate]');
  if (gate) {
    var gateContent = $('[data-gate-content]');
    gate.classList.add('is-open');
    var accept = $('[data-gate-accept]', gate);
    var cancel = $('[data-gate-cancel]', gate);
    var closeGate = function (show) {
      gate.classList.remove('is-open');
      if (gateContent) gateContent.hidden = show ? false : false;
    };
    if (accept) accept.addEventListener('click', function () {
      gate.classList.remove('is-open');
      if (gateContent) gateContent.hidden = false;
    });
    if (cancel) cancel.addEventListener('click', function () {
      gate.classList.remove('is-open');
      if (gateContent) gateContent.hidden = false;
    });
    gate.addEventListener('click', function (e) { if (e.target === gate) gate.classList.remove('is-open'); });
    if (gate.hasAttribute('data-gate-always')) gate.classList.remove('is-open');
  }

  /* ---------------------------------------------------------- copy buttons */
  $$('[data-copy]').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var target = $(btn.getAttribute('data-copy'));
      if (!target) return;
      var text = target.innerText || target.textContent;
      var done = function () {
        var old = btn.textContent;
        btn.textContent = 'Copied';
        setTimeout(function () { btn.textContent = old; }, 1600);
      };
      if (navigator.clipboard) {
        navigator.clipboard.writeText(text).then(done, done);
      } else { done(); }
    });
  });

  /* ----------------------------------------------------- in-page toc links */
  $$('[data-toc] a').forEach(function (a) {
    a.addEventListener('click', function () {
      if (mobileNav) mobileNav.classList.remove('is-open');
    });
  });
})();
