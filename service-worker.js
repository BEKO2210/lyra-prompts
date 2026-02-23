const CACHE_NAME = 'lyra-prompts-v2';

/* Base-Pfad ermitteln — funktioniert auf GitHub Pages (/lyra-prompts/) und lokal (/) */
const BASE = self.location.pathname.replace(/service-worker\.js$/, '');

const PRECACHE_ASSETS = [
  BASE,
  BASE + 'index.html',
  BASE + 'manifest.json',
  BASE + 'icons/icon-192x192.png',
  BASE + 'icons/icon-512x512.png',
  BASE + 'icons/apple-touch-icon.png'
];

// Install: Precache wichtige Assets
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      return cache.addAll(PRECACHE_ASSETS);
    })
  );
  self.skipWaiting();
});

// Activate: Alte Caches entfernen
self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((cacheNames) => {
      return Promise.all(
        cacheNames
          .filter((name) => name !== CACHE_NAME)
          .map((name) => caches.delete(name))
      );
    })
  );
  self.clients.claim();
});

// Fetch: Network-first mit Cache-Fallback fuer HTML,
// Cache-first fuer statische Assets
self.addEventListener('fetch', (event) => {
  const { request } = event;

  // Nur GET-Requests cachen
  if (request.method !== 'GET') return;

  // Externe Requests (Google Fonts etc.) — Stale-while-revalidate
  if (!request.url.startsWith(self.location.origin)) {
    event.respondWith(
      caches.match(request).then((cached) => {
        const fetched = fetch(request).then((response) => {
          if (response.ok) {
            const clone = response.clone();
            caches.open(CACHE_NAME).then((cache) => cache.put(request, clone));
          }
          return response;
        }).catch(() => cached);

        return cached || fetched;
      })
    );
    return;
  }

  // HTML-Seiten: Network-first, Fallback auf Cache
  if (request.headers.get('accept')?.includes('text/html')) {
    event.respondWith(
      fetch(request)
        .then((response) => {
          const clone = response.clone();
          caches.open(CACHE_NAME).then((cache) => cache.put(request, clone));
          return response;
        })
        .catch(() => caches.match(request).then((cached) => cached || caches.match(BASE + 'index.html')))
    );
    return;
  }

  // Statische Assets (Icons, Bilder): Cache-first
  event.respondWith(
    caches.match(request).then((cached) => {
      if (cached) return cached;

      return fetch(request).then((response) => {
        if (response.ok) {
          const clone = response.clone();
          caches.open(CACHE_NAME).then((cache) => cache.put(request, clone));
        }
        return response;
      });
    })
  );
});
