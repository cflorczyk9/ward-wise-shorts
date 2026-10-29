#!/bin/bash
# One command per episode:  renderer/make_video.sh episodes/walking-safety.json
# With a "voiceover" in the episode file it also voices the script and times the reveals to the voice.
# Output: ../output/<slug>/<slug>.mp4, cover.png and a contact sheet of 8 stills for checking.
set -euo pipefail
SPEC="$(cd "$(dirname "$1")" && pwd)/$(basename "$1")"   # absolute, so it works from any folder
cd "$(dirname "$0")"
SLUG="$(basename "$SPEC" .json)"
OUT="../output/$SLUG"
FPS=30
../music/get_music.sh
mkdir -p "$OUT"; rm -f "$OUT/voice.wav" "$OUT/voice_cues.json"
HAS_VOICE=$(python3 -c "import json,sys; print('yes' if 'voiceover' in json.load(open(sys.argv[1])) else 'no')" "$SPEC")
if [ "$HAS_VOICE" = yes ]; then   # one Kokoro take of the whole script; writes voice.wav and the cue times
  uv run --python 3.12 --with kokoro --with soundfile --with "misaki[en]" python ../voiceover/make_voice.py "$SPEC" "$OUT"
fi
python3 build_episode.py "$SPEC"
rm -rf "$OUT/frames"
node render.mjs "$OUT/video_data.json" "$OUT/frames" $FPS
N=$(ls "$OUT/frames" | wc -l | tr -d ' ')
DUR=$(python3 -c "print($N / $FPS)")
VOICE=""; [ "$HAS_VOICE" = yes ] && VOICE="$OUT/voice.wav"
python3 make_audio.py "$OUT/audio.wav" "$SPEC" "$DUR" $VOICE
ffmpeg -y -loglevel error -framerate $FPS -i "$OUT/frames/f%04d.png" -i "$OUT/audio.wav" \
  -c:v libx264 -pix_fmt yuv420p -crf 18 -preset slow -profile:v high -c:a aac -b:a 192k -movflags +faststart -shortest "$OUT/$SLUG.mp4"
# Stills for checking: shares of the running time. With a voice they sit just after each spoken cue.
if [ "$HAS_VOICE" = yes ]; then
  FR=($(python3 -c "
import json; c=json.load(open('$OUT/voice_cues.json')); q=c['cues']; d=$DUR
print(*[round(x/d,4) for x in (0, q['rank5']+0.6, q['rank4']+0.5, q['rank2']+1.5, q['rank1']+1.0, q['worst']+1.5, q['end']+1.5, d-0.1)])"))
else
  FR=(0 0.15 0.235 0.45 0.69 0.73 0.82 0.95)
fi
f() { python3 -c "print('$OUT/frames/f%04d.png' % min($N - 1, int($N * $1)))"; }
cp "$(f ${FR[1]})" "$OUT/cover.png"
ffmpeg -y -loglevel error -i "$(f ${FR[0]})" -i "$(f ${FR[1]})" -i "$(f ${FR[2]})" -i "$(f ${FR[3]})" \
  -i "$(f ${FR[4]})" -i "$(f ${FR[5]})" -i "$(f ${FR[6]})" -i "$(f ${FR[7]})" \
  -filter_complex "[0][1][2][3]hstack=4[a];[4][5][6][7]hstack=4[b];[a][b]vstack,scale=1600:-1" "$OUT/check_sheet.png"
rm -rf "$OUT/frames" "$OUT/audio.wav"
echo "Done: $OUT/$SLUG.mp4 ($DUR s)"
