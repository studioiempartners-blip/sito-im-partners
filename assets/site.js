/* I&M Partners · comportamenti comuni a tutte le pagine */
(function(){
  var doc=document, body=doc.body;

  /* vecchi indirizzi con # della versione a pagina unica */
  var old={'#studio':'/studio/','#servizi':'/aree/','#professionisti':'/professionisti/','#scadenze':'/scadenze/','#contatti':'/contatti/','#note-legali':'/note-legali/'};
  if(location.pathname==='/'&&old[location.hash]){location.replace(old[location.hash]);return;}

  /* vetrina d'ingresso: solo in home, una volta per sessione del browser */
  var v=doc.getElementById('vetrina'), entra=doc.getElementById('entra');
  if(v&&entra&&doc.documentElement.classList.contains('v-on')){
    body.classList.add('locked');
    try{entra.focus({preventScroll:true})}catch(x){}
    entra.addEventListener('click',function(){
      try{sessionStorage.setItem('imp-v','1')}catch(x){}
      v.classList.add('out');
      body.classList.remove('locked');
      setTimeout(function(){doc.documentElement.classList.remove('v-on')},650);
    });
  }

  /* menu a tutta pagina */
  var ov=doc.getElementById('menu'),apri=doc.getElementById('menu-apri'),chiudi=doc.getElementById('menu-chiudi');
  function menu(on){
    if(!ov) return;
    ov.hidden=!on;apri.setAttribute('aria-expanded',on?'true':'false');
    body.classList.toggle('locked',on);
    try{(on?chiudi:apri).focus({preventScroll:true})}catch(x){}
  }
  if(ov&&apri&&chiudi){
    apri.addEventListener('click',function(){menu(true)});
    chiudi.addEventListener('click',function(){menu(false)});
    doc.addEventListener('keydown',function(e){if(e.key==='Escape'&&!ov.hidden) menu(false)});
  }

  /* messaggi in apertura della home */
  var sl=[].slice.call(doc.querySelectorAll('#slides .slide')),cont=doc.getElementById('sl-c'),i=0,timer=null;
  if(sl.length>1&&cont){
    var vai=function(n){i=(n+sl.length)%sl.length;sl.forEach(function(s,k){s.classList.toggle('on',k===i);s.setAttribute('aria-hidden',k===i?'false':'true')});cont.textContent=(i+1)+' / '+sl.length;};
    var ferma=function(){if(timer){clearInterval(timer);timer=null}};
    var parti=function(){if(matchMedia('(prefers-reduced-motion:reduce)').matches) return;ferma();timer=setInterval(function(){vai(i+1)},8000);};
    doc.getElementById('sl-prev').addEventListener('click',function(){vai(i-1);parti()});
    doc.getElementById('sl-next').addEventListener('click',function(){vai(i+1);parti()});
    var hero=doc.querySelector('.hero');
    hero.addEventListener('pointerenter',ferma);hero.addEventListener('pointerleave',parti);
    hero.addEventListener('focusin',ferma);hero.addEventListener('focusout',parti);
    vai(0);parti();
  }

  /* la "&" segue appena il puntatore */
  var amp=doc.querySelector('.hero .amp');
  if(amp&&matchMedia('(hover:hover)').matches&&!matchMedia('(prefers-reduced-motion:reduce)').matches){
    addEventListener('pointermove',function(e){
      amp.style.transform='translate('+((e.clientX/innerWidth-.5)*-26)+'px,calc(-52% + '+((e.clientY/innerHeight-.5)*-18)+'px))';
    });
  }

  /* pulsanti "Copia" */
  [].forEach.call(doc.querySelectorAll('.copy[data-copy]'),function(b){
    b.addEventListener('click',function(){
      var el=doc.getElementById(b.dataset.copy),t=el.textContent.trim();
      function sel(){var r=doc.createRange();r.selectNodeContents(el);var s=getSelection();s.removeAllRanges();s.addRange(r);}
      function ok(){b.textContent='Copiato';setTimeout(function(){b.textContent='Copia'},1600);}
      try{navigator.clipboard.writeText(t).then(ok,sel);}catch(e){sel();}
    });
  });

  /* modulo di contatto: invio senza lasciare la pagina (senza script funziona comunque) */
  var f=doc.getElementById('modulo');
  if(f){
    var st=doc.getElementById('m-stato'),btn=f.querySelector('button[type=submit]');
    var dici=function(t){st.hidden=false;st.textContent=t;};
    f.addEventListener('submit',function(e){
      if(!f.checkValidity()) return;
      e.preventDefault();
      btn.disabled=true;dici('Invio in corso…');
      fetch('/',{method:'POST',headers:{'Content-Type':'application/x-www-form-urlencoded'},body:new URLSearchParams(new FormData(f)).toString()})
        .then(function(r){if(!r.ok) throw r;location.href='/grazie/';})
        .catch(function(){btn.disabled=false;dici('Il messaggio non è stato inviato. Riprova tra poco oppure scrivi a studioiempartners@gmail.com.');});
    });
  }
})();
