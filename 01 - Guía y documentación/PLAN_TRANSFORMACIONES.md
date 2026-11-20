# Transformaciones en partida — plan de implementación

> **Para quien lo ejecute (IA):** usa superpowers:executing-plans (o superpowers:subagent-driven-development si Josemi lo pide). Los pasos usan casillas (`- [ ]`) para marcar el avance. Apunta cada tarea terminada en la bitácora y haz commit al acabarla.

**Objetivo:** sustituir la transformación automática por nivel por una barra de ki que se carga con riesgo y sube forma a forma, cada forma con su tiempo de carga, su duración y una mejora fiel a la serie; los personajes de una sola forma entran en «poder máximo».

**Arquitectura:** la lógica pura (cadenas de formas, tiempos, niveles, mejoras y la máquina de carga) va en un archivo nuevo, `02 - Código del juego/transformaciones.js`, que define `window.TRANSF` y se prueba con Node sin navegador. `script.js` solo conecta esa lógica con el teclado y el toque, el movimiento, los golpes, las muertes, `stats()`, los enemigos y el HUD. Las auras salen de PixelFX (`efectos_pixelfx.js`, que ya expone `PFX.aura` y `PFX.transform`).

**Tecnología:** JavaScript sin módulos (el juego se abre con doble clic), Node 26 para las comprobaciones (`node:vm`, `node:assert/strict`), PixelFX 0.3.1 y esbuild para regenerar `efectos_pixelfx.js`.

**Diseño:** `01 - Guía y documentación/TRANSFORMACIONES.md` (aprobado por Josemi el 20 nov. 2026). Página visual: https://claude.ai/artifact/RrptqZhy8XLpckaqe87dMw

## Restricciones generales

- `index.html` tiene que seguir funcionando con doble clic: nada de `fetch`, `import` ni JSON en tiempo de ejecución.
- Personajes solo con sprites de `sprites/`; nada de personajes dibujados por código. Las auras y los destellos son efectos (PixelFX), no personajes.
- Todo el texto visible, en español. Sin aura permanente: el aura sale solo mientras se carga y mientras dura la transformación o el poder máximo.
- Se sube forma a forma: cargar → 1.ª forma; cargar otra vez ya transformado → 2.ª forma, y así hasta la última abierta.
- Cada forma de cada personaje tiene su tiempo de carga y su duración. Valores de partida: 1.ª forma carga 3 s y dura 25 s; cada forma siguiente carga 1,5 s más y dura 3 s menos (mínimo 8 s).
- Las formas se abren por niveles en la partida (Goku: una cada 5 niveles, del 5 al 40) y, además, hay que haberlas pedido a Shenron en el menú (`formasAbiertas(hid)`). El poder máximo no necesita deseo.
- Principales con cadena propia (solo formas de la serie): Goku, Vegeta, Gohan, Piccolo, Krilin, Trunks, Goten, Freezer, Cell, Majin Buu y Broly. Fuera de su cadena: Cell Golden, Cell Majin, Broly SSJ4 y «BASE MANGA» de Trunks. SSJ4 GT de Goku y Vegeta va aparte (no entra en la cadena por ahora).
- Al cambiar `script.js`, `transformaciones.js` o `efectos_pixelfx.js`, sube su `?v=` en `index.html`.
- Commits pequeños en español; apunta cada paso en `BITACORA.md`.

## Puntos de revisión

1. **Pausa, subida de nivel o pérdida de foco mientras se carga:** al volver, el personaje no sigue cargando solo y el tiempo de la transformación no corre durante la pausa (el juego borra `keys` al perder el foco; comprobar que la carga lee `keys.Space` cada fotograma y no un estado guardado).
2. **Soltar a medias:** la carga hecha se conserva, no se pierde al soltar (solo bajan los golpes).
3. **Personaje con varias formas sin ningún deseo pedido a Shenron:** no se transforma; la barra muestra «PIDE LA FORMA A SHENRON» en vez de llenarse para nada.
4. **Fin de la partida o reinicio estando transformado:** la partida nueva empieza en la forma base, con la carga a cero.
5. **Móvil:** se puede cargar sin teclado, manteniendo pulsado un botón táctil de la barra de ki.

---

### Tarea 1: datos de las transformaciones

