# Research lane: motion and visual craft for 9:16 map/ranking data videos

HONESTY NOTE. The web evidence for this niche is thin. TikTok, Instagram and YouTube pages do not load through WebFetch (returned only "TikTok - Make Your Day"), so I could NOT watch or measure any creator's video. I found no fetched page that analyses @mapsbyw, Visual Capitalist Reels, Economist/NYT/Bloomberg verticals, or bar chart races. Rules below are tagged:
- [SRC] = backed by a page I fetched this session (URL given)
- [SEARCH] = from a WebSearch result snippet only, page not opened (treat as unverified)
- [JUDGMENT] = my recommendation from general craft, not sourced. Test it.

## Build it like this (18 rules)

1. Total length 15-30 s, built from 3-5 segments of 3-5 s each. [SRC] https://spliceapp.com/blog/enhancing-youtube-shorts-world-map-travel-overlays/ (vendor guide, so promotional). Journalism shorts run longer (avg ~84 s, BBC 58 s, FT 105 s) but those are voiced pieces. [SRC] https://onlinejournalismblog.com/2026/08/10/how-data-journalism-is-done-on-tiktok-six-key-takeaways-from-watching-50-videos/ . Ward Wise: 20-25 s total.
2. Canvas 1080x1920. Keep key content inside the conservative safe zone: ~160 px top, ~480 px bottom, ~120 px sides. Sources disagree (131/367, 108/320, 160/480), so use the strictest. [SEARCH] houseofmarketers.com/guide-to-safe-zones-tiktok-facebook-instagram-stories-reels/ , poster.ly/tools/tiktok-safe-zone-checker . TikTok's only quoted official line: put main elements in the central area. [SEARCH]. Remotion has TikTok and Reels overlay PNGs to test against: https://www.remotion.dev/elements/overlays/social-safe-zones/ [SRC, no pixel numbers published there]. Result: live area about 840 x 1280, centered a bit high.
3. Animate everything. 29 of 33 data visuals in 50 TikTok data shorts were animated (zoom, reveal over time, color highlight); only 4 were static. [SRC] onlinejournalismblog URL above. Most used a single chart type; complex charts rarely appeared. So: one map, one ranking, nothing else.
4. Start wide, then zoom to the point. Splice: open on the wide view, zoom into the relevant region. [SRC] spliceapp URL above (no zoom factor given). For Ward Wise the "wide" view is the whole city, so open on the full 50-ward map and zoom to individual wards.
5. Easing: ease-out as the default for entering things, 200-500 ms. Ease-in has the same range but ends with a jolt, so avoid it for reveals. [SRC] https://web.dev/choosing-the-right-easing/ . Use a quint/expo ease-out (cubic-bezier(0.22,1,0.36,1)) for map zooms and number slides. [JUDGMENT on the exact curve; web.dev suggests quintic ease-out for a faster feel]
6. Use longer durations for bigger moves. A widely reused motion reference puts state changes at 200-300 ms, layout changes at 300-500 ms, entrances at 500-800 ms, and exits at ~75% of entrance. [SEARCH] snippet of git.secluded.site/.../motion-design.md (secondary, unopened). Map camera moves: 600-900 ms. Label pop-ins: 250-350 ms. [JUDGMENT]
7. Pace so viewers can read. Elements that appear too fast make people miss the point; sync each element to narration or beat. [SRC] https://www.capcut.com/resource/craft-infographics-for-videos (no numbers). Hold each full label+number for at least 1.5 s after it lands. [JUDGMENT, ~3 words/s reading plus a beat]
8. Keep scripts tight. Cut pauses and extra words; ~200 words max for a ~84 s short at 100-150 wpm. [SRC] onlinejournalismblog URL. At 25 s that means 50 words or fewer of voice-over, or none if you use text only.
9. Hook in the first second with the surprising answer or the question. A ranking map clip about egg consumption (Belgium beats larger countries) got ~6,700 likes in the search snippet, suggesting a "surprising #1" hook works. [SEARCH, unverified, page not opened; likes figures unreliable] Open Ward Wise with the finished colored map plus a one-line question ("Where in Chicago is walking most dangerous?"), then redraw it.
10. Choropleth color: a single-hue sequential ramp is standard for one ordered stat; lighter = lower, darker = higher. [SEARCH] ArcGIS blog https://www.esri.com/arcgis-blog/products/arcgis-pro/mapping/brewing-a-new-color-palette-for-arcgis-pro . Vary lightness, not just saturation, so it survives color blindness, and keep the legend simple (lowest, highest, a few steps). [SEARCH] Datawrapper https://www.datawrapper.de/academy/what-to-consider-when-creating-choropleth-maps (snippet only). Datawrapper flags equally bright red/green, orange/green, yellow/pink as the problem pairs. [SEARCH] https://notes.vis4.net/blog/1802-datawrapper-color-blind-check
11. Use a single blue ramp for "more crashes". Do NOT add a second hue to the ramp itself. Red meaning "danger" is cultural and the red/green pair is the colorblind trap; blue light-to-dark is also colorblind-safe per ApexCharts' flags (library's own claim). [SEARCH] https://apexcharts.com/apexmaps/docs/palettes/ . Make "danger" legible with words and rank numbers, not hue: put "Most dangerous" at the dark end of the legend. If you want an accent for the single worst ward, use a thick dark-navy outline plus the label, not red. [JUDGMENT]
12. Color alone must not carry the meaning. Pair every shaded ward with a rank number or label for the ones you call out; test in grayscale. [SEARCH] Visa guide https://design.visa.com/global-accessibility-requirements/mobile/visual/ ; WCAG 1.4.1 and 1.4.11 (3:1 for graphics needed to understand content). Check that the lightest blue still has about 3:1 against the white background, or give wards a thin gray 0.5-1 px outline. [JUDGMENT: pick ramp ends like #cfe3f9 to #0a3d7a, verify with a contrast checker]
13. Choose class breaks on purpose. More classes exaggerate contrast; quartiles are a compromise for showing geographic pattern. [SRC] https://www.datawrapper.de/blog/how-to-choose-a-color-palette-for-choropleth-maps . Use 5 classes (quintiles of 10 wards each) so the legend reads in one glance. [JUDGMENT]
14. Highlight one ward by dimming the rest. Spec: others to 25-35% opacity (or desaturate), selected ward at 100% with a 3 px white inner stroke and 4 px #0071e3-dark outer stroke, slight scale 1.0 to 1.04, soft shadow (0 8 24 rgba(0,0,0,.25)). Pulse once only (scale 1.0 to 1.06 to 1.0 over 500 ms). Camera zoom ~1.8-2.5x onto the ward. [JUDGMENT, none of this was in a fetched source]
15. Never flash. Fewer than 3 flashes in any second (WCAG 2.3.1); avoid fast blinking of saturated red. [SEARCH] secondary summary of WCAG. Use fades and slides, not strobes.
16. Sound: layer your own short SFX (soft tick on each count step, short whoosh under 0.4 s on camera moves) on top of a music bed, with SFX slightly under the music, and do not put an SFX on every beat. [SEARCH] morphic.com/resources/use-cases/sound-effects-for-tiktok ; Epidemic whoosh page https://www.epidemicsound.com/youtube/transition-sound-effects . Align the SFX transient exactly to the visual event. Check on phone speaker and headphones. No source gave BPM. Use 100-120 bpm lo-fi/ambient and cut on beat. [JUDGMENT]
17. Text sizes at 1080x1920 (all JUDGMENT, no source gave sizes; the sources said only "large, bold, high-contrast"): hook headline 72-84 px semibold, rank numeral 160-220 px bold, ward name 56-64 px, stat line (e.g., "41 crashes") 44-52 px, legend/source 28-32 px. Nothing below 28 px. Max 8-10 words per frame, one idea per frame. System font (SF Pro) per brand.
18. End card: 2-3 s hold. Logo ~160-200 px wide, URL in 44-52 px, one line of CTA ("Find your ward at wardwise.org" or whatever the real domain is), kept above the bottom 480 px. [JUDGMENT] Journalism shorts point to longer work with "link in bio" CTAs. [SRC] onlinejournalismblog URL. Note: all 50 analysed shorts had voice-over and 43 had a presenter; the article did not study music or branding visuals. A text-only map video is therefore off the sample and untested here.

