// Regresión del planificador: usa las definiciones y funciones reales del juego.
// Actualizada el 27 nov.: control exclusivo de la ranura elegida (sesión 17), tecla repetida y lista de partida propia.
const fs=require('node:fs'),vm=require('node:vm'),assert=require('node:assert/strict'),path=require('node:path');
const root=path.resolve(__dirname,'..');
const src=fs.readFileSync(path.join(root,'02 - Código del juego/script.js'),'utf8');
function section(a,b){const i=src.indexOf(a),j=src.indexOf(b,i);assert(i>=0&&j>i,a);return src.slice(i,j)}
const fired=[],c=vm.createContext({window:{},Math,Set,console});
vm.runInContext(section('const NUEVOS={','// formas añadidas'),c);
vm.runInContext(section('const MV={','const UNLOCK_LV='),c);
Object.assign(c,{S:{hid:'goku'},P:{x:0,y:0,sel:0,sigU:6,sigB:[],lvl:1,sigN:6,sigT:0},
 clamp:(v,a,b)=>Math.max(a,Math.min(b,v)),fxSl:[],fxRg:[],FO:null,
 nearest:()=>({x:90,y:0}),fire:(id,m,st)=>{assert(Number.isFinite(st.dmg));fired.push(id)},
 sfx:()=>{},state:'play'});
vm.runInContext(section('function baseSigs','function fireSig'),c);
for(let i=0;i<1200;i++)vm.runInContext('sigUpdate(1/60,{cd:1,dmg:1,area:1})',c);
// Control exclusivo: solo dispara la técnica de la ranura elegida y se repite al acabar su recarga.
assert.deepEqual([...new Set(fired)],['kiblast'],'Solo debe disparar la técnica de la ranura elegida');
assert(fired.length>3,'El ataque elegido debe repetirse');
// Ninguna técnica se emite mientras una animación de rayo está ocupada.
c.P.pend=null;const n=fired.length;c.P.cast={};for(let i=0;i<120;i++)vm.runInContext('sigUpdate(1/60,{cd:1,dmg:1,area:1})',c);
assert.equal(fired.length,n);assert.equal(c.P.sigTimers.kiblast,0,'La recarga debe avanzar durante el rayo');
// Elegir otra ranura prepara su técnica.
c.P.cast=null;c.P.sigTimers.genki=0;vm.runInContext('sigSelect(5);sigUpdate(1/60,{cd:1,dmg:1,area:1})',c);
assert.equal(c.P.sel,5);assert.equal(c.P.pend&&c.P.pend.id,'genki','Elegir la ranura 6 debe preparar su técnica');
// Pulsar otra vez la ranura ya elegida no adelanta su recarga ni anula el retardo global.
c.P.sigTimers.genki=0.2;c.P.sigT=0.15;vm.runInContext('sigSelect(5)',c);
assert.equal(c.P.sigTimers.genki,0.2,'Repetir la tecla adelanta la recarga');assert.equal(c.P.sigT,0.15,'Repetir la tecla anula el retardo global');
// La lista de la partida es una copia: cambiarla (por ejemplo, con la fusión) no toca SIGS.
c.P.sigs=[...vm.runInContext("baseSigs('goku')",c)];c.P.sigs[0]='kame';
assert.notEqual(vm.runInContext('SIGS.goku[0]',c),'kame','La lista de la partida comparte memoria con SIGS');
assert.equal(vm.runInContext('sigList()[0]',c),'kame','sigList debe usar la lista de la partida');
const {MV,SIGS}=vm.runInContext('({MV,SIGS})',c);
for(const [id,L] of Object.entries(SIGS))for(const move of L){assert(MV[move],id+': '+move);for(let l=1;l<=5;l++)assert(Number.isFinite(MV[move].st(l).dmg),id+': daño no finito')}
assert.equal(SIGS.bulma[0],'bulmagun');assert(!SIGS.videl.includes('kame'));assert(SIGS.granola.includes('granolasnipe'));
console.log('Rotación: control exclusivo de la ranura, recargas durante animaciones, selección, tecla repetida, lista de partida propia y daño finito correctos.');
