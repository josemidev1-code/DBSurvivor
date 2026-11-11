// Kienzan (bucle) para DBSurvivor, hecho con pixelfx (github.com/patch-gg/pixelfx, MIT).
// Un disco de energía fino y liso, visto un poco desde arriba (elipse): borde muy brillante que corta,
// interior más oscuro con brillos que giran deprisa, chispas en el filo y una estela corta detrás.
// El origen (0, 0) es el centro del disco; avanza hacia la derecha (el juego lo gira con su dirección).
import { fit, fract, TAU, WHITE } from "pixelfx";

const D = 0.25;
export const meta = {
  name: "Kienzan",
  desc: "Disco de energía fino que gira muy deprisa: filo blanco, brillos que giran, chispas y estela corta.",
  tags: ["ki", "disc", "kienzan", "projectile", "loop", "dragon ball"],
  size: [64, 36],
  origin: [40, 18],
  duration: D,
  loop: true,
  fps: 30,
  bg: "dark",
  options: { palette: ["#7a4a00", "#e0a010", "#ffd23f", "#fff8c0", "#ffffff"], seed: 2, radio: 11 },
};

export function draw(p, t, o) {
  const C = fit(o.palette, 5), R = o.radio, RY = R * 0.42, ph = t / D;
  // estela: dos líneas finas que se quedan atrás del filo
  for (let i = 0; i < 2; i++) {
    const y = (i ? 1 : -1) * RY * 0.7;
    p.line(-R - 14, y, -R + 2, y, (v) => (v > 0.6 ? C[3] : C[1]), (v) => v * 0.8);
  }
  // cuerpo del disco
  for (let y = -RY - 1; y <= RY + 1; y += 0.5) {
    for (let x = -R - 1; x <= R + 1; x += 0.5) {
      const q = Math.hypot(x / R, y / RY);
      if (q > 1.05) continue;
      if (q > 0.84) { p.px(x, y, y < 0 ? WHITE : q > 0.97 ? C[1] : C[4]); continue; } // filo
      // brillos que giran: franjas radiales según el ángulo
      const a = Math.atan2(y / RY, x / R), band = fract((a / TAU) * 4 - ph * 4);
      const c = band < 0.07 ? C[4] : q < 0.4 ? C[3] : q < 0.7 ? C[2] : C[3];
      p.px(x, y, c);
    }
  }
  // centro blanco
  p.circle(0, 0, Math.max(1, R * 0.15), WHITE);
  // chispas en el filo (giran con el disco)
  for (let i = 0; i < 3; i++) {
    const a = ph * TAU * 2 + (i * TAU) / 3, x = Math.cos(a) * (R + 1), y = Math.sin(a) * (RY + 1);
    p.line(x, y, x - 3, y + (Math.sin(a) > 0 ? 1 : -1), WHITE, 0.9);
  }
  p.glow(0, 0, R * 2.2, C[2], 0.5);
}
