HTML = r"""<!doctype html>
<html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Personal Agent</title>
<style>
body{margin:0;background:#10131a;color:#edf0f6;font:15px Segoe UI,Arial;display:grid;place-items:center;min-height:100vh}
main{width:min(900px,94vw);height:min(850px,94vh);display:flex;flex-direction:column;background:#191e28;border:1px solid #303848;border-radius:18px;overflow:hidden}
header,footer{padding:16px 20px;border-bottom:1px solid #303848}h1{font-size:18px;margin:0}.muted{color:#9ca8bb;font-size:12px}
#messages{padding:20px;overflow:auto;flex:1;display:flex;flex-direction:column;gap:12px}
.msg{padding:12px 15px;border-radius:14px;max-width:82%;white-space:pre-wrap;line-height:1.45}.user{align-self:flex-end;background:#294b72}.agent{align-self:flex-start;background:#252d3a}
form{display:flex;gap:10px;padding:16px;border-top:1px solid #303848}
textarea{flex:1;min-height:52px;max-height:150px;background:#101620;color:white;border:1px solid #39465a;border-radius:12px;padding:12px;font:inherit}
button{background:#75a9e8;color:#07111f;border:0;border-radius:12px;padding:0 20px;font-weight:700;cursor:pointer}button:disabled{opacity:.5}
</style></head><body><main>
<header><h1>Personal Agent</h1><div class="muted">Phase 1 · local development · <span id="status">Connecting</span></div></header>
<section id="messages"><div class="msg agent">Hello. Tell me what you want to accomplish. I can plan and work with files in my restricted workspace.</div></section>
<form id="form"><textarea id="input" placeholder="Tell your agent what to do…" required></textarea><button id="send">Send</button></form>
<footer class="muted">Development mode. Keep this service private. Consequential external actions require approval.</footer>
</main><script>
let cid=null;const box=document.querySelector('#messages'),input=document.querySelector('#input'),send=document.querySelector('#send'),status=document.querySelector('#status');
function add(t,c){let d=document.createElement('div');d.className='msg '+c;d.textContent=t;box.appendChild(d);box.scrollTop=box.scrollHeight;}
fetch('/api/health').then(r=>r.json()).then(()=>status.textContent='Online').catch(()=>status.textContent='Offline');
document.querySelector('#form').addEventListener('submit',async e=>{e.preventDefault();let message=input.value.trim();if(!message)return;add(message,'user');input.value='';send.disabled=true;status.textContent='Working…';
try{let r=await fetch('/api/chat',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({message,conversation_id:cid})});let data=await r.json();if(!r.ok)throw Error(data.detail||'Request failed');cid=data.conversation_id;add(data.reply,'agent');status.textContent='Online';}
catch(err){add('Error: '+err.message,'agent');status.textContent='Error';}finally{send.disabled=false;input.focus();}});
</script></body></html>"""