**Archivos:**
- Crear: `02 - Código del juego/transformaciones.js`
- Crear: `herramientas/comprobar_transformaciones.cjs`

**Interfaces:**
- Produce `window.TRANSF` con:
  - `CADENAS`: objeto `{hid: [nombreDeForma, …]}` con las 11 cadenas de los principales, en el orden del diseño (Goku: `BASE, KAIOKEN, SUPER SAIYAN, SUPER SAIYAN 2, SUPER SAIYAN 3, SSJ DIOS, SSJ BLUE, UI SEÑAL, UI DOMINADO`; el resto, como en la tabla de `TRANSFORMACIONES.md`). Krilin y Goten tienen cadena de un solo elemento.
  - `cadena(hid, forms) → number[]`: índices de `forms` (los de `HEROES[hid].forms`) en orden de subida, empezando por la base. Si `hid` está en `CADENAS`, se usan sus nombres (los que no existan en `forms` se saltan); si no, todos los índices en orden.
  - `tiempos(paso) → {carga, dura}` en segundos; `paso` = 1 para la 1.ª forma por encima de la base.
  - `nivelPaso(paso, pasos) → number`: nivel en que se abre ese paso. Con `pasos>1`: `Math.round(5+35*(paso-1)/(pasos-1))`; con `pasos===1`: 20.
  - `MEJORAS`: `{nombreDeForma: {dmg, spd, cd, hp, rasgo}}` (multiplicadores; `rasgo` es una de las cadenas de la tarea 4 o `null`).
  - `mejora(nombreDeForma) → {dmg, spd, cd, hp, rasgo}`; si la forma no está en la tabla, `{dmg:1.25, spd:1.06, cd:0.95, hp:1.15, rasgo:null}`.

- [ ] **Paso 1: escribir la comprobación que falla.** `comprobar_transformaciones.cjs` carga `transformaciones.js` en `vm.createContext({window:{}})` y comprueba:

```js
const T=c.window.TRANSF;
const goku=['BASE','SUPER SAIYAN','SUPER SAIYAN 2','SUPER SAIYAN 3','SSJ BLUE','UI SEÑAL','UI DOMINADO','SSJ4 GT','KAIOKEN','SSJ DIOS'];
assert.deepEqual(T.cadena('goku',goku),[0,8,1,2,3,9,4,5,6]);          // orden de la serie, sin SSJ4 GT
assert.deepEqual(T.cadena('cell',['IMPERFECTO','SEMIPERFECTO','PERFECTO','GOLDEN','MAJIN']),[0,1,2]);
assert.deepEqual(T.cadena('trunks',['BASE','SUPER SAIYAN','BASE MANGA','SSJ2 MANGA']),[0,1,3]);
assert.deepEqual(T.cadena('bardock',['BASE','SUPER SAIYAN','SUPER SAIYAN 4']),[0,1,2]); // no principal: todas
assert.deepEqual(T.cadena('krilin',['BASE']),[0]);
assert.deepEqual(T.tiempos(1),{carga:3,dura:25});
assert.deepEqual(T.tiempos(3),{carga:6,dura:19});
assert.equal(T.tiempos(9).dura,8);
assert.deepEqual([1,2,8].map(p=>T.nivelPaso(p,8)),[5,10,40]);
assert.equal(T.nivelPaso(1,1),20);
assert.equal(T.mejora('KAIOKEN').rasgo,'kaioken');
assert.deepEqual(T.mejora('FORMA INVENTADA'),{dmg:1.25,spd:1.06,cd:0.95,hp:1.15,rasgo:null});
```

