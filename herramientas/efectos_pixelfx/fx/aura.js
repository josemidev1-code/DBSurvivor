// Aura de ki (bucle) para DBSurvivor, hecha con pixelfx (github.com/patch-gg/pixelfx, MIT).
// Lenguas de energía que suben pegadas al cuerpo y se afilan arriba, un borde tramado, chispas que suben y luz.
// El origen (0, 0) son los pies. Va DETRÁS del personaje. palette: oscuro → claro (lo pone el juego por forma).
import { fit, fract, cycle, loopNoise, hex, TAU, WHITE } from "pixelfx";

const RAYO = hex("#bfe6ff");

const D = 0.8;

export const meta = {
  name: "Aura de ki",
  desc: "Aura de Dragon Ball: lenguas de energía que suben pegadas al cuerpo, borde tramado, chispas y luz.",
  tags: ["ki", "aura", "power", "loop", "dragon ball"],
  size: [64, 84],
  origin: [32, 76],
  duration: D,
  loop: true,
  fps: 30,
  bg: "ground",
  actor: 2,
  // ancho: medio ancho del cuerpo; alto: altura del cuerpo; rayos: chispas eléctricas (SSJ2)
  options: { palette: ["#a06008", "#e8a010", "#ffd23f", "#fff6a8", "#ffffff"], seed: 3, ancho: 11, alto: 40, rayos: 0 },
};

export function drawBack(p, t, o) {
  const C = fit(o.palette, 5), ph = t / D, S = o.seed | 0, AW = o.ancho, AH = o.alto;
  // óvalo pegado al cuerpo (un poco por debajo de los pies) con puntas de llama arriba
  const RX = AW + 6, RY = AH * 0.62, CY = -AH * 0.46;
  const halfW = (y) => { const v = (y - CY) / RY; return v * v >= 1 ? 0 : RX * Math.sqrt(1 - v * v); };
  const tongue = (x) => {
    const k = Math.abs(x) / RX;
    if (k >= 1) return 0;
    const n = loopNoise(ph, 2, S * 13 + Math.round(x / 2.5)) * 0.5 + 0.5;
    // puntas más altas en el centro y que suben y bajan sin costura
    return (1 - k) * (4 + n * 14) * (0.6 + 0.4 * Math.sin(x * 0.9 + ph * TAU * 2));
  };
  for (let x = -RX; x <= RX; x += 0.5) {
    const k = x / RX;
    if (Math.abs(k) >= 1) continue;
    const yTop = CY - RY * Math.sqrt(1 - k * k) - tongue(x), yBot = Math.min(1.5, CY + RY * Math.sqrt(1 - k * k));
    for (let y = yTop; y <= yBot; y += 0.5) {
      const dTop = y - yTop, dSide = y < CY - RY * 0.2 ? 99 : halfW(y) - Math.abs(x);
      const d = Math.min(dTop, dSide, (yBot - y) + 2.5);
      if (d < 1) p.px(x, y, C[1]);
      else if (d < 2) p.px(x, y, C[2]);
      else if (d < 3.2) p.dot(x, y, C[3], 0.85);
    }
  }
  p.glow(0, CY, AH * 0.8, C[2], 0.4);
  p.glow(0, -1, AW * 2, C[3], 0.25);
}

export function draw(p, t, o) {
  const C = fit(o.palette, 5), ph = t / D, S = o.seed | 0, AW = o.ancho, AH = o.alto;
  // chispas y briznas que suben por delante
  cycle(t, D, 9, S * 7 + 1, (g) => g.range(0.3, 0.6), (age, life, r) => {
    const q = age / life, x = r.range(-AW - 4, AW + 4), y = -r.range(0, AH * 0.5) - q * r.range(18, 32);
    const L = 2 + (1 - q) * 3;
    p.line(x, y, x, y + L, q < 0.4 ? WHITE : C[3], 1 - q);
  });
  // rayos eléctricos (SSJ2): zigzag corto que salta cerca del cuerpo
  if (o.rayos) {
    const k = Math.floor(ph * 8);
    for (let i = 0; i < 2; i++) {
      const sd = (S * 31 + k * 7 + i * 13) % 97;
      if (sd % 3 === 0) continue;
      let x = ((sd % 23) / 23 - 0.5) * AW * 2.2, y = -((sd % 17) / 17) * AH * 0.8 - 6;
      for (let j = 0; j < 5; j++) {
        const nx = x + (((sd + j * 5) % 5) - 2), ny = y + 3;
        p.line(x, y, nx, ny, j % 2 ? RAYO : WHITE);
        x = nx; y = ny;
      }
    }
  }
}
