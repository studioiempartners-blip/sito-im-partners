#!/usr/bin/env python3
"""Genera il sito statico di I&M Partners nella radice dell'archivio.

Uso:  python3 _sorgenti/build.py
Le pagine, il foglio di stile e la mappa del sito vengono riscritti a ogni esecuzione.
novita.json non viene toccato: lo aggiorna l'attività programmata ogni mattina feriale.
"""
import json, os, pathlib, datetime

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / '_sorgenti'
SITE = 'https://studioiempartners.it'
OGG = datetime.date.today().isoformat()

STUDIO = 'I&amp;M Partners'
TEL1, TEL2 = '+39 331 700 7176', '+39 331 839 0268'
MAIL = 'studioiempartners@gmail.com'
PEC1, PEC2 = 'salvatore.iorio1@commercialistinapolinord.it', 'nazareno.mollichella@commercialistinapolinord.it'
PIVA = '04942040611'
SEDE = 'Via Filippo Saporito 58, 81031 Aversa (CE)'
TODO_DEN = '<span class="todo">denominazione completa e forma giuridica</span>'
TODO_TIT = '<span class="todo">denominazione e sede del titolare</span>'

def tel(n):
    return 'tel:' + n.replace(' ', '')

# ---------------------------------------------------------------- icone
ICON = {
 'fiscale': '<path d="M12 6h18l8 8v28H12z"/><path d="M30 6v8h8M18 22h14M18 29h14M18 36h8"/>',
 'societario': '<path d="M6 18 24 7l18 11M8 41h32M10 18h28"/><path d="M14 22v15M24 22v15M34 22v15"/>',
 'contabilita': '<path d="M8 8h32v32H8zM24 8v32M8 16h32"/><path d="M13 23h6M13 29h6M29 23h6M29 29h6M29 35h6"/>',
 'internazionale': '<circle cx="24" cy="24" r="17"/><path d="M7 24h34M24 7c-9 9-9 25 0 34M24 7c9 9 9 25 0 34"/>',
 'crisi': '<path d="M24 8v32M14 40h20M8 16h32"/><path d="M8 16 3 28h10zM40 16l-5 12h10z"/><path d="M3 28a5 5 0 0 0 10 0M35 28a5 5 0 0 0 10 0"/>',
}
def icon(k):
    return f'<svg viewBox="0 0 48 48" aria-hidden="true" fill="none">{ICON[k]}</svg>'

