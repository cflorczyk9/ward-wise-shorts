# Ward Wise Ep. 1 video: design spec (1080x1920, 30 fps, 20.0 s)

Title idea: "Chicago's 5 safest wards for people on foot." Data: 2025 police-reported crashes where first impact hit a person walking or biking. Wards have about equal population, so raw counts compare fairly.

Verified from source: --blue #0071e3; light ramp --ramp-0..4 = #e3eefc #b7d3f7 #7fb1ee #3f86e0 #0a5cc2; dark ramp #33404e #2c5478 #2f74ad #2f97e0 #0a84ff; dark header blue #2997ff; font stack -apple-system, BlinkMacSystemFont, "SF Pro Text"/"SF Pro Display", "Helvetica Neue"; map = plain SVG, cos(lat) equirectangular, white seams; logo = rising data line in a light beam, #0071e3 line, dark dot #1c2433; og-image = white left panel, "Chicago, measured." in ~bold near-black, grey subline, blue link line, light-grey (#f5f5f7) right panel with blue map.

## 4. Color decisions (read first)
- Background: white #ffffff, map stage panel #f5f5f7. Reason: Connor's rule and og-image match; a bright block stands out in dark feed UIs. No dark version in v1 (one primary).
- Ink #1d1d1f, secondary #6e6e73, tertiary #86868b. Blue #0071e3 only accent.
- Map ramp (5 steps, site tokens, no new colors): 0 #e3eefc, 1 #b7d3f7, 2 #7fb1ee, 3 #3f86e0, 4 #0a5cc2. Seams: 2px #ffffff.
- Shading rule: darker blue = fewer crashes = better (site convention). Quintile by count: Q1 (fewest 10 wards) = ramp-4 ... Q5 (most) = ramp-0. Reason: matches the site, and the safest wards become the visual heroes.
- Active ward fill: #0071e3 (brand blue, brighter than ramp-4 so it reads as "selected"). Outline 6px #ffffff inner + 3px #1d1d1f? No: outline 4px #0a2f66 (deep navy) with white 2px halo outside. Reason: a navy edge reads on every ramp step.
- Dimmed wards: keep ramp fill but at 28% opacity over the #f5f5f7 stage. Reason: shape of the city stays readable.
- Danger flip: NO red (one blue). Same ramp. Active danger ward fills solid ink #1d1d1f with white numeral; countdown card turns from white to #1d1d1f. Reason: ink vs blue signals "other side" without adding a hue.

## 1. Storyboard (20.0 s, authoritative timeline)
Easing names: out-expo = cubic-bezier(0.16,1,0.3,1); out-cubic; in-out-cubic; spring (stiffness 220, damping 22, under 3% overshoot).

