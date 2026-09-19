"""Render the essay and reading list from their editable source files."""
import json, re, html, shutil, struct, subprocess
from pathlib import Path
from html.parser import HTMLParser

ROOT = Path(__file__).resolve().parent
ORIGINAL_IMAGES = ROOT/'images'
thesis = json.loads((ROOT/'source/thesis.json').read_text())
copy_edits=json.loads((ROOT/'copy-edits.json').read_text())
def tidy(text):
    for before,after in copy_edits.items():text=text.replace(before,after)
    return text
slugs = ['our-world','mixed-messages','emerging-superpowers','looking-closer','existential-threats','hacking-the-system','building-digital-models','examples','participate']
esc = html.escape

class Inline(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True); self.out=[]; self.in_link=False
    def handle_starttag(self, tag, attrs):
        attrs=dict(attrs)
        if tag=='a' and attrs.get('href','').startswith(('https://','http://')):
            self.out.append('<a href="'+esc(attrs['href'],quote=True)+'">');self.in_link=True
        elif tag in ('b','strong','em','i','br'): self.out.append('<'+tag+'>')
    def handle_endtag(self,tag):
        if tag=='a' and self.in_link:self.out.append('</a>');self.in_link=False
        elif tag in ('b','strong','em','i'):self.out.append('</'+tag+'>')
    def handle_data(self, data):
        if self.in_link:self.out.append(esc(data));return
        for part in re.split(r'(https?://[^\s<>]+)',data):
            if part.startswith(('http://','https://')):
                url=part.rstrip(').,;');tail=part[len(url):]
                self.out.append('<a href="'+esc(url,quote=True)+'">'+esc(url)+'</a>'+esc(tail))
            else:self.out.append(esc(part))
def inline(s):
    p=Inline();p.feed(s);p.close();return ''.join(p.out)
def prose(s):
    return ''.join('<p>'+inline(p.strip()).replace('\n','<br>')+'</p>' for p in re.split(r'\n\s*\n',s.strip()) if p.strip())
def plain(s):return re.sub(r'\s+',' ',re.sub('<[^>]+>',' ',s)).strip()
def image(name, alt, cover=False):
    dst=ROOT/'images'/name
    if not dst.exists():shutil.copy2(ORIGINAL_IMAGES/name,dst)
    dim=subprocess.check_output(['sips','-g','pixelWidth','-g','pixelHeight',str(dst)],text=True)
    w=re.search(r'pixelWidth: (\d+)',dim)[1];h=re.search(r'pixelHeight: (\d+)',dim)[1]
    return f'<img src="images/{esc(name,quote=True)}" alt="{esc(alt,quote=True)}" width="{w}" height="{h}" '+('fetchpriority="high"' if cover else 'loading="lazy"')+'>'

def nav(prefix=''):
    (ROOT/'thumbnails').mkdir(exist_ok=True)
    rows=[]
    for i,(slug,c) in enumerate(zip(slugs,thesis['children']),1):
        thumb=ROOT/'thumbnails'/f'{slug}.jpg'
        if not thumb.exists():
            source=ROOT/'images'/c['art']
            if not source.exists():source=ORIGINAL_IMAGES/c['art']
            subprocess.run(['sips','-Z','160','-s','format','jpeg',str(source),'--out',str(thumb)],check=True,stdout=subprocess.DEVNULL)
        rows.append(f'<a href="{prefix}#{slug}"><img src="thumbnails/{slug}.jpg" alt="" width="48" height="34"><span class="chapter-number">{i:02}</span><span class="chapter-name">{esc(c["label"])}</span></a>')
    return ''.join(rows)
