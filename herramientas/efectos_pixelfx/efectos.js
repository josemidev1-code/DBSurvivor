// Puente entre pixelfx (github.com/patch-gg/pixelfx, MIT) y AnimeSurvivor.
// Se empaqueta con esbuild en "02 - Código del juego/efectos_pixelfx.js" (un solo archivo, sin módulos ni fetch,
// para que el juego siga abriéndose con doble clic). Expone window.PFX.
import { createFrame, clearFrame, createFx, composite, painterFor } from "pixelfx";
import * as kame from "./fx/kamehameha.js";
import * as plasma from "pixelfx/fx/explosions/plasma-explosion";
import * as implosion from "pixelfx/fx/explosions/implosion";
import * as mana from "pixelfx/fx/arcane/mana-burst";
import * as spark from "pixelfx/fx/impacts/hit-spark";
import * as crit from "pixelfx/fx/impacts/crit-hit";

const LIB = { plasma, implosion, mana, spark, crit };
// tope de efectos vivos por tipo: en plena horda no se acumulan cientos
const CAP = { plasma: 10, implosion: 4, mana: 6, spark: 14, crit: 6 };
const MAX_T = { plasma: 1.2, implosion: 1.7, mana: 1.3, spark: 0.5, crit: 0.8 };

// rampa oscuro→claro a partir de los colores de la técnica del juego (que ya van de oscuro a claro)
const hexN = (h) => { h = h.replace("#", ""); if (h.length === 3) h = h.split("").map((c) => c + c).join(""); return parseInt(h, 16); };
const toHex = (n) => "#" + n.toString(16).padStart(6, "0");
const mixHex = (a, b, k) => {
  const A = hexN(a), B = hexN(b);
  const ch = (s) => Math.round(((A >> s) & 255) * (1 - k) + ((B >> s) & 255) * k) << s;
  return toHex(ch(16) | ch(8) | ch(0));
};
function ramp(cols) {
  const c = (cols || []).filter((x) => typeof x === "string" && /^#[0-9a-f]{3,6}$/i.test(x));
  if (!c.length) return undefined;
  // sin tonos casi negros: pixelfx está pensado para fondos oscuros y en la hierba se verían como manchas
  return [mixHex(c[0], "#000000", 0.3), ...c, "#ffffff"];
}

let live = [], seed = 1, rayos = [];

// ---- rayos tipo Kamehameha: un lienzo por rayo, del largo del rayo, que el juego gira con el ángulo del disparo
const RAYO_MAX = 4;
function nuevoRayo(b) {
  if (rayos.length >= RAYO_MAX) return null;
  const hw = Math.max(3, b.wid / 2), ML = Math.round(hw * 1.6 + 16), MR = Math.round(hw * 2.6 + 70);
  const w = Math.round(ML + b.len + MR), h = 2 * Math.round(Math.max(56, hw * 2.6 + 44));
  const cv = document.createElement("canvas"); cv.width = w; cv.height = h;
  const r = ramp(b.col);
  const e = {
    b, t: 0, ox: ML, oy: h / 2, cv, g: cv.getContext("2d"), frame: createFrame(w, h), img: new ImageData(w, h),
    end: b.T + b.dur + kame.BURST, wx: b.x, wy: b.y, a: b.a,
    o: { ...kame.meta.options, hx: 0, hy: 0, len: b.len, wid: b.wid, charge: b.T, fire: b.dur, seed: seed++, ...(r ? { palette: r } : {}) },
  };
  rayos.push(e);
  return e;
}
function pintaRayo(ctx, e, sx, sy) {
  clearFrame(e.frame);
  const p = painterFor(e.frame);
  p.place(e.ox, e.oy, false, 0); p.fade = 1; p.lightK = 1;
  kame.draw(p, Math.min(e.t, e.end - 1e-3), e.o);
  composite(e.frame, e.img.data, null);
  e.g.putImageData(e.img, 0, 0);
  ctx.save(); ctx.translate(Math.round(sx), Math.round(sy));
  // hacia la izquierda se refleja en vez de girar 180°: así el vapor sigue subiendo
  if (Math.cos(e.a) < 0) { ctx.scale(-1, 1); ctx.rotate(Math.PI - e.a); } else ctx.rotate(e.a);
  ctx.drawImage(e.cv, -e.ox, -e.oy);
  ctx.restore();
}
function spawn(id, x, y, o = {}) {
  const mod = LIB[id]; if (!mod) return null;
  if (live.filter((e) => e.id === id).length >= CAP[id]) return null;
  const [w, h] = mod.meta.size, [ox, oy] = mod.meta.origin;
  const opts = { x: ox, y: oy, seed: seed++ };
  if (o.flip) opts.flip = true;
  if (o.cols) { const r = ramp(o.cols); if (r) { opts.palette = r; if (mod.meta.options && mod.meta.options.accent) opts.accent = r.slice(1); } }
  const cv = document.createElement("canvas"); cv.width = w; cv.height = h;
  const e = { id, x, y, ox, oy, t: 0, fx: createFx(mod, opts), frame: createFrame(w, h), cv, g: cv.getContext("2d"), img: new ImageData(w, h), max: MAX_T[id] };
  live.push(e);
  return e;
}

window.PFX = {
  // explosión de ki (Big Bang, Masenko, Genkidama, Death Ball...): rad = radio de daño del juego
  boom(x, y, rad, cols) { return !!spawn("plasma", x, y, { cols }); },
  // técnicas de área alrededor del personaje
  nova(x, y, rad, cols, tipo) { return !!spawn(tipo === "hakai" ? "implosion" : tipo === "final" ? "plasma" : "mana", x, y, { cols: tipo === "hakai" ? null : cols }); },
  // golpe cuerpo a cuerpo: chispa en cada golpe, golpe crítico en el último del combo
  hit(x, y, dir, last) { return !!spawn(last ? "crit" : "spark", x, y, { flip: dir < 0 }); },
  // Kamehameha y familia: devuelve el estado que el juego guarda en el rayo (b.pfx)
  beam(b) { return nuevoRayo(b); },
  // el juego lo llama desde drawBeam con la posición de las manos en pantalla; el reloj es el del propio rayo
  drawBeam(ctx, b, sx, sy) {
    const e = b.pfx; if (!e) return false;
    e.t = b.t + b.T; e.wx = b.x; e.wy = b.y; e.a = b.a;
    pintaRayo(ctx, e, sx, sy);
    return true;
  },
  update(dt) {
    for (const e of rayos) e.t += dt;
    rayos = rayos.filter((e) => e.t < e.end);
    for (const e of live) { e.t += dt; e.fx.update(dt); if (e.t > e.max - 0.3) e.fx.stop(); }
    live = live.filter((e) => e.t < e.max && !e.fx.done());
  },
  draw(ctx, X, Y) {
    // la explosión final sigue en la punta cuando el juego ya ha quitado el rayo
    for (const e of rayos) if (e.t >= e.b.T + e.b.dur) pintaRayo(ctx, e, X(e.wx), Y(e.wy));
    for (const e of live) {
      clearFrame(e.frame); e.fx.draw(e.frame); composite(e.frame, e.img.data, null);
      e.g.putImageData(e.img, 0, 0);
      ctx.drawImage(e.cv, Math.round(X(e.x) - e.ox), Math.round(Y(e.y) - e.oy));
    }
  },
  clear() { live = []; rayos = []; },
  get n() { return live.length; },
};
