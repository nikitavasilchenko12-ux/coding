/* ═══════════════════════════════════════════════════════════════
   Dimino Physical Therapy — Main JavaScript
   ═══════════════════════════════════════════════════════════════ */

'use strict';

// ─── Navbar: scroll shadow + mobile menu ─────────────────────
(function () {
  const navbar    = document.getElementById('navbar');
  const hamburger = document.getElementById('hamburger');
  const navLinks  = document.getElementById('nav-links');

  // Shadow on scroll
  window.addEventListener('scroll', function () {
    navbar.classList.toggle('scrolled', window.scrollY > 20);
  }, { passive: true });

  // Toggle mobile menu
  hamburger.addEventListener('click', function () {
    const isOpen = navLinks.classList.toggle('open');
    hamburger.classList.toggle('active', isOpen);
    hamburger.setAttribute('aria-expanded', isOpen.toString());
  });

  // Close menu when a link is clicked
  navLinks.querySelectorAll('a').forEach(function (link) {
    link.addEventListener('click', function () {
      navLinks.classList.remove('open');
      hamburger.classList.remove('active');
      hamburger.setAttribute('aria-expanded', 'false');
    });
  });

  // Close on outside click
  document.addEventListener('click', function (e) {
    if (!navbar.contains(e.target)) {
      navLinks.classList.remove('open');
      hamburger.classList.remove('active');
      hamburger.setAttribute('aria-expanded', 'false');
    }
  });
})();

// ─── Active nav link on scroll ───────────────────────────────
(function () {
  const sections = document.querySelectorAll('section[id], div[id]');
  const navAnchors = document.querySelectorAll('.nav-links a:not(.btn)');

  function onScroll() {
    let current = '';
    sections.forEach(function (sec) {
      const top = sec.getBoundingClientRect().top;
      if (top <= 90) current = sec.id;
    });
    navAnchors.forEach(function (a) {
      a.style.color = '';
      a.style.background = '';
      const href = a.getAttribute('href');
      if (href === '#' + current || (current === 'home' && href === '#home')) {
        a.style.color = 'var(--blue)';
        a.style.background = 'var(--blue-light)';
      }
    });
  }

  window.addEventListener('scroll', onScroll, { passive: true });
})();

// ─── Scroll-triggered fade-in animations ─────────────────────
(function () {
  const targets = [
    '.service-card',
    '.review-card',
    '.info-card',
    '.about-content',
    '.about-image',
    '.hours-content',
    '.contact-info',
    '.contact-form-wrap',
    '.loc-detail',
    '.section-header',
  ];

  const allEls = document.querySelectorAll(targets.join(','));
  allEls.forEach(function (el) { el.classList.add('fade-in'); });

  const observer = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });

  allEls.forEach(function (el) { observer.observe(el); });

  // Stagger delay for grid children
  document.querySelectorAll('.services-grid, .reviews-grid, .info-grid').forEach(function (grid) {
    Array.from(grid.children).forEach(function (child, i) {
      child.style.transitionDelay = (i * 80) + 'ms';
    });
  });
})();

// ─── Contact form ─────────────────────────────────────────────
(function () {
  const form    = document.getElementById('contact-form');
  const success = document.getElementById('form-success');
  if (!form) return;

  form.addEventListener('submit', function (e) {
    e.preventDefault();

    const name  = form.querySelector('#f-name').value.trim();
    const phone = form.querySelector('#f-phone').value.trim();

    if (!name) {
      alert('Please enter your name.');
      form.querySelector('#f-name').focus();
      return;
    }
    if (!phone) {
      alert('Please enter your phone number.');
      form.querySelector('#f-phone').focus();
      return;
    }

    // Simulate submission (replace with real backend/email service)
    const btn = form.querySelector('button[type="submit"]');
    const origText = btn.textContent;
    btn.textContent = 'Sending…';
    btn.disabled = true;

    setTimeout(function () {
      form.reset();
      btn.textContent = origText;
      btn.disabled = false;
      success.textContent = '✓ Thank you, ' + name + '! We\'ll be in touch to confirm your appointment.';
      success.classList.add('visible');
      setTimeout(function () { success.classList.remove('visible'); }, 6000);
    }, 1200);
  });
})();

// ─── Footer year ─────────────────────────────────────────────
(function () {
  const yearEl = document.getElementById('year');
  if (yearEl) yearEl.textContent = new Date().getFullYear();
})();

// ─── Smooth scroll polyfill for older Safari ─────────────────
(function () {
  document.querySelectorAll('a[href^="#"]').forEach(function (anchor) {
    anchor.addEventListener('click', function (e) {
      const id = anchor.getAttribute('href').slice(1);
      if (!id) return;
      const target = document.getElementById(id);
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    });
  });
})();
