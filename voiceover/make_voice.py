"""Read the episode's whole script in ONE Kokoro take and find when each cue word is spoken.
Writes <out_dir>/voice.wav and <out_dir>/voice_cues.json (seconds on the video clock).
Usage: uv run --python 3.12 --with kokoro --with soundfile --with "misaki[en]" python make_voice.py <episode.json> <out_dir>"""
import json, os, re, sys
import numpy as np, soundfile as sf
from kokoro import KPipeline

SR = 24000
LEAD = 0.5   # seconds of picture before the voice starts
spec, out_dir = sys.argv[1], sys.argv[2]
vo = json.load(open(spec))["voiceover"]
os.makedirs(out_dir, exist_ok=True)

pipe = KPipeline(lang_code="a", repo_id="hexgrad/Kokoro-82M")
audio, words, offset = [], [], 0.0
for r in pipe(vo["script"], voice=vo.get("voice", "af_heart"), speed=vo.get("speed", 1.0), split_pattern=None):
    for t in r.tokens:  # tokens carry start_ts/end_ts relative to this chunk
        if t.start_ts is not None and re.search(r"\w", t.text):
            words.append((re.sub(r"[^\w']", "", t.text).lower(), offset + t.start_ts))
    a = r.audio.numpy() if hasattr(r.audio, "numpy") else np.asarray(r.audio)
    audio.append(a); offset += len(a) / SR
audio = np.concatenate(audio)
loud = np.where(np.abs(audio) > 0.01)[0]
audio = audio[: loud[-1] + 2400]  # trim the silence Kokoro leaves at the end

cues, pos = {}, 0
for name, word in vo["cues"].items():  # cues are in speaking order; each search starts after the last hit
    want = re.sub(r"[^\w']", "", word).lower()
    i = next((k for k in range(pos, len(words)) if words[k][0] == want), None)
    if i is None:
        sys.exit(f"Cue '{name}': word '{word}' not found in the script after the previous cue.")
    cues[name] = words[i][1]; pos = i + 1

# Stretch the pause before any cue that comes less than min_gap after the one before it, so each reveal stays up long enough to read.
# The silence goes in just before the cue word, inside the pause the voice already takes there, so the take itself is untouched.
MIN_GAP = vo.get("min_gap", 1.5)
names, shift, pieces, cut = list(cues), 0.0, [], 0
for a, b in zip(names, names[1:]):
    cues[a] += shift
    need = MIN_GAP - (cues[b] + shift - cues[a])
    if need > 0:
        at = int((cues[b] - 0.05) * SR)
        pieces += [audio[cut:at], np.zeros(int(need * SR), dtype=np.float32)]; cut = at; shift += need
cues[names[-1]] += shift
audio = np.concatenate(pieces + [audio[cut:]])
cues = {k: round(LEAD + v, 3) for k, v in cues.items()}
sf.write(f"{out_dir}/voice.wav", np.concatenate([np.zeros(int(LEAD * SR), dtype=np.float32), audio]), SR)
json.dump({"cues": cues, "voice_end": round(LEAD + len(audio) / SR, 3)}, open(f"{out_dir}/voice_cues.json", "w"), indent=1)
print("cues:", cues, "voice_end:", round(LEAD + len(audio) / SR, 2))