# ---------------------------------------------------------------- aree di attività
AREE = [
 dict(slug='fiscale-tributario', icon='fiscale', nome='Fiscale e tributario',
  breve="Dichiarazioni, imposte dirette e indirette, pianificazione e assistenza nei rapporti con l'Amministrazione finanziaria.",
  h1='Fiscale e tributario. <em>Prima, durante e dopo la dichiarazione.</em>',
  lead="Consulenza continuativa per società, imprese individuali, professionisti e persone fisiche: dalla pianificazione delle imposte agli adempimenti, fino all'assistenza quando l'Amministrazione finanziaria chiede chiarimenti.",
  desc="Consulenza fiscale e tributaria ad Aversa: dichiarazioni, IVA, regimi fiscali, ravvedimento, avvisi bonari, contraddittorio e contenzioso tributario.",
  gruppi=[
   ('Imposte e dichiarazioni', ["Dichiarazioni dei redditi di persone fisiche, società di persone e società di capitali", 'IRES, IRAP e imposte sostitutive', 'Modello 730 e Redditi Persone fisiche', 'IMU e tributi locali', "Certificazioni Uniche e modello 770 per i sostituti d'imposta"]),
   ('IVA', ['Liquidazioni periodiche e dichiarazione annuale', 'Fatturazione elettronica e corrispettivi telematici', 'Operazioni con l’estero, inversione contabile, esportatori abituali', 'Rimborsi e compensazioni dei crediti IVA']),
   ('Pianificazione', ['Scelta del regime fiscale: forfettario, semplificato, ordinario', "Agevolazioni e crediti d'imposta per le imprese", 'Concordato preventivo biennale: valutazione della proposta', "Interpelli all'Agenzia delle Entrate"]),
   ('Rapporti con il Fisco', ['Comunicazioni di irregolarità e avvisi bonari', 'Ravvedimento operoso', 'Verifiche, accessi e contraddittorio preventivo', 'Adesione, autotutela e assistenza nel contenzioso tributario']),
  ],
  faq=[
   ('Ho dimenticato un versamento o commesso un errore: posso rimediare?',
    ["Sì. Finché non sono stati notificati atti di liquidazione o di accertamento, comprese le comunicazioni di irregolarità, l'errore si può regolarizzare con il ravvedimento operoso: si versano l'imposta, gli interessi e una sanzione ridotta, tanto più bassa quanto prima si interviene.",
     'Conviene muoversi presto e verificare il calcolo prima di pagare, perché la riduzione della sanzione dipende dal momento in cui si regolarizza.'],
    'Art. 13 D.Lgs. 472/1997, come modificato dal D.Lgs. 87/2024'),
   ('Ho ricevuto una comunicazione di irregolarità (avviso bonario): cosa devo fare?',
    ["È l'esito del controllo automatizzato o formale della dichiarazione. Può derivare da un errore effettivo, ma anche da un dato non allineato o da un versamento non abbinato.",
     "Verifichiamo i conteggi: se la pretesa è corretta si paga con la sanzione ridotta, anche a rate; se non lo è, chiediamo all'Agenzia la correzione entro il termine indicato nella comunicazione."],
    'Art. 36-bis D.P.R. 600/1973 · Art. 54-bis D.P.R. 633/1972 · D.Lgs. 462/1997'),
   ('Che cos’è il contraddittorio preventivo?',
    ["Prima di emettere un atto impugnabile, l'Amministrazione finanziaria deve, salvo le eccezioni previste, comunicare al contribuente lo schema di atto e assegnargli un termine non inferiore a sessanta giorni per presentare osservazioni e accedere agli atti.",
     "È un passaggio decisivo: osservazioni documentate possono evitare l'accertamento o ridurne la portata."],
    'Art. 6-bis L. 212/2000 (Statuto dei diritti del contribuente), introdotto dal D.Lgs. 219/2023'),
   ('Quando conviene il regime forfettario?',
    ["Dipende dai ricavi attesi, dai costi effettivi, dai contributi e dalle cause di esclusione previste dalla legge. Il regime si applica con ricavi o compensi fino a 85.000 euro e prevede un'imposta sostitutiva del 15%, ridotta al 5% per i primi cinque anni di una nuova attività in presenza dei requisiti, su un reddito determinato con coefficienti di redditività.",
     'Per una prima stima è disponibile il <a href="/strumenti/#forfettario">simulatore del regime forfettario</a>.'],
    'Art. 1, commi 54-89, L. 190/2014'),
  ]),
 dict(slug='societario-operazioni-straordinarie', icon='societario', nome='Societario e operazioni straordinarie',
  breve='Costituzioni, riorganizzazioni, cessioni e acquisizioni d’azienda, valutazioni e due diligence.',
  h1='Società e operazioni straordinarie. <em>Le scelte che restano.</em>',
  lead="La forma giuridica, le regole tra soci, una cessione o una fusione producono effetti per anni. Le impostiamo valutando insieme gli aspetti civilistici, fiscali e contabili.",
  desc='Consulenza societaria ad Aversa: costituzione di società, statuti, cessione di quote, cessione e affitto d’azienda, fusioni, scissioni, valutazioni e due diligence.',
  gruppi=[
   ('Costituzione e governance', ['Scelta della forma giuridica e costituzione di società', 'Statuti, patti parasociali e regole di governance', 'Adeguati assetti organizzativi, amministrativi e contabili', 'Start-up e piccole e medie imprese innovative']),
   ('Operazioni straordinarie', ['Trasformazioni, fusioni e scissioni', 'Conferimenti di aziende e di partecipazioni', 'Cessione e affitto d’azienda', 'Liquidazione volontaria della società']),
   ('Partecipazioni e valutazioni', ['Cessione di quote di S.r.l. con atto a firma digitale', 'Valutazione d’azienda e perizie di stima', 'Due diligence contabile e fiscale', 'Passaggio generazionale dell’impresa']),
  ],
  faq=[
   ('S.r.l. o S.r.l. semplificata: che differenza c’è?',
    ["Entrambe sono società a responsabilità limitata e possono essere costituite anche con un capitale di un euro. La S.r.l. semplificata adotta però un atto costitutivo standard, che non si può personalizzare, e non comporta onorari notarili.",
     "La S.r.l. ordinaria consente uno statuto su misura: circolazione delle quote, amministrazione, diritti particolari dei soci. La scelta dipende da quanto le regole tra soci devono essere personalizzate."],
    'Artt. 2463 e 2463-bis c.c.'),
   ('La cessione di quote di S.r.l. deve passare dal notaio?',
    ["Non necessariamente. Oltre all'atto notarile, la legge consente di trasferire le quote con un atto sottoscritto con firma digitale dalle parti e depositato al Registro delle imprese da un commercialista iscritto nella sezione A dell'Albo."],
    'Art. 36, co. 1-bis, D.L. 112/2008 · Art. 2470 c.c.'),
   ('Cosa sono gli adeguati assetti organizzativi?',
    ["Il codice civile chiede all'imprenditore che opera in forma societaria o collettiva di dotarsi di un assetto organizzativo, amministrativo e contabile adeguato alla natura e alle dimensioni dell'impresa, anche per rilevare per tempo i segnali di crisi.",
     'In concreto: deleghe e responsabilità chiare, una contabilità aggiornata, strumenti di previsione dei flussi di cassa.'],
    'Art. 2086, co. 2, c.c. · Art. 3 D.Lgs. 14/2019'),
   ('Cessione d’azienda o cessione di quote?',
    ["Sono strade diverse. Nella cessione d'azienda vende la società, che trasferisce beni e rapporti; nella cessione di quote vendono i soci, e la società resta com'è, con la sua storia, i suoi debiti e i suoi rischi.",
     'Imposte, responsabilità per i debiti pregressi e tempi cambiano sensibilmente: la scelta va fatta dopo una verifica preliminare.'],
    'Artt. 2556-2560 c.c.'),
  ]),
 dict(slug='contabilita-bilanci', icon='contabilita', nome='Contabilità e bilanci',
  breve='Tenuta delle scritture, bilancio d’esercizio, situazioni periodiche e controllo di gestione.',
  h1='Contabilità e bilanci. <em>Numeri per decidere.</em>',
  lead="Una contabilità tenuta con metodo non serve solo agli adempimenti: è lo strumento con cui l'imprenditore capisce dove sta andando. Per questo i dati arrivano anche durante l'anno, non solo a bilancio chiuso.",
  desc='Contabilità e bilanci ad Aversa: contabilità ordinaria e semplificata, bilancio d’esercizio secondo i principi OIC, situazioni infrannuali, budget e controllo di gestione.',
  gruppi=[
   ('Contabilità', ['Contabilità ordinaria e semplificata', 'Registri IVA, cespiti e scritture di assestamento', 'Fatturazione elettronica e conservazione digitale', 'Riconciliazioni bancarie e scadenzario clienti e fornitori']),
   ('Bilancio', ['Bilancio d’esercizio ordinario, abbreviato e delle micro-imprese', 'Nota integrativa e relazione sulla gestione', 'Principi contabili nazionali OIC', 'Approvazione e deposito al Registro delle imprese']),
   ('Controllo di gestione', ['Situazioni contabili infrannuali', 'Budget, reporting e analisi degli scostamenti', 'Analisi di bilancio per indici e flussi di cassa', 'Rendiconti per banche e finanziatori']),
  ],
  faq=[
   ('Entro quando va approvato e depositato il bilancio?',
    ["L'assemblea approva il bilancio entro centoventi giorni dalla chiusura dell'esercizio, oppure entro centottanta giorni se lo statuto lo prevede e ricorrono le condizioni di legge. Entro trenta giorni dall'approvazione il bilancio va depositato al Registro delle imprese."],
    'Artt. 2364, 2435 e 2478-bis c.c.'),
   ('Contabilità semplificata o ordinaria?',
    ["Imprese individuali e società di persone possono tenere la contabilità semplificata se i ricavi dell'anno precedente non superano 500.000 euro per le attività di servizi o 800.000 euro per le altre attività; oltre queste soglie, o per scelta, si applica la contabilità ordinaria. Le società di capitali tengono sempre la contabilità ordinaria."],
    'Art. 18 D.P.R. 600/1973'),
   ('A cosa servono le situazioni contabili infrannuali?',
    ["Sono bilanci intermedi, di solito trimestrali o semestrali, che mostrano ricavi, costi, margini e liquidità durante l'anno. Servono a correggere la rotta in tempo, a stimare le imposte prima degli acconti e a dialogare con le banche su dati aggiornati."],
    None),
  ]),
 dict(slug='internazionalizzazione-gestione-societaria', icon='internazionale', nome='Internazionalizzazione e gestione societaria',
  breve='Fiscalità internazionale, presenza all’estero, segreteria societaria e adempimenti degli organi sociali.',
  h1='Internazionalizzazione <em>e gestione societaria.</em>',
  lead="Per le imprese che vendono, acquistano o si insediano all'estero, per le persone che si trasferiscono, e per chi vuole una società sempre in regola con assemblee, libri sociali e Registro delle imprese.",
  desc='Fiscalità internazionale e gestione societaria ad Aversa: residenza fiscale, doppie imposizioni, stabile organizzazione, IVA negli scambi con l’estero, impatriati, segreteria societaria.',
  gruppi=[
   ('Fiscalità internazionale', ['Residenza fiscale di persone e società', 'Convenzioni contro le doppie imposizioni e crediti per imposte estere', 'Stabile organizzazione e presenza all’estero', 'Prezzi di trasferimento e rapporti infragruppo']),
   ('IVA negli scambi con l’estero', ['Cessioni e acquisti intracomunitari, elenchi Intrastat', 'Esportazioni, importazioni e plafond', 'Identificazione IVA e rappresentanza fiscale di soggetti esteri', 'Servizi internazionali e regole di territorialità']),
   ('Persone che si trasferiscono', ['Rientro in Italia e regime per i lavoratori impatriati', 'Monitoraggio fiscale delle attività estere (quadro RW), IVIE e IVAFE', 'Redditi di fonte estera nella dichiarazione']),
   ('Gestione societaria', ['Segreteria societaria e tenuta dei libri sociali', 'Assemblee, verbali e rinnovo delle cariche', 'Pratiche presso il Registro delle imprese', 'Calendario degli adempimenti degli organi sociali']),
  ],
  faq=[
   ('Quando una persona è fiscalmente residente in Italia?',
    ["Dal 2024 è residente chi, per la maggior parte del periodo d'imposta, ha in Italia la residenza o il domicilio secondo il codice civile, inteso il domicilio come luogo in cui si sviluppano in via principale le relazioni personali e familiari, oppure vi è fisicamente presente. L'iscrizione anagrafica fa presumere la residenza, salvo prova contraria.",
     'Nei casi di doppia residenza si applicano i criteri della convenzione contro le doppie imposizioni.'],
    'Art. 2 TUIR, come modificato dal D.Lgs. 209/2023'),
   ('Una società estera che opera in Italia deve pagare le imposte qui?',
    ["Sì, se in Italia ha una stabile organizzazione: una sede fissa d'affari, come un ufficio o una filiale, o in determinati casi un soggetto che conclude abitualmente contratti per suo conto. La valutazione va fatta sulla base della legge italiana e della convenzione applicabile, prima di avviare l'attività."],
    'Art. 162 TUIR'),
   ('Chi rientra in Italia dall’estero ha agevolazioni?',
    ["Il regime per i lavoratori impatriati prevede, se ricorrono i requisiti di permanenza all'estero, di qualificazione e di residenza in Italia, che una parte del reddito di lavoro prodotto in Italia non concorra alla formazione del reddito imponibile, entro un limite annuo. Requisiti e misura vanno verificati prima del trasferimento."],
    'Art. 5 D.Lgs. 209/2023'),
  ]),
 dict(slug='crisi-sovraindebitamento', icon='crisi', nome='Crisi d’impresa e sovraindebitamento',
  breve='Prevenzione della crisi, composizione negoziata e procedure di sovraindebitamento per persone e piccole imprese.',
  h1='Crisi d’impresa e sovraindebitamento. <em>Affrontare i debiti con metodo.</em>',
  lead="Quando i debiti superano la capacità di pagarli, la legge offre strumenti per ristrutturarli o, in certi casi, per liberarsene. I professionisti dello studio sono iscritti al registro dei gestori della crisi da sovraindebitamento.",
  desc='Crisi d’impresa e sovraindebitamento ad Aversa: composizione negoziata, ristrutturazione dei debiti del consumatore, concordato minore, liquidazione controllata ed esdebitazione.',
  gruppi=[
   ('Prevenzione', ['Analisi della sostenibilità del debito e piani di tesoreria', 'Segnali di crisi e adeguati assetti', 'Rapporti con banche e fornitori nelle fasi di tensione finanziaria', 'Rateizzazioni e piani di rientro dei debiti tributari']),
   ('Imprese', ['Composizione negoziata della crisi', 'Accordi con i creditori e piani di risanamento', 'Valutazione degli strumenti di regolazione della crisi']),
   ('Persone, professionisti e piccole imprese', ['Ristrutturazione dei debiti del consumatore', 'Concordato minore', 'Liquidazione controllata', 'Esdebitazione']),
  ],
  extra=('Il ruolo del gestore della crisi',
   ["Nelle procedure di sovraindebitamento la domanda passa da un Organismo di composizione della crisi (OCC), che nomina un gestore. Il gestore esamina la documentazione, redige la relazione richiesta dalla legge e segue la procedura: una funzione terza rispetto al debitore e ai creditori.",
    "Per questo, nella stessa procedura, lo studio non assume insieme il ruolo di consulente del debitore e quello di gestore della crisi."]),
  faq=[
   ('Chi può accedere alle procedure di sovraindebitamento?',
    ["Consumatori, professionisti, imprenditori minori, imprenditori agricoli, start-up innovative e, in generale, i debitori che non possono accedere alla liquidazione giudiziale, quando si trovano in stato di crisi o di insolvenza.",
     "Lo strumento dipende dalla natura dei debiti: la ristrutturazione dei debiti del consumatore riguarda debiti estranei all'attività d'impresa o professionale; il concordato minore è riservato a chi esercita un'attività."],
    'Art. 2, co. 1, lett. c), artt. 67 ss. e 74 ss. D.Lgs. 14/2019'),
   ('Che cos’è l’esdebitazione?',
    ["È la liberazione dai debiti rimasti insoddisfatti al termine della procedura. Nella liquidazione controllata opera di diritto, decorso il periodo previsto dalla legge e in presenza dei requisiti.",
     "La persona fisica meritevole che non ha nulla da offrire ai creditori può chiedere l'esdebitazione del debitore incapiente, con l'obbligo di pagare se entro quattro anni sopravvengono utilità rilevanti."],
    'Artt. 282 e 283 D.Lgs. 14/2019'),
   ('Che cos’è la composizione negoziata della crisi?',
    ["È un percorso volontario e riservato per l'imprenditore che si trova in condizioni di squilibrio tali da rendere probabile la crisi o l'insolvenza, ma con prospettive di risanamento. Si avvia sulla piattaforma telematica delle Camere di commercio; un esperto indipendente agevola le trattative con i creditori."],
    'Artt. 12-25-undecies D.Lgs. 14/2019'),
  ]),
]

