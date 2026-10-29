# Ward Wise Shorts

A short video series for Instagram Reels and TikTok. Each video ranks Chicago's 50 wards on one Ward Wise measure, using the blue ward map from wardwise.org. Episode 1 ranks walking safety. Each video can also carry a smooth AI voiceover, and the map follows the voice.

To make a new episode, open `PROMPT.md` and paste it into Claude Code.

## What's in the folder

```
ward-wise-shorts/
├── PROMPT.md               Paste into Claude Code to make the next episode
├── README.md               This file
├── music/                  Song license and a download script (the song file is not stored here)
├── voiceover/              The program that reads the script aloud
├── output/                 Made videos land here (not saved in git)
├── episodes/               One JSON file per episode (on-screen text + metric + year)
├── renderer/               The code that turns an episode file into an MP4
├── data/                   All 271 measures, the next 20 episode ideas, flagged measures
├── research/               Platform, motion, Chicago and design research from the swarm
```

## Make a video

You need Python 3, Node 18 or newer, ffmpeg (`brew install ffmpeg`) and uv (`brew install uv`, runs the voice program).

1. Install the renderer once.
   ```
   cd renderer
   npm install
   npx playwright install chromium
   ```
2. Copy `episodes/walking-safety.json` to a new file, for example `episodes/cheapest-rent.json`.
3. Change `metric_id`, `year` and the on-screen text. Delete `best` and `worst` to have the script fill in the real top 5 and bottom 3.
4. Run the build.
   ```
   ./make_video.sh ../episodes/cheapest-rent.json   # or, from the main folder, renderer/make_video.sh episodes/cheapest-rent.json
   ```
5. Write the `voiceover` (next section).
6. Open `output/cheapest-rent/check_sheet.png` to check 8 frames at once, then watch the MP4.

The build prints the top 5 and bottom 3 with their values. Check them before you post.

## The voiceover

DRAFT: the script for episode 1 is a draft. Connor is still choosing the final words.

The episode file has a `voiceover` block: the voice, the speed, the whole script as one paragraph, and `cues`. Each cue names a moment on screen (`rank5` down to `rank1`, `worst`, `end`) and gives the first word of the phrase where that moment should land.

The voice program reads the whole script in one take, so the sentences flow together. It reports when each word is spoken. The video then lands each reveal on its cue word, and the video ends about 2 seconds after the voice stops. The song plays underneath and dips while the voice talks. Leave out `voiceover` and the video falls back to the old beat-locked version, 23 seconds, no voice.

Tips: keep the script to about 15 to 20 seconds. Say the ward names in the order of the countdown. If names come less than a second apart, the screen switches fast to keep up.

The voice is Kokoro (Apache-2.0, free, runs on this Mac, nothing is sent online). The first run downloads the voice model. `af_heart` is the warm female voice.

## The music

The song is not stored in this folder, because its license does not allow sharing the file alone. `make_video.sh` downloads it from Mixkit when it is missing (`music/get_music.sh`). If the download fails, the script prints the steps to save it by hand.

## Episode file fields

| Field | What it does |
|---|---|
| `metric_id`, `year` | The measure and year to pull from wardwise.org/api. The IDs are in `data/catalog.csv`. |
| `direction` | `lower` or `higher` is better. Leave it out to use the site's setting. |
| `unit`, `prefix`, `suffix`, `decimals` | How numbers show, for example `$` + `1,073` + `median rent`. |
| `title_html`, `sub` | The hook on the first frame. Wrap the blue words in `<span class="b">`. |
| `legend_dark`, `legend_light` | The labels on the ends of the color key. Dark blue is always the better end. |
| `best_title_html`, `worst_title_html`, `worst_sub`, `worst_header` | Text for the countdown and for the worst-3 screen. |
| `median_text`, `source`, `cta`, `cta2` | The typical-ward chip (leave it out to use the true median), the source line on the end card, and the end card text. |
| `voiceover` | `voice`, `speed`, `script` (one paragraph) and `cues` (first word of the phrase for each reveal). Optional. |
| `music` | `file`, `start` (seconds, on a downbeat) and `bpm`. The reveals follow the beat. |
| `best`, `worst` | The wards, #1 first. Each has `id`, `hood` (neighborhood label) and an optional `zoom` (1.6 to 2.0). |

## Rules the design follows

- Video is 1080 × 1920 at 30 fps. With a voiceover the reveals follow the voice and the video runs about 22 seconds. Without one it is 23 seconds, locked to the song: one reveal per bar (2.5 seconds at 96 BPM), each on a downbeat.
- Motion uses one family of easing with no bounce. The camera flies between wards on a smooth zoom path and drifts during holds. One card rolls through the countdown, and its number moves from the last ward's value.
- Keep everything in the box from x 120 to 890 and y 290 to 1440. The app captions and buttons cover the rest.
- Use one blue ramp, where darker means better. The worst wards turn black. There is no red.
- Keep neighborhood labels under about 26 characters, or they end in "…".
- Use full-year data. 2026 is partial for crashes, permits and every 311 measure.
- Rank counts fairly. Wards hold about the same number of residents, but downtown draws far more visitors, so say so on screen when it matters.

## Facts for Episode 1

- Measure: `pedestrian_cyclist_crashes_count`, from Chicago Police crash reports, 2025.
- Fewest crashes: Ward 10 (29), Ward 18 (31), Ward 41 (44), Ward 38 (51), Ward 12 (52).
- Most crashes: Ward 27 (319), Ward 42 (312), Ward 28 (233). The typical ward (median) had 94.5. The 50 wards total 5,324.
- Ward 34 really does cover the Near West Side and Loop. The 2023 ward map moved it there.

## Limits

- The research comes mostly from marketing blogs and ad guides. No one timed real TikTok or Instagram videos, because those pages need a login.
- The song is "Just Keep Walking" from Mixkit (see `music/LICENSE.md`). To change it, set `music.file`, `music.start` (a downbeat, in seconds) and `music.bpm` in the episode file. I picked the track by tempo and energy and never listened to it, so listen before posting.
- The safe zone was not checked inside the real TikTok or Instagram upload preview.
