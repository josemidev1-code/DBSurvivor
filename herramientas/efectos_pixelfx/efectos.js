// Puente entre pixelfx (github.com/patch-gg/pixelfx, MIT) y AnimeSurvivor.
// Se empaqueta con esbuild en "02 - Código del juego/efectos_pixelfx.js" (un solo archivo, sin módulos ni fetch,
// para que el juego siga abriéndose con doble clic). Expone window.PFX.
import { createFrame, clearFrame, createFx, composite, painterFor } from "pixelfx";
import * as kame from "./fx/kamehameha.js";
import * as aura from "./fx/aura.js";
import * as trans from "./fx/transformacion.js";
import * as kienzan from "./fx/kienzan.js";
import * as taiyo from "./fx/taiyoken.js";
import * as golpe from "./fx/golpe.js";
import * as blunt from "pixelfx/fx/impacts/blunt-hit";
import * as columna from "./fx/columna_esfera.js";
import * as collect from "pixelfx/fx/pickups/collect-burst";
import * as lvl from "pixelfx/fx/ui/level-up";
import * as clima from "./fx/clima.js";
import * as plasma from "pixelfx/fx/explosions/plasma-explosion";
import * as implosion from "pixelfx/fx/explosions/implosion";
import * as mana from "pixelfx/fx/arcane/mana-burst";
import * as spark from "pixelfx/fx/impacts/hit-spark";
import * as crit from "pixelfx/fx/impacts/crit-hit";

const LIB = { plasma, implosion, mana, spark, crit, trans, taiyo, golpe, blunt, collect, lvl };
// tope de efectos vivos por tipo: en plena horda no se acumulan cientos
const CAP = { plasma: 10, implosion: 4, mana: 6, spark: 14, crit: 6, trans: 2, taiyo: 2, golpe: 4, blunt: 8, collect: 6, lvl: 1 };
const MAX_T = { plasma: 1.2, implosion: 1.7, mana: 1.3, spark: 0.5, crit: 0.8, trans: 2.3, taiyo: 0.75, golpe: 0.4, blunt: 0.7, collect: 1.4, lvl: 2.6 };

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

let live = [], seed = 1, rayos = [], climaEstado = null;

