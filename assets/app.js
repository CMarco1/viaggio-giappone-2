/* Giappone 2026 — script condiviso. Nessuna dipendenza. */
(function () {
    'use strict';

    var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    /* ---- Data di oggi in formato AAAA-MM-GG, ora locale ---- */
    function isoToday() {
        var d = new Date();
        return d.getFullYear() + '-' +
               ('0' + (d.getMonth() + 1)).slice(-2) + '-' +
               ('0' + d.getDate()).slice(-2);
    }

    /* ---- Countdown alla partenza (solo in home) ---- */
    var box = document.getElementById('countdown');
    if (box) {
        var DEPARTURE = new Date(2026, 11, 2, 0, 0, 0);   /* 2 dicembre 2026 */
        var RETURN = new Date(2026, 11, 18, 23, 59, 59);  /* rientro a Roma */
        var now = new Date();
        var days = Math.ceil((DEPARTURE - now) / 86400000);
        var html = '';
        if (days > 1) {
            html = '<strong>' + days + '</strong><span>giorni alla partenza</span>';
        } else if (days === 1) {
            html = '<strong>Domani</strong><span>si parte!</span>';
        } else if (now <= RETURN) {
            html = '<strong>Giorno ' + (Math.floor((now - DEPARTURE) / 86400000) + 1) + '</strong><span>siete in Giappone 🎌</span>';
        }
        if (html) { box.innerHTML = html; box.hidden = false; }
    }

    /* ---- Evidenzia la giornata di oggi nella griglia della home ---- */
    var today = isoToday();
    var todayCard = document.querySelector('.daycard[data-date="' + today + '"]');
    if (todayCard) {
        todayCard.classList.add('is-today');
        var jump = document.getElementById('goToday');
        if (jump) {
            jump.href = todayCard.getAttribute('href');
            jump.hidden = false;
        }
    }

    /* ---- Striscia dei giorni: porta in vista quello corrente ---- */
    var strip = document.querySelector('.daystrip');
    if (strip) {
        var cur = strip.querySelector('[aria-current="page"]');
        if (cur) {
            var off = cur.offsetLeft - (strip.clientWidth / 2) + (cur.offsetWidth / 2);
            strip.scrollLeft = Math.max(0, off);
        }
        var chip = strip.querySelector('[data-date="' + today + '"]');
        if (chip) chip.classList.add('is-today');
    }

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
        if (t && (t.tagName === 'INPUT' || t.tagName === 'TEXTAREA' || t.isContentEditable)) return;
        var sel = e.key === 'ArrowLeft' ? '.dayfoot .prev' : (e.key === 'ArrowRight' ? '.dayfoot .next' : null);
        if (!sel) return;
        var link = document.querySelector(sel);
        if (link && link.href) window.location.href = link.href;
    });
})();