def metadata(reading):
    about=reading=='about'
    url='https://simulate.world/'+('about/' if about else 'reading.html' if reading else '')
    title='Reading list — Simulate World, by Anselm Hook' if reading else 'Simulate World — Civic models, ecology & collective decisions | Anselm Hook'
    description=('Books, essays, organizations and a video presentation on systems thinking, ecology and civic simulation, selected by Anselm Hook.' if reading else 'Anselm Hook’s essay on open digital models, ecology and collective decision-making: giving communities tools to understand and shape their world.')
    if about:
        title='About — Simulate World'
        description='Anselm Hook’s interests in digital twins, whole-system models, and tools for civic understanding.'
    graph={'@context':'https://schema.org','@type':'AboutPage' if about else 'CollectionPage' if reading else 'Article','name':title,'description':description,'url':url,'inLanguage':'en','author':{'@type':'Person','name':'Anselm Hook','url':'https://simulate.world/about/','sameAs':['https://anselm.substack.com/','https://anselm.medium.com/','https://x.com/anselm']},'image':'https://simulate.world/images/glacier.jpg','isPartOf':{'@type':'WebSite','name':'Simulate World','url':'https://simulate.world/'}}
    if not reading:graph.update(headline='Simulate World: Computationally predicting the future of our planet',articleSection=[c['label'] for c in thesis['children']])
    tags=f'<meta name="description" content="{esc(description,quote=True)}"><meta name="author" content="Anselm Hook"><link rel="canonical" href="{url}"><meta name="robots" content="index,follow,max-image-preview:large">'
    for key,value in {'og:type':'website' if reading else 'article','og:site_name':'Simulate World','og:title':title,'og:description':description,'og:url':url,'og:image':'https://simulate.world/images/glacier.jpg','og:image:alt':'A mountain lake beneath a glacier','og:locale':'en_US'}.items():
        tags+=f'<meta property="{key}" content="{esc(value,quote=True)}">'
    for key,value in {'twitter:card':'summary_large_image','twitter:creator':'@anselm','twitter:site':'@orbitalfdn','twitter:title':title,'twitter:description':description,'twitter:image':'https://simulate.world/images/glacier.jpg','twitter:image:alt':'A mountain lake beneath a glacier'}.items():
        tags+=f'<meta name="{key}" content="{esc(value,quote=True)}">'
    return tags+'<script type="application/ld+json">'+json.dumps(graph,ensure_ascii=False).replace('<','\\u003c')+'</script>'

SOCIAL='<div class="social-links"><a href="about/">Anselm Hook ↗</a><a href="https://x.com/orbitalfdn">@orbitalfdn ↗</a></div>'

