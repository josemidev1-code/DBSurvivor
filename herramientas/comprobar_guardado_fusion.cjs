// Comprueba dos arreglos del 27 nov. con el código real del juego, sin navegador:
// 1) loadSave conserva todos los campos guardados (antes perdía formas, freeD, pity4, guar e hist al recargar).
// 2) La técnica fusionada tiene los campos que necesita su tipo (antes las bolas salían con NaN y los rayos fallaban).
// Uso: node herramientas/comprobar_guardado_fusion.cjs
const fs=require('node:fs'),path=require('node:path'),vm=require('node:vm'),assert=require('node:assert/strict');
const raiz=path.resolve(__dirname,'..'),src=fs.readFileSync(path.join(raiz,'02 - Código del juego/script.js'),'utf8');
function tramo(desde,hasta){const a=src.indexOf(desde),b=src.indexOf(hasta,a);assert(a>=0&&b>a,`No se encuentra ${desde}`);return src.slice(a,b)}

// 1) Guardado
{
  let guardado={};
  const ls={getItem:()=>JSON.stringify(guardado),setItem:(k,v)=>{guardado=JSON.parse(v)}};
  const c=vm.createContext({localStorage:ls,JSON});
  vm.runInContext(tramo('let SAVE=null;','function loadBest'),c);
  guardado={tickets:3,zeni:50,formas:{goku:2},freeD:'2026-11-27',pity4:4,guar:1,hist:[{id:'goku'}]};
  const s=vm.runInContext('loadSave()',c);
  assert.equal(s.tickets,3);assert.equal(s.zeni,50);
  assert.equal(JSON.stringify(s.formas),JSON.stringify({goku:2}),'se pierden las formas pagadas');assert.equal(s.freeD,'2026-11-27','se pierde la cápsula gratis del día');
  assert.equal(s.pity4,4);assert.equal(s.guar,1);assert.equal(JSON.stringify(s.hist),JSON.stringify([{id:'goku'}]));
  vm.runInContext('writeSave()',c);assert.equal(guardado.freeD,'2026-11-27','el siguiente guardado borra campos');
  // Sin partida guardada, valores por defecto
  vm.runInContext('SAVE=null',c);guardado={};const d=vm.runInContext('loadSave()',c);
  assert.equal(d.tickets,10);assert.equal(d.sel,'goku');assert.equal(JSON.stringify(d.owned),JSON.stringify({goku:1,vegeta:1,piccolo:1}));
}

// 2) Fusión
{
  const c=vm.createContext({window:{},Math,Set,console});
  vm.runInContext(tramo('const NUEVOS={','// formas añadidas'),c);
  vm.runInContext(tramo('const MV={','const UNLOCK_LV='),c);
  vm.runInContext(tramo('const FUSION_RECIPES','function options'),c);
  vm.runInContext(tramo('function fusionMove','function applyOpt'),c);
  const {MV,SIGS,FUSION_RECIPES}=vm.runInContext('({MV,SIGS,FUSION_RECIPES})',c);
  const NECESITA={beam:['len','wid','dur'],shot:['count','spd'],big:['rad','spd'],melee:['hits','reach','rad'],sword:['rad','arc'],nova:['rad'],bomb:['rad'],disc:[]};
  let probadas=0;
  const probar=(idA,idB,rec,quien)=>{
    const W=c.fusionMove({idA,idB,fusName:'FUSIÓN',rec});
    assert(W.sig,`${quien}: la fusión no debe ofrecerse como técnica del sistema antiguo`);
    for(let l=1;l<=5;l++){const st=W.st(l),base=(MV[idA]||MV[idB]).st(l);
      assert(Number.isFinite(st.dmg)&&st.dmg>0,`${quien}: daño no válido`);
      for(const k of NECESITA[W.kind]||[])assert(Number.isFinite(st[k]),`${quien}: a la técnica de tipo ${W.kind} le falta ${k}`);
      if(MV[idA]&&W.kind===MV[idA].kind)assert(Math.abs(st.dmg-base.dmg*1.7)<1e-9,`${quien}: no da +70 % de daño`)}
    probadas++};
  // Lo que ocurre en partida: se fusionan las ranuras 1 y 2 de cada personaje.
  for(const [hid,L] of Object.entries(SIGS)){if(!L||L.length<2)continue;const k1=L[0]+'+'+L[1],k2=L[1]+'+'+L[0];
    const rec=FUSION_RECIPES[k1]||FUSION_RECIPES[k2];if(rec&&MV[rec.id])continue;probar(L[0],L[1],rec,hid)}
  // Y cada receta que no tiene ya su propia técnica.
  for(const [k,rec] of Object.entries(FUSION_RECIPES)){if(MV[rec.id])continue;const [a,b]=k.split('+');probar(a,b,rec,k)}
  console.log(`Guardado completo y ${probadas} fusiones con campos válidos (+70 % de daño).`);
}
