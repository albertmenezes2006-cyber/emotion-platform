const CACHE_NAME = 'emotion-v15';

self.addEventListener('install', function(e){
    self.skipWaiting();
    e.waitUntil(
        caches.open(CACHE_NAME).then(function(cache){
            return cache.addAll(['/','/login','/planos','/blog']);
        })
    );
});

self.addEventListener('activate', function(e){
    e.waitUntil(
        caches.keys().then(function(keys){
            return Promise.all(
                keys.filter(function(key){
                    return key !== CACHE_NAME;
                }).map(function(key){
                    return caches.delete(key);
                })
            );
        })
    );
    self.clients.claim();
});

self.addEventListener('fetch', function(e){
    e.respondWith(
        caches.match(e.request).then(function(response){
            return response || fetch(e.request);
        })
    );
});

// ============================================================
// PUSH NOTIFICATIONS
// ============================================================
self.addEventListener('push', function(e){
    var data = {};
    if(e.data){
        try { data = e.data.json(); } catch(err){ data = {title:'Emotion Intelligence', body: e.data.text()}; }
    }
    var title   = data.title   || '🧠 Emotion Intelligence';
    var options = {
        body:    data.body    || 'Voce tem uma nova mensagem!',
        icon:    data.icon    || '/static/favicon.svg',
        badge:   '/static/favicon.svg',
        tag:     data.tag     || 'emotion-notif',
        data:    { url: data.url || '/dashboard' },
        actions: [
            { action: 'abrir',   title: 'Abrir App' },
            { action: 'fechar',  title: 'Fechar'    }
        ]
    };
    e.waitUntil(self.registration.showNotification(title, options));
});

self.addEventListener('notificationclick', function(e){
    e.notification.close();
    if(e.action === 'fechar') return;
    var url = (e.notification.data && e.notification.data.url) ? e.notification.data.url : '/dashboard';
    e.waitUntil(
        clients.matchAll({type:'window'}).then(function(clientList){
            for(var i=0; i<clientList.length; i++){
                if(clientList[i].url === url && 'focus' in clientList[i]){
                    return clientList[i].focus();
                }
            }
            if(clients.openWindow){ return clients.openWindow(url); }
        })
    );
});

// ============================================================
// BACKGROUND SYNC — lembrete diario
// ============================================================
self.addEventListener('periodicsync', function(e){
    if(e.tag === 'lembrete-diario'){
        e.waitUntil(
            self.registration.showNotification('🧠 Emotion Intelligence', {
                body:  'Que tal registrar como voce esta se sentindo hoje?',
                icon:  '/static/favicon.svg',
                badge: '/static/favicon.svg',
                data:  { url: '/dashboard' }
            })
        );
    }
});