## Shot list (25 s, built from rules 1-9, timings are JUDGMENT)

| t (s) | Beat | Detail |
|---|---|---|
| 0.0-1.5 | Hook | Full 50-ward map already filled; headline "Where is walking in Chicago most dangerous?" fades up, ease-out 300 ms |
| 1.5-4.0 | Setup | Map resets to blank outline, then color wave sweeps wards light to dark, staggered 15-25 ms per ward (about 1 s total), legend slides in |
| 4.0-6.0 | Rule | One line: "Pedestrian and cyclist crashes per ward, 2025." Hold 2 s |
| 6.0-8.5 | #5 (or #10) | Others dim to 30%, camera eases to ward over 700 ms, rank badge + name + number count up over 600 ms, hold 1.5 s |
| 8.5-11 | #4 | Same pattern, camera pans (no zoom out) |
| 11-13.5 | #3 | Same |
| 13.5-16 | #2 | Same |
| 16-20 | #1 | Longer: 1.2x zoom, pulse once, number counts up with a larger numeral, hold 2.5 s |
| 20-22.5 | Wide | Zoom out to full map, top 5 stay dark with their rank badges, rest back to 100% |
| 22.5-25 | End card | Logo, URL, "Next: [episode 2]" |

Counting down from #5 to #1 builds suspense; each ward beat is 2.5 s, which matches the 3-5 s segment guidance only loosely, so group in threes if it feels rushed.

