// Transformación (una vez) para DBSurvivor, hecha con pixelfx (github.com/patch-gg/pixelfx, MIT).
//   0 .. CARGA     la energía se concentra: briznas que entran en espiral, el suelo vibra, un núcleo en el pecho
//   CARGA          estallido: destello, columna de luz, onda de choque en el suelo, rayos y piedras que saltan
//   después        llamarada que se apaga, chispas que suben y polvo que se posa
// El origen (0, 0) son los pies. CARGA coincide con la congelación del juego (S.freeze = 0.6 s).
import { fit, clamp, cycle, fly, ease, hex, Rng, TAU, WHITE } from "pixelfx";

const PIEDRA = hex("#8a7a62"), PIEDRA2 = hex("#5a4a3a"), POLVO = hex("#d8c8a8");

const BAYER = [0, 8, 2, 10, 12, 4, 14, 6, 3, 11, 1, 9, 15, 7, 13, 5].map((v) => (v + 0.5) / 16);
const bayer = (x, y) => BAYER[((Math.floor(y) & 3) << 2) | (Math.floor(x) & 3)];
export const CARGA = 0.6;
const D = 1.9;

export const meta = {
  name: "Transformación",
  desc: "Transformación de Dragon Ball: la energía se concentra, estalla en una columna de luz con onda de choque y piedras, y se apaga.",
  tags: ["ki", "aura", "power", "transformation", "burst", "dragon ball"],
  size: [200, 170],
  origin: [100, 136],
  duration: D,
  loop: false,
  fps: 30,
  bg: "ground",
  actor: 2,
  options: { palette: ["#a06008", "#e8a010", "#ffd23f", "#fff6a8", "#ffffff"], seed: 5, alto: 40 },
};

