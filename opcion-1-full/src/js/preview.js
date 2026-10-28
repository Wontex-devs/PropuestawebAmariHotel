// Vista previa (?preview): solo se puede desplazar; enlaces, botones y formularios quedan bloqueados
(function () {
  if (!/[?&]preview\b/.test(location.search)) return;
  var r = document.documentElement;
  r.classList.add('is-preview', 'no-splash');
  var st = document.createElement('style');
  st.textContent = 'a,button,input,select,textarea,label,summary,video,iframe,[role=button],[tabindex],[onclick]{pointer-events:none!important}html.is-preview{user-select:none;-webkit-user-select:none}.cookie-banner,.cookie-prefs{display:none!important}';
  document.head.appendChild(st);
  var stop = function (e) { e.preventDefault(); e.stopImmediatePropagation(); };
  ['click', 'dblclick', 'auxclick', 'contextmenu', 'submit', 'mousedown', 'pointerdown'].forEach(function (t) {
    window.addEventListener(t, stop, true);
  });
  window.addEventListener('keydown', function (e) {
    if (e.key === 'Tab' || e.key === 'Enter') stop(e);
  }, true);
  window.addEventListener('focusin', function (e) {
    if (e.target && e.target.blur) e.target.blur();
  }, true);
})();
