// Render the episode to PNG frames with headless Chromium.
// Usage: node render.mjs <video_data.json> <frames_dir> [fps] [comma-separated seconds for stills only]
import { chromium } from 'playwright';
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const [,, dataPath, outDir, fpsArg, onlyArg] = process.argv;
const fps = +fpsArg || 30;
const here = path.dirname(fileURLToPath(import.meta.url));
const html = fs.readFileSync(path.join(here, 'video.html'), 'utf8').replace('__DATA__', fs.readFileSync(dataPath, 'utf8'));
// CHROME_PATH lets you point at any Chromium build; otherwise Playwright uses its own download.
const browser = await chromium.launch(process.env.CHROME_PATH ? { executablePath: process.env.CHROME_PATH } : {});
const page = await browser.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: 1 });
page.on('pageerror', e => console.error('PAGE ERROR', e.message));
await page.setContent(html, { waitUntil: 'load' });
const dur = await page.evaluate(() => window.DUR);
fs.mkdirSync(outDir, { recursive: true });
const times = onlyArg ? onlyArg.split(',').map(Number) : Array.from({ length: Math.round(dur * fps) }, (_, i) => i / fps);
let i = 0;
for (const t of times) {
  await page.evaluate(t => window.renderAt(t), t);
  const name = onlyArg ? `still_${t.toFixed(2)}.png` : `f${String(i).padStart(4, '0')}.png`;
  await page.screenshot({ path: path.join(outDir, name), type: 'png' });
  i++;
}
await browser.close();
console.log(`Rendered ${times.length} frame(s) to ${outDir}`);
