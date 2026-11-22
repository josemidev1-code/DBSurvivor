// Simulador de partidas para ajustar la dificultad (22 nov. 2026).
// Un bot que huye de los enemigos y de los disparos, sin cargar ki, juega una partida acelerada y cuenta lo que pasa.
// Uso (consola del navegador, con el juego abierto desde un servidor local):
//   const s=document.createElement('script');s.src='/herramientas/simular_partida.js';document.head.append(s);
//   await SIMULAR.partida({hid:'goku',map:'namek',seg:600})   // devuelve un resumen por minuto
(function(){
  const K={KeyW:0,KeyA:0,KeyS:0,KeyD:0};
  function tecla(code,on){if(K[code]===on)return;K[code]=on;dispatchEvent(new KeyboardEvent(on?'keydown':'keyup',{code,bubbles:true}))}
  function soltar(){for(const k in K)tecla(k,0)}
  // elige, entre 8 direcciones, el punto de dentro de 0,4 s con menos peligro (enemigos y disparos cerca)
  const DIRS=[[1,0],[1,1],[0,1],[-1,1],[-1,0],[-1,-1],[0,-1],[1,-1]];
  function peligro(x,y){let p=0;
    for(const e of AS.enemies()){const d=Math.hypot(x-e.x,y-e.y);if(d<120)p+=(e.boss?4:1)/Math.max(8,d);
      // reacciona a los avisos: se aparta del que va a golpear y de la línea del que va a embestir
      const a=e.atk;if(a&&a.f==='aviso'&&d<34)p+=1.5;
      if(a&&(a.f==='carga'||a.f==='embiste')){const rx=x-e.x,ry=y-e.y,t=rx*a.ux+ry*a.uy,lat=Math.abs(rx*a.uy-ry*a.ux);if(t>-8&&t<100&&lat<14)p+=1.5}}
    // rayos de jefe (avisan con una línea roja) y embestidas de jefe avisadas
    const linea=(ox,oy,a,len,wid)=>{const ux=Math.cos(a),uy=Math.sin(a),rx=x-ox,ry=y-oy,t=rx*ux+ry*uy,lat=Math.abs(rx*uy-ry*ux);return t>-10&&t<len&&lat<wid/2+10};
    if(AS.ebeams)for(const b of AS.ebeams())if(linea(b.x,b.y+10,b.a,b.len,b.wid))p+=3;
    for(const e of AS.enemies())if(e.boss&&e.aiW>0&&linea(e.x,e.y,e.wa,e.wl+20,24))p+=3;
    for(const s of AS.eshots()){const d=Math.hypot(x-s.x,y-s.y);if(d<60)p+=3/Math.max(6,d)}
    // como un jugador de verdad, va a por las gemas de experiencia cuando no hay mucho peligro
    let g=0;for(const o of AS.gems()){const d=Math.hypot(x-o.x,y-o.y);if(d<140)g+=0.25/Math.max(10,d)}
    // y pelea: se queda a unos 45 px del enemigo más cercano para que sus ataques lleguen, sin huir de todo
    let dn=1e9;for(const e of AS.enemies())if(!e.crate)dn=Math.min(dn,Math.hypot(x-e.x,y-e.y));
    if(dn<400)p+=0.0015*Math.abs(dn-45);
    return p-g}
  function decidir(){
    const P=AS.P,v=AS.spd()*0.4;let mejor=peligro(P.x,P.y)-0.003,dir=null;
    for(const [a,b] of DIRS){const l=Math.hypot(a,b),ux=a/l,uy=b/l;let p=peligro(P.x+ux*v,P.y+uy*v);
      /* no ir hacia una pared: mira el camino, no solo el punto final */
      for(const f of [0.25,0.5,0.75,1])if(AS.solid(P.x+ux*v*f,P.y+uy*v*f,6)){p+=2*(1.25-f);break}
      if(p<mejor){mejor=p;dir=[a,b]}}
    if(!dir){soltar();return}
    tecla('KeyD',dir[0]>0?1:0);tecla('KeyA',dir[0]<0?1:0);tecla('KeyS',dir[1]>0?1:0);tecla('KeyW',dir[1]<0?1:0);
  }
  async function partida(o){
    o=Object.assign({hid:'goku',map:'namek',seg:600,diff:0},o||{});
    // con la ventana oculta el lienzo mide 0 y los enemigos aparecen pegados al jugador: la prueba no valdría
    if(!document.getElementById('game').width)throw new Error('El lienzo del juego mide 0: muestra la ventana o dale tamaño antes de simular');
    AS.setDiff(o.diff);AS.start(o.hid,o.map);const P=AS.P,S=AS.S;S.revives=0;
    const res=[];let ultMin=-1,golpes=0,hpAnt=P.hp,dano=0;
    for(let n=0;n<o.seg*10;n++){
      if(AS.state==='levelup'){AS.pick(0);continue}
      if(AS.state!=='play')break;
      if(n%2===0)decidir();
      AS.tick(0.1);
      if(P.hp<hpAnt){golpes++;dano+=hpAnt-P.hp}hpAnt=P.hp;
      const mi=Math.floor(S.t/60);
      if(mi!==ultMin){ultMin=mi;const en=AS.enemies();res.push({min:mi,nivel:P.lvl,enemigos:en.length,vidaMedia:Math.round(en.reduce((a,e)=>a+(e.boss?0:e.maxhp),0)/Math.max(1,en.filter(e=>!e.boss).length)),vida:Math.round(P.hp),golpes,dano:Math.round(dano)});golpes=0;dano=0}
      if(n%50===0)await new Promise(r=>setTimeout(r,0));
    }
    soltar();
    return {aguanto:Math.round(S.t),nivel:P.lvl,muertes:S.kills,estado:AS.state,minutos:res};
  }
  // sigue la partida en curso con el bot hasta el segundo t (para sacar capturas de un momento concreto)
  async function hasta(t){const S=AS.S;
    for(let n=0;S.t<t&&n<200000;n++){if(AS.state==='levelup'){AS.pick(0);continue}if(AS.state==='pause'){const b=document.querySelector('#pause button');if(b)b.click();continue}
      if(AS.state!=='play')break;if(n%2===0)decidir();AS.tick(0.1);if(n%50===0)await new Promise(r=>setTimeout(r,0))}
    soltar();return {t:Math.round(S.t),estado:AS.state,enemigos:AS.enemies().length,vida:Math.round(AS.P.hp),nivel:AS.P.lvl}}
  window.SIMULAR={partida,hasta};
})();