PER_CHI = [
 ('Imprese e società', "Dalla costituzione alla gestione ordinaria, fino alle operazioni straordinarie. Contabilità, bilancio e fiscalità seguiti da un unico interlocutore."),
 ('Professionisti e lavoratori autonomi', "Scelta del regime fiscale, adempimenti periodici, dichiarazioni e pianificazione dei versamenti nel corso dell'anno."),
 ('Imprese che operano con l’estero', "Scambi intracomunitari, esportazioni, presenza all'estero e rapporti infragruppo, con attenzione alle convenzioni contro le doppie imposizioni."),
 ('Persone e famiglie', "Dichiarazioni dei redditi, patrimoni all'estero, rientro in Italia e, quando i debiti diventano insostenibili, le procedure di sovraindebitamento."),
]

# ---------------------------------------------------------------- struttura comune
NAV = [('/studio/', 'Lo studio'), ('/aree/', 'Aree di attività'), ('/professionisti/', 'Professionisti'),
       ('/scadenze/', 'Scadenze e novità'), ('/strumenti/', 'Strumenti'), ('/contatti/', 'Contatti')]

FONTS_PRELOAD = ['bodoni-moda-latin-400-normal.woff2', 'barlow-latin-300-normal.woff2', 'barlow-condensed-latin-500-normal.woff2']

ORG = {
 '@context': 'https://schema.org', '@type': 'AccountingService', '@id': SITE + '/#studio',
 'name': 'I&M Partners Commercialisti', 'url': SITE + '/', 'logo': SITE + '/assets/logo.png', 'image': SITE + '/assets/og.png',
 'description': "Studio di dottori commercialisti ad Aversa: consulenza fiscale e tributaria, societaria, contabilità e bilanci, internazionalizzazione, crisi d'impresa e sovraindebitamento.",
 'telephone': TEL1.replace(' ', ''), 'email': MAIL, 'vatID': 'IT' + PIVA,
 'address': {'@type': 'PostalAddress', 'streetAddress': 'Via Filippo Saporito 58', 'postalCode': '81031', 'addressLocality': 'Aversa', 'addressRegion': 'CE', 'addressCountry': 'IT'},
 'areaServed': [{'@type': 'City', 'name': 'Aversa'}, {'@type': 'AdministrativeArea', 'name': 'Provincia di Caserta'}, {'@type': 'AdministrativeArea', 'name': 'Campania'}],
 'knowsLanguage': ['it', 'en'],
 'employee': [
   {'@type': 'Person', 'name': 'Salvatore Iorio', 'honorificPrefix': 'Dott.', 'jobTitle': 'Dottore Commercialista', 'url': SITE + '/professionisti/#iorio'},
   {'@type': 'Person', 'name': 'Nazareno Mollichella', 'honorificPrefix': 'Dott.', 'jobTitle': 'Dottore Commercialista', 'url': SITE + '/professionisti/#mollichella'}],
}

def ld(obj):
    return '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False).replace('</', '<\\/') + '</script>'

def crumbs_ld(items):
    return ld({'@context': 'https://schema.org', '@type': 'BreadcrumbList', 'itemListElement': [
        {'@type': 'ListItem', 'position': i + 1, 'name': n, 'item': SITE + p} for i, (p, n) in enumerate(items)]})

def crumbs(items):
    lis = ''.join(f'<li><a href="{p}">{n}</a></li>' if k < len(items) - 1 else f'<li aria-current="page">{n}</li>'
                  for k, (p, n) in enumerate(items))
    return f'<nav aria-label="Percorso"><ol class="crumbs">{lis}</ol></nav>'

def header(path, lang='it'):
    cur = ' aria-current="page"'
    nav = ''.join(f'<a href="{h}"{cur if path.startswith(h) else ""}>{t}</a>' for h, t in NAV)
    ov = ''.join(f'<li><a href="{h}">{t}</a></li>' for h, t in [('/', 'Home')] + NAV + [('/note-legali/', 'Note legali e privacy')])
    other = ('/', 'IT', 'Versione italiana') if lang == 'en' else ('/en/', 'EN', 'English version')
    return f'''<a class="skip" href="#contenuto">Vai al contenuto</a>
<header class="top">
  <div class="wrap">
    <a class="brand" href="/" aria-label="I&amp;M Partners Commercialisti, pagina iniziale"><img src="/assets/logo.png" alt="I&amp;M Partners Commercialisti" width="900" height="218"></a>
    <nav class="nav" aria-label="Sezioni del sito">{nav}</nav>
    <a class="lang" href="{other[0]}" hreflang="{other[1].lower()}" aria-label="{other[2]}">{other[1]}</a>
    <button class="menu-btn" id="menu-apri" type="button" aria-expanded="false" aria-controls="menu">Menu</button>
  </div>
</header>
<div class="ov" id="menu" hidden>
  <div class="ov-top"><img src="/assets/logo.png" alt="I&amp;M Partners Commercialisti" width="900" height="218"><button class="menu-btn" id="menu-chiudi" type="button">Chiudi</button></div>
  <nav aria-label="Menu"><ol>{ov}<li><a href="{other[0]}" hreflang="{other[1].lower()}">{other[2]}</a></li></ol></nav>
</div>'''

FOOTER = f'''<footer>
  <div class="wrap">
    <div class="col">
      <img class="fl" src="/assets/logo.png" alt="I&amp;M Partners Commercialisti" width="900" height="218" loading="lazy">
      <span>P. IVA {PIVA}</span>
      <span>{SEDE}</span>
      <span>Si riceve solo su appuntamento</span>
    </div>
    <div class="col">
      <a href="mailto:{MAIL}">{MAIL}</a>
      <a href="{tel(TEL1)}">{TEL1}</a>
      <a href="{tel(TEL2)}">{TEL2}</a>
    </div>
    <nav class="col fnav" aria-label="Menu secondario">
      {''.join(f'<a href="{h}">{t}</a>' for h, t in NAV)}
    </nav>
    <div class="col">
      <div class="ord"><img src="/assets/ordine.png" alt="" width="160" height="162" loading="lazy"><span>Iscritti all'Ordine dei Dottori Commercialisti e degli Esperti Contabili di Napoli Nord</span></div>
    </div>
  </div>
  <div class="fine">
    <div class="wrap">
      <span>© {datetime.date.today().year} {STUDIO}</span>
      <span><a href="/note-legali/">Note legali e privacy</a> · <a href="/en/" hreflang="en">English</a></span>
    </div>
  </div>
</footer>
<div class="dock"><a href="{tel(TEL1)}">Chiama</a><a class="alt" href="/contatti/#scrivici">Scrivici</a></div>'''

def page(path, title, desc, body, *, lang='it', scripts=(), head_extra='', vetrina=False, robots=None):
    canon = SITE + path
    fonts = ''.join(f'<link rel="preload" href="/fonts/{f}" as="font" type="font/woff2" crossorigin>' for f in FONTS_PRELOAD)
    vscript = ("<script>try{if(!sessionStorage.getItem('imp-v'))document.documentElement.classList.add('v-on')}"
               "catch(e){document.documentElement.classList.add('v-on')}</script>") if vetrina else ''
    alt = ''
    if path in ('/', '/en/'):
        alt = f'<link rel="alternate" hreflang="it" href="{SITE}/"><link rel="alternate" hreflang="en" href="{SITE}/en/"><link rel="alternate" hreflang="x-default" href="{SITE}/">'
    rob = f'<meta name="robots" content="{robots}">' if robots else ''
    js = ''.join(f'<script src="/assets/{s}" defer></script>' for s in ('site.js',) + tuple(scripts))
    return f'''<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
{rob}<link rel="canonical" href="{canon}">{alt}
<meta name="theme-color" content="#13131d">
<meta property="og:type" content="website">
<meta property="og:locale" content="{'en_GB' if lang == 'en' else 'it_IT'}">
<meta property="og:site_name" content="I&amp;M Partners Commercialisti">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{SITE}/assets/og.png">
<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/assets/favicon.png" type="image/png">
<link rel="apple-touch-icon" href="/assets/favicon.png">
{fonts}
<link rel="stylesheet" href="/assets/style.css">
{vscript}{head_extra}{js}
</head>
<body>
{header(path, lang)}
<main id="contenuto">
{body}
</main>
{FOOTER}
</body>
</html>
'''

