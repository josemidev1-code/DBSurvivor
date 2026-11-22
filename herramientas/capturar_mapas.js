// Saca una foto de cada mapa tal y como se ve en el juego (22 nov. 2026), para las portadas y para comparar cambios.
// Uso (consola del navegador, juego abierto desde un servidor local y ventana visible o con tamaño):
//   const s=document.createElement('script');s.src='/herramientas/capturar_mapas.js';document.head.append(s);
//   await CAPTURAR.todos({envio:'http://127.0.0.1:8766/', sufijo:'_antes'})
// Cada foto se manda por POST (data URL en el cuerpo) a envio+mapa+sufijo+'.png'. Recibe: un servidor que guarde el cuerpo.
(function(){
  const espera=ms=>new Promise(r=>setTimeout(r,ms)),fotograma=()=>new Promise(r=>requestAnimationFrame(()=>r()));
  // sitio de la foto: un poco apartado de la salida (que está despejada) para que se vea el terreno
  const SITIO=[14,9];
  async function mapa(id,o){o=o||{};
    AS.setDiff(0);AS.start(o.hid||'goku',id);const P=AS.P,S=AS.S,T=16;
    P.x=(o.tx||SITIO[0])*T;P.y=(o.ty||SITIO[1])*T;AS.place(P,5,1);
    AS.enemies().length=0;S.revives=9;
    for(let i=0;i<240;i++){if(AS.state==='levelup')AS.pick(0);AS.tick(1/30);AS.enemies().length=0;P.hp=999}  /* 8 s: se van los textos de ayuda del principio */
    P.x=(o.tx||SITIO[0])*T;P.y=(o.ty||SITIO[1])*T;AS.place(P,5,1);P.powT=0;for(let i=0;i<20;i++){AS.tick(1/30);AS.enemies().length=0}
    AS.gems().length=0;AS.pickups().length=0;
    S.freeze=999;S.banner=null;
    if(o.sinJugador){P.x+=5000;P.y+=5000}  /* con el juego congelado la cámara no se mueve: el jugador queda fuera de la foto */
    if(AS.state==='pause'){const b=document.querySelector('#pause button');if(b)b.click()}
    await fotograma();await fotograma();await espera(120);
    // recorte del centro sin el HUD de arriba y la barra de abajo, en proporción 1,6
    const cv=document.getElementById('game'),W=cv.width,H=cv.height,y0=Math.round(H*0.11),y1=Math.round(H*0.835),h=y1-y0,w=Math.round(h*1.6),x0=Math.round((W-w)/2);
    const c=document.createElement('canvas');c.width=o.ancho||528;c.height=Math.round(c.width/1.6);const g=c.getContext('2d');g.imageSmoothingEnabled=false;
    g.drawImage(cv,x0,y0,w,h,0,0,c.width,c.height);const url=c.toDataURL('image/png');
    if(o.envio)await fetch(o.envio+id+(o.sufijo||'')+'.png',{method:'POST',body:url});
    return url.length;
  }
  async function todos(o){const r={};for(const id of AS.maps())r[id]=await mapa(id,o);return r}
  window.CAPTURAR={mapa,todos};
})();