export function draw(p, t, o) {
  const C = fit(o.palette, 5), S = o.seed | 0, AH = o.alto, CY = -AH * 0.55;
  if (t < CARGA) {
    const k = t / CARGA;
    // briznas que entran en espiral hacia el pecho
    cycle(t, 0.35, 16, S * 3 + 1, (g) => g.range(0.2, 0.32), (age, life, r) => {
      const q = age / life, a = r.range(0, TAU) + q * 1.8, d = 10 + (1 - ease.inQuad(q)) * r.range(26, 44);
      const x = Math.cos(a) * d, y = CY + Math.sin(a) * d * 0.75;
      p.line(x, y, x + Math.cos(a) * 4, y + Math.sin(a) * 3, q > 0.6 ? WHITE : C[3], 0.5 + 0.5 * q);
    });
    // núcleo que crece en el pecho
    const r = 1 + k * 5;
    p.circle(0, CY, r + 1, C[3]);
    p.circle(0, CY, r, WHITE);
    p.glow(0, CY, 10 + k * 20, C[2], 0.4 + 0.5 * k);
    // el suelo tiembla: polvo a los pies
    for (let i = 0; i < 6; i++) {
      const sx = ((i * 37 + S) % 30) - 15 + Math.sin(t * 60 + i) * 1.5;
      p.dot(sx, -((i * 5 + Math.floor(t * 30)) % 3), C[1], 0.5);
    }
    return;
  }
  const u = t - CARGA, q = u / (D - CARGA), R = new Rng(S * 17 + 3);
  // destello blanco (dos fotogramas)
  if (u < 0.07) { p.circle(0, CY, 14 + u * 160, WHITE, 0.9); p.glow(0, CY, 56, WHITE, 1); }
  // columna de luz: ancha al principio, se estrecha y se apaga
  // columna estrecha y corta: el personaje tiene que verse transformado enseguida
  const cw = (7 + 9 * (1 - ease.outCubic(clamp(u / 0.3)))) * (1 - ease.inQuad(clamp(u / 0.38)));
  if (cw > 0.8) {
    for (let x = -cw; x <= cw; x += 0.5) {
      const qx = Math.abs(x) / cw, lv = qx < 0.35 ? 4 : qx < 0.6 ? 3 : qx < 0.85 ? 2 : 1;
      for (let y = 2; y > -112; y -= 0.5) {
        const fade = 1 - (-y / 112);
        if (bayer(x, y) > fade * 1.2 - qx * 0.25) continue;
        p.dot(x, y, C[lv], 0.7);
      }
    }
    p.glow(0, -50, cw * 3, C[3], 0.6);
  }
  // onda de choque en el suelo (elipse en perspectiva) y una segunda más tarde
  for (let k = 0; k < 2; k++) {
    const qq = clamp((u - k * 0.12) / 0.55);
    if (qq <= 0 || qq >= 1) continue;
    const rx = 8 + 74 * ease.outQuart(qq), ry = rx * 0.28;
    const w = Math.max(1, 3 * (1 - qq));
    for (let i = 0; i < 260; i++) {
      const a = (i / 260) * TAU;
      for (let j = 0; j < w; j += 0.5) p.px(Math.cos(a) * (rx - j), Math.sin(a) * (ry - j * 0.3), j < 1 ? (qq < 0.25 ? WHITE : C[3 - k]) : C[2]);
    }
  }
  // rayos de luz que salen del pecho al estallar
  if (u < 0.35) {
    const k = 1 - u / 0.35;
    for (let i = 0; i < 10; i++) {
      const a = (i / 10) * TAU + 0.3, l = 20 + 40 * ease.outCubic(u / 0.35);
      p.line(Math.cos(a) * 8, CY + Math.sin(a) * 8, Math.cos(a) * l, CY + Math.sin(a) * l, i % 2 ? WHITE : C[3], k);
    }
  }
  // llamarada del aura alrededor del cuerpo, más grande que la normal, que se encoge
  const fh = (AH + 26) * (1 - ease.inCubic(clamp(u / 0.7)));
  if (fh > 2) {
    for (let x = -18; x <= 18; x += 0.5) {
      const kx = Math.abs(x) / 18, h = fh * Math.pow(1 - kx, 0.6) * (0.85 + 0.15 * Math.sin(x * 1.3 + u * 30));
      for (let y = 0; y > -h; y -= 0.5) {
        const v = -y / h, lv = kx < 0.4 && v < 0.8 ? 3 : kx < 0.7 ? 2 : 1;
        if (v > 0.85 && bayer(x, y) > (1 - v) / 0.15) continue;
        p.dot(x, y, C[lv], 0.6);
      }
    }
  }
  // piedras que saltan del suelo y caen
  for (let i = 0; i < 12; i++) {
    const a = -Math.PI / 2 + R.range(-1.2, 1.2), sp = R.range(80, 170), life = R.range(0.6, 1.0);
    if (u > life) continue;
    const [x, y] = fly(R.range(-10, 10), 0, Math.cos(a) * sp, Math.sin(a) * sp, u, 420, 0.5);
    if (y > 1) continue;
    const s = R.range(1, 2.5);
    p.rect(x - s / 2, y - s / 2, s, s, i % 3 ? PIEDRA : PIEDRA2);
  }
  // chispas que suben y se apagan
  for (let i = 0; i < 22; i++) {
    const x0 = R.range(-16, 16), sp = R.range(40, 110), life = R.range(0.5, 1.2), d0 = R.range(0, 0.4);
    const uu = u - d0;
    if (uu < 0 || uu > life) continue;
    const kk = 1 - uu / life, y = -R.range(4, AH) - sp * uu;
    p.line(x0, y, x0, y + 3, kk > 0.5 ? WHITE : C[3], kk);
  }
  // polvo que se abre en el suelo y se posa
  for (let i = 0; i < 8; i++) {
    const dir = i % 2 ? 1 : -1, x = dir * (10 + R.range(0, 30) * ease.outCubic(clamp(u / 0.8))), rad = R.range(4, 8) * (0.6 + q);
    p.disc(x, -rad * 0.5, rad, POLVO, (dd) => 0.35 * (1 - q) * (1 - dd * dd));
  }
  p.glow(0, CY, 60 * (1 - q), C[2], 0.7 * (1 - q));
}
