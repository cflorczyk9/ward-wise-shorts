#!/bin/bash
# Download the Mixkit song if it is missing. The mp3 is not in the repo (the license forbids sharing it alone).
# Song: "Just Keep Walking" by Mixkit, item 963, Mixkit Stock Music Free License (see LICENSE.md).
set -euo pipefail
cd "$(dirname "$0")"
FILE=just-keep-walking.mp3
[ -s "$FILE" ] && exit 0
echo "Downloading the song from Mixkit..."
if curl -fsSL -o "$FILE.part" https://assets.mixkit.co/music/963/963.mp3 && [ -s "$FILE.part" ]; then
  mv "$FILE.part" "$FILE"
else
  rm -f "$FILE.part"
  echo "Could not download the song. Do it by hand:"
  echo "  1. Open https://mixkit.co/free-stock-music/ and search for 'Just Keep Walking' (item 963)."
  echo "  2. Click Download."
  echo "  3. Save the file as $(pwd)/$FILE"
  exit 1
fi