- [ ] **Paso 2: ejecutarla y ver que falla.** `node herramientas/comprobar_transformaciones.cjs` → error porque no existe `transformaciones.js`.
- [ ] **Paso 3: escribir `transformaciones.js`** como IIFE que asigna `window.TRANSF`, con los datos del diseño. Rasgos por forma: `kaioken` (KAIOKEN), `rayos` (SUPER SAIYAN 2, SSJ2 MANGA), `regenera` (SSJ DIOS, Piccolo BASE, PERFECTO, KID BUU), `esquiva` (UI SEÑAL), `esquivaContra` (UI DOMINADO), `ultraEgo` (ULTRA EGO), `bestia` (BESTIA), `majin` (MAJIN VEGETA), `absorbe` (IMPERFECTO, SUPER BUU, BUU GOHAN), `legendario` (LEGENDARIO), `cansancio` (100%). Los multiplicadores de daño crecen con la forma (SSJ 1,25 → UI DOMINADO 2,4) y SSJ3, SSJ BLUE y GOLDEN tienen además una duración más corta: `MEJORAS[forma].duraK` (0,7), que la tarea 2 aplica a `tiempos(paso).dura`.
- [ ] **Paso 4: ejecutar la comprobación y ver que pasa.** Salida esperada: una línea «Transformaciones: datos correctos.».
- [ ] **Paso 5: commit** «Transformaciones: datos de cadenas, tiempos y mejoras».

### Tarea 2: máquina de la carga de ki

**Archivos:**
- Modificar: `02 - Código del juego/transformaciones.js`
- Modificar: `herramientas/comprobar_transformaciones.cjs`

**Interfaces:**
- Consume: `tiempos`, `mejora` (tarea 1).
- Produce:
  - `nuevo() → T` con `T={carga:0, paso:0, t:0, cargando:false}` (`carga` de 0 a 1 hacia el paso siguiente; `paso` 0 = base; `t` = segundos que quedan de transformación).
  - `avanzar(T, e, dt) → evento|null`, con `e={cargando:bool, golpes:int, muertes:int, abiertos:int, nombre:(paso)=>string}`. Devuelve `'sube'`, `'vuelve'` o `null` y modifica `T`.
    - Si `e.cargando` y `T.paso<e.abiertos`: `T.carga += dt/tiempos(T.paso+1).carga`.
    - Cada golpe resta `0.35` a `T.carga` (mínimo 0); cada muerte suma `0.005` (aunque no se esté cargando).
    - Si `T.carga>=1`: `T.paso++`, `T.carga=0`, `T.t = tiempos(T.paso).dura * (mejora(e.nombre(T.paso)).duraK||1)` y devuelve `'sube'`. Si se sigue manteniendo, empieza a cargar el paso siguiente.
    - Si `T.paso>0`: `T.t-=dt`; al llegar a 0, `T.paso=0`, `T.carga=0` y devuelve `'vuelve'`.
  - Poder máximo: un personaje con cadena de un solo elemento usa `abiertos=1` y el paso 1 es «PODER MÁXIMO».

- [ ] **Paso 1: añadir a la comprobación los casos de la máquina:**

```js
const nom=()=> 'SUPER SAIYAN', T0=T.nuevo();
let ev=null;for(let i=0;i<31;i++)ev=T.avanzar(T0,{cargando:true,golpes:0,muertes:0,abiertos:2,nombre:nom},0.1)||ev;
assert.equal(ev,'sube');assert.equal(T0.paso,1);assert.equal(T0.t>24,true);           // 3 s de carga → 1.ª forma
const T1=T.nuevo();T.avanzar(T1,{cargando:true,golpes:0,muertes:0,abiertos:2,nombre:nom},1.5);
T.avanzar(T1,{cargando:false,golpes:1,muertes:0,abiertos:2,nombre:nom},0);
assert.ok(Math.abs(T1.carga-0.15)<1e-9);                                                // un golpe quita 0,35
T.avanzar(T1,{cargando:false,golpes:0,muertes:0,abiertos:2,nombre:nom},5);
assert.ok(Math.abs(T1.carga-0.15)<1e-9);                                                // soltar no pierde la carga
const T2=T.nuevo();T.avanzar(T2,{cargando:true,golpes:0,muertes:0,abiertos:0,nombre:nom},10);
assert.equal(T2.carga,0);                                                               // sin formas abiertas no carga
const T3={carga:0,paso:1,t:0.05,cargando:false};
assert.equal(T.avanzar(T3,{cargando:false,golpes:0,muertes:0,abiertos:2,nombre:nom},0.1),'vuelve');assert.equal(T3.paso,0);
const T4={carga:0.99,paso:1,t:20,cargando:true};
assert.equal(T.avanzar(T4,{cargando:true,golpes:0,muertes:0,abiertos:1,nombre:nom},1),null); // no pasa de la última abierta
```

