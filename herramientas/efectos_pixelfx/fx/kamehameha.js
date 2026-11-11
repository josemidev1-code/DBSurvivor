// Kamehameha para DBSurvivor, hecho con pixelfx (github.com/patch-gg/pixelfx, MIT).
// La construcción del rayo (bandas de núcleo blanco a borde oscuro, borde con trama, pulsos que recorren el rayo,
// destello en el origen y en la punta) está adaptada del energy beam de Sprite Fusion
// (https://www.spritefusion.com/pixel-art-vfx/energy), MIT License, Copyright (c) 2026 Hugo Duprez.
//
// Tres fases sobre un solo reloj:
//   0 .. charge                carga: una bola que crece entre las manos y absorbe chispas
//   charge .. charge+fire      rayo: sale disparado, se mantiene estable (no cambia de forma) y se estrecha al final
//   charge+fire .. +BURST      impacto: explosión en la punta (destello, anillo, chispas y vapor)
// El origen (0, 0) son las manos; el rayo apunta a la derecha. El juego gira el lienzo con el ángulo del disparo.
import { fit, ease, fract, clamp, cycle, fly, Rng, TAU, WHITE, READY } from "pixelfx";

// estilo: "kame" (Kamehameha), "galick" (chispas eléctricas en los bordes), "flash" (Final Flash: cabeza y
// explosión más grandes, rayos en la carga), "masenko" y "espiral" (Makankosappo: núcleo fino y dos espirales).
const hash = (a) => fract(Math.sin(a * 127.1 + 311.7) * 43758.5453);

const BAYER = [0, 8, 2, 10, 12, 4, 14, 6, 3, 11, 1, 9, 15, 7, 13, 5].map((v) => (v + 0.5) / 16);
const bayer = (x, y) => BAYER[((Math.floor(y) & 3) << 2) | (Math.floor(x) & 3)];

export const BURST = 0.6; // lo que dura la explosión final
const EXT = 0.14; // lo que tarda el rayo en llegar a su longitud
const SHRINK = 0.2; // lo que tarda en estrecharse antes de apagarse

const KAME = ["#0a2a6a", "#1f6fe0", "#3aa0ff", "#6cd0ff", "#c8f4ff", "#f4ffff"];

export const meta = {
  name: "Kamehameha",
  desc: "Una bola azul crece entre las manos, sale un rayo estable de núcleo blanco y borde azul y estalla en la punta.",
  tags: ["ki", "beam", "kamehameha", "charge", "impact", "directional"],
  size: [336, 110],
  origin: [26, 84],
  duration: 0.75 + 1.0 + BURST,
  loop: false,
  fps: 30,
  bg: "ground",
  actor: 2,
  // hx, hy: dónde están las manos respecto a los pies (en el juego son 0, 0 porque el lienzo se pone en la mano)
  options: { palette: KAME, seed: 7, len: 240, wid: 16, charge: 0.75, fire: 1.0, hx: 15, hy: -24, estilo: "kame", espiral: ["#5a1a90", "#a050ff", "#e8c8ff"] },
};

// Para la vista previa de pixelfx: manos atrás mientras carga, empuje hacia delante al disparar.
const CUP = { ...READY, x: -4, crouch: 5, lean: -4, fx: -2, fy: -20, bx: 1, by: -19, ffx: 9, fbx: -8, turn: 1 };
const PUSH = { ...READY, x: -3, crouch: 4, lean: 4, fx: 15, fy: -24, bx: 14, by: -22, ffx: 11, fbx: -9, toeB: true };
export const act = {
  target: { x: 252 },
  poses: [
    [-0.2, { ...READY, x: -3 }],
    [0.05, CUP],
    [0.7, { ...CUP, crouch: 6, lean: -5 }],
    [0.75, PUSH, "snap"],
    [1.6, { ...PUSH, crouch: 5 }],
    [1.9, { ...READY, x: -3 }],
  ],
  hits: [{ t: 0.82, stop: 0.06, shake: 0.2, amp: 2, push: 0.6, flash: 0.03, y: -24 }, { t: 1.75, stop: 0.08, shake: 0.25, amp: 2, push: 2, skin: "shock", y: -24 }],
  dust: [{ t: 0.75, x: -10, n: 6, dir: -1 }],
};

