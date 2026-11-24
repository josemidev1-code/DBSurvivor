// Vista aérea de un mapa (24 nov. 2026): dibuja a escala el suelo y los decorados reales de una zona grande,
// para juzgar cómo quedan repartidos los obstáculos. Uso en la consola (juego abierto desde servidor local):
//   const s=document.createElement('script');s.src='/herramientas/vista_aerea.js';document.head.append(s);
//   await AEREA('namek',{suelo:'#7a9a5a',agua:'#3a7ab0'})   // tapa la pantalla con la vista; AEREA.cerrar() la quita
(function(){
  const h2=(x,y,s=0)=>{let h=(Math.imul(x|0,374761393)+Math.imul(y|0,668265263)+Math.imul(s|0,982451653))|0;h=Math.imul(h^(h>>>13),1274126177);h^=h>>>16;return (h>>>0)/4294967296};
  async function AEREA(id,o={}){const sc=o.sc||0.3,W0=o.w||130,H0=o.h||72,x0=o.x0??-65,y0=o.y0??-36;
    AS.start('goku',id);const b=document.getElementById('bMute');if(b&&!/MUDO/.test(b.textContent))b.click();AS.S.freeze=999;
    await new Promise(r=>setTimeout(r,300));
    const {WORLD,decorDesplazamiento}=AS.mundo(),W=WORLD[id],T=16,c=document.createElement('canvas');c.width=W0*T*sc;c.height=H0*T*sc;
    const g=c.getContext('2d');g.imageSmoothingEnabled=false;g.fillStyle=o.suelo||'#7a9a5a';g.fillRect(0,0,c.width,c.height);g.fillStyle=o.agua||'#3a7ab0';
    const L=[];let n=0;
    for(let ty=y0;ty<y0+H0;ty++)for(let tx=x0;tx<x0+W0;tx++){
      if(W.special(tx,ty)){g.fillRect((tx-x0)*T*sc,(ty-y0)*T*sc,T*sc+1,T*sc+1);continue}
      const d=W.decor(tx,ty,h2(tx,ty,3));if(d){const [jx,jy]=decorDesplazamiento(id,tx,ty,d);L.push([tx*T+8+jx,ty*T+8+jy,d]);if(AS.obstacle(tx,ty))n++}}
    L.sort((a,b)=>a[1]-b[1]);for(const [x,y,d] of L)g.drawImage(d,(x-d.width/2-x0*T)*sc,(y-d.height/2-y0*T)*sc,d.width*sc,d.height*sc);
    g.strokeStyle='#ff0';g.strokeRect((-7-x0)*T*sc,(-7-y0)*T*sc,14*T*sc,14*T*sc); // zona de salida, siempre despejada
    let im=document.getElementById('aerea');
    if(!im){im=document.createElement('img');im.id='aerea';im.style.cssText='position:fixed;inset:0;width:100vw;height:100vh;object-fit:contain;z-index:99999;background:#000;image-rendering:pixelated';document.body.append(im)}
    im.src=c.toDataURL();im.hidden=false;return {solidos:n,casillas:W0*H0}}
  AEREA.cerrar=()=>{const im=document.getElementById('aerea');if(im)im.hidden=true};
  window.AEREA=AEREA;
})();
