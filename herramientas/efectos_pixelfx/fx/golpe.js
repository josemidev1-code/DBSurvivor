// Golpe final de combo (una vez) para DBSurvivor, hecho con pixelfx (github.com/patch-gg/pixelfx, MIT).
// Impacto de anime en pequeño: líneas de choque que salen del punto del golpe, una estrella blanca con un rayo
// largo en la dirección del golpe, un anillo que se rompe y chispas. Dura 0,35 s.
// El origen (0, 0) es el punto del golpe; el golpe va hacia la derecha (flip para la izquierda).
import { fit, clamp, ease, fract, TAU, WHITE } from "pixelfx";

const D = 0.35;
const hash = (a) => fract(Math.sin(a * 127.1 + 311.7) * 43758.5453);
export const meta = {
  name: "Golpe final",
  desc: "Impacto de anime: líneas de choque radiales, estrella blanca con un rayo largo hacia delante, anillo que se rompe y chispas.",
  tags: ["impact", "hit", "melee", "punch", "anime", "dragon ball"],
  size: [96, 72],
  origin: [44, 36],
  duration: D,
  loop: false,
  fps: 30,
  bg: "ground",
  options: { palette: ["#a06008", "#ffb020", "#ffe070", "#ffffff"], seed: 1 },
};

export function draw(p, t, o) {
  const C = fit(o.palette, 4), S = o.seed | 0, q = t / D;
  // líneas de choque: entran deprisa y se van hacia fuera
  if (t < 0.22) {
    const k = t / 0.22;
    for (let i = 0; i < 14; i++) {
      const a = (i / 14) * TAU + hash(i + S) * 0.3, r0 = 8 + 18 * ease.outCubic(k), L = (10 + hash(i * 3 + S) * 12) * (1 - k * 0.6);
      p.line(Math.cos(a) * r0, Math.sin(a) * r0 * 0.8, Math.cos(a) * (r0 + L), Math.sin(a) * (r0 + L) * 0.8, i % 3 ? WHITE : C[2], 1 - k * 0.5);
    }
  }
  // estrella blanca: cruz ladeada con un rayo largo hacia delante
  if (t < 0.16) {
    const k = 1 - t / 0.16, s = 3 + 7 * ease.outBack(clamp(t / 0.05)) * k;
    p.line(-s * 0.7, 0, s * 2.6, 0, WHITE);
    p.line(0, -s, 0, s, WHITE);
    p.line(-s * 0.5, -s * 0.5, s * 0.5, s * 0.5, C[2]);
    p.line(-s * 0.5, s * 0.5, s * 0.5, -s * 0.5, C[2]);
    p.circle(0, 0, 1 + s * 0.3, WHITE);
  }
  // anillo que se abre y se rompe en arcos
  if (t < 0.28) {
    const k = t / 0.28, r = 4 + 20 * ease.outQuart(k);
    for (let i = 0; i < 6; i++) {
      const a0 = (i / 6) * TAU + 0.2, a1 = a0 + (TAU / 6) * (1 - k * 0.7);
      p.arc(0, 0, r, Math.max(1, 2 * (1 - k)), a0, a1, k < 0.3 ? WHITE : C[1], 1 - k);
    }
  }
  // chispas hacia delante y hacia los lados
  for (let i = 0; i < 9; i++) {
    const a = (hash(i * 5 + S) - 0.5) * 2.2, sp = 90 + hash(i * 7 + S) * 110, life = 0.15 + hash(i * 9) * 0.15;
    if (t > life) continue;
    const kk = 1 - t / life, x = Math.cos(a) * sp * t, y = Math.sin(a) * sp * t;
    p.line(x - Math.cos(a) * 3, y - Math.sin(a) * 3, x, y, kk > 0.5 ? WHITE : C[2], kk);
  }
  p.glow(0, 0, 26 * (1 - q), C[2], 0.8 * (1 - q));
}
