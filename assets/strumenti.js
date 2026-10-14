/* Strumenti di calcolo: stime orientative, calcolate nel browser senza inviare dati */
(function(){
  var eur=new Intl.NumberFormat('it-IT',{style:'currency',currency:'EUR',maximumFractionDigits:0});
  var eur2=new Intl.NumberFormat('it-IT',{style:'currency',currency:'EUR',minimumFractionDigits:2,maximumFractionDigits:2});
  var pct=new Intl.NumberFormat('it-IT',{style:'percent',minimumFractionDigits:1,maximumFractionDigits:1});
  function num(id){var v=parseFloat(String(document.getElementById(id).value).replace(',','.'));return isFinite(v)&&v>0?v:0;}
  function cell(tr,txt,cls){var td=document.createElement('td');td.textContent=txt;if(cls)td.className=cls;tr.appendChild(td);}

  /* IRPEF lorda 2026: art. 11, co. 1, TUIR come modificato dall'art. 1, co. 3, L. 199/2025 */
  var SC=[[28000,.23],[50000,.33],[Infinity,.43]];
  var fi=document.getElementById('f-irpef');
  if(fi){
    var calcI=function(){
      var r=num('i-reddito'),prec=0,tot=0,marg=0,tb=document.getElementById('i-tab');
      tb.textContent='';
      SC.forEach(function(s,k){
        var quota=Math.max(0,Math.min(r,s[0])-prec),imp=quota*s[1];
        if(r>prec) marg=s[1];
        tot+=imp;
        var tr=document.createElement('tr');
        cell(tr,k===0?'Fino a 28.000 €':k===1?'Da 28.000 a 50.000 €':'Oltre 50.000 €');
        cell(tr,pct.format(s[1]).replace(',0',''),'n');
        cell(tr,eur.format(quota),'n');
        cell(tr,eur2.format(imp),'n');
        tb.appendChild(tr);
        prec=s[0];
      });
      var tr=document.createElement('tr');tr.className='tot';
      cell(tr,'Imposta lorda');cell(tr,'');cell(tr,eur.format(r),'n');cell(tr,eur2.format(tot),'n');tb.appendChild(tr);
      document.getElementById('i-out').textContent=eur.format(Math.round(tot));
      document.getElementById('i-media').textContent=r?pct.format(tot/r):'–';
      document.getElementById('i-marg').textContent=r?pct.format(marg).replace(',0',''):'–';
      document.getElementById('i-200').hidden=r<=200000;
    };
    fi.addEventListener('input',calcI);fi.addEventListener('submit',function(e){e.preventDefault();calcI()});
    calcI();
  }

  /* Regime forfettario: art. 1, commi 54-89, L. 190/2014 */
  var ff=document.getElementById('f-forf');
  if(ff){
    var calcF=function(){
      var ricavi=num('f-ricavi'),coeff=parseFloat(document.getElementById('f-gruppo').value),contr=num('f-contributi');
      var al=parseFloat((ff.querySelector('input[name=aliq]:checked')||{}).value||'0.15');
      var lordo=ricavi*coeff,imponibile=Math.max(0,lordo-contr),imposta=imponibile*al;
      document.getElementById('f-out').textContent=eur.format(Math.round(imposta));
      var tb=document.getElementById('f-tab');tb.textContent='';
      [['Ricavi o compensi incassati',eur.format(ricavi)],
       ['Coefficiente di redditività',pct.format(coeff).replace(',0','')],
       ['Reddito forfettario',eur.format(lordo)],
       ['Contributi previdenziali dedotti','− '+eur.format(Math.min(contr,lordo))],
       ['Reddito imponibile',eur.format(imponibile)],
       ['Aliquota imposta sostitutiva',pct.format(al).replace(',0','')]].forEach(function(r){
        var tr=document.createElement('tr');cell(tr,r[0]);cell(tr,r[1],'n');tb.appendChild(tr);
      });
      var tr=document.createElement('tr');tr.className='tot';cell(tr,'Imposta sostitutiva');cell(tr,eur2.format(imposta),'n');tb.appendChild(tr);
      document.getElementById('f-carico').textContent=ricavi?pct.format(imposta/ricavi):'–';
      var w=document.getElementById('f-warn');
      if(ricavi>100000){w.hidden=false;w.textContent='Oltre 100.000 € di ricavi o compensi il regime cessa già nell’anno in cui la soglia è superata (art. 1, co. 71, L. 190/2014).';}
      else if(ricavi>85000){w.hidden=false;w.textContent='Oltre 85.000 € il regime resta applicabile per l’anno in corso, ma non per l’anno successivo (art. 1, co. 54 e 71, L. 190/2014).';}
      else w.hidden=true;
    };
    ff.addEventListener('input',calcF);ff.addEventListener('change',calcF);ff.addEventListener('submit',function(e){e.preventDefault();calcF()});
    calcF();
  }
})();
