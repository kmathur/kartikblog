Title: Tech IPOs Since 2010
Date: 2026-11-16
Category: Tech

<style>
  article.single { margin-left: 2%; margin-right: 2%; }
  #ipo-frame { display: block; width: 100%; height: 1400px; border: 0; background: transparent; }
</style>
<iframe id="ipo-frame" src="{static}/extra/tech-ipos-since-2010.html" title="Tech IPOs since 2010" scrolling="no" loading="lazy"></iframe>
<script>
document.getElementById('ipo-frame').addEventListener('load', function () {
  var f = this, d;
  try { d = f.contentDocument; } catch (e) { return; }
  // Blend into the host page: transparent background, no inner gutters, no duplicate title.
  var st = d.createElement('style');
  st.textContent = 'body{background:transparent!important}body::before{display:none}' +
    '.wrap{max-width:none!important;padding:0 0 24px!important}header h1{display:none}' +
    'thead th{position:static!important}';
  d.head.appendChild(st);
  function fit() { f.style.height = d.documentElement.scrollHeight + 'px'; }
  fit(); setTimeout(fit, 300);
  try { new ResizeObserver(fit).observe(d.body); } catch (e) {}
});
</script>

[← Back to Tech](../) | [← Back to Home](../../../)
