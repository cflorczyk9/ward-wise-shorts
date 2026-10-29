# Prompt for the next episode

Paste everything below the line into Claude Code, opened in this `ward-wise-shorts` folder. Change the first line to the topic you want, or leave it to let Claude pick the next one from the list.

---

Make the next Ward Wise Shorts episode. Topic: **[pick the highest-ranked unmade topic in data/topics.md, or write one here, e.g. "Chicago's cheapest wards to rent"]**.

Read `README.md` first. It explains the folder, the episode file fields and the design rules. Episode 1 is in `episodes/walking-safety.json` (it has a `voiceover` block). Match its look and timing exactly, and do not change `renderer/video.html` unless something breaks.

Work in this order.

1. Find the measure in `data/catalog.csv` and check `data/broken_metrics.json`. Skip any measure with fewer than 45 wards or mostly zeros. Use the last full year, because 2026 is partial for crashes, permits and every 311 measure.
2. Pull the real values with `python3 renderer/build_episode.py` on a draft episode file that leaves out `best` and `worst`. Read the top 5 and bottom 3 it prints. Tell me the numbers and one fairness caveat before you write any copy.
3. Write the episode file in `episodes/<slug>.json`. Keep the copy short.
   - The hook is 2 lines, with the key words in blue.
   - The subline is one line of 50 characters or fewer, and it names the year.
   - Neighborhood labels stay under 26 characters. Use the names people know.
   - The worst-3 screen gets one line that explains the result fairly, for example why downtown leads.
   - Write no em dashes, no colons in sentences, and no "not X, it's Y" lines.
4. Write the voiceover. Add a `voiceover` block to the episode file: `{"voice": "af_heart", "speed": 1.0, "script": "...", "cues": {"rank5": "...", ..., "worst": "...", "end": "..."}}`.
   - The script is one paragraph of 15 to 20 seconds, in plain spoken English, with the same facts as the screen. It names the 5 best wards in countdown order, then the worst area, then ends with a question and the link in the bio.
   - Each cue is the first word of the phrase where that reveal should land. Cues must appear in the script in speaking order, and `rank3`, `rank2` are needed too.
   - Set `cta` and `cta2` to match the last lines of the script.
   - STOP and show me the script and cues. Wait for my OK before rendering.
5. Run `renderer/make_video.sh episodes/<slug>.json`. Open `output/<slug>/check_sheet.png` and look for text that wraps, overlaps or runs past the card. Fix the episode file and run it again until the sheet is clean.
6. Check every number on screen against `https://www.wardwise.org/api/metrics/delta?metric_id=<id>&from_year=<year>&to_year=<year>` and list each check.
7. Write a post caption of 2 to 4 sentences. Use plain words people search for (Chicago, ward, the topic) and at most 2 hashtags. End it with "Check the link in our bio."

Done when:
- `output/<slug>/<slug>.mp4` exists and `ffprobe` shows 1080x1920, about 22 s, with an audio track, and the voice reads the script in one take.
- Each reveal lands on its cue word (compare the cue times the build prints in `voice_cues.json` with the on-screen reveal).
- The check sheet shows no wrapped subline, no overlap and no clipped number.
- Every on-screen number matches the API call, and you list the call next to it.
- The caption has no em dash and no more than 2 hashtags.

If you need the setup, run `cd renderer && npm install && npx playwright install chromium`, and install ffmpeg if it is missing.