def faq_html(faq, h2=True):
    out = []
    for q, ans, norma in faq:
        ps = ''.join(f'<p>{a}</p>' for a in ans)
        nr = f'<p class="norma"><b>Riferimenti</b> · {norma}</p>' if norma else ''
        out.append(f'<details><summary>{q}<span class="pm" aria-hidden="true"></span></summary><div class="ans">{ps}{nr}</div></details>')
    return '<div class="faq">' + ''.join(out) + '</div>'

def faq_ld(faq):
    import re
    strip = lambda s: re.sub('<[^>]+>', '', s)
    return ld({'@context': 'https://schema.org', '@type': 'FAQPage', 'mainEntity': [
        {'@type': 'Question', 'name': strip(q), 'acceptedAnswer': {'@type': 'Answer', 'text': strip(' '.join(a))}} for q, a, _ in faq]})

CLOSING = '''<section class="sec">
  <div class="wrap closing">
    <h2>Il primo passo è <em>una conversazione.</em></h2>
    <p class="soft">Lo studio riceve solo su appuntamento, in via Filippo Saporito 58 ad Aversa. Scrivici o telefona per fissare un incontro.</p>
    <div class="row"><a class="cta" href="/contatti/">Richiedi un incontro</a><a class="cta ghost" href="{tel}">Chiama lo studio</a></div>
  </div>
</section>'''.replace('{tel}', tel(TEL1))

# ---------------------------------------------------------------- pagine
pages = {}

def card(a):
    return f'''<a class="card" href="/aree/{a['slug']}/">
          {icon(a['icon'])}
          <h3>{a['nome']}</h3>
          <p class="soft">{a['breve']}</p>
          <span class="more">Approfondisci <i>→</i></span>
        </a>'''

# --- home
home = f'''
<div class="vetrina" id="vetrina" role="dialog" aria-modal="true" aria-label="I&amp;M Partners Commercialisti">
  <div class="v-in">
    <img class="v-logo" src="/assets/logo.png" alt="I&amp;M Partners Commercialisti" width="900" height="218">
    <span class="v-rule" aria-hidden="true"></span>
    <div class="v-ord">
      <img src="/assets/ordine.png" alt="" width="160" height="162">
      <span>Ordine dei Dottori Commercialisti<br>e degli Esperti Contabili di Napoli Nord</span>
    </div>
    <button class="v-btn" id="entra" type="button">Entra</button>
  </div>
</div>

<section class="sec hero">
  <div class="amp" aria-hidden="true">&amp;</div>
  <div class="wrap stack">
    <p class="label">{STUDIO} · Dottori commercialisti in Aversa</p>
    <div class="slides" id="slides" aria-live="polite">
      <div class="slide on">
        <h1>«Dove non è ordine,<br><em>ivi è confusione.»</em></h1>
        <p class="cite">Luca Pacioli, <i>Summa de arithmetica</i>, 1494 · «ubi non est ordo, ibi est confusio»</p>
        <p class="lead">Lo scrisse il frate che per primo descrisse la partita doppia. È ancora il nostro mestiere: mettere ordine nei conti, nelle società e negli adempimenti.</p>
      </div>
      <div class="slide">
        <p class="hx">Fisco, società e bilanci.<br><em>Con un interlocutore diretto.</em></p>
        <p class="lead">Ogni cliente ha un professionista di riferimento, che conosce la sua storia e segue la pratica dall'inizio alla fine.</p>
      </div>
      <div class="slide">
        <p class="hx">Dal primo incontro<br><em>all'affiancamento.</em></p>
        <p class="lead">Analisi della situazione, incarico scritto, scadenze pianificate: un percorso chiaro per imprese, società, professionisti e famiglie.</p>
      </div>
    </div>
    <div class="row">
      <a class="cta" href="/contatti/">Richiedi un incontro</a>
      <a class="cta ghost" href="/aree/">Aree di attività</a>
    </div>
    <div class="sl-nav">
      <button class="sl-b" id="sl-prev" type="button" aria-label="Messaggio precedente">←</button>
      <span class="sl-c" id="sl-c">1 / 3</span>
      <button class="sl-b" id="sl-next" type="button" aria-label="Messaggio successivo">→</button>
    </div>
  </div>
</section>

<section class="next">
  <div class="wrap">
    <a class="nx" href="/scadenze/">
      <span class="label">Prossima scadenza</span>
      <span class="nx-d" id="nx-d"></span>
      <span class="nx-t" id="nx-t">Calendario delle scadenze fiscali</span>
      <span class="nx-c" id="nx-c"></span>
      <span class="go" aria-hidden="true">→</span>
    </a>
  </div>
</section>

<section class="sec">
  <div class="wrap split even">
    <div class="stack">
      <p class="label">Chi siamo</p>
      <h2>Uno studio raccolto, <em>due firme.</em></h2>
      <p>{STUDIO} è lo studio dei dottori commercialisti Salvatore Iorio e Nazareno Mollichella. Assistiamo imprese, società, professionisti e famiglie nella gestione fiscale, societaria e contabile, in Italia e nei rapporti con l'estero.</p>
      <p class="soft">Ogni incarico è seguito personalmente da un professionista dello studio, dall'analisi iniziale fino all'adempimento. Il cliente sa sempre con chi parla e a che punto è la sua pratica.</p>
      <a class="cta ghost" href="/studio/">Conosci lo studio</a>
    </div>
    <dl class="ledger">
      <div class="lh"><span>Scheda dello studio</span><span>I&amp;M</span></div>
      <div><dt>Sede</dt><dd>Aversa, via Filippo Saporito 58</dd></div>
      <div><dt>Professionisti</dt><dd>Iorio <em>&amp;</em> Mollichella</dd></div>
      <div><dt>Albo</dt><dd>ODCEC Napoli Nord, sezione A</dd></div>
      <div><dt>Registri</dt><dd>Gestori della crisi da sovraindebitamento</dd></div>
      <div><dt>Lingue</dt><dd>Italiano · English</dd></div>
      <div><dt>Ricevimento</dt><dd>Solo su appuntamento</dd></div>
    </dl>
  </div>
</section>

<section class="sec band">
  <div class="wrap">
    <p class="quote wide">Radicati ad Aversa, al fianco di imprese che guardano <em>oltre i confini.</em></p>
  </div>
</section>

<section class="sec">
  <div class="wrap stack" style="gap:40px">
    <div class="stack">
      <p class="label">Aree di attività</p>
      <h2>Cinque aree, <em>un solo interlocutore.</em></h2>
    </div>
    <div class="cards">
      {''.join(card(a) for a in AREE)}
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap stack" style="gap:40px">
    <div class="stack">
      <p class="label">Per chi lavoriamo</p>
      <h2>Imprese, professionisti, <em>persone.</em></h2>
    </div>
    <div class="grid4">
      {''.join(f'<article class="pr"><h3>{t}</h3><p class="soft">{x}</p></article>' for t, x in PER_CHI)}
    </div>
  </div>
</section>

<section class="sec band">
  <div class="wrap duo">
    <div class="stack">
      <p class="label">Prossime scadenze</p>
      <ul class="mini" id="mini-scad"><li><span class="d"></span><div><h3>Calendario delle scadenze fiscali</h3><p>Ricalcolato a ogni visita sulla data del giorno.</p></div></li></ul>
      <a class="morelink" href="/scadenze/">Tutte le scadenze</a>
    </div>
    <div class="stack">
      <p class="label">Ultime novità</p>
      <ul class="mini" id="mini-nov"><li><span class="d"></span><div><h3>Novità fiscali e normative</h3><p>Aggiornate ogni mattina dei giorni feriali.</p></div></li></ul>
      <a class="morelink" href="/scadenze/#novita">Tutte le novità</a>
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap split">
    <div class="stack">
      <p class="label">Strumenti</p>
      <h2>Fare due conti, <em>prima di decidere.</em></h2>
    </div>
    <div class="stack">
      <p class="soft">Due calcolatori per una prima stima: l'IRPEF lorda con gli scaglioni in vigore dal 2026 e l'imposta sostitutiva del regime forfettario. I dati restano nel browser e non vengono inviati a nessuno.</p>
      <div class="row"><a class="cta ghost" href="/strumenti/#irpef">Calcolo IRPEF 2026</a><a class="cta ghost" href="/strumenti/#forfettario">Simulatore forfettario</a></div>
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap stack" style="gap:40px">
    <div class="stack">
      <p class="label">I professionisti</p>
      <h2>Iorio <em>&amp;</em> Mollichella.</h2>
    </div>
    <div class="people">
      <a class="person link" href="/professionisti/#iorio">
        <span class="ini" aria-hidden="true">I</span>
        <h3>Dott. Salvatore Iorio</h3>
        <p class="soft">Dottore Commercialista · ODCEC Napoli Nord n. 1849A</p>
        <span class="more">Profilo <i>→</i></span>
      </a>
      <a class="person link" href="/professionisti/#mollichella">
        <span class="ini" aria-hidden="true">M</span>
        <h3>Dott. Nazareno Mollichella</h3>
        <p class="soft">Dottore Commercialista · ODCEC Napoli Nord n. 1860A</p>
        <span class="more">Profilo <i>→</i></span>
      </a>
    </div>
  </div>
</section>
{CLOSING}
'''
pages['/'] = page('/', 'I&amp;M Partners · Dottori commercialisti ad Aversa',
    "Studio di dottori commercialisti ad Aversa: consulenza fiscale e tributaria, societaria, contabilità e bilanci, internazionalizzazione, crisi d'impresa e sovraindebitamento.",
    home, scripts=('scadenze.js',), vetrina=True, head_extra=ld(ORG))

