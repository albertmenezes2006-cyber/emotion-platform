const CACHE_NAME = 'emotion-v16';
const CACHE_STATIC = [
  '/', '/login', '/cadastro', '/blog', '/planos', '/premium',
  '/terapia', '/faq', '/sobre', '/static/favicon.svg'
];

// INSTALL — cacheia assets estaticos
self.addEventListener('install', function(e) {
  self.skipWaiting();
  e.waitUntil(
    caches.open(CACHE_NAME).then(function(cache) {
      return cache.addAll(CACHE_STATIC);
    }).catch(function(err) {
      console.log('[SW] Erro no cache:', err);
    })
  );
});

// ACTIVATE — limpa caches antigos
self.addEventListener('activate', function(e) {
  e.waitUntil(
    caches.keys().then(function(keys) {
      return Promise.all(
        keys.filter(function(key) {
          return key !== CACHE_NAME;
        }).map(function(key) {
          console.log('[SW] Removendo cache antigo:', key);
          return caches.delete(key);
        })
      );
    })
  );
  self.clients.claim();
});

// FETCH — network first para API, cache first para estaticos
self.addEventListener('fetch', function(e) {
  const url = new URL(e.request.url);

  // API e rotas dinamicas — sempre network
  if (
    url.pathname.startsWith('/api') ||
    url.pathname.startsWith('/analisar') ||
    url.pathname.startsWith('/chat') ||
    url.pathname.startsWith('/diario') ||
    url.pathname.startsWith('/stats') ||
    url.pathname.startsWith('/admin') ||
    url.pathname.startsWith('/exportar') ||
    url.pathname.startsWith('/certificado') ||
    url.pathname.startsWith('/cupom') ||
    url.pathname.startsWith('/webhook') ||
    e.request.method !== 'GET'
  ) {
    e.respondWith(fetch(e.request).catch(function() {
      return new Response('{"error":"offline"}', {
        headers: {'Content-Type': 'application/json'}
      });
    }));
    return;
  }

  // Estaticos — cache first, fallback network
  if (
    url.pathname.startsWith('/static') ||
    url.pathname.endsWith('.svg') ||
    url.pathname.endsWith('.png') ||
    url.pathname.endsWith('.ico') ||
    url.pathname.endsWith('.json')
  ) {
    e.respondWith(
      caches.match(e.request).then(function(cached) {
        return cached || fetch(e.request).then(function(response) {
          const clone = response.clone();
          caches.open(CACHE_NAME).then(function(cache) {
            cache.put(e.request, clone);
          });
          return response;
        });
      })
    );
    return;
  }

  // Paginas HTML — network first, fallback cache
  e.respondWith(
    fetch(e.request).then(function(response) {
      const clone = response.clone();
      caches.open(CACHE_NAME).then(function(cache) {
        cache.put(e.request, clone);
      });
      return response;
    }).catch(function() {
      return caches.match(e.request).then(function(cached) {
        return cached || caches.match('/');
      });
    })
  );
});

// PUSH NOTIFICATIONS
self.addEventListener('push', function(e) {
  var data = {};
  if (e.data) {
    try { data = e.data.json(); } catch(err) {
      data = { title: 'Emotion Intelligence', body: e.data.text() };
    }
  }
  var title = data.title || '🧠 Emotion Intelligence';
  var options = {
    body:    data.body    || 'Voce tem uma nova mensagem!',
    icon:    data.icon    || '/static/favicon.svg',
    badge:   '/static/favicon.svg',
    tag:     data.tag     || 'emotion-notif',
    data:    { url: data.url || '/dashboard' },
    actions: [
      { action: 'abrir',  title: '📊 Abrir Dashboard' },
      { action: 'fechar', title: '✕ Fechar' }
    ],
    vibrate: [200, 100, 200],
    requireInteraction: false
  };
  e.waitUntil(self.registration.showNotification(title, options));
});

// NOTIFICATION CLICK
self.addEventListener('notificationclick', function(e) {
  e.notification.close();
  var url = (e.notification.data && e.notification.data.url) ? e.notification.data.url : '/dashboard';
  if (e.action === 'fechar') return;
  e.waitUntil(
    clients.matchAll({ type: 'window', includeUncontrolled: true }).then(function(clientList) {
      for (var i = 0; i < clientList.length; i++) {
        if (clientList[i].url.includes(self.location.origin) && 'focus' in clientList[i]) {
          clientList[i].navigate(url);
          return clientList[i].focus();
        }
      }
      if (clients.openWindow) return clients.openWindow(url);
    })
  );
});

// BACKGROUND SYNC — para analises offline
self.addEventListener('sync', function(e) {
  if (e.tag === 'sync-analises') {
    e.waitUntil(
      clients.matchAll().then(function(clientList) {
        clientList.forEach(function(client) {
          client.postMessage({ type: 'SYNC_COMPLETE' });
        });
      })
    );
  }
});
