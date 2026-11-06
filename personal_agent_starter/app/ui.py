HTML = r"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>P1 — Personal Creator</title>
<style>
:root{color-scheme:dark;--bg:#0c1018;--panel:#141b27;--panel2:#192333;--line:#293548;--text:#edf3fc;--muted:#91a0b5;--accent:#a9d6c4;--accent2:#d1f0e4}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--text);font:14px Inter,ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif}
button,textarea{font:inherit}.app{min-height:100vh;display:grid;grid-template-columns:238px 1fr}
aside{padding:25px 17px;border-right:1px solid var(--line);background:#101722;display:flex;flex-direction:column;gap:25px}
.brand{display:flex;align-items:center;gap:11px;padding:0 8px}.logo{width:35px;height:35px;border-radius:12px;background:var(--accent);color:#12221d;display:grid;place-items:center;font-weight:900;font-size:19px}.brand strong{font-size:17px;letter-spacing:.4px}.brand small{display:block;color:var(--muted);font-size:11px;margin-top:2px}
.nav-label{color:#6f8098;font-size:10px;font-weight:800;letter-spacing:1.4px;padding:0 10px;margin-bottom:7px}.nav{display:grid;gap:5px}.nav button{border:0;background:transparent;color:#aab7c9;text-align:left;padding:11px 12px;border-radius:10px;cursor:pointer}.nav button.active,.nav button:hover{background:#202c3c;color:var(--accent2)}.nav button span{display:inline-block;width:24px;color:var(--accent)}
.aside-bottom{margin-top:auto;border:1px solid var(--line);background:var(--panel);padding:13px;border-radius:12px;color:var(--muted);font-size:12px;line-height:1.6}
main{max-width:1200px;width:100%;margin:auto;padding:35px clamp(20px,5vw,64px) 50px}.top{display:flex;justify-content:space-between;align-items:center;gap:15px;margin-bottom:35px}.eyebrow{color:var(--accent);font-size:11px;font-weight:800;letter-spacing:1.6px;text-transform:uppercase}h1{font-size:clamp(26px,4vw,38px);letter-spacing:-1.2px;margin:9px 0}.sub{color:var(--muted);font-size:14px;line-height:1.6}.status{border:1px solid var(--line);background:var(--panel);border-radius:30px;padding:9px 13px;color:var(--muted);font-size:11px;white-space:nowrap}.dot{display:inline-block;width:7px;height:7px;border-radius:50%;background:var(--accent);margin-right:7px}
.grid{display:grid;grid-template-columns:repeat(3,1fr);gap:13px;margin:26px 0}.card{border:1px solid var(--line);background:var(--panel);border-radius:15px;padding:17px;min-height:122px}.card .icon{font-size:19px}.card h3{font-size:14px;margin:12px 0 5px}.card p{color:var(--muted);font-size:12px;line-height:1.5;margin:0}.section-title{font-size:15px;margin:30px 0 12px}.workbench{border:1px solid var(--line);background:linear-gradient(145deg,#172333,#121a27);border-radius:18px;padding:21px}.workbench-head{display:flex;justify-content:space-between;align-items:center;gap:10px;margin-bottom:12px}.workbench-head h2{font-size:16px;margin:0}.tag{color:var(--accent);font-size:10px;border:1px solid #38564d;padding:5px 8px;border-radius:20px}
#messages{display:flex;flex-direction:column;gap:10px;max-height:370px;overflow:auto;padding:8px 2px}.msg{white-space:pre-wrap;line-height:1.65;padding:13px 15px;border-radius:13px;max-width:90%;font-size:13px}.agent{background:#202c3b;color:#e8eef8;align-self:flex-start}.user{background:#315344;color:white;align-self:flex-end}
form{display:flex;gap:10px;margin-top:14px}textarea{flex:1;min-height:54px;max-height:140px;resize:vertical;background:#0e1621;border:1px solid #34445a;border-radius:12px;color:white;padding:14px;outline:none}textarea:focus{border-color:var(--accent)}.send{border:0;border-radius:12px;padding:0 22px;background:var(--accent);color:#10221b;font-weight:800;cursor:pointer}.send:disabled{opacity:.5}
.prompts{display:flex;gap:8px;flex-wrap:wrap;margin-top:12px}.prompt{background:#1b2938;color:#b9c8d8;border:1px solid var(--line);padding:8px 11px;border-radius:20px;font-size:11px;cursor:pointer}.prompt:hover{border-color:var(--accent);color:var(--accent2)}
.notice{font-size:11px;color:var(--muted);line-height:1.6;margin-top:16px}.footer{margin-top:28px;color:#64748b;font-size:11px}
@media(max-width:760px){.app{grid-template-columns:1fr}aside{display:none}main{padding:25px 17px}.grid{grid-template-columns:1fr}.top{align-items:flex-start;flex-direction:column}.status{align-self:flex-start}form{flex-direction:column}.send{padding:14px}}
</style>
</head>
<body><div class="app">
<aside>
 <div class="brand"><div class="logo">P</div><div><strong>P1 Creator</strong><small>Your personal content studio</small></div></div>
 <div><div class="nav-label">WORKSPACE</div><nav class="nav">
  <button class="active" type="button"><span>⌂</span> Overview</button>
  <button type="button" title="Coming in a later phase"><span>✧</span> AI Content Studio</button>
  <button type="button" title="Coming in a later phase"><span>▦</span> Content Library</button>
  <button type="button" title="Coming in a later phase"><span>▤</span> Social Planner</button>
 </nav></div>
 <div><div class="nav-label">ACCOUNT</div><nav class="nav">
  <button type="button" title="Coming in a later phase"><span>⚙</span> Settings</button>
 </nav></div>
 <div class="aside-bottom">Built for people with ideas who want to create content without being on camera.<br><br><strong style="color:var(--accent2)">P1 · Early prototype</strong></div>
</aside>
<main>
 <div class="top"><div><div class="eyebrow">YOUR CREATIVE WORKSPACE</div><h1>Turn your ideas into content.</h1><div class="sub">Plan a story, shape a script and build your next piece of content — without needing to appear on camera.</div></div><div class="status"><span class="dot"></span><span id="status">Checking app…</span></div></div>
 <div class="grid">
  <div class="card"><div class="icon">✦</div><h3>Ideas & research</h3><p>Find a useful angle and turn a rough thought into a clear content idea.</p></div>
  <div class="card"><div class="icon">▤</div><h3>Scripts & stories</h3><p>Shape hooks, narration and scene-by-scene outlines for short videos.</p></div>
  <div class="card"><div class="icon">◉</div><h3>Faceless content</h3><p>Plan narration, visuals and captions without recording yourself on camera.</p></div>
 </div>
 <div class="section-title">Start creating</div>
 <section class="workbench">
  <div class="workbench-head"><h2>Talk to your creative assistant</h2><span class="tag">P1 ASSISTANT</span></div>
  <div id="messages"><div class="msg agent">Welcome to P1. Tell me what you want to create. For example, share a topic and I can help shape it into a short-video concept, hook, script and production outline. This first version runs in demo mode, so no paid AI key is needed.</div></div>
  <form id="form"><textarea id="input" placeholder="I want to create a faceless video about…" required></textarea><button class="send" id="send">Create draft ↗</button></form>
  <div class="prompts">
   <button class="prompt" type="button" data-prompt="Give me 5 faceless YouTube video ideas about personal growth.">5 video ideas</button>
   <button class="prompt" type="button" data-prompt="Write a 30-second Instagram Reel script about building good habits.">Write a Reel script</button>
   <button class="prompt" type="button" data-prompt="Help me plan a motivational short video with narration and visual scenes.">Plan a short video</button>
  </div>
  <div class="notice">Demo mode: the interface and sample workflow work without a paid API. Live AI research, custom image/video/avatar generation, voice generation and social publishing are not connected yet.</div>
 </section>
 <div class="footer">P1 Personal Creator · Private development prototype · Do not use for public customer data yet.</div>
</main></div>
<script>
let cid=null;
const box=document.querySelector('#messages'),input=document.querySelector('#input'),send=document.querySelector('#send'),status=document.querySelector('#status');
function add(text,kind){const node=document.createElement('div');node.className='msg '+kind;node.textContent=text;box.appendChild(node);box.scrollTop=box.scrollHeight;}
fetch('/api/health').then(r=>r.json()).then(data=>{status.textContent=data.mode==='demo'?'Demo mode · no API key':'Live AI mode';}).catch(()=>{status.textContent='Server unavailable';});
document.querySelectorAll('[data-prompt]').forEach(button=>button.addEventListener('click',()=>{input.value=button.dataset.prompt;input.focus();}));
document.querySelector('#form').addEventListener('submit',async event=>{
 event.preventDefault();const message=input.value.trim();if(!message)return;
 add(message,'user');input.value='';send.disabled=true;send.textContent='Working…';status.textContent='Creating draft…';
 try{const response=await fetch('/api/chat',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({message,conversation_id:cid})});const data=await response.json();if(!response.ok)throw new Error(data.detail||'Request failed');cid=data.conversation_id;add(data.reply,'agent');status.textContent=data.mode==='demo'?'Demo mode · no API key':'Live AI mode';}
 catch(error){add('Could not reach the assistant: '+error.message,'agent');status.textContent='Connection error';}
 finally{send.disabled=false;send.textContent='Create draft ↗';input.focus();}
});
</script></body></html>"""