## Rank list beside a map in 9:16 (JUDGMENT)
Do not put a full 50-row list beside the map; at phone width it is unreadable. Put the map in the middle 55% of height, a single "current ward" card under it (rank badge, name, count), and a compact top-5 stack along the lower third that fills as each rank is revealed (5 rows, 56 px type). Count-up on the number: 600 ms, ease-out, integers only.

## Examples worth studying (what I could and could not verify)
I could not load any of these in a player, so "what to copy" is based on the article's description only.
1. FT, John Burn-Murdoch birth-rate line chart, https://www.tiktok.com/@financialtimes/video/7548754660601908502 : named in the article, page did not render. Copy: animated reveal over time. Unverified.
2. The Times, UK expatriates, https://www.tiktok.com/@thetimes/video/7657589204440009987 : article says animated text highlights rising figures. Page did not render.
3. Guardian, super-majority animated graphics, https://www.tiktok.com/@guardian/video/7388201464289643809 : article says the Guardian used the most elaborate animation. Page not rendered.
4. ITV Politics, Makerfield by-election bar chart, https://www.tiktok.com/@itvpolitics/video/7652400134977752342 : bar chart, not rendered.
5. Creator ranking-map clips (egg consumption, GDP ranking) on TikTok discover pages. Not opened; no URLs I can cite.
All five sources for examples come from https://onlinejournalismblog.com/2026/08/10/how-data-journalism-is-done-on-tiktok-six-key-takeaways-from-watching-50-videos/ . None is a choropleth ranking, so treat them as pacing/animation references only.

## Gaps for the next lane
- Need someone to watch 5-10 real map-ranking Reels in a browser or with a screen recorder (mcp__claude-in-chrome) and time the beats and measure text height. Candidate handles to look up: @mapsbyw, @geographyfocus, Visual Capitalist, The Economist, Bloomberg Graphics. Not verified that these accounts exist in the form named in the brief.
- The 20 guidelines in Tang et al., Journal of Visualization 23(4):707-720, 2020 (https://scholar.xjtlu.edu.cn/en/publications/design-guidelines-for-augmenting-short-form-videos-using-animated/) are not in the fetched abstract. Worth getting the full text.
- No source for music BPM, SFX loudness, or logo size.
