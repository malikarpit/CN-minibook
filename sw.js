/**
 * ⚡ Arpit | sw.js — CN MiniBook 2026 Service Worker (v3)
 * Network-First for Navigation (always fresh HTML) + Cache-First for static assets
 */

const CACHE_NAME    = 'cn-minibook-v4';
const RUNTIME_CACHE = 'cn-minibook-runtime-v4';
const ASSETS = [
  './',
  './index.html',
  './progress.html',
  './chapters/ch01-fundamentals.html',
  './chapters/ch02-types-topologies.html',
  './chapters/ch03-models-addressing.html',
  './chapters/ch04-devices-sdn.html',
  './chapters/ch05-physical-fundamentals.html',
  './chapters/ch06-media-signaling.html',
  './chapters/ch07-modulation-switching.html',
  './chapters/ch08-dll-fundamentals.html',
  './chapters/ch09-protocols-sliding.html',
  './chapters/ch10-mac-ethernet.html',
  './exams/mock-exam.html',
  './exams/unit-quiz.html',
  './assets/js/quiz-data.js',
  './assets/css/main.css',
  './assets/css/components.css',
  './assets/css/animations.css',
  './assets/css/timer.css',
  './assets/css/chapters.css',
  './assets/js/state.js',
  './assets/js/core.js',
  './assets/js/modes.js',
  './assets/js/tts.js',
  './assets/js/print.js',
  './assets/js/notes.js',
  './assets/js/glossary.js',
  './assets/js/timer.js',
  './assets/js/timer-settings.js',
  './assets/js/timer-analytics.js',
  './assets/js/timer-notifications.js',
  './assets/js/timer-ui.js',
  './manifest.json',
  'https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600&display=swap'
];

function isCacheableResponse(response) {
  return response && response.status === 200 && response.type !== 'opaque';
}

function isNavigationRequest(request) {
  return request.mode === 'navigate' || (request.headers && request.headers.get('accept') && request.headers.get('accept').includes('text/html'));
}

/* ── INSTALL: Pre-cache all core assets ───────────────────── */
self.addEventListener('install', event => {
  self.skipWaiting();
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => {
        return Promise.allSettled(
          ASSETS.map(url => cache.add(url).catch(err => console.warn('SW cache miss:', url, err)))
        );
      })
  );
});

/* ── ACTIVATE: Clean up old caches immediately ───────────── */
self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(keys =>
      Promise.all(
        keys.filter(k => k !== CACHE_NAME && k !== RUNTIME_CACHE).map(k => caches.delete(k))
      )
    ).then(() => self.clients.claim())
  );
});

/* ── FETCH: Network-first for HTML, Cache-first for assets ─ */
self.addEventListener('fetch', event => {
  if (event.request.method !== 'GET') return;
  if (!event.request.url.startsWith('http')) return;

  // 1. Navigation requests (HTML pages): Network-First with cache fallback
  if (isNavigationRequest(event.request)) {
    event.respondWith(
      fetch(event.request)
        .then(response => {
          if (isCacheableResponse(response)) {
            const clone = response.clone();
            caches.open(CACHE_NAME).then(cache => cache.put(event.request, clone));
          }
          return response;
        })
        .catch(() => {
          return caches.match(event.request).then(cached => {
            if (cached) return cached;
            return caches.match('./index.html');
          });
        })
    );
    return;
  }

  // 2. Static Assets: Cache-first with background revalidation
  event.respondWith(
    caches.match(event.request).then(cached => {
      const networkFetch = fetch(event.request)
        .then(response => {
          if (isCacheableResponse(response)) {
            const clone = response.clone();
            caches.open(RUNTIME_CACHE).then(cache => cache.put(event.request, clone));
          }
          return response;
        })
        .catch(() => null);

      if (cached) {
        event.waitUntil(networkFetch);
        return cached;
      }

      return networkFetch.then(response => response || undefined);
    })
  );
});

/* ── BACKGROUND SYNC / SKIP_WAITING ──────────────────────── */
self.addEventListener('message', event => {
  if (event.data === 'SKIP_WAITING') {
    self.skipWaiting();
    event.waitUntil(
      self.clients.matchAll({ type: 'window', includeUncontrolled: true })
        .then(clients => clients.forEach(client => client.postMessage({ type: 'SW_SKIP_WAITING' })))
    );
  }
});
