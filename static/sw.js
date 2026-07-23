
self.addEventListener('install', (e) => {
  e.waitUntil(caches.open('emotion-v1').then((cache) => {
    return cache.addAll(['/', '/app/login', '/static/manifest.json']);
  }));
});

self.addEventListener('fetch', (e) => {
  e.respondWith(caches.match(e.request).then((response) => {
    return response || fetch(e.request);
  }));
});