// Bola de energía con bandas: blanco en el centro y borde azul tramado.
function orb(p, x, y, r, C, ph) {
  if (r < 0.6) return;
  const LV = [WHITE, C[5], C[4], C[3], C[2], C[1]];
  const R = r * 1.25;
  for (let dy = -R; dy <= R; dy += 0.5) for (let dx = -R; dx <= R; dx += 0.5) {
    const q = Math.hypot(dx, dy) / r;
    if (q > 1.25) continue;
    const lv = q < 0.34 ? 0 : q < 0.52 ? 1 : q < 0.7 ? 2 : q < 0.88 ? 3 : q < 1.05 ? 4 : 5;
    if (lv === 5 && bayer(x + dx, y + dy) > (1.25 - q) / 0.15) continue;
    p.px(x + dx, y + dy, LV[lv]);
  }
  p.glow(x, y, r * 2.4 + 5, C[3], 0.55);
  p.glow(x, y, r + 2, WHITE, 0.35 + 0.1 * Math.sin(ph * TAU * 6));
}

// arcos eléctricos cortos alrededor de un punto (carga del Galick Gun)
function arcs(p, x0, y0, r, k, S, C) {
  for (let i = 0; i < 3; i++) {
    const a = hash(k * 5 + i * 17 + S) * TAU;
    let x = x0 + Math.cos(a) * r, y = y0 + Math.sin(a) * r;
    for (let j = 0; j < 4; j++) {
      const nx = x + Math.cos(a) * 2 + (hash(k + i * 3 + j) - 0.5) * 4, ny = y + Math.sin(a) * 2 + (hash(k * 7 + j + i) - 0.5) * 4;
      p.line(x, y, nx, ny, j % 2 ? C[4] : WHITE);
      x = nx; y = ny;
    }
  }
}

