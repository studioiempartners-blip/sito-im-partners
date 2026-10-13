# Sito I&M Partners Commercialisti

Sito statico multipagina dello studio, pubblicato da Netlify su https://studioiempartners.it.
Ogni modifica al ramo `main` viene ripubblicata automaticamente.

## Come è fatto
- Le pagine HTML (`index.html`, `studio/`, `aree/…`, `professionisti/`, `scadenze/`, `strumenti/`, `contatti/`, `note-legali/`, `en/`, `404.html`, `grazie/`) e `assets/style.css` sono **generate** da `_sorgenti/build.py`: per modificare testi o struttura si interviene lì e si rilancia `python3 _sorgenti/build.py`.
- `assets/site.js`, `assets/scadenze.js`, `assets/strumenti.js`: comportamenti del sito, calendario delle scadenze, calcolatori.
- `novita.json`: notizie della sezione "Scadenze e novità", aggiornate ogni mattina feriale da un'attività programmata di Claude. Campi: `data` (AAAA-MM-GG), `tema`, `titolo`, `sintesi`, `fonte`, `url` (https). Il sito mostra le 12 più recenti. Il generatore non tocca questo file.
- `fonts/`, `assets/*.png`: caratteri e immagini serviti dal sito stesso (nessuna chiamata a terzi).
- Il modulo di contatto usa Netlify Forms (modulo "contatti").
- `netlify.toml`: intestazioni, cache e blocco della cartella `_sorgenti`.

Lo scadenzario non dipende da file: è calcolato nel browser sulla data del giorno.
