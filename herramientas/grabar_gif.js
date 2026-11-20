// Grabador de GIF para mandar a Josemi cómo va el juego (sin ffmpeg ni Pillow).
// Uso (en la consola del navegador, con el juego abierto desde un servidor local):
//   const s=document.createElement('script');s.src='/herramientas/grabar_gif.js';document.head.append(s);
//   const gif=await GRABAR.recorte(12, 120);   // 12 s, un fotograma cada 120 ms, recorte alrededor del personaje
//   GRABAR.descargar(gif,'goku.gif')          // o envíalo con fetch a donde haga falta
(function(){
  // codificador GIF89a: paleta de los 256 colores más usados (5 bits por canal) y LZW
  function gif(frames,W,H,delay){
    const cnt=new Map();for(const f of frames)for(let i=0;i<f.length;i+=16){const k=(f[i]>>3)<<10|(f[i+1]>>3)<<5|(f[i+2]>>3);cnt.set(k,(cnt.get(k)||0)+1)}
    const top=[...cnt.entries()].sort((a,b)=>b[1]-a[1]).slice(0,256).map(e=>e[0]);
    const pal=top.map(k=>[((k>>10)&31)<<3|4,((k>>5)&31)<<3|4,(k&31)<<3|4]);while(pal.length<256)pal.push([0,0,0]);
    const memo=new Map(),idx=(r,g,b)=>{const k=(r>>3)<<10|(g>>3)<<5|(b>>3);let v=memo.get(k);if(v!==undefined)return v;let bd=1e9;v=0;
      for(let i=0;i<pal.length;i++){const p=pal[i],d=(p[0]-r)**2+(p[1]-g)**2+(p[2]-b)**2;if(d<bd){bd=d;v=i}}memo.set(k,v);return v};
    const out=[],w16=n=>{out.push(n&255,(n>>8)&255)};for(const c of 'GIF89a')out.push(c.charCodeAt(0));
    w16(W);w16(H);out.push(0xF7,0,0);for(const p of pal)out.push(...p);
    out.push(0x21,0xFF,11,...[...'NETSCAPE2.0'].map(c=>c.charCodeAt(0)),3,1,0,0,0);
    for(const f of frames){
      out.push(0x21,0xF9,4,0x04);w16(delay);out.push(0,0);out.push(0x2C);w16(0);w16(0);w16(W);w16(H);out.push(0);
      const ind=new Uint8Array(W*H);for(let i=0,j=0;j<ind.length;i+=4,j++)ind[j]=idx(f[i],f[i+1],f[i+2]);
      let size=9,next=258,cur=0,bits=0;const dict=new Map(),bytes=[],emit=c=>{cur|=c<<bits;bits+=size;while(bits>=8){bytes.push(cur&255);cur>>>=8;bits-=8}};
      emit(256);let w=ind[0];
      for(let i=1;i<ind.length;i++){const k=ind[i],key=w*4096+k,g=dict.get(key);if(g!==undefined){w=g;continue}emit(w);
        if(next===4096){emit(256);dict.clear();size=9;next=258}else{if(next>=(1<<size))size++;dict.set(key,next++)}w=k}
      emit(w);emit(257);if(bits>0)bytes.push(cur&255);
      out.push(8);for(let i=0;i<bytes.length;i+=255){const ch=bytes.slice(i,i+255);out.push(ch.length,...ch)}out.push(0);
    }
    out.push(0x3B);return new Uint8Array(out);
  }
  // graba el centro del lienzo del juego (donde está el personaje) durante seg segundos
  async function recorte(seg,cada=120,lado=0.36,sal=304){
    const cv=document.getElementById('game'),SRC=Math.round(cv.height*lado),t=document.createElement('canvas');t.width=t.height=sal;
    const x=t.getContext('2d');x.imageSmoothingEnabled=false;const fr=[],n=Math.round(seg*1000/cada);
    for(let i=0;i<n;i++){await new Promise(r=>setTimeout(r,cada));x.fillStyle='#000';x.fillRect(0,0,sal,sal);
      x.drawImage(cv,cv.width/2-SRC/2,cv.height/2-SRC*0.58,SRC,SRC,0,0,sal,sal);fr.push(x.getImageData(0,0,sal,sal).data.slice())}
    return gif(fr,sal,sal,Math.round(cada/10));
  }
  function descargar(bytes,nombre){const a=document.createElement('a');a.href=URL.createObjectURL(new Blob([bytes],{type:'image/gif'}));a.download=nombre;a.click()}
  window.GRABAR={gif,recorte,descargar};
})();
