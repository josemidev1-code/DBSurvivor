// Servidor local mínimo para depurar en el navegador: node herramientas/servidor.cjs [puerto]
const http=require('node:http'),fs=require('node:fs'),path=require('node:path');
const raiz=path.resolve(__dirname,'..'),port=+process.env.PORT||+process.argv[2]||8765;
const T={'.html':'text/html; charset=utf-8','.js':'text/javascript; charset=utf-8','.css':'text/css','.png':'image/png','.json':'application/json','.gif':'image/gif','.jpg':'image/jpeg','.mp3':'audio/mpeg','.ogg':'audio/ogg','.wav':'audio/wav','.webp':'image/webp'};
http.createServer((q,r)=>{let f=path.join(raiz,decodeURIComponent(q.url.split('?')[0]));if(!f.startsWith(raiz)){r.writeHead(403);return r.end()}
  if(f.endsWith(path.sep))f+='index.html';fs.readFile(f,(e,d)=>{if(e){r.writeHead(404);return r.end()}r.writeHead(200,{'Content-Type':T[path.extname(f)]||'application/octet-stream'});r.end(d)})}).listen(port,()=>console.log('http://localhost:'+port));
