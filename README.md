# Sito I&M Partners Commercialisti

Sito statico dello studio, pubblicato da Netlify su https://studioiempartners.it.
Ogni modifica a questo archivio viene ripubblicata automaticamente.

- `index.html`: il sito (tutte le sezioni)
- `novita.json`: notizie della sezione "Scadenze e novità", aggiornate ogni mattina feriale da un'attività programmata di Claude. Campi: `data` (AAAA-MM-GG), `tema`, `titolo`, `sintesi`, `fonte`, `url` (https). Il sito mostra le 12 più recenti.
- `assets/`, `fonts/`: immagini e caratteri, serviti dal sito stesso (nessuna chiamata a terzi).
- `netlify.toml`: impostazioni di pubblicazione.

Lo scadenzario non dipende da file: è calcolato nel browser sulla data del giorno.
