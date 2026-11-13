// Clima de los escenarios (bucle) para DBSurvivor, hecho con pixelfx (github.com/patch-gg/pixelfx, MIT).
// Capa transparente para vista cenital que se repite sin costuras en horizontal y vertical (el juego la pone en
// mosaico sobre la pantalla). tipo: "lluvia", "hojas", "ceniza", "niebla" o "destellos".
// Para que el bucle no tenga salto, cada partícula recorre un número entero de lienzos en D segundos.
import { fit, fract, hex, Rng, TAU, WHITE } from "pixelfx";

const D = 6, W = 320, H = 180;
export const meta = {
  name: "Clima",
  desc: "Capa de clima para vista cenital que se repite: lluvia con salpicaduras, hojas, ceniza y brasas, niebla o destellos.",
  tags: ["weather", "rain", "leaves", "ash", "fog", "loop", "overlay"],
  size: [W, H],
  origin: [0, 0],
  duration: D,
  loop: true,
  fps: 30,
  bg: "ground",
  options: { tipo: "lluvia", palette: ["#3a5a8a", "#7aa8d8", "#c8e4ff"], seed: 9, densidad: 1 },
};

const wrap = (v, m) => ((v % m) + m) % m;

export function draw(p, t, o) {
  const C = fit(o.palette, 3), R = new Rng(o.seed | 0), k = o.densidad, ph = t / D, tipo = o.tipo;
  if (tipo === "lluvia") {
    // gotas inclinadas: bajan 3-5 lienzos y se desplazan 1 lienzo a la izquierda por vuelta
    const n = Math.round(130 * k);
    for (let i = 0; i < n; i++) {
      const x0 = R.range(0, W), y0 = R.range(0, H), cy = R.int(3, 6), far = R.chance(0.4);
      const x = wrap(x0 - ph * W, W), y = wrap(y0 + ph * H * cy, H), L = far ? 4 : 7;
      p.line(x, y, x - L * 0.35, y - L, far ? C[0] : C[1], far ? 0.45 : 0.75);
    }
    // salpicaduras: anillos pequeños que se abren en el suelo
    for (let i = 0; i < Math.round(26 * k); i++) {
      const x = R.range(0, W), y = R.range(0, H), off = R.range(0, 1), q = fract(ph * 6 + off);
      if (q > 0.35) continue;
      const r = 1 + q * 8;
      p.ellipse(x, y, r, r * 0.45, C[2], (1 - q / 0.35) * 0.6);
    }
    return;
  }
  if (tipo === "hojas") {
    const n = Math.round(40 * k);
    for (let i = 0; i < n; i++) {
      const x0 = R.range(0, W), y0 = R.range(0, H), cx = R.int(1, 3), cy = R.int(1, 2), sw = R.range(4, 9), sp = R.int(2, 5);
      const x = wrap(x0 + ph * W * cx + Math.sin(ph * TAU * sp + i) * sw, W), y = wrap(y0 + ph * H * cy, H);
      const a = ph * TAU * sp * 2 + i, c = C[i % 3], fl = Math.abs(Math.cos(a));
      // hoja de 4x3: se estrecha al ponerse de canto y enseña el envés más claro
      const lx = Math.cos(a) * 2.5, ly = Math.sin(a) * 2.5;
      p.line(x - lx, y - ly, x + lx, y + ly, fl > 0.4 ? c : C[2]);
      if (fl > 0.35) { const nx = -ly * 0.4 * fl, ny = lx * 0.4 * fl; p.line(x - lx * 0.6 + nx, y - ly * 0.6 + ny, x + lx * 0.6 + nx, y + ly * 0.6 + ny, c); }
      p.dot(x + lx, y + ly, C[0]);
    }
    return;
  }
  if (tipo === "ceniza") {
    const n = Math.round(70 * k);
    for (let i = 0; i < n; i++) {
      const x0 = R.range(0, W), y0 = R.range(0, H), cy = R.int(1, 2), sw = R.range(2, 6), fq = R.int(1, 4), ember = R.chance(0.3);
      const x = wrap(x0 + Math.sin(ph * TAU * fq + i) * sw, W), y = wrap(y0 - ph * H * cy, H);
      if (ember) {
        const fl = 0.6 + 0.4 * Math.sin(ph * TAU * R.int(4, 9) + i);
        p.dot(x, y, fl > 0.8 ? C[2] : C[1], fl);
        p.light(x, y, C[1], 0.5 * fl);
      } else p.dot(x, y, C[0], 0.55);
    }
    return;
  }
  if (tipo === "niebla") {
    // bancos grandes y translúcidos que cruzan despacio (1 lienzo por vuelta)
    for (let i = 0; i < Math.round(9 * k); i++) {
      const x0 = R.range(0, W), y = R.range(0, H), r = R.range(26, 52), dir = i % 2 ? 1 : 2;
      const x = wrap(x0 + ph * W * dir, W);
      for (const dx of [-W, 0, W]) for (const dy of [-H, 0, H]) {
        const cx = x + dx, cyy = y + dy;
        if (cx < -r || cx > W + r || cyy < -r || cyy > H + r) continue;
        p.disc(cx, cyy, r, C[1], (d) => 0.24 * (1 - d * d));
      }
    }
    return;
  }
  // destellos: lucecitas que se encienden y se apagan donde están, con un brillo en cruz al máximo
  for (let i = 0; i < Math.round(48 * k); i++) {
    const x = R.range(0, W), off = R.range(0, 1), sp = R.int(1, 3), y = wrap(R.range(0, H) - ph * H, H);
    const v = Math.sin((ph * sp + off) * TAU) * 0.5 + 0.5;
    if (v < 0.3) continue;
    const a = (v - 0.3) / 0.7;
    p.dot(x, y, a > 0.7 ? WHITE : C[1], a);
    if (a > 0.5) { p.dot(x - 1, y, C[2], a * 0.6); p.dot(x + 1, y, C[2], a * 0.6); p.dot(x, y - 1, C[2], a * 0.6); p.dot(x, y + 1, C[2], a * 0.6); }
    p.light(x, y, C[1], 0.4 * a);
  }
}
