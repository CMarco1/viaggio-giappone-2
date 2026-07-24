import re

file_path = "/home/jupyter/giappone/viaggio-giappone-2/index.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

replacements = {
    "Ramen caldo per riprendersi dal jet lag. Una ciotola da Ichiran (dove mangiate nei cubicoli singoli) è perfetta per la prima sera.": "<strong>Fu-unji (Shinjuku):</strong> Famoso per il suo <em>Tsukemen</em> (ramen in cui i noodles vengono intinti a parte in un brodo denso). In alternativa, esplorate <strong>Omoide Yokocho</strong> per spiedini <em>Yakitori</em> annaffiati da birra ghiacciata.",
    
    "Melon pan appena sfornato e Ningyoyaki (dolcetti) lungo la strada dei templi. A cena, un ottimo Tonkatsu (maiale fritto).": "<strong>Asakusa Kagetsudo:</strong> Celebre per il suo <em>Jumbo Melon Pan</em> appena sfornato, croccante fuori e soffice dentro. A cena provate <strong>Asakusa Imahan</strong>, locale storico rinomato per il suo eccellente <em>Sukiyaki</em> (fettine di manzo cotte al tavolo).",

    "Curry giapponese piccante (es. Go! Go! Curry) perfetto per ricaricare le energie. Vivete l'esperienza super pop in un Maid Cafe come @Home Cafe.": "<strong>Go! Go! Curry (Akihabara):</strong> Ordinate il famoso <em>Katsu Curry</em> (riso al curry denso con cotoletta). Per un'esperienza a tema, provate l'omelette rice all'<strong>@Home Cafe</strong> (Maid Cafe) o la morbida cotoletta di manzo da <strong>Gyukatsu Motomura</strong>.",

    "Le famosissime e fotogeniche Crêpes ripiene di Takeshita Street e sushi al nastro a cena (Genki Sushi o Uobei).": "<strong>Marion Crepes (Harajuku):</strong> Tappa obbligata per le iconiche <em>Crêpes giapponesi</em> ripiene. A Shibuya, cenate da <strong>Uobei Shibuya Dogenzaka</strong> per un <em>Kaiten Sushi</em> dove i piatti arrivano sfrecciando su binari ad alta velocità.",

    "Fermatevi a mangiare nei piccoli Izakaya o nei ramen bar nascosti nelle stradine parallele fuori dal centro commerciale (Nakano Sunmall).": "<strong>Chuka Soba Aoba (Nakano):</strong> Un'istituzione del quartiere. Il loro piatto forte è il <em>Chuka Soba</em> (Ramen) con un doppio brodo stellare che unisce la ricchezza del maiale e del pollo al sapore delicato di pesce.",

    "Provate un Anime Cafe tematico o mangiate i famosi Taiyaki (dolcetti caldi a forma di pesce). Ottima zona per provare anche un BBQ coreano (Yakiniku).": "<strong>Mutekiya (Ikebukuro):</strong> Preparatevi alla fila, ma il loro <em>Tonkotsu Ramen</em> (brodo di maiale ricco e saporito) è leggendario. Per un dolce veloce, prendete un <em>Taiyaki</em> ai chioschi intorno a Sunshine City.",

    "L'Aqua City Odaiba ha numerosi ristoranti con vista sulla baia e sul Rainbow Bridge. Un piatto di Tempura o Soba guardando il mare è perfetto.": "<strong>Tsukiji Tama Sushi (Odaiba):</strong> Situato nel centro commerciale Decks, offre un'ottima formula <em>All-You-Can-Eat Sushi</em> di alta qualità con una vista mozzafiato sul Rainbow Bridge e sulla baia di Tokyo.",

    "La sera perdetevi nei vicoli di Pontocho, stracolmi di lanterne rosse e piccoli ristorantini che affacciano sul fiume. Ideale per un po' di Yakitori.": "<strong>Tsujiri (Gion):</strong> Ottimo per una merenda con il loro inimitabile <em>Parfait al Matcha</em>. Per cena, passeggiate a Pontocho e provate <strong>Kyoto Gion Mikaku</strong> (per la carne Wagyu sulla piastra) o un Izakaya sul fiume per spiedini <em>Yakitori</em>.",

    "Assaggiate i dolci al Matcha (gelato o parfait) e bevete tè caldo nelle tradizionali sale da tè di Sannenzaka.": "<strong>Okutan Kiyomizu:</strong> Ristorante centenario circondato da un giardino stupendo. Il piatto forte è lo <em>Yudofu</em> (tofu artigianale in brodo, perfetto per riscaldarsi). Lungo Ninenzaka, c'è uno <strong>Starbucks</strong> unico, ospitato in una casa tradizionale tatami.",

    "Street food! Provate il Tako Tamago (piccolo polpo con un uovo di quaglia dentro la testa), crocchette di tofu e gli spiedini di carne o pesce freschissimi.": "<strong>Mercato Nishiki:</strong> Cercate il chiosco <strong>Kari-Kari Hakase</strong> per i <em>Takoyaki</em> e <strong>Daiyasu</strong> per il famoso <em>Tako Tamago</em>. Vicino al museo, provate <strong>Gogyo Kyoto</strong> per il particolarissimo <em>Ramen al Miso Bruciato</em> (Kogashi Miso).",

    "La zona di Arashiyama è famosa per lo Yudofu (tofu bollito artigianale servito in un brodo delicatissimo), perfetto per scaldarsi.": "<strong>Arashiyama Yoshimura:</strong> Ristorante con magnifica vista sul fiume Katsura. Il loro piatto principale è la <em>Soba fatta a mano</em>. Per gli amanti del caffè, fate un salto da <strong>% Arabica Kyoto Arashiyama</strong>.",

    "Shinsekai è il paradiso del Kushikatsu: spiedini di carne e verdure impanati, fritti e immersi in una salsa dolce-salata. Una birra ghiacciata è d'obbligo.": "<strong>Kushikatsu Daruma (Shinsekai):</strong> L'inventore del <em>Kushikatsu</em>! Ordinate vassoi di spiedini fritti da intingere (una sola volta!) nella loro salsa segreta. Riconoscerete il locale dall'enorme statua dell'uomo arrabbiato all'ingresso.",

    "La capitale del cibo di strada! Takoyaki ustionanti (polpette di polpo) o un Okonomiyaki da cuocere sulla piastra davanti a voi (ad es. da Mizuno).": "<strong>Mizuno (Dotonbori):</strong> Un'istituzione per l'<em>Okonomiyaki</em> (premiata Michelin). Per i <em>Takoyaki</em>, mettetevi in fila da <strong>Acchichi Honpo</strong> (vicino al ponte) per polpette croccanti fuori e morbidissime dentro.",

    "Scegliete il vostro piatto preferito del viaggio e bissatelo! Oppure provate le sale sotterranee della stazione di Kyoto piene di ristorantini veloci e di alta qualità (Porta Dining).": "<strong>Katsukura (Kyoto Station):</strong> Situato all'11° piano dell'edificio The Cube. Serve uno dei migliori <em>Tonkatsu</em> (cotoletta di maiale impanata) di Kyoto. Potrete macinare voi stessi i semi di sesamo per la salsa di accompagnamento.",

    "Comprate un Ekiben (bento da stazione) preparato alla perfezione per mangiarlo durante il rilassante tragitto in treno verso l'aeroporto.": "<strong>551 Horai (Kansai Airport / Kyoto St.):</strong> Prima di partire, comprate i loro famosissimi <em>Butaman</em> (soffici panini al vapore ripieni di maiale e cipolla). Sono il comfort food perfetto per l'attesa o il tragitto in treno."
}

for old_str, new_str in replacements.items():
    if old_str in content:
        content = content.replace(old_str, new_str)
    else:
        print(f"Non trovato: {old_str[:50]}...")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Aggiornamento completato.")
