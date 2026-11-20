// Comprueba el deseo de transformación: las formas se desbloquean pidiéndoselas a Shenron en el menú.
// Uso: node herramientas/comprobar_formas.cjs
const fs=require('node:fs'),path=require('node:path'),vm=require('node:vm'),assert=require('node:assert/strict');
const raiz=path.resolve(__dirname,'..'),src=fs.readFileSync(path.join(raiz,'02 - Código del juego/script.js'),'utf8');
function tramo(desde,hasta){const a=src.indexOf(desde),b=src.indexOf(hasta,a);assert(a>=0&&b>a,`No se encuentra ${desde}`);return src.slice(a,b)}
let save={},escrito=0;
const c=vm.createContext({Math,HEROES:{goku:{name:'GOKU',forms:['BASE','SUPER SAIYAN','SSJ2','SSJ3']},a16:{name:'ANDROIDE 16',forms:['BASE']}},
  FORM_LV:[0,10,20,30,40],loadSave:()=>save,writeSave:()=>escrito++,clamp:(v,a,b)=>Math.max(a,Math.min(b,v)),
  stats:()=>({maxhp:100}),cam:{shake:0},sfx:()=>{},burst:()=>{}});
vm.runInContext(tramo('const FORMA_TK=','// ---------- fin del deseo de transformación')+';this.FORMA_TK=FORMA_TK',c);
vm.runInContext(fs.readFileSync(path.join(raiz,'02 - Código del juego/transformaciones.js'),'utf8').replace('window.TRANSF=','this.TRANSF='),c);
vm.runInContext(tramo('function trAbiertos(','\n'),c);

// Sin deseo pedido, solo la forma base
assert.equal(c.formasAbiertas('goku'),0);
save={formas:{goku:9}};assert.equal(c.formasAbiertas('goku'),3,'no se limita a las formas que existen');
// Pedir el deseo: cuesta FORMA_TK por la 1ª forma, el doble por la 2ª…; sin tickets no hace nada
save={tickets:4};escrito=0;assert.equal(c.pedirForma('goku'),'faltan');assert.equal(save.tickets,4);assert.equal(escrito,0);
save={tickets:20};assert.equal(c.costeForma('goku'),c.FORMA_TK);
assert.equal(c.pedirForma('goku'),'ok');assert.equal(save.tickets,20-c.FORMA_TK);assert.equal(save.formas.goku,1);assert.equal(escrito,1);
assert.equal(c.costeForma('goku'),2*c.FORMA_TK);
save={tickets:999,formas:{goku:3}};assert.equal(c.pedirForma('goku'),'todas');assert.equal(save.tickets,999);
assert.equal(c.pedirForma('a16'),'todas','un personaje sin transformaciones no gasta tickets');
// En partida (barra de ki, 20 nov.): se puede subir hasta la forma abierta por nivel Y pedida a Shenron
const abiertos=(hid,forms,lvl,deseos)=>{save={formas:{[hid]:deseos}};c.HEROES[hid]={name:hid,forms};c.S={hid};c.P={lvl,trCad:[...c.TRANSF.cadena(hid,forms)]};return c.trAbiertos()};
const GOKU=['BASE','SUPER SAIYAN','SUPER SAIYAN 2','SUPER SAIYAN 3','SSJ BLUE','UI SEÑAL','UI DOMINADO','SSJ4 GT','KAIOKEN','SSJ DIOS'];
assert.equal(abiertos('goku',GOKU,12,3),2,'Goku nivel 12 con 3 deseos: 2 formas');
assert.equal(abiertos('goku',GOKU,40,1),1,'Goku nivel 40 con 1 deseo: 1 forma');
assert.equal(abiertos('goku',GOKU,40,9),8,'Goku nivel 40 con todos los deseos: las 8');
assert.equal(abiertos('goku',GOKU,4,9),0,'antes del nivel 5 no hay formas');
assert.equal(abiertos('krilin',['BASE'],1,0),1,'Krilin: poder máximo sin deseo');
// La pantalla de Shenron tiene el botón y lo prepara al abrirse
assert(fs.readFileSync(path.join(raiz,'index.html'),'utf8').includes('id="gForma"'),'falta el botón #gForma');
assert(tramo('function openGacha(','\n').includes('formaUI()'),'openGacha no prepara el botón');
assert(tramo('function formaUI(','\n').includes('companion()'),'formaUI no usa el compañero del menú (sel puede no existir)');
console.log('Deseo de transformación correcto');