// ---- aura de cada forma: los fotogramas del bucle se pintan una vez por color y se guardan
// (los mismos colores que las llamas de antes del juego, auraFlames en script.js)
const AURA_COL = { gold: ["#e8a010", "#ffd23f", "#fff6a8"], white: ["#7ab8e8", "#bfe6ff", "#ffffff"], orange: ["#d0501a", "#ff9a3a", "#ffe0a0"], red: ["#a01030", "#ff3a5a", "#ffb0c0"], blue: ["#1a7ad8", "#3ad0f0", "#c0f8ff"], green: ["#5aa010", "#b8f040", "#f0ffc0"], purple: ["#5a1a90", "#a050ff", "#e8c8ff"], silver: ["#8a94a8", "#c8d0dc", "#ffffff"] };
const auraCache = {};
const RECOGER_COL = { dball: ["#d48e18", "#f5b92c", "#ffde5e"], senzu: ["#3a8a20", "#7ad040", "#c8f080"], senzuBolsa: ["#3a8a20", "#7ad040", "#c8f080"], zeni: ["#c89a10", "#f0d040", "#fff6a0"], capsulaVida: ["#c02040", "#ff5a7a", "#ffc0d0"], capsulaKi: ["#1a6ad8", "#5ab0ff", "#c8ecff"], capsulaDorada: ["#c89a10", "#ffd23f", "#fff6a8"], capsulaRoja: ["#a01020", "#ff4a4a", "#ffc0c0"], radar: ["#2a9a40", "#6ad870", "#d0ffd0"], chest: ["#c89a10", "#ffd23f", "#fff6a8"], otro: ["#3a8ad8", "#8ac8ff", "#e0f4ff"] };
// bucle de cualquier efecto pintado una vez (fotogramas guardados por clave)
function loopFrames(mod, key, opts) {
  if (auraCache[key]) return auraCache[key];
  const [w, h] = mod.meta.size, [ox, oy] = mod.meta.origin, n = Math.max(1, Math.round(mod.meta.duration * mod.meta.fps));
  const o = { ...mod.meta.options, ...opts }, frame = createFrame(w, h), img = new ImageData(w, h), out = [];
  for (let i = 0; i < n; i++) {
    clearFrame(frame);
    const p = painterFor(frame); p.place(ox, oy, false, 0); p.fade = 1; p.lightK = 1;
    const t = (i / n) * mod.meta.duration;
    if (mod.drawBack) { p.layer = "back"; mod.drawBack(p, t, o); }
    p.layer = "front"; mod.draw(p, t, o);
    composite(frame, img.data, null);
    const cv = document.createElement("canvas"); cv.width = w; cv.height = h; cv.getContext("2d").putImageData(img, 0, 0);
    out.push(cv);
  }
  return (auraCache[key] = { out, ox, oy, fps: mod.meta.fps });
}
function auraFrames(kind, rayos) {
  const key = kind + (rayos ? "+" : "");
  if (auraCache[key]) return auraCache[key];
  const [w, h] = aura.meta.size, [ox, oy] = aura.meta.origin, n = Math.round(aura.meta.duration * aura.meta.fps);
  const o = { ...aura.meta.options, palette: ramp(AURA_COL[kind] || AURA_COL.gold), rayos: rayos ? 1 : 0 };
  const frame = createFrame(w, h), img = new ImageData(w, h), out = [];
  for (let i = 0; i < n; i++) {
    clearFrame(frame);
    const p = painterFor(frame); p.place(ox, oy, false, 0); p.fade = 1; p.lightK = 1;
    const t = (i / n) * aura.meta.duration;
    p.layer = "back"; aura.drawBack(p, t, o); p.layer = "front"; aura.draw(p, t, o);
    composite(frame, img.data, null);
    const cv = document.createElement("canvas"); cv.width = w; cv.height = h; cv.getContext("2d").putImageData(img, 0, 0);
    out.push(cv);
  }
  return (auraCache[key] = { out, ox, oy, fps: aura.meta.fps });
}

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
    o: { ...kame.meta.options, hx: 0, hy: 0, len: b.len, wid: b.wid, charge: b.T, fire: b.dur, estilo: b.estilo || "kame", seed: seed++, ...(r ? { palette: r } : {}) },
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
  if (o.text) opts.text = o.text;
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
  nova(x, y, rad, cols, tipo) { if (tipo === "taiyoken") return !!spawn("taiyo", x, y - 10, {}); return !!spawn(tipo === "hakai" ? "implosion" : tipo === "final" ? "plasma" : "mana", x, y, { cols: tipo === "hakai" ? null : cols }); },
  // golpe cuerpo a cuerpo: chispa en cada golpe, golpe crítico en el último del combo
  // golpe cuerpo a cuerpo: tipo "normal" (golpe sordo o chispa, alternando), "final" (último del combo) o "dragon"
  hit(x, y, dir, tipo) {
    if (tipo === true) tipo = "dragon";
    if (tipo === "final" || tipo === "dragon") { const a = !!spawn("golpe", x, y, { flip: dir < 0 }); if (tipo === "dragon") spawn("crit", x, y, { flip: dir < 0 }); return a; }
    return !!spawn((seed & 1) ? "blunt" : "spark", x, y, { flip: dir < 0 });
  },
  // aura de la forma, detrás del personaje: (x, y) son los pies en pantalla; k, la escala del dibujo
  aura(ctx, x, y, kind, time, rayos, k = 1) {
    const A = auraFrames(kind, rayos), im = A.out[Math.floor(time * A.fps) % A.out.length];
    ctx.drawImage(im, Math.round(x - A.ox * k), Math.round(y - A.oy * k), im.width * k, im.height * k);
    return true;
  },
  // disco (Kienzan y parecidos): (x, y) el centro en pantalla, r el radio del juego, a el ángulo de avance
  disc(ctx, x, y, r, cols, a, time) {
    const R = Math.max(6, Math.round(r * 1.6)), F = loopFrames(kienzan, "disc" + R + (cols || []).join(), { radio: R, ...(ramp(cols) ? { palette: ramp(cols) } : {}) });
    const im = F.out[Math.floor(time * F.fps) % F.out.length];
    ctx.save(); ctx.translate(Math.round(x), Math.round(y)); ctx.rotate(a); ctx.drawImage(im, -F.ox, -F.oy); ctx.restore();
    return true;
  },
  // columna de luz dorada sobre una Esfera del Dragón en el suelo (detrás de la esfera): (x, y) la base en pantalla
  columna(ctx, x, y, time) {
    const F = loopFrames(columna, "columna", { palette: ["#2a1405", "#5c3008", "#9a5a0e", "#d48e18", "#f5b92c", "#ffde5e", "#fff4bc", "#ffffff"] });
    const im = F.out[Math.floor(time * F.fps) % F.out.length];
    ctx.drawImage(im, Math.round(x - F.ox), Math.round(y - F.oy));
    return true;
  },
  // estallido al recoger un objeto, con el color del objeto
  recoger(x, y, kind) { return !!spawn("collect", x, y, { cols: RECOGER_COL[kind] || RECOGER_COL.otro }); },
  // subida de nivel alrededor del personaje
  nivel(x, y, n) { return !!spawn("lvl", x, y, { text: "NIVEL " + n }); },
  // clima del escenario: capa en mosaico pegada al mundo (se mueve con la cámara); se repinta a 30 fps como mucho
  clima(ctx, tipo, cols, camX, camY, time, vw, vh, densidad = 1) {
    const [w, h] = clima.meta.size, key = tipo + (cols || []).join() + densidad;
    let c = climaEstado;
    if (!c || c.key !== key) {
      const cv = document.createElement("canvas"); cv.width = w; cv.height = h;
      c = climaEstado = { key, cv, g: cv.getContext("2d"), frame: createFrame(w, h), img: new ImageData(w, h), f: -1, o: { ...clima.meta.options, tipo, densidad, seed: 9, ...(cols ? { palette: cols } : {}) } };
    }
    const f = Math.floor(time * 30);
    if (f !== c.f) {
      c.f = f; clearFrame(c.frame);
      const p = painterFor(c.frame); p.place(0, 0, false, 0); p.fade = 1; p.lightK = 1;
      clima.draw(p, time % clima.meta.duration, c.o);
      composite(c.frame, c.img.data, null); c.g.putImageData(c.img, 0, 0);
    }
    const ox = -(((Math.round(camX) % w) + w) % w), oy = -(((Math.round(camY) % h) + h) % h);
    for (let y = oy; y < vh; y += h) for (let x = ox; x < vw; x += w) ctx.drawImage(c.cv, x, y);
    return true;
  },
  // Taiyoken: destello cegador en la cara
  taiyoken(x, y) { return !!spawn("taiyo", x, y, {}); },
  // estallido al transformarse, en los pies del personaje, con el color del aura de la nueva forma
  transform(x, y, kind) { return !!spawn("trans", x, y, { cols: AURA_COL[kind] || AURA_COL.gold }); },
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
