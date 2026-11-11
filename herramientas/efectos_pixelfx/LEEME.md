# Efectos de pixelfx

`efectos.js` es el puente entre [pixelfx](https://github.com/patch-gg/pixelfx) (MIT, por Patch; método de Hugo Duprez)
y el juego. Se empaqueta en un solo archivo, `02 - Código del juego/efectos_pixelfx.js`, que define `window.PFX`.
Así el juego sigue funcionando con doble clic (sin módulos ni fetch).

Qué hace ahora (prueba del 4 nov. 2026):

| Momento del juego | Efecto de pixelfx | Dónde se llama en `script.js` |
|---|---|---|
| Explosiones de ki (`explode`: Big Bang, Masenko, Genkidama, Death Ball…) | `explosions/plasma-explosion`, con los colores de la técnica | `explode()` |
| Hakai | `explosions/implosion` | `fireSig()`, rama `nova` |
| Final Explosion y Autodestrucción | `explosions/plasma-explosion` | `fireSig()`, rama `nova` |
| Otras técnicas de área (Gigantic Roar, Kill Driver…) | `arcane/mana-burst` | `fireSig()`, rama `nova` |
| Kamehameha y variantes (técnicas con `kame` en el id): carga, rayo e impacto | `fx/kamehameha.js` (propio, hecho con pixelfx) | `fire()`, rama `beam` (`PFX.beam`), y `drawBeam` (`PFX.drawBeam`) |
| Cada golpe del combo que toca | `impacts/hit-spark`; el último, `impacts/crit-hit` | `update`, bloque `P.combo` |

Hay un tope de efectos vivos por tipo (`CAP`) y una duración máxima (`MAX_T`). Si `efectos_pixelfx.js` no carga,
el juego usa sus efectos de siempre.

## Volver a generarlo (después de cambiar `efectos.js`)

Dentro de esta carpeta, con Node instalado:

```
npm i --no-save ../pixelfx esbuild
npx esbuild efectos.js --bundle --minify --format=iife --legal-comments=none --outfile="../../02 - Código del juego/efectos_pixelfx.js"
```

Después sube `efectos_pixelfx.js?v=` en `index.html`. Generado con pixelfx `a841596` (31 oct. 2026); la librería
tiene pocos días y puede cambiar.

## Efectos propios (11 nov. 2026)

`fx/kamehameha.js` importa de `pixelfx`. Para verlo con las herramientas de pixelfx, clona el repositorio en `herramientas/pixelfx` (está en `.gitignore`), copia el archivo a `herramientas/pixelfx/src/fx/ki/kamehameha.js` cambiando `from "pixelfx"` por `from "../../core/index.js"` y usa `node tools/render.mjs ki/kamehameha`, `node tools/check.mjs ki/kamehameha` y `node tools/act.mjs ki/kamehameha --sheet`.

Opciones que pasa el juego: `len` y `wid` (largo y grosor del rayo), `charge` y `fire` (segundos de carga y de rayo), `palette` (los colores de la técnica). Desde el 11 nov. se genera con pixelfx 0.3.1 (`044e12a`).
