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