| t (s) | Beat | What moves | Text on screen |
|---|---|---|---|
| 0.0-2.6 | Hook + map draw-in (together, no dead air) | Frame 0 shows ward outlines only (2px #b7d3f7 on #f5f5f7 stage). Outlines draw 0-1.2 s (in-out-cubic, 14 ms stagger by ward number). Fills ramp in 0.8-2.6 s (out-cubic, 20 ms stagger by value, darkest last). Map scales 0.94 to 1.0 over 1.6 s (out-expo). Title fades in 0.0-0.4 (out-cubic, 12 px rise). | "Where is Chicago safest" / "to walk?" ; subline at 1.0 s: "5,324 walking and biking crashes in 2025." |
| 2.6-4.4 | Legend | Title lifts and fades 2.6-3.0. Legend chip fades in. | "Darker = fewer crashes" |
| 4.4-5.0 | Setup | All wards dim to 28% (out-cubic 0.4 s). | "The 5 safest wards" |
| 5.0-7.4 | #5 Ward 12 | cycle below | #5, Ward 12, Brighton Park, McKinley Park, 52 |
| 7.4-9.6 | #4 Ward 38 | cycle | 51, Dunning, Portage Park |
| 9.6-11.8 | #3 Ward 41 | cycle | 44, Norwood Park, Edison Park |
| 11.8-14.0 | #2 Ward 18 | cycle | 31, Ashburn |
| 14.0-16.6 | #1 Ward 10 | cycle, zoom 2.6x, extra hold. At 15.4 "Fewest in the city" fades in. At 15.6 median chip "City median: 97". | 29, South Deering, Hegewisch |
| 16.6-17.0 | Breath | Camera out-expo to full map, all wards 100% for 0.4 s. | none |
| 17.0-18.6 | Flip | Wards re-dim to 28%. Wards 27, 42, 28 turn solid ink #1d1d1f at 17.0, 17.3, 17.6 with 64px counts popping above each. Title swaps in. | "Now the other end." ; "Ward 27  319" "Ward 42  312" "Ward 28  233" (36px stack) |
| 18.6-20.0 | End card | Map shrinks to a small pin (in-out-cubic 0.6 s), logo and CTA stagger in. Hold the last 1.0 s. | "Find your ward." wardwise.org |

Per-rank cycle (each rank 2.2 to 2.4 s as in the table; the next card begins while the old one exits):
- 0.00-0.45 camera: map pans+zooms to ward (zoom 2.2x, out-expo 0.7 s starting 0.0), active ward un-dims to 100%, gets outline (stroke-width 0 to 4 px in 0.25 s) and lifts (see 5).
- 0.15-0.55 rank card slides up from y+80 and fades in (spring).
- 0.25-1.45 numeral counts 0 to N (out-cubic, 1.2 s, tabular). Ends on exact N.
- 1.45-2.0 hold; previous card exits at the next cycle start (fade + y-40, 0.3 s in-out-cubic).

## 2. Layout grid (px, 1080x1920)
Safe zones: top 220, bottom 420, right 140, left margin 72. Content box: x 72-940 (width 868), y 220-1500.
- Title block: y 240-420, left aligned at x=72, max width 868.
- Map stage: rounded rect 28px radius, fill #f5f5f7, x 72, y 460, w 868, h 868 (to y 1328). City map fitted inside with 40px padding (aspect about 0.62 w:h, so map height 788, width about 490, centered x 261-751). Zoomed ward views fill the stage and clip to it.
- Rank card: x 72, y 1352, w 868, h 148 (to y 1500), radius 28, fill #ffffff, shadow 0 8 32 rgba(0,0,0,0.10), 1px #e5e5ea border. Layout inside: numeral left (x 104), ward label stack right of it.
- Source line: y 1508-1540 (inside the safe bottom, 1500 limit relaxed by 40 px for a 22px caption only), x 72.
- End card text block: y 560-1300 centered in the 868 column.
- Everything else (bottom 420 px, y 1500-1920) stays empty background so platform UI never covers content.

## 3. Type scale (system stack: -apple-system, BlinkMacSystemFont, "SF Pro Display" at >=28px, "SF Pro Text" below, "Helvetica Neue", Arial, sans-serif)
- Title: 84px / 88 line, weight 700, letter-spacing -0.035em, #1d1d1f.
- Subline/legend: 38px, weight 500, #6e6e73, -0.01em.
- Big numeral (rank card): 120px, weight 700, -0.04em, font-variant-numeric: tabular-nums, #0071e3 for safe, #ffffff on ink card for danger. Rank badge "#1": 40px weight 700 in a 72px circle, fill #0071e3, white text.
- Ward label: 52px weight 650 (use 600 if missing), -0.02em, #1d1d1f. Neighborhood: 34px weight 500, #6e6e73.
- Caption (units under numeral, "crashes"): 30px weight 500, #86868b.
- Source line: 22px weight 500, #86868b: "Source: Chicago police crash reports, 2025 | wardwise.org".
- All text min 22px; nothing under 22.

## 5. Active ward highlight
- Outline: 4px #0a2f66 inside edge, 2px white halo outside (draw as two strokes).
- Lift: drop shadow 0 14 28 rgba(10,47,102,0.35); fill brightens to #0071e3; translateY -6px; scale 1.03 about the ward centroid (out-cubic 0.3 s). No glow (glow looks like a template effect).
- Zoom factor: 2.2x for wards 12/38/18, 2.0x for 41 (large), 2.6x for Ward 10 (the hero). Always keep ward fully inside stage with 60px padding, so cap the zoom.
- Others: 28% opacity of their ramp fill. During the flip, danger wards use fill #1d1d1f at 100%.

## 6. Number treatment
- Count-up 1.2 s out-cubic, integer steps, tabular-nums so width never jitters. Ends with a 100 ms scale 1.0-1.05-1.0 pop (spring).
- "crashes" caption beneath in 30px. Ward 10 only: median chip "City median: 97" (pill, fill #e3eefc, text #0a5cc2, 30px, weight 600).
- Flip numbers: no count-up, pop in at 64px weight 700.

## 7. Ward labels
Format: "Ward 10" (52px) with neighborhood below ("South Deering", 34px). Pulled from wardwise.org/api/wards community_area_overlaps (largest ward_area_pct), 2nd in parentheses where the first is under 60%:
- Ward 10: South Deering (44.9%), then Hegewisch 25.3%, East Side 14.4%. Label: "South Deering, Hegewisch"
- Ward 18: Ashburn (68.8%). Label: "Ashburn"
- Ward 41: O'Hare (67.3%), Norwood Park 21.4%, Edison Park 6.6%. Label: "Norwood Park, Edison Park" (do NOT lead with O'Hare: it is the airport zone, most people won't read it as a neighborhood.)
- Ward 38: Dunning (50.2%), O'Hare 28.2%, Portage Park 21.5%. Label: "Dunning, Portage Park"
- Ward 12: Brighton Park (45.8%), McKinley Park 20.3%, New City 16.8%. Label: "Brighton Park, McKinley Park"
- Ward 27: Near West Side (37.1%), West Town 19.9%, Humboldt Park 17.5%. Label: "Near West Side, West Town"
- Ward 42: Near North Side (50.4%), Loop (45.2%). Label: "Near North, Loop"
- Ward 28: Near West Side (38.1%), East Garfield Park 19.4%, West Garfield Park 16.4%. Label: "East and West Garfield Park"
- Ward 34: API returns Near West Side 69.7%, Loop 26.8%. THIS LOOKS WRONG: Ward 34 (Ald. William Conway) is on the Far South Side, and neighborhood_labels is empty. Do not show these. Not on screen in the current storyboard (only top 3 shown in flip). Flag to Connor and fix API/data before using.
- Ward 1: West Town (58.2%), Logan Square (41.8%). Label: "West Town, Logan Square"
Name caveat: the API capitalizes "Mckinley Park" and "Ohare"; use "McKinley Park" and "O'Hare" on screen.
Max label width 868 minus numeral width: one line at 34px must be under about 24 characters; shorten as above.

## 8. End card (18.6-20.0, hold last 1.0 s)
- Map shrinks to a 300px-tall pin in the stage, all wards full opacity, ramp colors.
- Logo (static/logo.svg) 120px at x center, y 640; wordmark "Ward Wise" 72px weight 700 -0.03em beside it (match og-image lockup).
- CTA line (46px weight 600, #1d1d1f), y 860: "Find your ward."
- Subline 36px #6e6e73, y 930: "Look up any ward or neighborhood."
- URL pill y 1030: "wardwise.org", 52px weight 600, text #ffffff on #0071e3 pill, 72px tall, radius 36, padding 40. (No left bars, no em dashes.)
- Fade/rise in staggered 120 ms each, out-expo 0.5 s.

## 9. Cover frame (thumbnail, render as separate still at 1080x1920, also 1080x1350 center-safe crop)
- Background #ffffff. Title top-left at y 300: "Chicago's safest wards" 108px / 100 line weight 800 -0.04em, then "to walk" in #0071e3 on the line below.
- Map at 100% ramp, stage panel #f5f5f7, ward 10 highlighted navy outline, with a tag "29" in 160px #0071e3 pill-less numeral beside it and caption "crashes in 2025".
- Small logo lockup bottom-left of content box at y 1440 (inside safe zone).
- Everything inside x 72-940, y 240-1500. No text smaller than 34px.
