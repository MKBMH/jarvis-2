const CACHE='jarvis2-v3-20261126-mandai4';
const FILES=['./','./index.html','./manifest.webmanifest','./icon-192.png','./icon-512.png'];
self.addEventListener('install',e=>e.waitUntil(caches.open(CACHE).then(c=>c.addAll(['./','./index.html'].map(url=>new Request(url,{cache:'reload'}))).then(()=>Promise.allSettled(FILES.slice(2).map(url=>c.add(new Request(url,{cache:'reload'})))))).then(()=>self.skipWaiting())));
self.addEventListener('activate',e=>e.waitUntil(caches.keys().then(keys=>Promise.all(keys.filter(k=>k.startsWith('jarvis2-')&&k!==CACHE).map(k=>caches.delete(k)))).then(()=>self.clients.claim())));
self.addEventListener('fetch',e=>{if(e.request.method!=='GET'||new URL(e.request.url).origin!==location.origin)return;e.respondWith(fetch(e.request).catch(()=>caches.open(CACHE).then(c=>c.match(e.request)).then(r=>r||(e.request.mode==='navigate'?caches.open(CACHE).then(c=>c.match('./index.html')).then(r=>r||Response.error()):Response.error()))))});
