#!/usr/bin/env python3
"""Build the render data for one episode from the live Ward Wise API.

Usage:  python3 build_episode.py ../episodes/walking-safety.json
Writes: ../output/<slug>/video_data.json, then prints the top 5 and bottom 3 so you can check them.

The episode file holds the on-screen text plus the metric and year. Leave "best" or "worst"
out and the script fills them with the real top 5 and bottom 3 and neighborhood labels from
the API. Fill them in by hand when you want shorter or friendlier neighborhood labels.
If the episode has a "voiceover" and make_video.sh has already voiced it, the spoken cue times are added too.
"""
import json, math, os, statistics, sys, urllib.request

API = "https://www.wardwise.org/api"
NAME_FIX = {"Mckinley Park": "McKinley Park", "Ohare": "O'Hare"}


def get(path):
    with urllib.request.urlopen(API + path, timeout=90) as r:
        return json.load(r)


def rings(geom):
    return [geom["coordinates"]] if geom["type"] == "Polygon" else geom["coordinates"]


def main(spec_path):
    ep = json.load(open(spec_path))
    slug = os.path.splitext(os.path.basename(spec_path))[0]
    out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "output", slug)
    os.makedirs(out_dir, exist_ok=True)

    manifest = get("/explorer/manifest")
    meta = next(m for m in manifest["metrics"] if m["metric_id"] == ep["metric_id"])
    ep.setdefault("direction", meta["direction"])
    year = ep["year"]
    deltas = get(f"/metrics/delta?metric_id={ep['metric_id']}&from_year={year}&to_year={year}")["deltas"]
    values = {d["area_id"]: d["to_value"] for d in deltas if d["to_value"] is not None}
    if len(values) < 50:
        print(f"WARNING: only {len(values)} of 50 wards have a {year} value. Pick another year or metric.")

    wards_api = {w["alderperson"]["ward_id"]: w for w in get("/wards")["wards"]}
    geo = get("/wards.geojson")

    # Same projection as the site's civic_map.js: equirectangular scaled by cos(latitude).
    lons, lats = [], []
    for f in geo["features"]:
        for poly in rings(f["geometry"]):
            for ring in poly:
                for x, y in ring:
                    lons.append(x); lats.append(y)
    mnx, mxx, mny, mxy = min(lons), max(lons), min(lats), max(lats)
    k = math.cos(math.radians((mny + mxy) / 2))
    S = 1000 / (mxy - mny)

    wards = {}
    for f in geo["features"]:
        wid = str(f["properties"]["ward_id"]).zfill(2)
        parts = []
        for poly in rings(f["geometry"]):
            for ring in poly:
                pts = [((x - mnx) * k * S, (mxy - y) * S) for x, y in ring]
                parts.append("M" + "L".join(f"{a:.1f},{b:.1f}" for a, b in pts) + "Z")
        if wid not in values:
            print(f"WARNING: ward {wid} has no value; it is drawn at the median.")
        wards[wid] = {"d": "".join(parts), "value": values.get(wid)}
    # True median. With 50 wards it is the average of the two middle wards, so it can end in .5.
    med = statistics.median(values.values())
    for w in wards.values():
        if w["value"] is None:
            w["value"] = med

    def hood(wid):
        ov = sorted(wards_api[wid].get("community_area_overlaps", []), key=lambda o: -o["ward_area_pct"])
        names = [NAME_FIX.get(o["name"], o["name"]) for o in ov if o["ward_area_pct"] >= 15][:2]
        return ", ".join(names) or NAME_FIX.get(ov[0]["name"], ov[0]["name"])

    order = sorted(wards, key=lambda w: -wards[w]["value"] if ep["direction"] == "higher" else wards[w]["value"])
    ep.setdefault("best", [{"id": w, "hood": hood(w)} for w in order[:5]])
    ep.setdefault("worst", [{"id": w, "hood": hood(w)} for w in order[::-1][:3]])
    dec = ep.get("decimals", 0) if med == round(med, ep.get("decimals", 0)) else ep.get("decimals", 0) + 1
    ep.setdefault("median_text", f"Typical ward had {ep.get('prefix', '')}{med:,.{dec}f}{ep.get('suffix', '')}")

    # Word times from the voiceover step (voiceover/make_voice.py), if this episode has a voice.
    vc = os.path.join(out_dir, "voice_cues.json")
    if ep.get("voiceover") and os.path.exists(vc):
        ep["voice_timing"] = json.load(open(vc))

    out = {"width": round((mxx - mnx) * k * S, 1), "height": 1000, "wards": wards, "episode": ep}
    json.dump(out, open(os.path.join(out_dir, "video_data.json"), "w"))

    print(f"{meta['label']} ({ep['metric_id']}), {year}, {ep['direction']} is better, median {med}")
    print("Best 5:  " + " | ".join(f"Ward {int(b['id'])} {values.get(b['id'])} ({b['hood']})" for b in ep["best"]))
    print("Worst 3: " + " | ".join(f"Ward {int(b['id'])} {values.get(b['id'])} ({b['hood']})" for b in ep["worst"]))
    print("Wrote " + os.path.normpath(os.path.join(out_dir, "video_data.json")))


if __name__ == "__main__":
    main(sys.argv[1])
