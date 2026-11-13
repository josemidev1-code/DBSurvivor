// Taiyoken (una vez) para DBSurvivor, hecho con pixelfx (github.com/patch-gg/pixelfx, MIT).
// Destello que ciega: un punto en la cara que estalla en una estrella de rayos largos y un anillo blanco,
// y se apaga deprisa. El origen (0, 0) es la cara del personaje.
import { fit, clamp, ease, TAU, WHITE } from "pixelfx";

const D = 0.7;
export const meta = {
  name: "Taiyoken",
  desc: "Destello cegador desde la cara: estrella de rayos largos, anillo blanco y luz que se apaga deprisa.",
  tags: ["ki", "flash", "light", "taiyoken", "burst", "dragon ball"],
  size: [220, 220],
  origin: [110, 110],
  duration: D,
  loop: false,
  fps: 30,
  bg: "ground",
  options: { palette: ["#a08020", "#f0d040", "#fff8c0", "#ffffff"], seed: 4, radio: 90 },
};

export function draw(p, t, o) {
  const C = fit(o.palette, 4), RM = o.radio, q = t / D;
  const grow = ease.outExpo(clamp(t / 0.12)), fade = 1 - ease.inQuad(clamp((t - 0.1) / (D - 0.1)));
  if (fade <= 0) return;
  // estrella: 12 rayos, los largos y los cortos alternados, que se estiran y se adelgazan
  for (let i = 0; i < 12; i++) {
    const a = (i / 12) * TAU + 0.13 + q * 0.3, L = RM * grow * (i % 2 ? 0.55 : 1) * (0.9 + 0.1 * Math.sin(i * 3.1));
    p.line(0, 0, Math.cos(a) * L, Math.sin(a) * L, (v) => (v < 0.35 ? WHITE : v < 0.7 ? C[2] : C[1]), (v) => fade * (1 - v * 0.8));
    if (i % 2 === 0) p.line(Math.cos(a + 0.03) * 2, Math.sin(a + 0.03) * 2, Math.cos(a) * L * 0.7, Math.sin(a) * L * 0.7, WHITE, fade * 0.7);
  }
  // núcleo blanco y anillo que se abre
  p.circle(0, 0, 6 + 10 * grow * fade, WHITE, fade);
  const rr = RM * 0.9 * ease.outQuart(clamp(t / 0.45));
  if (t < 0.45) p.ring(0, 0, rr, Math.max(1, 3 * (1 - t / 0.45)), t < 0.12 ? WHITE : C[2], 1 - t / 0.45);
  p.glow(0, 0, RM * 1.2 * grow, WHITE, 0.9 * fade);
  p.glow(0, 0, RM * 0.5, C[2], 0.6 * fade);
}
