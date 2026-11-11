// Transformación (una vez) para DBSurvivor, hecha con pixelfx (github.com/patch-gg/pixelfx, MIT).
// Como en la serie:
//   0 .. CARGA   el suelo tiembla, las piedras flotan hacia arriba, el aura chisporrotea y crece a tirones,
//                relámpagos cortos alrededor del cuerpo
//   CARGA        estallido: destello blanco, llamarada enorme del aura hacia arriba, anillos de choque en el suelo,
//                relámpagos y las piedras salen despedidas
//   después      la llamarada se encoge hasta desaparecer: al final no queda nada alrededor del personaje
// El origen (0, 0) son los pies. CARGA coincide con la congelación del juego (S.freeze = 0.6 s).
import { fit, clamp, fract, ease, hex, loopNoise, Rng, TAU, WHITE } from "pixelfx";

const PIEDRA = hex("#8a7a62"), PIEDRA2 = hex("#5a4a3a"), POLVO = hex("#d8c8a8"), RAYO = hex("#bfe6ff");
const hash = (a) => fract(Math.sin(a * 127.1 + 311.7) * 43758.5453);
export const CARGA = 0.6;
const D = 1.6;

export const meta = {
  name: "Transformación",
  desc: "Transformación de Dragon Ball: tiembla el suelo y flotan las piedras, el aura estalla en una llamarada con relámpagos y anillos de choque, y se apaga del todo.",
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

// llamarada de aura con forma de llama (óvalo con puntas que suben), borde de tres tonos y el interior vacío
function llamarada(p, C, s, ph, S, AH, alpha) {
  if (s < 0.05) return;
  const RX = 17 * s, RY = AH * 0.62 * s, CY = -RY * 0.75;
  for (let x = -RX; x <= RX; x += 0.5) {
    const k = x / RX;
    if (Math.abs(k) >= 1) continue;
    const n = loopNoise(ph, 2, S * 13 + Math.round(x / (2.5 * Math.max(0.6, s)))) * 0.5 + 0.5;
    const tongue = (1 - Math.abs(k)) * (6 + n * 22) * s * (0.6 + 0.4 * Math.sin(x * 0.7 + ph * TAU * 3));
    const yTop = CY - RY * Math.sqrt(1 - k * k) - tongue, yBot = Math.min(1.5, CY + RY * Math.sqrt(1 - k * k));
    for (let y = yTop; y <= yBot; y += 0.5) {
      const v = (y - CY) / RY, hw = v * v >= 1 ? 0 : RX * Math.sqrt(1 - v * v);
      const d = Math.min(y - yTop, y < CY - RY * 0.2 ? 99 : hw - Math.abs(x), yBot - y + 2.5);
      if (d < 1) p.dot(x, y, C[1], alpha);
      else if (d < 2) p.dot(x, y, C[2], alpha);
      else if (d < 3.2) p.dot(x, y, C[3], alpha * 0.85);
      else if (d < 5) p.dot(x, y, C[4], alpha * 0.25);
    }
  }
  p.glow(0, CY, RY * 1.4, C[2], 0.5 * alpha);
}

// relámpago en zigzag de (x0, y0) hacia un lado
function relampago(p, x0, y0, dir, len, k) {
  let x = x0, y = y0;
  for (let j = 0; j < len; j++) {
    const nx = x + dir * (2 + hash(k + j * 3) * 3), ny = y + (hash(k * 7 + j) - 0.5) * 7;
    p.line(x, y, nx, ny, j % 2 ? RAYO : WHITE);
    x = nx; y = ny;
  }
}

export function draw(p, t, o) {
  const C = fit(o.palette, 5), S = o.seed | 0, AH = o.alto, CY = -AH * 0.5, R = new Rng(S * 17 + 3);
  // piedras: flotan durante la carga y salen despedidas en el estallido
  for (let i = 0; i < 14; i++) {
    const x0 = (hash(S + i) - 0.5) * 70, s = 1 + hash(S + i * 3) * 2, up = 4 + hash(S + i * 5) * 18, d0 = hash(S + i * 7) * 0.25;
    let x, y;
    if (t < CARGA) {
      const q = clamp((t - d0) / (CARGA - d0));
      if (q <= 0) continue;
      x = x0 + Math.sin(t * 40 + i) * 0.6; y = -ease.outCubic(q) * up;
    } else {
      const u = t - CARGA, vx = Math.sign(x0 || 1) * (60 + hash(i * 11) * 90), vy = -60 - hash(i * 13) * 80;
      x = x0 + vx * u; y = -up + vy * u + 260 * u * u;
      if (y > 1) continue;
    }
    p.rect(x - s / 2, y - s / 2, s, s, i % 3 ? PIEDRA : PIEDRA2);
  }

  if (t < CARGA) {
    const k = t / CARGA, f = Math.floor(t * 15);
    // el aura chisporrotea y crece a tirones (parpadea, como cuando está a punto de estallar)
    if (hash(f + S) < 0.35 + 0.6 * k) llamarada(p, C, 0.55 + 0.35 * k + hash(f) * 0.1, t / 0.8, S, AH, 0.6 + 0.4 * k);
    // relámpagos cortos alrededor del cuerpo
    if (hash(f * 3 + S) < 0.3 + 0.5 * k) relampago(p, (hash(f * 5) - 0.5) * 16, CY + (hash(f * 9) - 0.5) * AH * 0.7, hash(f * 2) < 0.5 ? -1 : 1, 4, f);
    // polvo que tiembla en el suelo
    for (let i = 0; i < 8; i++) p.dot((hash(i * 3 + f) - 0.5) * 40, -hash(i + f) * 2, POLVO, 0.6);
    p.glow(0, CY, 20 + k * 20, C[2], 0.3 + 0.4 * k);
    return;
  }

  const u = t - CARGA, q = u / (D - CARGA);
  // destello blanco (dos fotogramas)
  if (u < 0.07) { p.circle(0, CY, 14 + u * 160, WHITE, 0.85); p.glow(0, CY, 56, WHITE, 1); }
  // llamarada enorme que sale disparada y se encoge hasta desaparecer
  const s = u < 0.08 ? 1 + ease.outQuad(u / 0.08) * 0.9 : 1.9 * (1 - ease.inQuad(clamp((u - 0.08) / 0.75)));
  llamarada(p, C, s, u / 0.5, S + 1, AH, 1 - 0.4 * clamp((u - 0.4) / 0.4));
  // anillos de choque en el suelo
  for (let k = 0; k < 2; k++) {
    const qq = clamp((u - k * 0.1) / 0.5);
    if (qq <= 0 || qq >= 1) continue;
    const rx = 8 + 78 * ease.outQuart(qq), ry = rx * 0.26, w = Math.max(1, 3 * (1 - qq));
    for (let i = 0; i < 260; i++) {
      const a = (i / 260) * TAU;
      for (let j = 0; j < w; j += 0.5) p.px(Math.cos(a) * (rx - j), Math.sin(a) * (ry - j * 0.3), j < 1 ? (qq < 0.25 ? WHITE : C[3 - k]) : C[2]);
    }
  }
  // relámpagos durante el estallido
  if (u < 0.45) {
    const f = Math.floor(u * 15);
    for (let i = 0; i < 2; i++) if (hash(f * 3 + i + S) < 0.7) relampago(p, (i ? 1 : -1) * (6 + hash(f + i) * 8), CY + (hash(f * 9 + i) - 0.5) * AH, i ? 1 : -1, 5, f * 2 + i);
  }
  // chispas que suben y se apagan
  for (let i = 0; i < 18; i++) {
    const x0 = R.range(-18, 18), sp = R.range(50, 120), life = R.range(0.4, 0.8), d0 = R.range(0, 0.2);
    const uu = u - d0;
    if (uu < 0 || uu > life) continue;
    const kk = 1 - uu / life, y = -R.range(4, AH) - sp * uu;
    p.line(x0, y, x0, y + 3, kk > 0.5 ? WHITE : C[3], kk);
  }
  // polvo que se abre en el suelo y se posa
  for (let i = 0; i < 8; i++) {
    const dir = i % 2 ? 1 : -1, x = dir * (10 + R.range(0, 34) * ease.outCubic(clamp(u / 0.6))), rad = R.range(4, 8) * (0.6 + q);
    p.disc(x, -rad * 0.5, rad, POLVO, (dd) => 0.35 * (1 - q) * (1 - dd * dd));
  }
  p.glow(0, CY, 60 * (1 - q), C[2], 0.6 * (1 - q));
}