- [ ] **Paso 2: ejecutarla y ver que falla** (`T.nuevo is not a function`).
- [ ] **Paso 3: implementar `nuevo` y `avanzar`** en `transformaciones.js` según la interfaz.
- [ ] **Paso 4: ejecutarla y ver que pasa.**
- [ ] **Paso 5: commit** «Transformaciones: carga de ki forma a forma».

### Tarea 3: conectar la carga con la partida

**Archivos:**
- Modificar: `index.html` (cargar `transformaciones.js?v=1` justo antes de `script.js`; subir `script.js?v=`)
- Modificar: `02 - Código del juego/script.js`: teclado (línea ~4094), `pointerdown` del lienzo (~4115), creación de `P` (~4026), `update` (~5160: movimiento, disparo automático en ~4399 y la llamada a `checkForm()` en ~5370), `hitPlayer` (~4271), muerte de enemigo (~4230), `checkForm` (~5103).
- Modificar: `herramientas/comprobar_formas.cjs` (el `checkForm` de antes desaparece; la comprobación del deseo a Shenron se queda)

**Interfaces:**
- Consume: `TRANSF.cadena`, `nivelPaso`, `nuevo`, `avanzar` (tareas 1 y 2); `formasAbiertas(hid)`.
- Produce en `script.js`: `P.tr` (el `T` de la tarea 2), `P.trCad` (la cadena del héroe), `P.trGolpes`, `P.trMuertes`, `trAbiertos() → int` (pasos abiertos = mínimo entre los abiertos por nivel con `nivelPaso` y `formasAbiertas(S.hid)`; 1 para los de una sola forma) y `cargandoKi() → bool` (`keys.Space` o el botón táctil mantenido, y `state==='play'`). En `window.AS`: `tr:()=>P.tr`.

- [ ] **Paso 1: actualizar `comprobar_formas.cjs`**: quitar los casos de «En partida: el nivel solo transforma…» y añadir uno que cargue `transformaciones.js` y el tramo de `trAbiertos` de `script.js` y compruebe: Goku nivel 12 con 3 deseos → 2 pasos; nivel 40 con 1 deseo → 1 paso; Krilin sin deseos → 1 paso.
- [ ] **Paso 2: ejecutarla y ver que falla** (no existe `trAbiertos`).
- [ ] **Paso 3: implementar en `script.js`**: `P.tr=TRANSF.nuevo()` y `P.trCad` al crear `P`; `P.form=P.trCad[P.tr.paso]` cada fotograma; mientras `cargandoKi()` y la carga avanza: sin movimiento ni disparo automático, y `P.dir`/pose de carga (`Pow`); `hitPlayer` suma `P.trGolpes`; la muerte de un enemigo suma `P.trMuertes`; en `'sube'` reutilizar el estallido de la antigua `checkForm` (banner con el nombre de la forma, `S.flash`, `S.freeze=0.4`, temblor, `sfx('trans')`, `PFX.transform`) y actualizar `P.hp` a la nueva vida máxima sin curar de más; en `'vuelve'`, banner corto «FIN DE LA TRANSFORMACIÓN». Quitar la llamada automática a `checkForm()` por nivel. La carga no avanza fuera de `state==='play'`.
- [ ] **Paso 4: ejecutar** `node --check "02 - Código del juego/script.js"`, `node herramientas/comprobar_formas.cjs` y `node herramientas/comprobar_transformaciones.cjs`: todo pasa.
- [ ] **Paso 5: probar en el navegador** (servidor de `.claude/launch.json` o `python3 -m http.server`): con Goku, mantener Espacio → se queda quieto, en 3 s pasa a SSJ, sigue cargando → SSJ2 si está abierto; a los 25 s vuelve a la base. Revisar los cinco puntos de revisión de arriba.
- [ ] **Paso 6: commit** «Transformaciones: la barra de ki sustituye a la transformación por nivel».

### Tarea 4: mejoras de cada forma

**Archivos:**
- Modificar: `02 - Código del juego/transformaciones.js` (función pura `efecto`)
- Modificar: `02 - Código del juego/script.js`: `stats()` (~4044), `hitPlayer`, muerte de enemigo, impactos de los ataques (`hurt`, ~4218) y `update`
- Modificar: `herramientas/comprobar_transformaciones.cjs`