# --- studio
studio = f'''
<section class="sec">
  <div class="wrap ph">
    {crumbs([('/', 'Home'), ('/studio/', 'Lo studio')])}
    <p class="label">Lo studio</p>
    <h1>Uno studio <em>a misura di cliente.</em></h1>
    <p class="lead">{STUDIO} nasce dall'incontro di due commercialisti, Salvatore Iorio e Nazareno Mollichella, e da una convinzione semplice: chi affida a uno studio i conti della propria impresa deve poter parlare con chi quei conti li conosce davvero.</p>
    <p class="soft" style="max-width:62ch">Per questo abbiamo scelto una dimensione raccolta. Ogni cliente ha un professionista di riferimento, che conosce la sua storia, segue la pratica dall'inizio alla fine e risponde in prima persona. Fisco, società e bilanci vengono letti insieme, perché insieme producono i loro effetti.</p>
  </div>
</section>
<section class="sec band">
  <div class="wrap"><p class="quote">Dietro ogni bilancio c'è una storia d'impresa. Il nostro lavoro comincia da lì, <em>prima dei numeri.</em></p></div>
</section>
<section class="sec">
  <div class="wrap stack" style="gap:40px">
    <div class="stack"><p class="label">Cosa ci guida</p><h2>Quattro impegni, <em>presi sul serio.</em></h2></div>
    <div class="grid2">
      <article class="pr"><h3>Ascolto</h3><p class="soft">Il primo incontro serve a capire l'attività, le persone e gli obiettivi. Le soluzioni vengono dopo, e sono costruite su quella specifica situazione.</p></article>
      <article class="pr"><h3>Chiarezza</h3><p class="soft">Spieghiamo norme e scelte con parole comprensibili e mettiamo per iscritto ciò che conta: incarico, compenso, scadenze.</p></article>
      <article class="pr"><h3>Metodo</h3><p class="soft">Versamenti, dichiarazioni e depositi sono pianificati in anticipo. Il cliente riceve per tempo ciò che deve firmare, pagare o trasmettere.</p></article>
      <article class="pr"><h3>Riservatezza</h3><p class="soft">Le informazioni affidate allo studio sono coperte dal segreto professionale e trattate nel rispetto della normativa sulla protezione dei dati personali.</p></article>
    </div>
  </div>
</section>
<section class="sec">
  <div class="wrap stack" style="gap:40px">
    <div class="stack"><p class="label">A chi ci rivolgiamo</p><h2>Imprese, professionisti, <em>persone.</em></h2></div>
    <div class="grid4">
      {''.join(f'<article class="pr"><h3>{t}</h3><p class="soft">{x}</p></article>' for t, x in PER_CHI)}
    </div>
  </div>
</section>
<section class="sec">
  <div class="wrap split">
    <div class="stack"><p class="label">Il percorso</p><h2>Dal primo incontro <em>all'affiancamento.</em></h2></div>
    <ol class="steps">
      <li><span class="n" aria-hidden="true">1</span><div class="stack" style="gap:8px"><h3>Primo incontro</h3><p class="soft">Su appuntamento, nella sede di Aversa. Raccogliamo documenti, domande e obiettivi.</p></div></li>
      <li><span class="n" aria-hidden="true">2</span><div class="stack" style="gap:8px"><h3>Analisi</h3><p class="soft">Esaminiamo la posizione fiscale, societaria e contabile e indichiamo criticità e possibili interventi.</p></div></li>
      <li><span class="n" aria-hidden="true">3</span><div class="stack" style="gap:8px"><h3>Incarico scritto</h3><p class="soft">Attività, grado di complessità e compenso sono comunicati prima, per iscritto, come previsto dall'art. 9, comma 4, del D.L. 1/2012.</p></div></li>
      <li><span class="n" aria-hidden="true">4</span><div class="stack" style="gap:8px"><h3>Affiancamento</h3><p class="soft">Seguiamo gli adempimenti durante l'anno e aggiorniamo il cliente sulle novità che lo riguardano.</p></div></li>
    </ol>
  </div>
</section>
{CLOSING}
'''
pages['/studio/'] = page('/studio/', 'Lo studio · I&amp;M Partners Commercialisti, Aversa',
    "Lo studio dei dottori commercialisti Salvatore Iorio e Nazareno Mollichella ad Aversa: un professionista di riferimento per ogni cliente, incarico scritto, adempimenti pianificati.",
    studio, head_extra=crumbs_ld([('/', 'Home'), ('/studio/', 'Lo studio')]))

# --- indice aree
aree_idx = f'''
<section class="sec">
  <div class="wrap ph">
    {crumbs([('/', 'Home'), ('/aree/', 'Aree di attività')])}
    <p class="label">Aree di attività</p>
    <h1>Cinque aree, <em>una visione d'insieme.</em></h1>
    <p class="lead">Le scelte fiscali, societarie e contabili si influenzano a vicenda. Per questo lo studio le segue insieme, con un professionista di riferimento per ogni cliente.</p>
  </div>
  <div class="wrap" style="margin-top:56px">
    <ol class="arealist">
      {''.join(f'<li><a href="/aree/{a["slug"]}/"><h2>{a["nome"]}</h2><p>{a["breve"]}</p><span class="go" aria-hidden="true">→</span></a></li>' for a in AREE)}
    </ol>
  </div>
</section>
{CLOSING}
'''
pages['/aree/'] = page('/aree/', 'Aree di attività · I&amp;M Partners Commercialisti, Aversa',
    "Le aree di attività dello studio: fiscale e tributario, societario e operazioni straordinarie, contabilità e bilanci, internazionalizzazione, crisi d'impresa e sovraindebitamento.",
    aree_idx, head_extra=crumbs_ld([('/', 'Home'), ('/aree/', 'Aree di attività')]))

# --- pagine delle aree
for a in AREE:
    p = f"/aree/{a['slug']}/"
    cr = [('/', 'Home'), ('/aree/', 'Aree di attività'), (p, a['nome'])]
    gruppi = ''.join(f'<div class="blk"><h3>{t}</h3><ul class="ticks">{"".join(f"<li>{x}</li>" for x in items)}</ul></div>' for t, items in a['gruppi'])
    extra = ''
    if a.get('extra'):
        t, ps = a['extra']
        extra = f'''<section class="sec band"><div class="wrap split"><div class="stack"><p class="label">Da sapere</p><h2>{t}</h2></div><div class="prose">{''.join(f'<p>{x}</p>' for x in ps)}</div></div></section>'''
    rel = ''.join(f'<a href="/aree/{b["slug"]}/">{b["nome"]} <i>→</i></a>' for b in AREE if b is not a)
    body = f'''
<section class="sec">
  <div class="wrap ph">
    {crumbs(cr)}
    <p class="label">Area di attività</p>
    <h1>{a['h1']}</h1>
    <p class="lead">{a['lead']}</p>
    <div class="row"><a class="cta" href="/contatti/?area={a['slug']}#scrivici">Richiedi un incontro</a><a class="cta ghost" href="#domande">Domande frequenti</a></div>
  </div>
</section>
<section class="sec">
  <div class="wrap stack" style="gap:40px">
    <div class="stack"><p class="label">Cosa facciamo</p><h2>Le attività <em>dell'area.</em></h2></div>
    <div class="grid-svc">{gruppi}</div>
  </div>
</section>
{extra}
<section class="sec" id="domande">
  <div class="wrap split">
    <div class="stack"><p class="label">Domande frequenti</p><h2>Risposte <em>brevi.</em></h2><p class="soft" style="font-size:15px">Indicazioni generali, aggiornate al {datetime.date.today().strftime('%d/%m/%Y')}: non sostituiscono l'esame del caso concreto.</p></div>
    {faq_html(a['faq'])}
  </div>
</section>
<section class="sec">
  <div class="wrap stack" style="gap:28px">
    <p class="label">Altre aree</p>
    <div class="rel">{rel}</div>
  </div>
</section>
{CLOSING}
'''
    pages[p] = page(p, f"{a['nome']} · I&amp;M Partners Commercialisti, Aversa", a['desc'], body,
                    head_extra=crumbs_ld(cr) + faq_ld(a['faq']))

