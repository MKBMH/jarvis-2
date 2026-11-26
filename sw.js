const CACHE = 'jarvis2-v10-traffic-20261126-1';
self.addEventListener('install', event => {
  event.waitUntil((async () => {
    const cache = await caches.open(CACHE);
    await cache.addAll(['./','./index.html'].map(url => new Request(url,{cache:'reload'})));
    await Promise.allSettled(['./manifest.webmanifest','./icon-192.png','./icon-512.png'].map(url => cache.add(new Request(url,{cache:'reload'}))));
    await self.skipWaiting();
  })());
});
self.addEventListener('activate', event => {
  event.waitUntil((async () => {
    await Promise.all((await caches.keys()).filter(k => k.startsWith('jarvis2-') && k !== CACHE).map(k => caches.delete(k)));
    await self.clients.claim();
  })());
});
self.addEventListener('fetch', event => {
  const req=event.request;
  if(req.method!=='GET'||new URL(req.url).origin!==self.location.origin)return;
  event.respondWith((async()=>{
    try { return await fetch(req,{cache:req.mode==='navigate'?'no-store':'default'}); }
    catch { const c=await caches.open(CACHE); return (await c.match(req))||(req.mode==='navigate'?await c.match('./index.html'):null)||Response.error(); }
  })());
});