def shell(title,body,reading=False):
    n=nav('index.html' if reading else '')
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="theme-color" content="#f4f2e9"><title>{title}</title>{metadata(reading)}<link rel="stylesheet" href="style.css"><link rel="stylesheet" href="edition.css?v=20260919-captions"><script src="edition.js" defer></script><noscript><style>@media(max-width:760px){{.sidebar{{display:block;position:static;max-height:none}}.mobile-header button{{display:none}}}}</style></noscript></head><body>
<a class="skip" href="#content">Skip to content</a><header class="mobile-header"><a class="brand" href="index.html">simulate.world<span class="brand-dot">●</span></a><button id="menu-toggle" aria-expanded="false" aria-controls="chapter-nav">Chapters ＋</button></header>
<aside class="sidebar"><div class="palette-heading"><a class="brand desktop-brand" href="index.html">simulate.world<span class="brand-dot">●</span></a><button id="desktop-toggle" aria-expanded="true" aria-controls="chapter-nav" aria-label="Collapse chapter menu">−</button></div><div class="sidebar-center"><p class="eyebrow">An essay in nine chapters</p><nav id="chapter-nav" aria-label="Chapters">{n}</nav><div class="reading-progress" aria-hidden="true"><div id="progress-fill"></div></div></div><div class="sidebar-bottom"><a href="reading.html">Reading list ↗</a><time datetime="2015-06-24">June 24, 2015</time></div></aside>
<main>{body}</main></body></html>'''

# The audited source is authoritative; history retains earlier wording.
def edited_notes(text, chapter, slide):
    return tidy(text)

def render_notes(slide, chapter, position):
    text=edited_notes(slide['notes'],chapter,position)
    if 'statistics' not in slide:return prose(text)
    before,after=text.split('{{drought_statistics}}')
    rows=''.join('<tr>'+''.join('<td>'+esc(cell)+'</td>' for cell in row[:3])+f'<td><a href="{esc(row[4],quote=True)}">{esc(row[3])}</a></td></tr>' for row in slide['statistics'])
    return prose(before)+'<div class="statistics-scroll" tabindex="0" role="region" aria-label="California water statistics"><table class="statistics-table"><caption>California water: quantities, scope and sources</caption><thead><tr><th scope="col">Measure</th><th scope="col">Estimate</th><th scope="col">Scope</th><th scope="col">Source</th></tr></thead><tbody>'+rows+'</tbody></table></div>'+prose(after)

body=f'''<section class="cover" id="top"><div class="edition-cover-image">{image('glacier.jpg','A snowy mountain lake.',True)}</div><div class="cover-shade"></div><div class="cover-top"><span>Ecology · Models · Civic life</span><span>2015</span></div><div class="cover-copy"><p class="eyebrow">World Makers</p><h1>Simulate<br>World.</h1><p>Computationally predicting<br>the future of our planet.</p><a class="cover-author" href="about/">Anselm Hook ↗</a><a class="begin" href="#our-world">Begin the thesis <span aria-hidden="true">↓</span></a></div><div class="cover-bottom"><time datetime="2015-06-24">June 24, 2015</time><span>Nine chapters</span></div></section>
<div id="content"></div>'''
for ci,(slug,chapter) in enumerate(zip(slugs,thesis['children']),1):
    body+=f'<section class="chapter original-chapter" id="{slug}" aria-labelledby="{slug}-title"><header class="chapter-heading"><p class="eyebrow">{ci:02} / {len(thesis["children"]):02} · 2015</p><h2 id="{slug}-title">{esc(chapter["label"])}</h2><p class="chapter-length">{len(chapter["children"])} parts</p></header>'
    for si,slide in enumerate(chapter['children'],1):
        label=tidy(slide.get('label',''));label='Lake Merritt' if label=='Lake Merrit' else label;meaningful=label not in ['nothing','details','', 'disorder']
        captions=[plain(c.get('notes','')).strip() for c in slide.get('children',[]) if c.get('kind')=='text']
        labeltext=' · '.join(captions) if captions else (label if meaningful else chapter['label'])
        body+=f'<article class="original-slide" id="{slug}-{si}" data-source-chapter="{ci}" data-source-slide="{si}"><div class="slide-position"><span>{ci:02}.{si:02}</span><a href="#{slug}-{si}" aria-label="Link to part {si} of {esc(chapter["label"],quote=True)}">Permalink ↗</a></div><figure class="original-figure">{image(slide["art"],labeltext)}'
        if slide.get('image_note'):body+='<figcaption class="image-context">'+inline(tidy(slide['image_note']))+'</figcaption>'
        body+='</figure>'
        if captions:body+='<h3 class="original-caption">'+''.join('<span>'+esc(t)+'</span>' for t in captions)+'</h3>'
        elif meaningful:body+='<h3 class="original-caption">'+esc(label)+'</h3>'
        body+='<div class="prose original-text">'+render_notes(slide,ci,si)+'</div>'
        body+='</article>'
    if ci<len(slugs):body+=f'<a class="next" href="#{slugs[ci]}"><span>Next chapter<strong>{esc(thesis["children"][ci]["label"])}</strong></span><span aria-hidden="true">↗</span></a>'
    else:body+='<a class="next" href="reading.html"><span>Continue exploring<strong>Reading list</strong></span><span aria-hidden="true">↗</span></a>'
    body+='</section>'
body+='''<footer><p class="eyebrow">Simulate World</p><h2>World Makers</h2><p><time datetime="2015-06-24">June 24, 2015</time></p>'''+SOCIAL+'''<div class="footer-bottom"><a href="reading.html">Reading list ↗</a><a href="#top">Back to top ↑</a></div></footer>'''
(ROOT/'index.html').write_text(shell('Simulate World — Civic models &amp; collective decisions | Anselm Hook',body))
print('Rendered',sum(len(c['children']) for c in thesis['children']),'original parts.')
reading=json.loads((ROOT/'reading-data.json').read_text())
r='''<div class="reading-page" id="content"><header><p class="eyebrow">Simulate World · Reading list</p><h1>Reading list.</h1><p>Books, essays, and models for thinking about our world.</p><p class="section-note">A companion to the essay, from ecological relationships and collective decision-making to models we can explore.</p><nav class="reading-nav" aria-label="Reading categories"><a href="#books">Books</a><a href="#papers">Essays &amp; papers</a><a href="#interactive">Interactive reading</a><a href="#news">News &amp; links</a><a href="#organizations">Organizations</a><a href="#voices">Voices</a><a href="#philosophy">Philosophy</a><a href="#models">Models</a></nav></header>'''
r+='''<section class="presentation-link" aria-labelledby="presentation-title"><a class="presentation-thumbnail" href="https://www.youtube.com/watch?v=ibgt7Mbw2tE&amp;t=3s" aria-label="Watch the Simulate World presentation"><img src="images/presentation-thumbnail.jpg" alt="" width="480" height="360"><span aria-hidden="true">▶</span></a><div class="presentation-copy"><p class="eyebrow">Video presentation</p><h2 id="presentation-title"><a href="https://www.youtube.com/watch?v=ibgt7Mbw2tE&amp;t=3s">Watch the Simulate World presentation ↗</a></h2><p>Anselm Hook · YouTube</p></div></section>'''
for section,slug in [('Books','books'),('Essays & papers','papers'),('Interactive reading','interactive')]:
 r+=f'<section id="{slug}"><h2>{esc(section)}</h2>'
 for item in reading:
  if item['section']!=section:continue
  cover=f'<img class="book-cover" src="{esc(item["cover"],quote=True)}" alt="Cover of {esc(item["title"],quote=True)}" loading="lazy">' if item.get('cover') else ''
  lead=cover if cover else f'<span class="year">{item["year"]}</span>'
  date=f'<span class="year">{item["year"]}</span>' if cover else ''
  kind=' book-item' if cover else ''
  r+=f'''<article class="reading-item{kind}">{lead}<div>{date}<h3><a href="{esc(item['url'],quote=True)}">{esc(item['title'])} ↗</a></h3><p class="author">{esc(item['author'])}</p><p>{esc(item['description'])}</p></div></article>'''
 r+='</section>'
# Render the curated resource directory.
resources=json.loads((ROOT/'source/resources.json').read_text())
groups=[]
for item in resources['children']:
 if item['label'].startswith('<h1>'):
  groups.append((plain(item['label']),[]))
 else:groups[-1][1].append(item)
section_ids={'News and Links':'news','Orgs':'organizations','Voices':'voices','Philosophy':'philosophy','Models':'models'}
for name,items in groups:
 title='Organizations' if name=='Orgs' else name
 r+=f'<section class="resource-section" id="{section_ids[name]}"><h2>{esc(title)}</h2><ul class="resource-list">'
 for item in items:
  label=esc(tidy(item['label']));url=item.get('url',item.get('link',''))
  title=f'<a href="{esc(url,quote=True)}">{label} <span aria-hidden="true">↗</span></a>' if url else label
  parent=f'<span class="resource-context">{esc(item["parent"])}</span>' if item.get('parent') else ''
  if name=='Voices':
   portrait=''
   if item.get('portrait'):
    credit=item['portrait_credit']
    portrait=f'<figure class="voice-portrait"><img src="{esc(item["portrait"],quote=True)}" alt="{esc(item["label"],quote=True)}" width="80" height="80" loading="lazy"><figcaption><a href="{esc(credit["source"],quote=True)}">Photo credit</a></figcaption></figure>'
   r+=f'<li class="voice-item">{portrait}<div><h3>{title}</h3><p>{esc(item.get("description",""))}</p></div></li>'
  else:r+=f'<li>{title}{parent}</li>'

 r+='</ul></section>'
r+='<details class="portrait-credits"><summary>Portrait credits</summary><ul>'
for item in resources['children']:
 if item.get('portrait_credit'):
  c=item['portrait_credit']
  r+=f'<li><a href="{esc(c["source"],quote=True)}">{esc(item["label"])}</a> — {esc(c["artist"])}. <a href="{esc(c["license_url"],quote=True)}">{esc(c["license"])}</a>. Displayed as a square crop.</li>'
r+='</ul></details>'
r+='''<div class="reading-footer">'''+SOCIAL+'''<div class="edition-links"><a href="index.html">Return to the essay ↗</a></div></div></div>'''
(ROOT/'reading.html').write_text(shell('Reading list — Simulate World (2015)',r,True))

# A brief author page, separate from the essay’s period argument.
about_body='''<div class="reading-page about-page" id="content"><header><p class="eyebrow">Simulate World</p><h1>About.</h1></header><p>I’m Anselm Hook. I’m interested in digital twins and models of whole systems: ways to make the relationships between people, places, and the environment easier to see.</p><p>I’d like these tools to help people understand their surroundings, explore possible futures, and take a more informed part in civic decisions. Simulate World is an essay about that possibility.</p><nav class="about-links" aria-label="More from Anselm"><a href="https://anselm.substack.com/" rel="me">Substack ↗</a><a href="https://anselm.medium.com/" rel="me">Medium ↗</a><a href="https://x.com/anselm" rel="me">@anselm on X ↗</a><a href="https://x.com/orbitalfdn">@orbitalfdn on X ↗</a></nav><div class="reading-footer"><a href="index.html">Read the essay ↗</a><a href="reading.html">Reading list ↗</a></div></div>'''
about_html=shell('About — Simulate World',about_body,True).replace(metadata(True),metadata('about')).replace('<head>','<head><base href="../">')
(ROOT/'about').mkdir(exist_ok=True)
(ROOT/'about/index.html').write_text(about_html)