# --- professionisti
def prof(id_, ini, nome, num):
    return f'''<article class="prof" id="{id_}">
      <div class="stack" style="gap:14px"><span class="ini" aria-hidden="true">{ini}</span><h2>{nome}</h2><p class="label">Dottore Commercialista</p></div>
      <dl class="facts">
        <div><dt>Albo</dt><dd>Ordine dei Dottori Commercialisti e degli Esperti Contabili di Napoli Nord, sezione A, n. {num}</dd></div>
        <div><dt>Formazione</dt><dd>Laurea con lode, Facoltà di Economia dell'Università degli Studi della Campania «Luigi Vanvitelli»</dd></div>
        <div><dt>Registri</dt><dd>Iscritto al registro dei gestori della crisi da sovraindebitamento</dd></div>
        <div><dt>Aree</dt><dd>Fiscale e tributario · Societario · Contabilità e bilanci · Internazionalizzazione · Crisi e sovraindebitamento</dd></div>
        <div><dt>Contatti</dt><dd><a href="/contatti/">Tramite la segreteria dello studio</a></dd></div>
      </dl>
    </article>'''
profs = f'''
<section class="sec">
  <div class="wrap ph">
    {crumbs([('/', 'Home'), ('/professionisti/', 'Professionisti')])}
    <p class="label">Professionisti</p>
    <h1>Iorio <em>&amp;</em> Mollichella.</h1>
    <p class="lead">Due dottori commercialisti iscritti all'Ordine di Napoli Nord. Ogni cliente ha uno dei due come professionista di riferimento, che segue personalmente la pratica.</p>
  </div>
  <div class="wrap" style="margin-top:56px">
    {prof('iorio', 'I', 'Dott. Salvatore Iorio', '1849A')}
    {prof('mollichella', 'M', 'Dott. Nazareno Mollichella', '1860A')}
  </div>
</section>
{CLOSING}
'''
pages['/professionisti/'] = page('/professionisti/', 'Professionisti · I&amp;M Partners Commercialisti, Aversa',
    "Dott. Salvatore Iorio e Dott. Nazareno Mollichella, dottori commercialisti iscritti all'ODCEC di Napoli Nord e al registro dei gestori della crisi da sovraindebitamento.",
    profs, head_extra=crumbs_ld([('/', 'Home'), ('/professionisti/', 'Professionisti')]))

# --- scadenze e novità
scad = f'''
<section class="sec">
  <div class="wrap ph">
    {crumbs([('/', 'Home'), ('/scadenze/', 'Scadenze e novità')])}
    <p class="label">Scadenze e novità</p>
    <h1>Il calendario <em>del contribuente.</em></h1>
    <p class="lead">Le prossime scadenze fiscali e contributive, ricalcolate a ogni visita sulla data del giorno, e le novità di interesse per imprese e professionisti, aggiornate ogni mattina dei giorni feriali.</p>
  </div>
  <div class="wrap stack" style="margin-top:48px;gap:28px">
    <div class="chips" role="group" aria-label="Filtra le scadenze">
      <button class="chip" type="button" data-f="tutte" aria-pressed="true">Tutte</button>
      <button class="chip" type="button" data-f="versamenti" aria-pressed="false">Versamenti</button>
      <button class="chip" type="button" data-f="iva" aria-pressed="false">IVA</button>
      <button class="chip" type="button" data-f="dichiarazioni" aria-pressed="false">Dichiarazioni</button>
      <button class="chip" type="button" data-f="lavoro" aria-pressed="false">Lavoro e previdenza</button>
    </div>
    <ol class="cal" id="cal" aria-live="polite"><li><div class="dt"></div><div class="its"><p class="soft">Il calendario richiede JavaScript attivo. Puoi consultare lo <a href="https://www1.agenziaentrate.gov.it/servizi/scadenzario/main.php" target="_blank" rel="noopener">scadenzario dell'Agenzia delle Entrate</a>.</p></div></li></ol>
    <p class="note">Calendario ordinario delle scadenze ricorrenti. I termini che cadono di sabato o in un giorno festivo sono riportati al primo giorno lavorativo successivo (art. 7, co. 1, lett. h, D.L. 70/2011); quelli compresi tra il 1° e il 20 agosto sono riportati al 20 agosto (art. 37, co. 11-bis, D.L. 223/2006). Il calendario non tiene conto di proroghe, festività locali e termini particolari: fa fede lo <a href="https://www1.agenziaentrate.gov.it/servizi/scadenzario/main.php" target="_blank" rel="noopener">scadenzario dell'Agenzia delle Entrate</a>.</p>
  </div>
</section>
<section class="sec" id="novita">
  <div class="wrap split">
    <div class="stack">
      <p class="label">Novità</p>
      <h2>Prassi, norme <em>e sentenze.</em></h2>
      <p class="soft">Provvedimenti, circolari, decreti e pronunce di interesse per imprese e professionisti, con rinvio alla fonte. Selezione aggiornata ogni mattina dei giorni feriali.</p>
    </div>
    <div class="news" id="nov"><p class="soft" id="nov-vuoto">Caricamento delle novità…</p></div>
  </div>
</section>
{CLOSING}
'''
pages['/scadenze/'] = page('/scadenze/', 'Scadenze fiscali e novità · I&amp;M Partners Commercialisti',
    "Calendario delle prossime scadenze fiscali e contributive (F24, IVA, dichiarazioni, INPS) con i riferimenti normativi, e novità fiscali aggiornate ogni giorno feriale.",
    scad, scripts=('scadenze.js',), head_extra=crumbs_ld([('/', 'Home'), ('/scadenze/', 'Scadenze e novità')]))

# --- strumenti
GRUPPI_FORF = [
 ('0.40', "Industrie alimentari e delle bevande · Commercio all'ingrosso e al dettaglio · Commercio ambulante di prodotti alimentari · Alloggio e ristorazione", '40%'),
 ('0.54', 'Commercio ambulante di altri prodotti', '54%'),
 ('0.62', 'Intermediari del commercio', '62%'),
 ('0.67', 'Altre attività economiche', '67%'),
 ('0.78', 'Attività professionali, scientifiche, tecniche, sanitarie, di istruzione, servizi finanziari e assicurativi', '78%'),
 ('0.86', 'Costruzioni e attività immobiliari', '86%'),
]
opts = ''.join(f'<option value="{v}"{" selected" if v == "0.78" else ""}>{p} · {t}</option>' for v, t, p in GRUPPI_FORF)
link_utili = [('https://www.agenziaentrate.gov.it', 'Agenzia delle Entrate'), ('https://www.inps.it', 'INPS'), ('https://www.inail.it', 'INAIL'),
              ('https://www.registroimprese.it', 'Registro delle imprese'), ('https://www.adm.gov.it', 'Agenzia delle Dogane e dei Monopoli'),
              ('https://www.normattiva.it', 'Normattiva'), ('https://www.commercialisti.it', 'Consiglio Nazionale dei Commercialisti'),
              ('https://composizionenegoziata.camcom.it', 'Composizione negoziata della crisi')]
strum = f'''
<section class="sec">
  <div class="wrap ph">
    {crumbs([('/', 'Home'), ('/strumenti/', 'Strumenti')])}
    <p class="label">Strumenti</p>
    <h1>Fare due conti, <em>prima di decidere.</em></h1>
    <p class="lead">Calcolatori per una prima stima. I valori inseriti restano nel tuo browser: non vengono inviati né conservati.</p>
  </div>
</section>

<section class="sec" id="irpef">
  <div class="wrap stack" style="gap:30px">
    <div class="stack"><p class="label">Calcolo IRPEF 2026</p><h2>Imposta lorda <em>per scaglioni.</em></h2></div>
    <div class="tool">
      <form class="form" id="f-irpef" novalidate>
        <label for="i-reddito">Reddito complessivo imponibile (€)</label>
        <input id="i-reddito" type="number" inputmode="decimal" min="0" step="100" value="40000">
        <p class="note" style="margin-top:18px">Reddito al netto degli oneri deducibili. Scaglioni dell'art. 11, co. 1, TUIR, come modificato dall'art. 1, co. 3, L. 30 dicembre 2025, n. 199 (23% fino a 28.000 €, 33% fino a 50.000 €, 43% oltre).</p>
      </form>
      <div class="res" aria-live="polite">
        <div><p class="label">Imposta lorda</p><p class="big" id="i-out">–</p></div>
        <p class="soft">Aliquota media <b id="i-media">–</b> · aliquota marginale <b id="i-marg">–</b></p>
        <table class="tab"><thead><tr><th>Scaglione</th><th class="n">Aliquota</th><th class="n">Reddito</th><th class="n">Imposta</th></tr></thead><tbody id="i-tab"></tbody></table>
        <p class="warn" id="i-200" hidden>Con reddito complessivo oltre 200.000 € alcune detrazioni sono ridotte di 440 € (art. 16-ter, co. 5-ter, TUIR, introdotto dall'art. 1, co. 4, L. 199/2025).</p>
        <p class="note">Imposta lorda prima delle detrazioni per lavoro, carichi di famiglia e oneri (artt. 12-16 TUIR) e senza le addizionali regionale e comunale.</p>
      </div>
    </div>
  </div>
</section>

<section class="sec" id="forfettario">
  <div class="wrap stack" style="gap:30px">
    <div class="stack"><p class="label">Simulatore regime forfettario</p><h2>Imposta sostitutiva <em>stimata.</em></h2></div>
    <div class="tool">
      <form class="form" id="f-forf" novalidate>
        <label for="f-ricavi">Ricavi o compensi incassati nell'anno (€)</label>
        <input id="f-ricavi" type="number" inputmode="decimal" min="0" step="100" value="40000">
        <label for="f-gruppo">Attività e coefficiente di redditività</label>
        <select id="f-gruppo">{opts}</select>
        <label for="f-contributi">Contributi previdenziali obbligatori versati nell'anno (€)</label>
        <input id="f-contributi" type="number" inputmode="decimal" min="0" step="50" value="0">
        <fieldset style="border:0;padding:0;margin:12px 0 0"><legend class="label" style="color:var(--mute);font-size:14px">Aliquota</legend>
          <div class="radios">
            <label><input type="radio" name="aliq" value="0.15" checked> 15% · aliquota ordinaria</label>
            <label><input type="radio" name="aliq" value="0.05"> 5% · nuova attività, primi cinque anni, se ricorrono i requisiti del co. 65</label>
          </div>
        </fieldset>
      </form>
      <div class="res" aria-live="polite">
        <div><p class="label">Imposta sostitutiva</p><p class="big" id="f-out">–</p></div>
        <p class="soft">Incidenza sui ricavi <b id="f-carico">–</b></p>
        <table class="tab"><tbody id="f-tab"></tbody></table>
        <p class="warn" id="f-warn" hidden></p>
        <p class="note">Coefficienti dell'allegato 4 alla L. 190/2014; contributi deducibili ai sensi del co. 64. La stima non comprende i contributi dovuti sul reddito, né verifica requisiti e cause di esclusione del regime (co. 54 e 57).</p>
      </div>
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap split">
    <div class="stack"><p class="label">Link utili</p><h2>Siti <em>istituzionali.</em></h2></div>
    <ul class="links">{''.join(f'<li><a href="{u}" target="_blank" rel="noopener">{t} <i>↗</i></a></li>' for u, t in link_utili)}</ul>
  </div>
</section>
<section class="sec">
  <div class="wrap"><p class="note">Le stime hanno valore orientativo e non costituiscono consulenza: il risultato dipende da elementi che il calcolatore non considera. Per una valutazione sul caso concreto, <a href="/contatti/">contatta lo studio</a>.</p></div>
</section>
'''
pages['/strumenti/'] = page('/strumenti/', 'Calcolo IRPEF 2026 e simulatore forfettario · I&amp;M Partners',
    "Calcolatori online: IRPEF lorda 2026 con i nuovi scaglioni (23%, 33%, 43%) e simulatore dell'imposta sostitutiva del regime forfettario.",
    strum, scripts=('strumenti.js',), head_extra=crumbs_ld([('/', 'Home'), ('/strumenti/', 'Strumenti')]))

