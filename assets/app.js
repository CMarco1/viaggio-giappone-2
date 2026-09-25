/* Giappone 2026 — script condiviso. Nessuna dipendenza. */
(function () {
    'use strict';

    var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    var TRIP_START = '2026-12-03';   /* Giorno 1 */
    var TRIP_DAYS = 15;

    function pad(n) { return ('0' + n).slice(-2); }
    function iso(d) { return d.getFullYear() + '-' + pad(d.getMonth() + 1) + '-' + pad(d.getDate()); }

    /* ---- Data di oggi. Per provare la modalità "Oggi": ?oggi=2026-12-05 (resta per la sessione) ---- */
    function isoToday() {
        var m = /[?&]oggi=(\d{4}-\d{2}-\d{2})/.exec(location.search);
        try {
            if (m) sessionStorage.setItem('g26-oggi', m[1]);
            var saved = sessionStorage.getItem('g26-oggi');
            if (saved) return saved;
        } catch (e) { if (m) return m[1]; }
        return iso(new Date());
    }
    var today = isoToday();

    /* Numero del giorno di viaggio (1-15) per una data, oppure 0 */
    function dayNumber(isoDate) {
        var a = new Date(TRIP_START + 'T12:00:00'), b = new Date(isoDate + 'T12:00:00');
        var n = Math.round((b - a) / 86400000) + 1;
        return (n >= 1 && n <= TRIP_DAYS) ? n : 0;
    }
    var todayN = dayNumber(today);
    function dayPage(n) { return 'giorno-' + pad(n) + '.html'; }

    function icon(name) {
        var s = document.createElement('span');
        s.className = 'ic ic-' + name;
        s.setAttribute('aria-hidden', 'true');
        return s;
    }

    /* ---- Countdown alla partenza (solo in home) ---- */
    var box = document.getElementById('countdown');
    if (box) {
        var dep = new Date(2026, 11, 2), now = new Date(today + 'T12:00:00');
        var days = Math.round((dep - new Date(now.getFullYear(), now.getMonth(), now.getDate())) / 86400000);
        var html = '';
        if (days > 1) html = '<strong>' + days + '</strong><span>giorni alla partenza</span>';
        else if (days === 1) html = '<strong>Domani</strong><span>si parte</span>';
        else if (days === 0) html = '<strong>Oggi</strong><span>si parte</span>';
        else if (todayN) html = '<strong>Giorno ' + todayN + '</strong><span>di 15, in Giappone</span>';
        if (html) { box.innerHTML = html; box.hidden = false; }
    }

    /* ---- Modalità "Oggi": voce nel menu e scheda in cima alla home ---- */
    var nav = document.querySelector('.mainnav');
    if (nav && todayN) {
        var t = document.createElement('a');
        t.href = dayPage(todayN);
        t.className = 'nav-today';
        t.appendChild(icon('sun'));
        var tl = document.createElement('span');
        tl.textContent = 'Oggi';
        t.appendChild(tl);
        nav.insertBefore(t, nav.firstChild);
    }

    var todayCard = document.querySelector('.daycard[data-date="' + today + '"]');
    if (todayCard) {
        todayCard.classList.add('is-today');
        var jump = document.getElementById('goToday');
        if (jump) { jump.href = todayCard.getAttribute('href'); jump.hidden = false; }
    }

    var main = document.querySelector('main.wrap');
    var isHome = !!document.getElementById('riepilogo');
    function makeTodayBox(eyebrow, title, text, href, goLabel, img, next) {
        var tb = document.createElement('section');
        tb.className = 'todaybox';
        tb.innerHTML =
            '<div class="tb-img"></div><div class="tb-body">' +
            '<span class="tb-eyebrow"></span><h2></h2><p class="tb-text"></p>' +
            '<a class="tb-go"></a><span class="tb-next"></span></div>';
        tb.querySelector('.tb-img').style.backgroundImage = img;
        tb.querySelector('.tb-eyebrow').textContent = eyebrow;
        tb.querySelector('h2').textContent = title;
        tb.querySelector('.tb-text').textContent = text;
        var go = tb.querySelector('.tb-go');
        go.href = href; go.textContent = goLabel + ' '; go.appendChild(icon('arrow'));
        var nx = tb.querySelector('.tb-next');
        if (next) nx.textContent = next; else nx.remove();
        main.insertBefore(tb, main.firstChild);
    }
    if (isHome && main && todayCard) {
        var nextCard = document.querySelector('.daycard[data-date="' + iso(new Date(new Date(today + 'T12:00:00').getTime() + 86400000)) + '"]');
        makeTodayBox(
            'Oggi · ' + todayCard.querySelector('.num').textContent + ' · ' + todayCard.querySelector('.date').textContent,
            todayCard.querySelector('h3').textContent,
            todayCard.querySelector('.teaser').textContent,
            todayCard.getAttribute('href'), 'Apri la giornata',
            todayCard.querySelector('.thumb').style.backgroundImage,
            nextCard ? 'Domani: ' + nextCard.querySelector('h3').textContent : 'Stasera si vola a casa.'
        );
    } else if (isHome && main && today === '2026-12-02') {
        makeTodayBox('Oggi si parte', 'Fiumicino T3, volo QR132 alle 15:10',
            'Scalo a Doha, arrivo a Osaka KIX domani alle 16:25. Check-in online, passaporti, Visit Japan Web.',
            'prenotazioni.html#voli', 'Orari dei voli', "url('images/thumbs/airport.jpg')",
            'Domani: arrivo in serata a Kyoto');
    }

    /* ---- Striscia dei giorni: porta in vista quello corrente ---- */
    var strip = document.querySelector('.daystrip');
    if (strip) {
        var cur = strip.querySelector('[aria-current="page"]');
        if (cur) strip.scrollLeft = Math.max(0, cur.offsetLeft - (strip.clientWidth / 2) + (cur.offsetWidth / 2));
        var chip = strip.querySelector('[data-date="' + today + '"]');
        if (chip) chip.classList.add('is-today');
    }

    /* ---- Itinerario a colpo d'occhio: due righe per tappa, il resto al tocco ---- */
    var tls = document.querySelectorAll('.timeline');
    Array.prototype.forEach.call(tls, function (ol) {
        var items = [];
        Array.prototype.forEach.call(ol.children, function (li) {
            var d = li.querySelector('div');
            if (!d) return;
            li.classList.add('has-more');
            if (d.scrollHeight <= d.clientHeight + 2) { li.classList.remove('has-more'); return; }
            items.push(li);
            li.setAttribute('tabindex', '0');
            li.setAttribute('aria-expanded', 'false');
            function toggle() {
                var open = li.classList.toggle('open');
                li.setAttribute('aria-expanded', open ? 'true' : 'false');
            }
            li.addEventListener('click', function (e) {
                if (e.target.closest('a')) return;
                if (window.getSelection && String(window.getSelection()).length) return;
                toggle();
            });
            li.addEventListener('keydown', function (e) {
                if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); toggle(); }
            });
        });
        var h2 = ol.closest('.card') && ol.closest('.card').querySelector('h2');
        if (h2 && items.length) {
            var b = document.createElement('button');
            b.type = 'button';
            b.className = 'tl-toggle';
            b.textContent = 'Apri tutto';
            b.addEventListener('click', function () {
                var openAll = b.textContent === 'Apri tutto';
                items.forEach(function (li) {
                    li.classList.toggle('open', openAll);
                    li.setAttribute('aria-expanded', openAll ? 'true' : 'false');
                });
                b.textContent = openAll ? 'Riduci' : 'Apri tutto';
            });
            h2.appendChild(b);
        }
    });

    /* ---- Mappa incorporata solo quando la si tocca: niente dati consumati prima ---- */
    Array.prototype.forEach.call(document.querySelectorAll('.mapload[data-embed]'), function (a) {
        a.addEventListener('click', function (e) {
            e.preventDefault();
            var f = document.createElement('iframe');
            f.src = a.getAttribute('data-embed');
            f.title = 'Mappa delle tappe della giornata';
            f.setAttribute('referrerpolicy', 'no-referrer-when-downgrade');
            f.setAttribute('allowfullscreen', '');
            var big = document.createElement('a');
            big.className = 'maplink';
            big.href = a.href;
            big.target = '_blank';
            big.rel = 'noopener';
            big.textContent = 'Apri la mappa grande in Google Maps ↗';
            a.parentNode.insertBefore(big, a.nextSibling);
            a.parentNode.replaceChild(f, a);
        });
    });

    /* ---- Torna su ---- */
    var toTop = document.querySelector('.to-top');
    if (toTop) {
        toTop.addEventListener('click', function () {
            window.scrollTo({ top: 0, behavior: reduceMotion ? 'auto' : 'smooth' });
        });
        var ticking = false;
        window.addEventListener('scroll', function () {
            if (ticking) return;
            ticking = true;
            window.requestAnimationFrame(function () {
                toTop.classList.toggle('visible', window.scrollY > 700);
                ticking = false;
            });
        }, { passive: true });
    }

    /* ---- Uso offline: le pagine già aperte restano consultabili senza rete ---- */
    if ('serviceWorker' in navigator && location.protocol === 'https:') {
        window.addEventListener('load', function () {
            navigator.serviceWorker.register('sw.js').catch(function () {});
        });
    }

    /* ---- Frecce sinistra/destra per passare da un giorno all'altro ---- */
    document.addEventListener('keydown', function (e) {
        if (e.altKey || e.ctrlKey || e.metaKey || e.shiftKey) return;
        var t = e.target;
        if (t && (t.tagName === 'INPUT' || t.tagName === 'TEXTAREA' || t.isContentEditable || t.closest && t.closest('.timeline'))) return;
        var sel = e.key === 'ArrowLeft' ? '.dayfoot .prev' : (e.key === 'ArrowRight' ? '.dayfoot .next' : null);
        if (!sel) return;
        var link = document.querySelector(sel);
        if (link && link.href) window.location.href = link.href;
    });
})();
