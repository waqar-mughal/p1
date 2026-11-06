HTML = r"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>P1 — Personal Creator</title>
<style>
:root{color-scheme:dark;--bg:#0b111a;--panel:#141e2b;--panel2:#1b2939;--line:#2a3a4e;--text:#edf4fb;--muted:#9aabc0;--mint:#a9d9c5;--mint2:#d5f2e6;--red:#f0a5a5}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--text);font:14px Inter,system-ui,-apple-system,"Segoe UI",sans-serif}button,input,textarea,select{font:inherit}button{cursor:pointer}
.layout{min-height:100vh;display:grid;grid-template-columns:230px 1fr}aside{background:#101925;border-right:1px solid var(--line);padding:25px 16px;display:flex;flex-direction:column;gap:28px}.brand{display:flex;align-items:center;gap:10px;padding:0 8px}.logo{width:36px;height:36px;border-radius:12px;background:var(--mint);color:#10251c;display:grid;place-items:center;font-weight:900;font-size:20px}.brand strong{font-size:17px}.brand small{display:block;color:var(--muted);font-size:11px;margin-top:2px}.label{font-size:10px;color:#71839b;font-weight:800;letter-spacing:1.4px;padding:0 10px;margin-bottom:8px}.nav{display:grid;gap:5px}.nav button{border:0;background:transparent;color:#aebbd0;text-align:left;padding:11px;border-radius:10px}.nav button:hover,.nav button.active{background:#213044;color:var(--mint2)}.nav button span{display:inline-block;width:25px;color:var(--mint)}.side-note{margin-top:auto;border:1px solid var(--line);background:var(--panel);border-radius:12px;padding:13px;color:var(--muted);font-size:11px;line-height:1.6}
main{width:100%;max-width:1200px;margin:auto;padding:34px clamp(18px,5vw,60px) 55px}.top{display:flex;justify-content:space-between;align-items:flex-start;gap:15px;margin-bottom:28px}.eyebrow{font-size:10px;letter-spacing:1.6px;color:var(--mint);font-weight:800}.top h1{font-size:clamp(26px,4vw,36px);letter-spacing:-1px;margin:8px 0}.sub{color:var(--muted);line-height:1.6;max-width:690px}.status,.pill{border:1px solid var(--line);background:var(--panel);border-radius:30px;padding:8px 12px;color:var(--muted);font-size:11px;white-space:nowrap}.dot{display:inline-block;width:7px;height:7px;background:var(--mint);border-radius:50%;margin-right:7px}
.view{display:none}.view.active{display:block}.cards{display:grid;grid-template-columns:repeat(3,1fr);gap:13px;margin:22px 0}.card,.panel{background:var(--panel);border:1px solid var(--line);border-radius:15px;padding:17px}.card{min-height:122px}.card .icon{font-size:20px}.card h3{font-size:14px;margin:12px 0 5px}.card p,.muted{font-size:12px;color:var(--muted);line-height:1.6;margin:0}.section-head{display:flex;align-items:center;justify-content:space-between;gap:12px;margin:27px 0 12px}.section-head h2{font-size:16px;margin:0}.primary,.secondary,.danger{border-radius:10px;padding:10px 14px;font-weight:700}.primary{background:var(--mint);color:#10251c;border:0}.secondary{background:#1d2a3a;color:var(--text);border:1px solid var(--line)}.danger{background:#39242a;color:#ffd6d6;border:1px solid #68434a}.composer{background:linear-gradient(145deg,#19283a,#121b28);border:1px solid var(--line);border-radius:17px;padding:20px}.composer textarea,.field,select{width:100%;background:#0d1723;border:1px solid #34475e;color:var(--text);padding:12px;border-radius:10px;outline:none}.composer textarea{min-height:100px;resize:vertical}.composer textarea:focus,.field:focus,select:focus{border-color:var(--mint)}.row{display:grid;grid-template-columns:repeat(2,1fr);gap:13px;margin:13px 0}.field-label{display:block;color:var(--muted);font-size:11px;margin:0 0 7px}.actions{display:flex;gap:9px;flex-wrap:wrap;margin-top:14px}.message-list{display:grid;gap:10px;max-height:420px;overflow:auto;margin-top:15px}.message{padding:13px;border-radius:11px;white-space:pre-wrap;line-height:1.6;font-size:13px;max-width:95%}.assistant{background:#223145}.user{background:#315544;justify-self:end}.prompt{border:1px solid var(--line);background:#1b2939;color:#c4d2e2;border-radius:30px;padding:8px 11px;font-size:11px}.prompt:hover{border-color:var(--mint)}.list{display:grid;gap:10px}.item{display:flex;align-items:center;justify-content:space-between;gap:14px;padding:14px;border:1px solid var(--line);background:#111b28;border-radius:12px}.item strong{font-size:13px}.item small{display:block;color:var(--muted);margin-top:5px;font-size:11px}.empty{padding:26px;text-align:center;border:1px dashed #3a4b60;border-radius:13px;color:var(--muted);line-height:1.7}.calendar{display:grid;grid-template-columns:repeat(7,1fr);gap:7px}.day{border:1px solid var(--line);background:#111b28;border-radius:9px;min-height:86px;padding:9px;font-size:11px;color:var(--muted)}.day strong{display:block;color:var(--text);margin-bottom:8px}.notice{font-size:11px;color:var(--muted);line-height:1.65;margin-top:15px}.notice strong{color:var(--mint2)}.hidden{display:none!important}
@media(max-width:760px){.layout{grid-template-columns:1fr}aside{padding:12px;gap:12px;border-right:0;border-bottom:1px solid var(--line)}aside .label,aside .side-note{display:none}.nav{display:flex;overflow:auto}.nav button{white-space:nowrap;padding:9px}.brand{padding:3px 8px}main{padding:23px 15px}.cards{grid-template-columns:1fr}.row{grid-template-columns:1fr}.top{flex-direction:column}.calendar{grid-template-columns:repeat(2,1fr)}}
</style></head>
<body><div class="layout">
<aside>
 <div class="brand"><div class="logo">P</div><div><strong>P1 Creator</strong><small>Your personal content studio</small></div></div>
 <div><div class="label">WORKSPACE</div><nav class="nav">
  <button class="active" data-view="home"><span>⌂</span>Home</button>
  <button data-view="create"><span>✦</span>Create</button>
  <button data-view="projects"><span>▦</span>My Projects</button>
  <button data-view="social"><span>◎</span>Social Accounts</button>
  <button data-view="calendar"><span>▤</span>Calendar</button>
  <button data-view="approvals"><span>✓</span>Approvals</button>
 </nav></div>
 <div class="side-note">Made for creators with ideas. Start with a thought, build it into content, and stay in control before anything is published.<br><br><strong style="color:var(--mint2)">P1 · Prototype</strong></div>
</aside>
<main>
 <header class="top"><div><div class="eyebrow">YOUR CREATIVE WORKSPACE</div><h1 id="page-title">Turn your ideas into content.</h1><div class="sub" id="page-sub">Plan a story, shape a script and build your next piece of content — without needing to appear on camera.</div></div><div class="status"><span class="dot"></span><span id="status">Checking app…</span></div></header>

 <section class="view active" id="view-home">
  <div class="cards">
   <article class="card"><div class="icon">✦</div><h3>Ideas & research</h3><p>Turn a rough thought into a clear content idea and outline.</p></article>
   <article class="card"><div class="icon">▤</div><h3>Scripts & stories</h3><p>Shape hooks, narration and scene-by-scene storyboards.</p></article>
   <article class="card"><div class="icon">◉</div><h3>Faceless content</h3><p>Plan narration, visuals and captions without appearing on camera.</p></article>
  </div>
  <div class="section-head"><h2>What would you like to create today?</h2><button class="primary" data-go="create">Start creating →</button></div>
  <div class="composer"><textarea id="home-idea" placeholder="Tell P1 your idea. You can write naturally — for example, “I want a motivational video about starting again after failure.”"></textarea><div class="actions"><button class="secondary" id="home-voice" type="button">🎙 Voice input (not connected)</button><button class="primary" id="home-create" type="button">Create my content →</button></div><div class="notice">You can type your idea now. Voice recording will be added in a later phase.</div></div>
  <div class="section-head"><h2>Recent projects</h2><button class="secondary" data-go="projects">View all</button></div><div id="home-projects" class="list"><div class="empty">Your saved drafts will appear here.</div></div>
 </section>

 <section class="view" id="view-create">
  <div class="section-head"><h2>Let's shape your idea</h2><span class="pill">Beginner workflow</span></div>
  <div class="composer">
   <label class="field-label" for="idea">1 · Describe what you want to create</label>
   <textarea id="idea" placeholder="Example: A 30-second emotional video about someone who loses everything but finds the courage to start again."></textarea>
   <div class="row">
    <div><label class="field-label" for="format">2 · Content format</label><select id="format"><option>Short video / Reel</option><option>YouTube video</option><option>Instagram Story</option><option>Image post</option><option>Carousel</option><option>Audio narration</option><option>Article</option></select></div>
    <div><label class="field-label" for="duration">3 · Length</label><select id="duration"><option>30 seconds</option><option>60 seconds</option><option>90 seconds</option><option>3 minutes</option><option>5 minutes</option></select></div>
    <div><label class="field-label" for="tone">4 · Style / tone</label><select id="tone"><option>Emotional</option><option>Motivational</option><option>Educational</option><option>Professional</option><option>Funny and entertaining</option><option>Storytelling</option></select></div>
    <div><label class="field-label" for="camera">5 · On-camera preference</label><select id="camera"><option>Faceless — do not show me</option><option>AI avatar</option><option>I will appear on camera</option><option>No preference</option></select></div>
   </div>
   <div class="row">
    <div><label class="field-label" for="language">Language</label><select id="language"><option>English</option><option>Urdu</option><option>Roman Urdu</option><option>English and Urdu</option></select></div>
    <div><label class="field-label" for="platform">Main platform</label><select id="platform"><option>Instagram</option><option>YouTube</option><option>Facebook</option><option>TikTok</option><option>Multiple platforms</option><option>Not decided</option></select></div>
   </div>
   <div class="actions"><button class="primary" id="generate">Generate my draft →</button><button class="secondary" id="clear-create">Clear</button></div>
  </div>
  <div class="section-head"><h2>Draft and assistant conversation</h2><span class="pill">You approve every step</span></div>
  <div id="create-messages" class="message-list"><div class="empty">Your script concept and production outline will appear here after you generate a draft.</div></div>
  <div class="notice">This prototype creates a text-based sample plan. It does not yet generate a finished video, voice, avatar or images.</div>
 </section>

 <section class="view" id="view-projects">
  <div class="section-head"><h2>Your content workspace</h2><button class="primary" data-go="create">+ New project</button></div>
  <div id="project-list" class="list"><div class="empty">No projects saved yet. Create a draft to see it here.</div></div>
  <div class="notice">Projects are currently saved in this browser only. Cloud sync and user accounts are not implemented.</div>
 </section>

 <section class="view" id="view-social">
  <div class="section-head"><h2>Connect your social accounts</h2><span class="pill">Connections unavailable</span></div>
  <div class="cards">
   <article class="card"><div class="icon">◎</div><h3>Instagram</h3><p>Professional Creator or Business account connection will be supported after Meta app setup and permission approval.</p><div class="actions"><span class="pill">Not connected</span><button class="secondary" disabled>Connect later</button></div></article>
   <article class="card"><div class="icon">f</div><h3>Facebook Pages</h3><p>Page publishing and insights require an authorized Page and approved Meta permissions.</p><div class="actions"><span class="pill">Not connected</span><button class="secondary" disabled>Connect later</button></div></article>
   <article class="card"><div class="icon">▶</div><h3>YouTube</h3><p>Channel uploads and management require Google OAuth consent and YouTube API configuration.</p><div class="actions"><span class="pill">Not connected</span><button class="secondary" disabled>Connect later</button></div></article>
  </div>
  <div class="panel"><h3>Permission and safety principle</h3><p class="muted">P1 will request only the permissions needed for a selected feature. You will be able to review the requested access and disconnect an account. No account is connected in this prototype, and no content can be published from this screen.</p></div>
 </section>

 <section class="view" id="view-calendar">
  <div class="section-head"><h2>Publishing calendar</h2><span class="pill">Preview only</span></div>
  <div class="panel"><p class="muted">Your planned content schedule will appear here. Live scheduling and publishing are not connected yet.</p><div class="calendar" id="calendar-grid"></div></div>
  <div class="notice">Calendar entries are a visual placeholder in this first UI pass. No posts will be scheduled or sent to social platforms.</div>
 </section>

 <section class="view" id="view-approvals">
  <div class="section-head"><h2>Review before anything goes out</h2><span class="pill">User approval required</span></div>
  <div id="approval-list" class="list"><div class="empty">No approval requests are available yet.</div></div>
  <div class="notice">The approval list reads the prototype API. Final publishing actions will be added only after social account authorization and explicit confirmation.</div>
 </section>
</main></div>
<script>
const titles={home:['Turn your ideas into content.','Plan a story, shape a script and build your next piece of content — without needing to appear on camera.'],create:['Create something worth sharing.','Describe your idea and P1 will help shape a first draft.'],projects:['Your projects.','Keep your drafts and ideas together.'],social:['Your social accounts.','Connect accounts only when the secure authorization flow is ready.'],calendar:['Plan your publishing.','See what you intend to share and when.'],approvals:['Nothing publishes without your say-so.','Review content before any future publishing action.']};
function showView(name){document.querySelectorAll('.view').forEach(x=>x.classList.toggle('active',x.id==='view-'+name));document.querySelectorAll('[data-view]').forEach(x=>x.classList.toggle('active',x.dataset.view===name));document.querySelector('#page-title').textContent=titles[name][0];document.querySelector('#page-sub').textContent=titles[name][1];if(name==='projects')renderProjects();if(name==='approvals')loadApprovals();}
document.querySelectorAll('[data-view]').forEach(b=>b.addEventListener('click',()=>showView(b.dataset.view)));document.querySelectorAll('[data-go]').forEach(b=>b.addEventListener('click',()=>showView(b.dataset.go)));
const storeKey='p1.creator.projects.v1';function getProjects(){try{return JSON.parse(localStorage.getItem(storeKey)||'[]')}catch{return []}}function saveProject(p){const list=getProjects();list.unshift(p);localStorage.setItem(storeKey,JSON.stringify(list.slice(0,40)));renderProjects();}
function renderProjects(){const list=getProjects();const html=list.length?list.map(p=>'<div class="item"><div><strong>'+escapeHtml(p.title)+'</strong><small>'+escapeHtml(p.format)+' · '+escapeHtml(p.created)+'</small></div><span class="pill">Draft</span></div>').join(''):'<div class="empty">No projects saved yet. Create a draft to see it here.</div>';document.querySelector('#project-list').innerHTML=html;document.querySelector('#home-projects').innerHTML=list.length?list.slice(0,3).map(p=>'<div class="item"><div><strong>'+escapeHtml(p.title)+'</strong><small>'+escapeHtml(p.format)+' · '+escapeHtml(p.created)+'</small></div><span class="pill">Draft</span></div>').join(''):'<div class="empty">Your saved drafts will appear here.</div>';}
function escapeHtml(s){return String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));}
function addMessage(target,text,kind){const box=document.querySelector(target);if(box.querySelector('.empty'))box.innerHTML='';const el=document.createElement('div');el.className='message '+kind;el.textContent=text;box.appendChild(el);box.scrollTop=box.scrollHeight;}
async function requestDraft(message,target){addMessage(target,message,'user');const box=document.querySelector(target);const loading=document.createElement('div');loading.className='message assistant';loading.textContent='P1 is preparing your draft…';box.appendChild(loading);try{const response=await fetch('/api/chat',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({message})});const data=await response.json();if(!response.ok)throw new Error(data.detail||'Assistant request failed');loading.textContent=data.reply;const project={title:message.length>65?message.slice(0,62)+'…':message,format:document.querySelector('#format')?.value||'Content idea',created:new Date().toLocaleString()};saveProject(project);return data;}catch(err){loading.textContent='Could not create a draft: '+err.message;return null;}}
document.querySelector('#home-create').addEventListener('click',()=>{const idea=document.querySelector('#home-idea').value.trim();if(!idea){showView('create');document.querySelector('#idea').focus();return;}document.querySelector('#idea').value=idea;showView('create');});
document.querySelector('#home-voice').addEventListener('click',()=>alert('Voice input is planned but is not connected in this prototype. You can type your idea for now.'));
document.querySelector('#generate').addEventListener('click',async()=>{const idea=document.querySelector('#idea').value.trim();if(!idea){document.querySelector('#idea').focus();return;}const details='Create a content draft with these preferences. Idea: '+idea+'; format: '+document.querySelector('#format').value+'; duration: '+document.querySelector('#duration').value+'; tone: '+document.querySelector('#tone').value+'; camera preference: '+document.querySelector('#camera').value+'; language: '+document.querySelector('#language').value+'; platform: '+document.querySelector('#platform').value+'. Please provide a hook, a script and a scene-by-scene production outline.';const button=document.querySelector('#generate');button.disabled=true;button.textContent='Creating…';await requestDraft(details,'#create-messages');button.disabled=false;button.textContent='Generate my draft →';});
document.querySelector('#clear-create').addEventListener('click',()=>{document.querySelector('#idea').value='';document.querySelector('#create-messages').innerHTML='<div class="empty">Your script concept and production outline will appear here after you generate a draft.</div>';});
async function loadApprovals(){const box=document.querySelector('#approval-list');try{const r=await fetch('/api/approvals');const data=await r.json();if(!data.items||!data.items.length){box.innerHTML='<div class="empty">No approval requests are available yet.</div>';return;}box.innerHTML=data.items.map(item=>'<div class="item"><div><strong>'+escapeHtml(item.title||item.name||'Content approval')+'</strong><small>'+escapeHtml(item.status||'Awaiting review')+'</small></div><span class="pill">Review</span></div>').join('');}catch{box.innerHTML='<div class="empty">Could not load approval requests from the local app.</div>';}}
function buildCalendar(){const grid=document.querySelector('#calendar-grid');const days=['Mon','Tue','Wed','Thu','Fri','Sat','Sun'];grid.innerHTML=days.map((d,i)=>'<div class="day"><strong>'+d+'</strong>'+(i===1?'Draft ideas':i===4?'Review content':'—')+'</div>').join('');}
fetch('/api/health').then(r=>r.json()).then(d=>{document.querySelector('#status').textContent=d.mode==='demo'?'Demo mode · no paid API':'Live AI mode';}).catch(()=>{document.querySelector('#status').textContent='App unavailable';});
renderProjects();buildCalendar();
</script></body></html>"""
