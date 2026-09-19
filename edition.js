const button=document.querySelector('#menu-toggle'),sidebar=document.querySelector('.sidebar');
function closeMenu(){sidebar.classList.remove('open');button.setAttribute('aria-expanded','false');}
button.addEventListener('click',()=>{button.setAttribute('aria-expanded',String(sidebar.classList.toggle('open')));});
document.querySelectorAll('.sidebar a').forEach(a=>a.addEventListener('click',closeMenu));
document.addEventListener('keydown',e=>{if(e.key==='Escape'&&sidebar.classList.contains('open')){closeMenu();button.focus();}});
document.addEventListener('click',e=>{if(!sidebar.contains(e.target)&&!button.contains(e.target))closeMenu();});
matchMedia('(min-width:761px)').addEventListener('change',closeMenu);
const chapters=[...document.querySelectorAll('.chapter')],links=[...document.querySelectorAll('#chapter-nav a')];
let pending=false;
function update(){let active;chapters.forEach(c=>{if(c.getBoundingClientRect().top<=innerHeight*.3)active=c;});links.forEach(a=>{if(active&&a.hash==='#'+active.id)a.setAttribute('aria-current','location');else a.removeAttribute('aria-current');});if(chapters.length){const first=chapters[0].offsetTop,last=chapters.at(-1);document.querySelector('#progress-fill').style.width=Math.max(0,Math.min(100,100*(scrollY-first)/Math.max(1,last.offsetTop+last.offsetHeight-innerHeight-first)))+'%';}pending=false;}
function schedule(){if(!pending){pending=true;requestAnimationFrame(update);}}
addEventListener('scroll',schedule,{passive:true});addEventListener('resize',schedule);addEventListener('load',update);update();
const desktopButton=document.querySelector('#desktop-toggle');
desktopButton.addEventListener('click',()=>{
 const folded=sidebar.classList.toggle('folded');
 desktopButton.setAttribute('aria-expanded',String(!folded));
 desktopButton.setAttribute('aria-label',folded?'Expand chapter menu':'Collapse chapter menu');
 desktopButton.textContent=folded?'+':'−';
});
