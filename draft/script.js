const toggle = document.querySelector('#menu-toggle');
const sidebar = document.querySelector('.sidebar');
const links = [...document.querySelectorAll('#chapter-nav a')];
const chapters = [...document.querySelectorAll('.chapter')];
function closeMenu() { sidebar.classList.remove('open'); toggle.setAttribute('aria-expanded', 'false'); }
toggle.addEventListener('click', () => { const open = sidebar.classList.toggle('open'); toggle.setAttribute('aria-expanded', String(open)); });
links.forEach(link => link.addEventListener('click', closeMenu));
document.addEventListener('keydown', event => { if (event.key === 'Escape' && sidebar.classList.contains('open')) { closeMenu(); toggle.focus(); } });
document.addEventListener('click', event => { if (!sidebar.contains(event.target) && !toggle.contains(event.target)) closeMenu(); });
matchMedia('(min-width: 761px)').addEventListener('change', closeMenu);
let scheduled = false;
function updateReading() {
  const target = innerHeight * .35;
  let active = null;
  chapters.forEach(chapter => { if (chapter.getBoundingClientRect().top <= target) active = chapter; });
  links.forEach(link => { if (active && link.hash === '#' + active.id) link.setAttribute('aria-current', 'location'); else link.removeAttribute('aria-current'); });
  const start = chapters[0].offsetTop;
  const end = chapters.at(-1).offsetTop + chapters.at(-1).offsetHeight - innerHeight;
  const ratio = Math.max(0, Math.min(1, (scrollY - start) / Math.max(1, end - start)));
  document.querySelector('#progress-fill').style.width = `${ratio * 100}%`;
  scheduled = false;
}
function scheduleUpdate() { if (!scheduled) { scheduled = true; requestAnimationFrame(updateReading); } }
addEventListener('scroll', scheduleUpdate, {passive: true});
addEventListener('resize', scheduleUpdate);
addEventListener('load', updateReading);
const words = chapters.map(chapter => chapter.innerText).join(' ').trim().split(/\s+/).length;
document.querySelector('#reading-time').textContent = Math.ceil(words / 210);
updateReading();
