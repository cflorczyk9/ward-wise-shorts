#!/usr/bin/env python3
"""Write audio.wav: the episode's song, cut to the video length and started on a downbeat.
The song's "start" in the episode file is a downbeat, so the reveals in video.html land on the beat.
The track fades out over the last 1.5 s and is leveled to -14 LUFS, the loudness Reels and TikTok play at.
With a voice file, the song is pushed down while the voice talks (sidechain duck) and the mix is leveled to -14 LUFS.
Usage: python3 make_audio.py <out.wav> <episode.json> <duration_seconds> [voice.wav]"""
import json, os, subprocess, sys
out, spec, dur = sys.argv[1], sys.argv[2], float(sys.argv[3])
voice = sys.argv[4] if len(sys.argv) > 4 else None
music = json.load(open(spec))["music"]
song = os.path.join(os.path.dirname(os.path.abspath(spec)), "..", music["file"])
cut = ["-ss", str(music["start"]), "-t", str(dur), "-i", song]
if voice:
    fade = f"afade=t=in:d=0.04,afade=t=out:st={dur - 1.5}:d=1.5"
    fc = (f"[0:a]volume=0.55,{fade},aresample=48000[m];[1:a]aresample=48000,apad=whole_dur={dur},asplit[v][k];"
          "[m][k]sidechaincompress=threshold=0.02:ratio=8:attack=20:release=400[d];"
          f"[d][v]amix=inputs=2:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=11,aresample=48000,atrim=0:{dur}[a]")
    cmd = ["ffmpeg", "-y", "-loglevel", "error", *cut, "-i", voice, "-filter_complex", fc, "-map", "[a]", "-ac", "2", out]
else:
    cmd = ["ffmpeg", "-y", "-loglevel", "error", *cut,
           "-af", f"afade=t=in:d=0.04,afade=t=out:st={dur - 1.5}:d=1.5,loudnorm=I=-14:TP=-1.5:LRA=11,aresample=48000", "-ac", "2", out]
subprocess.run(cmd, check=True)
