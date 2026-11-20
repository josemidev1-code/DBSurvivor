// Comprueba la lógica pura de las transformaciones (02 - Código del juego/transformaciones.js).
// Uso: node herramientas/comprobar_transformaciones.cjs
const fs=require('node:fs'),path=require('node:path'),vm=require('node:vm'),assert=require('node:assert/strict');
const raiz=path.resolve(__dirname,'..');
const c=vm.createContext({window:{},Math});
vm.runInContext(fs.readFileSync(path.join(raiz,'02 - Código del juego/transformaciones.js'),'utf8'),c);
const T=c.window.TRANSF;
const cerca=(a,b,m)=>assert.ok(Math.abs(a-b)<1e-9,`${m||''}: ${a} ≠ ${b}`);

// ---- datos: cadenas en el orden de la serie, tiempos, niveles y mejoras
const goku=['BASE','SUPER SAIYAN','SUPER SAIYAN 2','SUPER SAIYAN 3','SSJ BLUE','UI SEÑAL','UI DOMINADO','SSJ4 GT','KAIOKEN','SSJ DIOS'];
assert.deepEqual([...T.cadena('goku',goku)],[0,8,1,2,3,9,4,5,6],'Goku en orden de la serie y sin SSJ4 GT');
assert.deepEqual([...T.cadena('cell',['IMPERFECTO','SEMIPERFECTO','PERFECTO','GOLDEN','MAJIN'])],[0,1,2],'Cell sin formas fanmade');
assert.deepEqual([...T.cadena('trunks',['BASE','SUPER SAIYAN','BASE MANGA','SSJ2 MANGA'])],[0,1,3],'Trunks sin BASE MANGA');
assert.deepEqual([...T.cadena('bardock',['BASE','SUPER SAIYAN','SUPER SAIYAN 4'])],[0,1,2],'no principal: todas en orden');
assert.deepEqual([...T.cadena('krilin',['BASE'])],[0]);
assert.deepEqual({...T.tiempos(1)},{carga:3,dura:25});
assert.deepEqual({...T.tiempos(3)},{carga:6,dura:19});
assert.equal(T.tiempos(9).dura,8,'la duración no baja de 8 s');
assert.deepEqual([1,2,8].map(p=>T.nivelPaso(p,8)),[5,10,40]);
assert.equal(T.nivelPaso(1,1),20);
assert.equal(T.mejora('KAIOKEN').rasgo,'kaioken');
assert.deepEqual({...T.mejora('FORMA INVENTADA')},{dmg:1.25,spd:1.06,cd:0.95,hp:1.15,rasgo:null});
for(const id in T.CADENAS)for(const n of T.CADENAS[id])assert.ok(n==='BASE'||T.MEJORAS[n]||['IMPERFECTO','GORDO','CONTENIDO','1ª FORMA'].includes(n),`${id}: ${n} sin mejora`);

console.log('Transformaciones: datos correctos.');

// ---- máquina de la carga de ki: se sube forma a forma, cada una con sus tiempos
{const nom=()=>'SUPER SAIYAN',e=(cargando,golpes=0,muertes=0,abiertos=2)=>({cargando,golpes,muertes,abiertos,nombre:nom});
  const T0=T.nuevo();let ev=null;for(let i=0;i<31;i++)ev=T.avanzar(T0,e(true),0.1)||ev;
  assert.equal(ev,'sube','3 s de carga transforman');assert.equal(T0.paso,1);assert.ok(T0.t>24,'dura unos 25 s');
  const T1=T.nuevo();T.avanzar(T1,e(true),1.5);T.avanzar(T1,e(false,1),0);
  cerca(T1.carga,0.15,'un golpe quita 0,35');
  T.avanzar(T1,e(false),5);cerca(T1.carga,0.15,'soltar no pierde la carga');
  T.avanzar(T1,e(false,0,2),0);cerca(T1.carga,0.16,'cada muerte da 0,005 (poco: matar no basta para transformarse)');
  const T2=T.nuevo();T.avanzar(T2,e(true,0,0,0),10);assert.equal(T2.carga,0,'sin formas abiertas no carga');
  const T3={carga:0,paso:1,t:0.05,cargando:false};
  assert.equal(T.avanzar(T3,e(false),0.1),'vuelve');assert.equal(T3.paso,0);assert.equal(T3.carga,0);
  const T4={carga:0.99,paso:1,t:20,cargando:true};
  assert.equal(T.avanzar(T4,e(true,0,0,1),1),null,'no pasa de la última forma abierta');assert.equal(T4.paso,1);
  // ya transformado, seguir cargando sube a la siguiente forma con su propia duración
  const T5={carga:0,paso:1,t:20,cargando:true};let ev5=null,n5=0;while(!ev5&&n5++<100)ev5=T.avanzar(T5,e(true,0,0,3),0.1);
  assert.ok(n5>=45&&n5<=46,'la 2.ª forma tarda 4,5 s en cargar');
  assert.equal(ev5,'sube');assert.equal(T5.paso,2);cerca(T5.t,22,'la 2.ª forma dura 22 s');
  // una forma que gasta mucho (duraK) dura menos
  const T6={carga:0.999,paso:0,t:0,cargando:true};T.avanzar(T6,{...e(true),nombre:()=>'SSJ BLUE'},0.1);cerca(T6.t,25*0.7,'SSJ Blue dura un 30 % menos')}
console.log('Transformaciones: carga de ki correcta.');