**Interfaces:**
- Produce: `TRANSF.efecto(nombreForma, ctx) → {dmg, spd, cd, hpMax, recibe, regen, drenaje, esquiva, contra, cura, rayos}` con `ctx={vidaFrac, tTrans}` (`vidaFrac` de 0 a 1; `tTrans`, segundos transformado). Valores neutros: multiplicadores 1 y demás 0/false.
  - `kaioken`: `drenaje` 0,02 de la vida máxima por segundo (nunca baja de 1 de vida).
  - `regenera`: `regen` 0,015 de la vida máxima por segundo.
  - `esquiva`: probabilidad 0,3; `esquivaContra`: 0,6 y `contra:true` (al esquivar, golpe a quien atacó).
  - `ultraEgo`: `dmg` × (1 + 0,8 × (1 − vidaFrac)). `bestia`: igual con 1,0. `legendario`: `dmg` × (1 + min(0,5; tTrans/40)).
  - `majin`: `recibe` 1,25. `absorbe`: `cura` 0,01 de la vida máxima por enemigo muerto. `rayos`: `rayos:true` (cada impacto salta a un enemigo a 60 px con el 40 % del daño). `cansancio`: `dmg` × (1 − min(0,3; tTrans/60)).
  - Se combinan con los multiplicadores de `mejora(nombre)` (dmg, spd, cd, hp).

- [ ] **Paso 1: casos en la comprobación**: `efecto('ULTRA EGO',{vidaFrac:0.5,tTrans:0}).dmg` ≈ `mejora('ULTRA EGO').dmg*1.4`; `efecto('KAIOKEN',…).drenaje===0.02`; `efecto('BASE',…)` neutro salvo los multiplicadores de `mejora`; `efecto('LEGENDARIO',{vidaFrac:1,tTrans:40}).dmg` ≈ `mejora('LEGENDARIO').dmg*1.5`.
- [ ] **Paso 2: ver que falla.**
- [ ] **Paso 3: implementar `efecto`** y usarlo en `script.js`: `stats()` cambia `(1+0.25*f)`, `15*f`, `(1+0.06*f)` y `(1-0.05*f)` por los valores de `efecto`; `update` aplica `drenaje` y `regen`; `hitPlayer` aplica `recibe`, `esquiva` y `contra`; la muerte de enemigo aplica `cura`; `hurt` aplica `rayos`. En base (`paso 0`) todo neutro.
- [ ] **Paso 4: ver que pasa** y `node --check`.
- [ ] **Paso 5: probar en el navegador** Kaioken (baja la vida poco a poco), UI Señal (texto «ESQUIVA» en algunos golpes) y Perfecto (sube la vida).
- [ ] **Paso 6: commit** «Transformaciones: mejora propia de cada forma».

### Tarea 5: los enemigos castigan la carga

**Archivos:**
- Modificar: `02 - Código del juego/script.js`: movimiento de enemigos (~5212), `bossAI` (~4751), `bossBeam` (~4743)

**Interfaces:**
- Consume: `cargandoKi()` y `P.tr` (tarea 3).

- [ ] **Paso 1: implementar**: mientras se carga, los enemigos normales a menos de 260 px van a por el jugador con velocidad × 1,35 e ignoran la distancia de los tiradores (`rolAI` devuelve `null` para ellos); los jefes a menos de 320 px adelantan su rayo (`e.bT=Math.min(e.bT,1.2)`) y su embestida (`e.aiT=Math.min(e.aiT,0.8)`).
- [ ] **Paso 2: probar en el navegador**: cargar en una horda (llegan más rápido y quitan carga) y delante de un jefe (`AS.spawnBoss`): dispara antes.
- [ ] **Paso 3: `node --check`, `node herramientas/comprobar_roles.cjs` y `node herramientas/comprobar_combate.cjs`** siguen pasando.
- [ ] **Paso 4: commit** «Transformaciones: los enemigos van a por quien carga».

### Tarea 6: barra de ki en el HUD y botón táctil

**Archivos:**
- Modificar: `02 - Código del juego/script.js`: `hud(time)` (~7480) y `pointerdown`/`pointerup` del lienzo (~4115)

