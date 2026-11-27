from pathlib import Path
from playwright.sync_api import sync_playwright
import sys
base=Path(sys.argv[1] if len(sys.argv)>1 else '/mnt/data/JARVIS14-MasterAccess/index.html'); new=Path(__file__).resolve().parents[1]/'index.html'
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox','--disable-dev-shm-usage'],headless=True)
 def load(path):
  page=b.new_page(); errs=[];page.on('pageerror',lambda e:errs.append(str(e)));page.route('**/*',lambda r:r.abort())
  page.evaluate('''(()=>{const m=new Map();Object.defineProperty(window,'localStorage',{value:{getItem:k=>m.has(k)?m.get(k):null,setItem:(k,v)=>m.set(k,String(v)),removeItem:k=>m.delete(k),clear:()=>m.clear(),key:i=>[...m.keys()][i],get length(){return m.size}}})})();''')
  page.set_content(path.read_text(),wait_until='domcontentloaded');return page,errs
 page,errs=load(base);old=page.evaluate('modules.map(m=>m.c)');oldcmd=page.evaluate('infCommands().map(m=>m.id)');page.close()
 page,errs=load(new);ids=page.evaluate('modules.map(m=>m.c)');cmd=page.evaluate('infCommands().map(m=>m.id)');assert set(old)<=set(ids) and len(ids)==len(set(ids))==84;assert set(oldcmd)<=set(cmd) and len(cmd)==208;assert 'THE ONE PROTOCOL' in page.locator('.royal-sub').inner_text();page.evaluate("run('/theone')");assert 'THE ONE PROTOCOL' in page.locator('#resulttitle').inner_text()
 u=page.get_by_label('Your private portal HTTPS Worker URL');u.fill('http://example.workers.dev/');page.get_by_role('button',name='Save portal address').click();assert 'Enter your own HTTPS' in page.locator('#v3Panel').inner_text();u.fill('https://my-owner-portal.example.workers.dev/');page.get_by_role('button',name='Save portal address').click();assert 'Saved locally' in page.locator('#v3Panel').inner_text();assert not errs,errs
 print(f'PASS: {len(old)} original modules, {len(oldcmd)} commands; {len(ids)} unique modules and {len(cmd)} commands; title, new route, safe URL input, no runtime errors. Isolated DOM and localStorage test.')
 b.close()
