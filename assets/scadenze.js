/* Scadenzario calcolato sulla data del giorno e novità lette da /novita.json */
(function(){
  var MESI=['gennaio','febbraio','marzo','aprile','maggio','giugno','luglio','agosto','settembre','ottobre','novembre','dicembre'];
  var MES=['gen','feb','mar','apr','mag','giu','lug','ago','set','ott','nov','dic'];
  var GG=['domenica','lunedì','martedì','mercoledì','giovedì','venerdì','sabato'];
  function pasqua(y){var a=y%19,b=Math.floor(y/100),c=y%100,d=Math.floor(b/4),e=b%4,f=Math.floor((b+8)/25),g=Math.floor((b-f+1)/3),h=(19*a+b-d-g+15)%30,i=Math.floor(c/4),k=c%4,l=(32+2*e+2*i-h-k)%7,m=Math.floor((a+11*h+22*l)/451),n=h+l-7*m+114;return new Date(y,Math.floor(n/31)-1,(n%31)+1);}
  function festivo(d){
    var k=(d.getMonth()+1)+'-'+d.getDate();
    if(['1-1','1-6','4-25','5-1','6-2','8-15','11-1','12-8','12-25','12-26'].indexOf(k)>=0) return true;
    if(k==='10-4'&&d.getFullYear()>=2026) return true;
    var p=pasqua(d.getFullYear());p.setDate(p.getDate()+1);
    return p.getMonth()===d.getMonth()&&p.getDate()===d.getDate();
  }
  /* sabato e festivi slittano al primo giorno lavorativo (art. 7, co. 1, lett. h, D.L. 70/2011);
     1-20 agosto slitta al 20 agosto (art. 37, co. 11-bis, D.L. 223/2006) */
  function utile(d){
    if(d.getMonth()===7&&d.getDate()<20) d.setDate(20);
    while(d.getDay()===0||d.getDay()===6||festivo(d)) d.setDate(d.getDate()+1);
    return d;
  }
  function anno(y){
    var L=[];
    function add(m,g,t,x,n,c){L.push({d:utile(new Date(y,m,g)),t:t,x:x,n:n,c:c});}
    for(var m=0;m<12;m++){
      add(m,16,'Versamento F24 mensile','Ritenute IRPEF su redditi di lavoro dipendente e autonomo, contributi INPS dei dipendenti e IVA dei contribuenti mensili, riferiti al mese precedente.','Art. 18 D.Lgs. 241/1997 · Art. 1 D.P.R. 100/1998','versamenti');
      add(m,25,'Elenchi Intrastat',[0,3,6,9].indexOf(m)>=0?'Operazioni intracomunitarie del mese precedente (contribuenti mensili) e del trimestre precedente (contribuenti trimestrali).':'Operazioni intracomunitarie del mese precedente, per i contribuenti con obbligo mensile.','Art. 50, co. 6, D.L. 331/1993','iva');
      add(m+1,0,'Flusso Uniemens','Denuncia all’INPS delle retribuzioni e dei contributi del mese precedente.','Art. 44, co. 9, D.L. 269/2003','lavoro');
    }
    [1,4,7,10].forEach(function(m){add(m,16,'Contributi fissi artigiani e commercianti','Rata trimestrale dei contributi INPS sul minimale di reddito.','L. 233/1990 · Art. 18 D.Lgs. 241/1997','lavoro');});
    [4,7,10].forEach(function(m){add(m,16,'IVA trimestrale','Liquidazione e versamento dell’IVA del trimestre precedente, con interessi dell’1%.','Art. 7 D.P.R. 542/1999','iva');});
    add(1,16,'Autoliquidazione INAIL','Versamento del premio in unica soluzione o della prima rata.','Artt. 28 e 44 D.P.R. 1124/1965','lavoro');
    add(2,16,'Saldo IVA annuale','Versamento dell’IVA a debito risultante dalla dichiarazione annuale.','Artt. 6 e 7 D.P.R. 542/1999','iva');
    add(2,16,'Certificazioni Uniche','Invio all’Agenzia delle Entrate delle certificazioni dei redditi di lavoro dipendente e assimilati.','Art. 4, co. 6-quinquies, D.P.R. 322/1998','dichiarazioni');
    add(2,16,'Tassa annuale libri sociali','Versamento della tassa di concessione governativa per le società di capitali.','Art. 23 Tariffa D.P.R. 641/1972','versamenti');
    [[2,0,'quarto'],[4,31,'primo'],[8,30,'secondo'],[10,30,'terzo']].forEach(function(q){
      add(q[0],q[1],'Liquidazioni periodiche IVA','Comunicazione dei dati delle liquidazioni del '+q[2]+' trimestre.','Art. 21-bis D.L. 78/2010','iva');
      add(q[0],q[1],'Imposta di bollo sulle fatture elettroniche','Versamento dell’imposta relativa al '+q[2]+' trimestre.','Art. 6 D.M. 17 giugno 2014','versamenti');
    });
    add(3,30,'Dichiarazione IVA annuale','Termine di presentazione della dichiarazione relativa all’anno precedente.','Art. 8 D.P.R. 322/1998','dichiarazioni');
    add(5,16,'IMU: acconto','Versamento della prima rata dell’imposta municipale propria.','Art. 1, co. 762, L. 160/2019','versamenti');
    add(5,30,'Saldo e primo acconto delle imposte sui redditi','IRPEF, IRES, IRAP e diritto annuale camerale risultanti dalle dichiarazioni.','Art. 17 D.P.R. 435/2001','versamenti');
    add(6,30,'Imposte sui redditi con maggiorazione','Versamento di saldo e primo acconto con la maggiorazione dello 0,40%.','Art. 17, co. 2, D.P.R. 435/2001','versamenti');
    add(8,30,'Modello 730','Termine di presentazione della dichiarazione dei redditi con modello 730.','D.M. 164/1999','dichiarazioni');
    add(9,31,'Modelli Redditi e IRAP','Presentazione telematica delle dichiarazioni dei redditi e IRAP per i soggetti con esercizio solare.','Art. 2 D.P.R. 322/1998','dichiarazioni');
    add(9,31,'Modello 770','Dichiarazione dei sostituti d’imposta.','Art. 4 D.P.R. 322/1998','dichiarazioni');
    add(10,30,'Secondo acconto delle imposte sui redditi','Seconda o unica rata di acconto IRPEF, IRES e IRAP.','Art. 17, co. 3, D.P.R. 435/2001','versamenti');
    add(11,16,'IMU: saldo','Versamento della seconda rata a conguaglio.','Art. 1, co. 762, L. 160/2019','versamenti');
    add(11,27,'Acconto IVA','Versamento dell’acconto per l’ultimo periodo dell’anno.','Art. 6 L. 405/1990','iva');
    return L;
  }
  var oggi=new Date();oggi.setHours(0,0,0,0);
  var tutte=anno(oggi.getFullYear()).concat(anno(oggi.getFullYear()+1))
    .filter(function(s){return s.d>=oggi}).sort(function(a,b){return a.d-b.d});
  function fra(d){var n=Math.round((d-oggi)/864e5);return n===0?'Oggi':n===1?'Domani':'Tra '+n+' giorni';}
  function el(tag,cls,txt){var e=document.createElement(tag);if(cls)e.className=cls;if(txt!=null)e.textContent=txt;return e;}

  /* calendario completo (pagina Scadenze) */
  var cal=document.getElementById('cal'),filtro='tutte';
  function disegna(){
    cal.textContent='';
    var gruppi=[],chiave={};
    tutte.forEach(function(s){
      if(filtro!=='tutte'&&s.c!==filtro) return;
      var k=+s.d;
      if(chiave[k]===undefined){if(gruppi.length>=12) return;chiave[k]=gruppi.length;gruppi.push({d:s.d,v:[]});}
      gruppi[chiave[k]].v.push(s);
    });
    gruppi.forEach(function(g){
      var li=el('li'),dt=el('div','dt');
      dt.appendChild(el('span','day',String(g.d.getDate())));
      dt.appendChild(el('span','mon',MESI[g.d.getMonth()]+' '+g.d.getFullYear()+' · '+GG[g.d.getDay()]));
      dt.appendChild(el('span','in',fra(g.d)));
      var its=el('div','its');
      g.v.forEach(function(s){
        var it=el('div','it');
        it.appendChild(el('h3',null,s.t));
        it.appendChild(el('p',null,s.x));
        it.appendChild(el('span','nr',s.n));
        its.appendChild(it);
      });
      li.appendChild(dt);li.appendChild(its);cal.appendChild(li);
    });
  }
  if(cal){
    disegna();
    [].forEach.call(document.querySelectorAll('.chip'),function(b){
      b.addEventListener('click',function(){
        filtro=b.dataset.f;
        [].forEach.call(document.querySelectorAll('.chip'),function(c){c.setAttribute('aria-pressed',c===b?'true':'false')});
        disegna();
      });
    });
  }

  /* barra "prossima scadenza" e anteprima in home */
  if(tutte.length&&document.getElementById('nx-d')){
    var p=tutte[0];
    document.getElementById('nx-d').textContent=p.d.getDate()+' '+MESI[p.d.getMonth()];
    document.getElementById('nx-t').textContent=p.t;
    document.getElementById('nx-c').textContent=fra(p.d);
  }
  var ms=document.getElementById('mini-scad');
  if(ms){
    ms.textContent='';
    tutte.slice(0,4).forEach(function(s){
      var li=el('li'),d=el('span','d',String(s.d.getDate()));
      d.appendChild(el('small',null,MES[s.d.getMonth()]+' · '+fra(s.d).toLowerCase()));
      var w=el('div');w.appendChild(el('h3',null,s.t));w.appendChild(el('p',null,s.n));
      li.appendChild(d);li.appendChild(w);ms.appendChild(li);
    });
  }

  /* novità */
  var box=document.getElementById('nov'),vuoto=document.getElementById('nov-vuoto'),mn=document.getElementById('mini-nov');
  if(!box&&!mn) return;
  function dataIt(s){var d=/^\d{4}-\d{2}-\d{2}$/.test(s||'')?s.split('-'):null;return d?(+d[2])+' '+MESI[+d[1]-1]+' '+d[0]:'';}
  fetch((window.IMP_ROOT||'./')+'novita.json',{cache:'no-cache'}).then(function(r){return r.ok?r.json():[]}).then(function(l){
    l=(Array.isArray(l)?l:[]).filter(function(n){return n&&n.titolo}).sort(function(a,b){return String(b.data).localeCompare(String(a.data))}).slice(0,12);
    if(box){
      [].forEach.call(box.querySelectorAll('article'),function(a){a.remove()});
      if(vuoto) vuoto.hidden=l.length>0;
      l.forEach(function(n){
        var a=el('article');
        a.appendChild(el('span','meta',dataIt(n.data)+(n.tema?' · '+n.tema:'')));
        a.appendChild(el('h3',null,String(n.titolo||'')));
        a.appendChild(el('p',null,String(n.sintesi||'')));
        if(/^https:\/\//.test(n.url||'')){var k=el('a',null,'Fonte: '+String(n.fonte||'apri'));k.href=n.url;k.target='_blank';k.rel='noopener';a.appendChild(k);}
        box.appendChild(a);
      });
    }
    if(mn){
      mn.textContent='';
      if(!l.length){var li0=el('li');li0.appendChild(el('span'));li0.appendChild(el('p',null,'Nessuna novità pubblicata al momento.'));mn.appendChild(li0);}
      l.slice(0,3).forEach(function(n){
        var li=el('li'),d=n.data&&n.data.split('-'),dd=el('span','d',d?String(+d[2]):'');
        dd.appendChild(el('small',null,d?MES[+d[1]-1]+' '+d[0]:''));
        var a=el('a');a.href=(window.IMP_ROOT||'./')+'scadenze/index.html#novita';a.appendChild(el('h3',null,String(n.titolo)));a.appendChild(el('p',null,(n.tema||'')+(n.fonte?' · '+n.fonte:'')));
        li.appendChild(dd);li.appendChild(a);mn.appendChild(li);
      });
    }
  }).catch(function(){if(vuoto){vuoto.hidden=false;vuoto.textContent='Le novità non sono disponibili in questo momento.';}});
})();