export function draw(p, t, o) {
  const C = fit(o.palette, 6), S = o.seed | 0, HX = o.hx, HY = o.hy;
  const CH = o.charge, FI = o.fire, L = o.len;
  let hw = Math.max(3, o.wid / 2);
  const u = t - CH, te = t - CH - FI;

  // ---- carga
  if (t < CH) {
    const k = ease.outCubic(clamp(t / CH));
    // la bola cabe entre las manos: no debe tapar al personaje
    const r = 1.5 + k * Math.min(7, hw * 0.55) + 0.4 * Math.sin(t * 40) * k;
    // chispas que entran en espiral hacia las manos
    cycle(t, 0.5, 14, S * 5 + 1, (g) => g.range(0.22, 0.4), (age, life, rr) => {
      const q = age / life, a = rr.range(0, TAU) + q * 2.2, d = (r + 4) + (1 - ease.inQuad(q)) * rr.range(14, 26);
      const x = HX + Math.cos(a) * d, y = HY + Math.sin(a) * d * 0.8;
      p.line(x, y, x + Math.cos(a) * 3, y + Math.sin(a) * 2.4, q > 0.6 ? WHITE : C[4]);
    });
    // dos anillos que se cierran sobre la bola
    for (let i = 0; i < 2; i++) {
      const q = fract(t / 0.42 + i / 2), rad = r + 2 + (1 - ease.outQuad(q)) * 12;
      p.ring(HX, HY, rad, 1, q > 0.7 ? WHITE : C[3], 0.35 + 0.5 * q);
    }
    orb(p, HX, HY, r, C, t);
    if (o.estilo === "flash" || o.estilo === "masenko") {
      // destello en estrella que crece con la carga
      const L = r * (o.estilo === "flash" ? 3 : 2.2) * (0.85 + 0.15 * Math.sin(t * 50));
      for (let i = 0; i < 4; i++) { const a = (i * TAU) / 4 + TAU / 8; p.line(HX, HY, HX + Math.cos(a) * L, HY + Math.sin(a) * L, (v) => (v < 0.5 ? WHITE : C[3]), (v) => 1 - v); }
    }
    if (o.estilo === "galick") arcs(p, HX, HY, r + 3, Math.floor(t * 15), S, C);
    return;
  }

  // ---- rayo
  if (u < FI) {
    const ext = ease.outQuart(clamp(u / EXT));
    const sh = 1 - ease.inQuad(clamp((u - (FI - SHRINK)) / SHRINK));
    const esp = o.estilo === "espiral", Lc = L * ext, w0 = (esp ? Math.max(1.5, hw * 0.45) : hw) * sh;
    const LV = [WHITE, C[5], C[4], C[3], C[2], C[1]];
    for (let d = 0; d <= Lc; d += 0.5) {
      const x = HX + d;
      // grosor estable: se abre al salir de las manos y una ondulación de medio píxel como mucho
      const w = w0 * (0.45 + 0.55 * Math.min(1, d / 26)) * (1 + 0.035 * Math.sin(d * 0.21 - u * 34));
      if (w < 0.6) continue;
      const pulse = fract(d * 0.02 - u * 3.2) < 0.06 ? 1 : 0;
      for (let q0 = -w * 1.22; q0 <= w * 1.22; q0 += 0.5) {
        const q = Math.abs(q0) / w, y = HY + q0;
        let lv = q < 0.26 ? 0 : q < 0.42 ? 1 : q < 0.6 ? 2 : q < 0.78 ? 3 : q < 0.96 ? 4 : 5;
        lv = Math.max(0, lv - pulse);
        if (lv === 5 && bayer(x, y) > (1.22 - q) / 0.2) continue;
        p.px(x, y, LV[lv]);
      }
      if ((Math.round(d * 2) % 12) === 0) p.glow(x, HY, w * 2 + 6, C[3], 0.22 * sh);
    }
    // chispas que se desprenden por los bordes
    cycle(u, 0.6, 18, S * 5 + 2, (g) => g.range(0.2, 0.45), (age, life, rr) => {
      const q = age / life, x = HX + rr.range(12, Math.max(14, Lc - 8)) + q * 26, side = rr.sign();
      const y = HY + side * (w0 + 1 + q * rr.range(4, 10));
      if (x < HX + Lc) p.dot(x, y, q < 0.5 ? WHITE : C[4], 1 - q);
    });
    if (esp) {
      // dos espirales que se enroscan alrededor del núcleo; la de delante, más clara
      const SP = fit(o.espiral, 3), R2 = hw + 2;
      for (let d = 2; d <= Lc; d += 1) {
        for (let s2 = 0; s2 < 2; s2++) {
          const a = d * 0.22 - u * 28 + s2 * Math.PI, off = Math.sin(a) * R2 * sh, front = Math.cos(a) > 0;
          p.rect(HX + d, HY + off - 1, 1, 2, front ? (Math.cos(a) > 0.7 ? WHITE : SP[2]) : SP[1]);
        }
      }
    }
    if (o.estilo === "galick") {
      // chispas eléctricas que saltan por los bordes del rayo
      const k = Math.floor(u * 15);
      for (let i = 0; i < 5; i++) {
        const d0 = hash(k * 7 + i * 13 + S) * Math.max(8, Lc - 20) + 10, side = hash(k + i * 3) < 0.5 ? -1 : 1;
        let x = HX + d0, y = HY + side * (w0 + 1);
        for (let j = 0; j < 5; j++) {
          const nx = x + 2 + hash(k * 3 + i * 5 + j) * 3, ny = HY + side * (w0 + 1 + hash(k * 11 + i + j * 7) * 5);
          p.line(x, y, nx, ny, j % 2 ? C[4] : WHITE);
          x = nx; y = ny;
        }
      }
    }
    // fogonazo en las manos
    orb(p, HX, HY, Math.min(7, w0 * 0.6) + 0.4 * Math.sin(u * 50), C, u);
    // la cabeza del rayo: más ancha, con rayos hacia atrás y anillos
    const EX = HX + Lc, hr = esp ? w0 * 1.6 + 1 : w0 * (o.estilo === "flash" ? 1.6 : 1.3);
    for (let i = 0; i < 6; i++) {
      const a = Math.PI + (i - 2.5) * 0.42, l = hr + 4 + 4 * fract(Math.sin((i + 1) * 12.9 + Math.floor(u * 15)) * 43758);
      p.line(EX, HY, EX + Math.cos(a) * l, HY + Math.sin(a) * l, (v) => (v < 0.45 ? WHITE : C[4]), (v) => (v < 0.6 ? 1 : 1.6 - v));
    }
    for (let k = 0; k < 2; k++) {
      const q = fract(u * 2.6 + k / 2);
      p.ring(EX, HY, hr + 2 + 12 * ease.outCubic(q), Math.max(1, 2 * (1 - q)), q < 0.3 ? WHITE : C[3], (1 - q) * sh);
    }
    orb(p, EX, HY, hr, C, u);
    p.glow(EX, HY, 34, C[3], 0.6 * sh);
    return;
  }

  // ---- explosión en la punta
  if (te < BURST) {
    const EX = HX + L, q = te / BURST, R = new Rng(S * 31 + 9);
    if (o.estilo === "flash") hw = hw * 1.35;
    if (o.estilo === "espiral") hw = Math.max(5, hw * 0.8);
    // destello blanco que se encoge
    if (te < 0.16) orb(p, EX, HY, hw * 1.6 * (1 - te / 0.16) + 3, C, te);
    // dos anillos de choque
    for (let k = 0; k < 2; k++) {
      const qq = clamp((te - k * 0.07) / 0.4);
      if (qq > 0 && qq < 1) p.ring(EX, HY, 4 + (hw * 2.4 + 14) * ease.outQuart(qq), Math.max(1, 3 * (1 - qq)), qq < 0.25 ? WHITE : C[3 - k], 1 - qq);
    }
    // bola de energía que se deshace con trama
    const br = hw * 1.5 * (1 - ease.inQuad(q)) * ease.outQuart(clamp(te / 0.08));
    if (br > 0.8) {
      for (let dy = -br; dy <= br; dy += 0.5) for (let dx = -br; dx <= br; dx += 0.5) {
        const d = Math.hypot(dx, dy) / br;
        if (d > 1 || bayer(EX + dx, HY + dy) < q * 0.9) continue;
        p.px(EX + dx, HY + dy, d < 0.4 ? WHITE : d < 0.7 ? C[4] : C[3]);
      }
    }
    // chispas en todas direcciones
    for (let i = 0; i < 26; i++) {
      const a = R.range(0, TAU), sp = R.range(90, 230), life = R.range(0.25, 0.5);
      if (te > life) continue;
      const [x, y] = fly(EX, HY, Math.cos(a) * sp, Math.sin(a) * sp, te, 0, 3), k = 1 - te / life;
      const [x2, y2] = fly(EX, HY, Math.cos(a) * sp, Math.sin(a) * sp, Math.max(0, te - 0.025), 0, 3);
      p.line(x2, y2, x, y, k > 0.5 ? WHITE : C[4]);
    }
    // vapor azul que sube y se aclara
    for (let i = 0; i < 6; i++) {
      const ox = R.range(-hw, hw), oy = R.range(-hw, hw), rad = R.range(3, 6) * (0.7 + q);
      p.disc(EX + ox, HY + oy - q * R.range(8, 18), rad, C[3], (dd) => 0.3 * Math.sin(q * Math.PI) * (1 - dd * dd));
    }
    p.glow(EX, HY, 40 * (1 - q) + 6, C[3], 0.8 * (1 - q));
  }
}