# --- contatti
area_opts = ''.join(f'<option value="{a["slug"]}">{a["nome"]}</option>' for a in AREE)
cont = f'''
<section class="sec">
  <div class="wrap ph">
    {crumbs([('/', 'Home'), ('/contatti/', 'Contatti')])}
    <p class="label">Contatti</p>
    <h1>Parliamone <em>di persona.</em></h1>
    <p class="lead">Scrivi o telefona allo studio per fissare un primo incontro. Lo studio riceve solo su appuntamento, in via Filippo Saporito 58 ad Aversa.</p>
  </div>
  <div class="wrap" style="margin-top:56px">
    <dl class="contacts">
      <div><dt>Telefono</dt><dd id="c-tel1"><a href="{tel(TEL1)}" style="text-decoration:none">{TEL1}</a></dd><button class="copy" type="button" data-copy="c-tel1">Copia</button></div>
      <div><dt>Telefono</dt><dd id="c-tel2"><a href="{tel(TEL2)}" style="text-decoration:none">{TEL2}</a></dd><button class="copy" type="button" data-copy="c-tel2">Copia</button></div>
      <div><dt>E-mail</dt><dd id="c-mail">{MAIL}</dd><span class="acts"><a class="copy go" href="mailto:{MAIL}?subject=Richiesta%20di%20appuntamento">Scrivici</a><button class="copy" type="button" data-copy="c-mail">Copia</button></span></div>
      <div><dt>PEC · Dott. Iorio</dt><dd id="c-pec1">{PEC1}</dd><button class="copy" type="button" data-copy="c-pec1">Copia</button></div>
      <div><dt>PEC · Dott. Mollichella</dt><dd id="c-pec2">{PEC2}</dd><button class="copy" type="button" data-copy="c-pec2">Copia</button></div>
      <div><dt>Sede</dt><dd>{SEDE}</dd><a class="copy" href="https://www.google.com/maps/search/?api=1&amp;query=Via+Filippo+Saporito+58+81031+Aversa" target="_blank" rel="noopener">Mappa ↗</a></div>
      <div><dt>Ricevimento</dt><dd>Solo su appuntamento</dd><span></span></div>
    </dl>
  </div>
</section>

<section class="sec" id="scrivici">
  <div class="wrap split">
    <div class="stack">
      <p class="label">Modulo di contatto</p>
      <h2>Inviaci <em>un messaggio.</em></h2>
      <p class="soft">Rispondiamo di norma entro due giorni lavorativi. Per questioni con scadenze ravvicinate è preferibile telefonare.</p>
    </div>
    <form class="form" id="modulo" name="contatti" method="POST" action="https://api.web3forms.com/submit">
      <input type="hidden" name="access_key" value="26752f22-884a-4b22-976e-b9f31f8bffcb">
      <input type="hidden" name="subject" value="Nuovo messaggio dal sito studioiempartners.it">
      <input type="hidden" name="from_name" value="Sito I&amp;M Partners">
      <input type="hidden" name="redirect" value="https://studioiempartners.it/grazie/">
      <p class="hp"><label>Non compilare questo campo <input type="checkbox" name="botcheck" tabindex="-1" autocomplete="off"></label></p>
      <label for="m-nome">Nome e cognome</label>
      <input id="m-nome" name="nome" type="text" autocomplete="name" required>
      <label for="m-mail">E-mail</label>
      <input id="m-mail" name="email" type="email" autocomplete="email" required>
      <label for="m-tel">Telefono (facoltativo)</label>
      <input id="m-tel" name="telefono" type="tel" autocomplete="tel">
      <label for="m-area">Argomento</label>
      <select id="m-area" name="argomento"><option value="">Scegli un argomento</option>{area_opts}<option value="altro">Altro</option></select>
      <label for="m-testo">Messaggio</label>
      <textarea id="m-testo" name="messaggio" rows="5" required></textarea>
      <label class="check" for="m-priv"><input id="m-priv" name="privacy" type="checkbox" value="letta" required><span>Ho letto l'<a href="/note-legali/#privacy">informativa sul trattamento dei dati personali</a> (art. 13 Reg. UE 2016/679).</span></label>
      <button class="cta" type="submit">Invia il messaggio</button>
      <p class="stato" id="m-stato" role="status" hidden></p>
    </form>
  </div>
</section>

<section class="sec band">
  <div class="wrap stack" style="gap:30px">
    <div class="stack"><p class="label">Il primo incontro</p><h2>Cosa portare <em>allo studio.</em></h2></div>
    <ol class="bring">
      <li>Documento d'identità e codice fiscale</li>
      <li>Ultime dichiarazioni presentate</li>
      <li>Visura camerale e statuto, per le società</li>
      <li>Ultimo bilancio o situazione contabile</li>
      <li>Comunicazioni ricevute da Agenzia delle Entrate, INPS o altri enti</li>
      <li>Un elenco delle domande da porre</li>
    </ol>
  </div>
</section>
<script>
(function(){{var a=new URLSearchParams(location.search).get('area'),s=document.getElementById('m-area');if(a&&s&&s.querySelector('option[value="'+a.replace(/[^a-z-]/g,'')+'"]'))s.value=a;}})();
</script>
'''
pages['/contatti/'] = page('/contatti/', 'Contatti · I&amp;M Partners Commercialisti, Aversa',
    "Contatti dello studio I&amp;M Partners, via Filippo Saporito 58, Aversa (CE): telefono, e-mail, PEC e modulo per richiedere un incontro. Si riceve su appuntamento.",
    cont, head_extra=ld(ORG) + crumbs_ld([('/', 'Home'), ('/contatti/', 'Contatti')]))

# --- grazie
pages['/grazie/'] = page('/grazie/', 'Messaggio inviato · I&amp;M Partners', 'Il messaggio è stato inviato allo studio.', f'''
<section class="sec nf"><div class="wrap ph">
  <p class="label">Messaggio inviato</p>
  <h1>Grazie, <em>a presto.</em></h1>
  <p class="lead">Il messaggio è arrivato allo studio. Ti risponderemo all'indirizzo e-mail indicato; per questioni urgenti puoi telefonare al {TEL1}.</p>
  <div class="row"><a class="cta" href="/">Torna alla home</a><a class="cta ghost" href="/scadenze/">Scadenze e novità</a></div>
</div></section>''', robots='noindex')