**Interfaces:**
- Consume: `P.tr`, `P.trCad`, `trAbiertos()`, `TRANSF.tiempos`.
- Produce: `P.kiR=[x,y,w,h]` (rectángulo del botón táctil, en las mismas coordenadas que `P.barR`) y `P.kiToque` (bool).

- [ ] **Paso 1: implementar** bajo la barra de experiencia del panel de arriba a la izquierda una barra de ki dorada: se llena con `P.tr.carga`; a su lado, el nombre de la forma siguiente («SSJ2», «PODER MÁXIMO») o «MÁX.» si no hay más abiertas; transformado, una segunda línea con la cuenta atrás (`P.tr.t`); sin deseos pedidos, el texto «PIDE LA FORMA A SHENRON». En pantallas táctiles, un botón redondo «KI» abajo a la derecha (`P.kiR`) que carga mientras se mantiene pulsado.
- [ ] **Paso 2: probar en el navegador** en escritorio y con `resize_window` móvil (375×812): la barra se lee y el botón carga.
- [ ] **Paso 3: commit** «Transformaciones: barra de ki y botón táctil».

### Tarea 7: auras con PixelFX y GIF para Josemi

**Archivos:**
- Modificar: `herramientas/efectos_pixelfx/fx/aura.js` y, si hace falta, `fx/transformacion.js`
- Regenerar: `02 - Código del juego/efectos_pixelfx.js` (pasos de `herramientas/efectos_pixelfx/LEEME.md`)
- Modificar: `02 - Código del juego/script.js`: dibujo del jugador (~7182, donde está comentado `PFX.aura`)
- Modificar: `index.html` (`efectos_pixelfx.js?v=`)

**Interfaces:**
- Consume: `PFX.aura(ctx,x,y,kind,time,rayos,k)`, `PFX.transform(x,y,kind)`, `heroAura(hid,form)`.

- [ ] **Paso 1: mejorar el aura con el skill de PixelFX** (`pixelfx:pixelfx`; copia en `herramientas/pixelfx/`) tomando como modelo las hojas `05 - Sprites nuevos encontrados/04_Assets_y_Objetos/03_Efectos_FX_y_Auras/DBZ_Auras_Todas_las_Fases_SWL_[JustOruma_Samuca0123].png` y `Carga_de_Ki_Aura_Secuencia_[ZaruMania].png`: llamas en bucle detrás y delante del personaje, chispas que suben y polvo en el suelo mientras se carga. Colores: blanco (carga y poder máximo), dorado, azul, rojo, morado, rosa, verde, naranja y plateado (UI). Renderizar con `node tools/act.mjs … --sheet` y revisarlo a ojo.
- [ ] **Paso 2: regenerar `efectos_pixelfx.js`** y subir su `?v=`.
- [ ] **Paso 3: dibujar el aura** solo mientras `cargandoKi()` (blanca, con rayos) o `P.tr.paso>0` (color de `heroAura`; blanca en poder máximo). Nunca en base sin cargar.
- [ ] **Paso 4: grabar un GIF** con Goku: carga → SSJ → carga → SSJ2 → fin; y otro con Krilin en poder máximo. Mandárselos a Josemi y esperar su opinión antes de seguir.
- [ ] **Paso 5: commit** «Transformaciones: auras de PixelFX al cargar y transformarse».

### Tarea 8: cierre

**Archivos:**
- Modificar: `01 - Guía y documentación/TRANSFORMACIONES.md`, `ESTADO_ACTUAL.md`, `LISTA_PENDIENTES.md` (marcar los puntos 1-5), `BITACORA.md`, `PRUEBAS_RAPIDAS.md` (añadir `comprobar_transformaciones.cjs`)

- [ ] **Paso 1: ejecutar todas las comprobaciones** (`node --check`, `comprobar_transformaciones`, `comprobar_formas`, `comprobar_roles`, `comprobar_combate`, `comprobar_personajes`) y anotar en la bitácora cuáles pasan y cuáles fallaban ya antes (enemigos, objetos y rotación fallan desde el 6 nov.).
- [ ] **Paso 2: jugar una partida corta** con Goku, Vegeta, Cell y Krilin y apuntar qué se probó.
- [ ] **Paso 3: actualizar los documentos** y hacer commit «Transformaciones: documentación y estado».
