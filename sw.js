/* Giappone 2026 — service worker: il sito resta consultabile anche senza rete
   (metropolitana, eSIM esaurita). Le pagine si scaricano tutte alla prima visita;
   le foto man mano che si guardano. Cambiando il sito, alzare VERSION. */
var VERSION = 'g26-v3';
var PAGES = [
    './', 'index.html', 'prenotazioni.html', 'pratica.html', 'shopping.html',
    'giorno-01.html', 'giorno-02.html', 'giorno-03.html', 'giorno-04.html', 'giorno-05.html',
    'giorno-06.html', 'giorno-07.html', 'giorno-08.html', 'giorno-09.html', 'giorno-10.html',
    'giorno-11.html', 'giorno-12.html', 'giorno-13.html', 'giorno-14.html', 'giorno-15.html',
    'assets/style.css', 'assets/app.js'
];

self.addEventListener('install', function (e) {
    e.waitUntil(caches.open(VERSION).then(function (c) { return c.addAll(PAGES); }).then(function () { return self.skipWaiting(); }));
});

self.addEventListener('activate', function (e) {
    e.waitUntil(caches.keys().then(function (keys) {
        return Promise.all(keys.filter(function (k) { return k !== VERSION; }).map(function (k) { return caches.delete(k); }));
    }).then(function () { return self.clients.claim(); }));
});

self.addEventListener('fetch', function (e) {
    var req = e.request;
    if (req.method !== 'GET' || new URL(req.url).origin !== location.origin) return;
    var isPage = req.mode === 'navigate' || /\.(html|css|js)$/.test(new URL(req.url).pathname);
    if (isPage) {
        /* Pagine: prima la rete (per avere le modifiche), la copia salvata se la rete non c'è */
        e.respondWith(fetch(req).then(function (res) {
            var copy = res.clone();
            caches.open(VERSION).then(function (c) { c.put(req, copy); });
            return res;
        }).catch(function () {
            return caches.match(req).then(function (r) { return r || caches.match('index.html'); });
        }));
    } else {
        /* Foto: la copia salvata se c'è, altrimenti si scarica e si salva */
        e.respondWith(caches.match(req).then(function (r) {
            return r || fetch(req).then(function (res) {
                var copy = res.clone();
                caches.open(VERSION).then(function (c) { c.put(req, copy); });
                return res;
            });
        }));
    }
});