# --- note legali
legal = f'''
<section class="sec">
  <div class="wrap stack legal" style="gap:18px">
    {crumbs([('/', 'Home'), ('/note-legali/', 'Note legali e privacy')])}
    <p class="label">Note legali e privacy</p>
    <h1>Informazioni <em>obbligatorie.</em></h1>

    <h3>Dati dello studio</h3>
    <p>Informazioni rese ai sensi dell'art. 7 del D.Lgs. 9 aprile 2003, n. 70 e dell'art. 35, comma 1, del D.P.R. 26 ottobre 1972, n. 633.</p>
    <ul>
      <li><strong>Denominazione:</strong> {STUDIO} {TODO_DEN}</li>
      <li><strong>Sede:</strong> {SEDE}</li>
      <li><strong>Partita IVA:</strong> {PIVA}</li>
      <li><strong>Contatti:</strong> {MAIL} · PEC {PEC1} · PEC {PEC2}</li>
      <li><strong>Professionisti:</strong> Dott. Salvatore Iorio e Dott. Nazareno Mollichella, iscritti all'Albo dei Dottori Commercialisti e degli Esperti Contabili tenuto dall'Ordine di Napoli Nord, sezione A, rispettivamente ai numeri 1849A e 1860A</li>
      <li><strong>Titolo professionale:</strong> Dottore Commercialista, conseguito in Italia</li>
      <li><strong>Norme professionali:</strong> D.Lgs. 28 giugno 2005, n. 139 e Codice deontologico della professione approvato dal Consiglio Nazionale dei Dottori Commercialisti e degli Esperti Contabili, consultabile sul sito del Consiglio Nazionale</li>
    </ul>

    <h3>Contenuti del sito</h3>
    <p>Le informazioni pubblicate, comprese scadenze, novità e calcolatori, hanno carattere generale e informativo, sono aggiornate alla data indicata e non costituiscono consulenza professionale. Il calendario delle scadenze non tiene conto di proroghe e termini particolari.</p>

    <h3 id="privacy">Informativa sul trattamento dei dati personali</h3>
    <p>Informativa resa ai sensi dell'art. 13 del Regolamento (UE) 2016/679.</p>
    <ul>
      <li><strong>Titolare del trattamento:</strong> {TODO_TIT}, contattabile all'indirizzo {MAIL}.</li>
      <li><strong>Dati trattati:</strong> dati di navigazione necessari al funzionamento del sito; dati che l'utente comunica spontaneamente con il modulo di contatto (nome, e-mail, telefono, argomento e messaggio), per e-mail o per telefono.</li>
      <li><strong>Finalità e base giuridica:</strong> riscontro alle richieste dell'utente ed esecuzione di misure precontrattuali (art. 6, par. 1, lett. b); sicurezza e funzionamento del sito (art. 6, par. 1, lett. f).</li>
      <li><strong>Conferimento:</strong> facoltativo; senza nome, e-mail e messaggio non è possibile rispondere alla richiesta.</li>
      <li><strong>Conservazione:</strong> per il tempo necessario a dare riscontro alla richiesta e, in caso di conferimento dell'incarico, per i termini previsti dalla legge.</li>
      <li><strong>Destinatari:</strong> fornitori dei servizi tecnici del sito, nominati responsabili del trattamento ai sensi dell'art. 28, tra cui Netlify, Inc. (Stati Uniti), che ospita il sito, GitHub, Inc. (Stati Uniti), che conserva il codice del sito, e il servizio Web3Forms, che inoltra all'indirizzo e-mail dello studio i messaggi inviati con il modulo di contatto. L'eventuale trasferimento di dati verso Paesi terzi avviene con le garanzie previste dal Capo V del Regolamento.</li>
      <li><strong>Diritti dell'interessato:</strong> accesso, rettifica, cancellazione, limitazione, portabilità e opposizione (artt. 15-22), oltre al reclamo al Garante per la protezione dei dati personali (art. 77).</li>
    </ul>

    <h3>Cookie</h3>
    <p>Il sito utilizza soltanto strumenti tecnici, per i quali non è richiesto il consenso dell'utente ai sensi dell'art. 122 del D.Lgs. 30 giugno 2003, n. 196 e delle Linee guida del Garante del 10 giugno 2021. Per non riproporre la pagina d'ingresso a ogni visita il sito memorizza nel browser un'indicazione tecnica che si cancella alla chiusura della scheda. Non sono presenti cookie di profilazione, strumenti di statistica né contenuti di terze parti: caratteri tipografici e immagini sono serviti dal sito stesso.</p>
    <p class="note">Ultimo aggiornamento: {datetime.date.today().strftime('%d/%m/%Y')}.</p>
  </div>
</section>
'''
pages['/note-legali/'] = page('/note-legali/', 'Note legali e privacy · I&amp;M Partners Commercialisti',
    "Informazioni obbligatorie, informativa sul trattamento dei dati personali e cookie del sito di I&amp;M Partners Commercialisti.",
    legal, head_extra=crumbs_ld([('/', 'Home'), ('/note-legali/', 'Note legali e privacy')]))

# --- English
en = f'''
<section class="sec">
  <div class="wrap ph">
    <p class="label">I&amp;M Partners · Chartered accountants in Aversa, Italy</p>
    <h1>Tax, corporate and accounting advice <em>in Italy.</em></h1>
    <p class="lead">I&amp;M Partners is the practice of Salvatore Iorio and Nazareno Mollichella, Italian chartered accountants (Dottori Commercialisti) registered with the Order of Naples North. We assist companies, entrepreneurs and individuals with Italian tax, corporate and accounting matters, including cross-border situations.</p>
    <div class="row"><a class="cta" href="mailto:{MAIL}?subject=Enquiry">Write to us</a><a class="cta ghost" href="{tel(TEL1)}">Call {TEL1}</a></div>
  </div>
</section>
<section class="sec">
  <div class="wrap stack" style="gap:40px">
    <div class="stack"><p class="label">Practice areas</p><h2>How we can <em>help.</em></h2></div>
    <div class="grid-svc">
      <div class="blk"><h3>Italian tax</h3><ul class="ticks soft"><li>Tax returns for companies and individuals</li><li>VAT, e-invoicing and cross-border transactions</li><li>Tax residence and double tax treaties</li><li>Tax audits and disputes</li></ul></div>
      <div class="blk"><h3>Setting up in Italy</h3><ul class="ticks soft"><li>Incorporation of Italian companies and branches</li><li>Permanent establishment assessment</li><li>VAT registration and fiscal representation</li><li>Ongoing bookkeeping and statutory accounts</li></ul></div>
      <div class="blk"><h3>Corporate</h3><ul class="ticks soft"><li>Transfers of shares and business units</li><li>Mergers, demergers and reorganisations</li><li>Company secretarial services</li><li>Valuations and due diligence</li></ul></div>
      <div class="blk"><h3>Moving to Italy</h3><ul class="ticks soft"><li>Inbound worker tax regime (impatriati)</li><li>Reporting of foreign assets</li><li>Foreign-source income in Italian returns</li></ul></div>
    </div>
  </div>
</section>
<section class="sec band">
  <div class="wrap split">
    <div class="stack"><p class="label">Contact</p><h2>Meetings by <em>appointment.</em></h2></div>
    <dl class="facts">
      <div><dt>Office</dt><dd>Via Filippo Saporito 58, 81031 Aversa (CE), Italy</dd></div>
      <div><dt>Phone</dt><dd><a href="{tel(TEL1)}">{TEL1}</a> · <a href="{tel(TEL2)}">{TEL2}</a></dd></div>
      <div><dt>E-mail</dt><dd><a href="mailto:{MAIL}">{MAIL}</a></dd></div>
      <div><dt>VAT number</dt><dd>IT{PIVA}</dd></div>
      <div><dt>Languages</dt><dd>Italian, English</dd></div>
    </dl>
  </div>
</section>
<section class="sec"><div class="wrap"><p class="note">Information on this page is general in nature and does not constitute professional advice. Legal notices and privacy information are available in Italian on the <a href="/note-legali/">Note legali e privacy</a> page.</p></div></section>
'''
pages['/en/'] = page('/en/', 'I&amp;M Partners · Chartered accountants in Aversa, Italy',
    "Italian chartered accountants in Aversa (Caserta): Italian tax, VAT, company formation, corporate transactions and cross-border tax advice. Meetings by appointment.",
    en, lang='en', head_extra=ld(ORG))

# --- 404
pages['/404.html'] = page('/404.html', 'Pagina non trovata · I&amp;M Partners', 'La pagina richiesta non esiste.', '''
<section class="sec nf"><div class="wrap ph">
  <p class="big">404</p>
  <h1>Questa pagina <em>non esiste.</em></h1>
  <p class="lead">Forse l'indirizzo è cambiato. Puoi ripartire dalla home o dalle aree di attività.</p>
  <div class="row"><a class="cta" href="/">Home</a><a class="cta ghost" href="/aree/">Aree di attività</a><a class="cta ghost" href="/contatti/">Contatti</a></div>
</div></section>''', robots='noindex')

# ---------------------------------------------------------------- scrittura
for path, html in pages.items():
    out = ROOT / ('404.html' if path == '/404.html' else (path.strip('/') + '/index.html' if path != '/' else 'index.html'))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding='utf-8')

css = (SRC / 'fonts.css').read_text() + (SRC / 'base.css').read_text() + (SRC / 'extra.css').read_text()
(ROOT / 'assets' / 'style.css').write_text(css, encoding='utf-8')

urls = [p for p in pages if p not in ('/404.html', '/grazie/')]
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(
    f'  <url><loc>{SITE}{p}</loc><lastmod>{OGG}</lastmod></url>\n' for p in urls) + '</urlset>\n'
(ROOT / 'sitemap.xml').write_text(sm, encoding='utf-8')
print(f'{len(pages)} pagine generate')
