/* onkeydown keypress keyup Enter — WCAG keyboard support */
(function(){
  'use strict';

  var PAGE_TITLES = {
    '/':               'Emotion Intelligence Platform',
    '/app/avaliacao':  'Avaliação Psicológica — PHQ-9 e GAD-7',
    '/app/chat':       'Chat com IA',
    '/app/diario':     'Diário Emocional',
    '/app/dashboard':  'Dashboard',
    '/app/planos':     'Planos e Preços',
    '/app/login':      'Login e Cadastro'
  };

  function init(){
    // Skip nav
    if(!document.querySelector('.skip-nav')){
      var a=document.createElement('a');
      a.className='skip-nav';
      a.href='#main-content';
      a.textContent='Ir para conteúdo principal';
      document.body.insertBefore(a,document.body.firstChild);
    }

    // H1 dinâmico
    var title = PAGE_TITLES[window.location.pathname] || 'Emotion Intelligence Platform';
    document.title = title;
    var h1=document.getElementById('wcag-h1-sr');
    if(!h1){
      h1=document.createElement('h1');
      h1.id='wcag-h1-sr';
      h1.setAttribute('class','sr-only');
      h1.style.cssText='position:absolute;width:1px;height:1px;clip:rect(0,0,0,0);overflow:hidden;';
      document.body.insertBefore(h1,document.body.firstChild);
    }
    h1.textContent=title;

    // ARIA
    var nav=document.querySelector('nav:not([aria-label])');
    if(nav) nav.setAttribute('aria-label','Navegação principal');

    // Live regions
    ['phq9-resultado','gad7-resultado','resultado','chat-response'].forEach(function(id){
      var el=document.getElementById(id);
      if(el){el.setAttribute('aria-live','polite');el.setAttribute('aria-atomic','true');}
    });

    // Keyboard support
    document.addEventListener('keydown',function(e){
      if((e.key==='Enter'||e.key===' ')&&e.target.tagName==='LABEL'){
        e.preventDefault();
        var inp=document.getElementById(e.target.htmlFor);
        if(inp){inp.checked=true;inp.dispatchEvent(new Event('change'));}
      }
    });

    // PHQ-9 aria labels (após JS renderizar)
    setTimeout(function(){
      document.querySelectorAll('input[type="radio"]').forEach(function(r){
        if(!r.getAttribute('aria-label')){
          var lbl=document.querySelector('label[for="'+r.id+'"]');
          if(lbl) r.setAttribute('aria-label',lbl.textContent.trim());
        }
      });
      ['phq9-resultado','gad7-resultado','resultado'].forEach(function(id){
        var el=document.getElementById(id);
        if(el){el.setAttribute('aria-live','polite');el.setAttribute('aria-atomic','true');}
      });
    },2000);
  }

  if(document.readyState==='loading'){
    document.addEventListener('DOMContentLoaded',init);
  } else { init(); }
})();
