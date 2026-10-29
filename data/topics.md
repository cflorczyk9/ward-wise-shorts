# Ward Wise short-video topics: top 20

All values pulled live from https://www.wardwise.org/api on 2026-10-13. "Top 5" means the five wards that best fit the title; "Bottom 3" is the opposite end. Format is ward:value. Walking safety (pedestrian crashes) is excluded as episode 1.

## 1. Chicago's 5 hottest wards in summer
- Metric: `summer_surface_temp_c` (Summer Surface Temperature), direction: lower is better, confidence: high, wards: 50
- Year: 2026
- Top 5: W25 40.2 C, W12 40.2 C, W23 40.2 C, W13 40.1 C, W14 39.9 C
- Bottom 3: W46 34.3 C, W10 34.4 C, W42 34.5 C
- Call: https://www.wardwise.org/api/metrics/delta?metric_id=summer_surface_temp_c&from_year=2026&to_year=2026
- Why it works: Everyone feels it, and the hot list (23, 13, 14) holds year after year while the lakefront and Ward 10 stay cool (high confidence).
- Fairness caveat: Satellite surface temperature, not air temperature, from one summer. Tracks pavement and tree cover, so it is fair per ward. 2025 and 2026 differ in the exact top 5 but 23, 13, 14 recur 2022-2024.

## 2. Chicago's 5 cheapest wards to rent
- Metric: `median_gross_rent` (Rent (ACS, rents paid)), direction: lower is better, confidence: medium, wards: 50
- Year: 2023
- Top 5: W10 $996, W22 $1,039, W14 $1,046, W6 $1,072, W16 $1,074
- Bottom 3: W42 $2,575, W34 $2,278, W43 $2,175
- Call: https://www.wardwise.org/api/metrics/delta?metric_id=median_gross_rent&from_year=2023&to_year=2023
- Why it works: Rent is the number one dinner-table topic and the bottom (Ward 42, 34, 43) is the downtown crowd.
- Fairness caveat: Survey estimate (ACS 2023, medium confidence). Median covers all units, not apartments listed today.

## 3. Chicago's 5 safest wards (violent crime)
- Metric: `violent_crime_rate_per_10000` (Violent Crime), direction: lower is better, confidence: medium, wards: 50
- Year: 2025
- Top 5: W43 92, W45 93, W41 100, W38 100, W32 103
- Bottom 3: W6 615, W24 527, W20 525
- Call: https://www.wardwise.org/api/metrics/delta?metric_id=violent_crime_rate_per_10000&from_year=2025&to_year=2025
- Why it works: Guaranteed comments. Rate per 10,000 residents, full-year 2025.
- Fairness caveat: Reported crime. Ward 42 is not at the extreme because the rate divides by residents, not visitors. Not the walking-safety episode: it counts assaults, battery, homicide and sexual assault, not crashes.

## 4. Chicago's 5 wards with the most bars
- Metric: `dedicated_bars_count` (Bars & taverns (Google Maps sweep)), direction: higher is better, confidence: high, wards: 50
- Year: 2026
- Top 5: W42 92, W44 79, W27 74, W1 68, W32 47
- Bottom 3: W9 2, W37 3, W7 3
- Call: https://www.wardwise.org/api/metrics/delta?metric_id=dedicated_bars_count&from_year=2026&to_year=2026
- Why it works: Ward 44 (Wrigleyville) and Ward 1 rank above Ward 32 and the rest, and Ward 42 leads. Bar-count arguments fill comments.
- Fairness caveat: Count, so downtown and nightlife corridors win. Ward 42 leads partly because of non-residents. Google Maps sweep (high confidence).

## 5. Chicago's 5 wards with the fewest chain restaurants
- Metric: `chain_restaurant_share_pct` (Chain restaurant share (Google Maps sweep)), direction: lower is better, confidence: high, wards: 50
- Year: 2026
- Top 5: W11 6.0%, W35 9.1%, W26 9.5%, W25 9.6%, W1 10.9%
- Bottom 3: W21 35.0%, W5 33.6%, W7 30.9%
- Call: https://www.wardwise.org/api/metrics/delta?metric_id=chain_restaurant_share_pct&from_year=2026&to_year=2026
- Why it works: Ward 11 (Bridgeport) at 6% is a surprise; Lincoln Park Ward 43 is not on the list.
- Fairness caveat: Share, not count, so it is fair. Depends on what the sweep counted as a chain.

## 6. Chicago's 5 highest-income wards
- Metric: `median_household_income` (Income), direction: higher is better, confidence: medium, wards: 50
- Year: 2023
- Top 5: W32 $166,248, W43 $154,506, W42 $137,022, W1 $135,175, W2 $122,626
- Bottom 3: W16 $39,254, W20 $40,491, W17 $42,191
- Call: https://www.wardwise.org/api/metrics/delta?metric_id=median_household_income&from_year=2023&to_year=2023
- Why it works: Shareable and arguable (Ward 32 beats Ward 43).
- Fairness caveat: ACS 2023 medium confidence. Household median is distorted in wards with many students or retirees.

## 7. Chicago's 5 wards that vote the most
- Metric: `voter_turnout_pct` (Voter Turnout), direction: higher is better, confidence: high, wards: 50
- Year: 2023
- Top 5: W19 62.0%, W47 56.5%, W48 53.2%, W41 53.1%, W43 52.1%
- Bottom 3: W16 21.0%, W14 22.3%, W15 22.4%
- Call: https://www.wardwise.org/api/metrics/delta?metric_id=voter_turnout_pct&from_year=2023&to_year=2023
- Why it works: Ward 19 (Beverly) beats every lakefront ward, and the bottom is a stark gap.
- Fairness caveat: Only the 2023 municipal election (period end 2023-04-04) is available. Turnout is of registered voters.

## 8. Chicago's 5 wards with the most coffee shops
- Metric: `coffee_shops_count` (Coffee shops (Google Maps sweep)), direction: higher is better, confidence: high, wards: 50
- Year: 2026
- Top 5: W42 186, W34 120, W27 89, W2 75, W44 71
- Bottom 3: W9 6, W8 6, W37 7
- Call: https://www.wardwise.org/api/metrics/delta?metric_id=coffee_shops_count&from_year=2026&to_year=2026
- Why it works: Easy 6-word stat, with Ward 42 at 186 and Ward 8 at 6.
- Fairness caveat: Count, so downtown wins by volume. Per-10k version (licensed_coffee_shops_per_10000_residents) puts Ward 11 in the top 4.

## 9. Chicago's 5 wards that fix potholes fastest
- Metric: `c311_service_pothole_days` (Pothole repair (service)), direction: lower is better, confidence: unrated, wards: 50
- Year: 2025
- Top 5: W3 0.4 days, W42 0.9 days, W9 2.1 days, W34 2.3 days, W49 2.9 days
- Bottom 3: W24 50.0 days, W26 44.8 days, W33 39.0 days
- Call: https://www.wardwise.org/api/metrics/delta?metric_id=c311_service_pothole_days&from_year=2025&to_year=2025
- Why it works: Everyone hates potholes. Ward 24 is the slowest in 2022, 2025 and 2026.
- Fairness caveat: Confidence unrated. The ranking swings by year (weather and crew timing) and tiny ward samples make Ward 3 at 0.4 days suspect. 2026 is partial through 29 Sep. Say the year on screen.

## 10. Chicago's 5 sunniest wards (fewest shadows)
- Metric: `annual_sun_access_pct` (Sun Access), direction: higher is better, confidence: unrated, wards: 50
- Year: single snapshot (latest)
- Top 5: W41 96.1%, W13 95.2%, W10 95.0%, W23 94.0%, W18 93.5%
- Bottom 3: W42 57.0%, W2 63.6%, W34 69.6%
- Call: https://www.wardwise.org/api/metrics/comparison?metrics=annual_sun_access_pct
- Why it works: Fresh, visual: Ward 42 gets 57% of the sun and 40% on the winter solstice.
- Fairness caveat: Confidence unrated. Modeled from building heights, so it reflects tall buildings, not weather. Downtown is naturally lowest.

## 11. Chicago's 5 wards where the alderman shows up least
- Metric: `council_attendance_pct` (Attendance), direction: higher is better, confidence: medium, wards: 50
- Year: single snapshot (latest)
- Top 5: W27 41%, W42 67%, W9 70%, W37 72%, W15 79%
- Bottom 3: W39 97%, W17 97%, W5 97%
- Call: https://www.wardwise.org/api/metrics/comparison?metrics=council_attendance_pct
- Why it works: Names an alderman. Ward 27 at 41% is eye-catching.
- Fairness caveat: Medium confidence. Several wards tie at 97%, so the top is a tie. Excused absences may not be counted. Name carefully.

## 12. Chicago's 5 wards with the fewest cars per home
- Metric: `vehicles_per_household` (Cars per Household), direction: lower is better, confidence: unrated, wards: 50
- Year: single snapshot (latest)
- Top 5: W2 0.56, W34 0.64, W42 0.66, W44 0.67, W46 0.70
- Bottom 3: W23 1.85, W18 1.73, W13 1.69
- Call: https://www.wardwise.org/api/metrics/comparison?metrics=vehicles_per_household
- Why it works: The car-free map: Ward 2, 34, 42 below 0.7 cars per home.
- Fairness caveat: Confidence unrated. Mostly a density story, not choice. Pair with the L map.

## 13. Chicago's 5 wards with the most new businesses
- Metric: `business_openings_per_10000_residents` (Business openings), direction: higher is better, confidence: medium, wards: 50
- Year: 2025
- Top 5: W42 84.9 per 10k, W27 63.3 per 10k, W34 57.3 per 10k, W25 38.7 per 10k, W12 36.2 per 10k
- Bottom 3: W9 8.6 per 10k, W13 9.6 per 10k, W23 10.1 per 10k
- Call: https://www.wardwise.org/api/metrics/delta?metric_id=business_openings_per_10000_residents&from_year=2025&to_year=2025
- Why it works: Wards 25 (Pilsen) and 12 in the top 5 are the surprise.
- Fairness caveat: Per resident, so downtown inflates. Based on licence openings (medium confidence).

## 14. Chicago's 5 wards with the most languages at home
- Metric: `linguistic_diversity` (Linguistic Diversity), direction: higher is better, confidence: medium, wards: 50
- Year: 2023
- Top 5: W50 67.6, W38 64.0, W33 61.0, W11 59.3, W39 59.1
- Bottom 3: W6 8.5, W8 8.7, W21 10.0
- Call: https://www.wardwise.org/api/metrics/delta?metric_id=linguistic_diversity&from_year=2023&to_year=2023
- Why it works: Ward 50 (West Rogers Park) on top is a surprise. Warm, positive topic.
- Fairness caveat: ACS 2023 medium confidence. Score is an index (not a count of languages).

## 15. Chicago's 5 wards with the most murals
- Metric: `murals_registered_count` (Registered murals), direction: higher is better, confidence: high, wards: 50
- Year: 2026
- Top 5: W46 49, W32 39, W4 36, W1 28, W26 25
- Bottom 3: W41 1, W33 1, W31 1
- Call: https://www.wardwise.org/api/metrics/delta?metric_id=murals_registered_count&from_year=2026&to_year=2026
- Why it works: Uptown's Ward 46 leads Ward 32 and Ward 4.
- Fairness caveat: Registered murals only, so wards with active artist groups register more. Cumulative count, not a 2026 total.

## 16. Chicago's 5 wards with the longest commutes
- Metric: `long_commute_pct` (Long Commutes), direction: lower is better, confidence: medium, wards: 50
- Year: 2023
- Top 5: W7 41.4%, W9 40.2%, W18 39.1%, W10 38.9%, W8 37.6%
- Bottom 3: W2 12.5%, W34 12.9%, W42 13.8%
- Call: https://www.wardwise.org/api/metrics/delta?metric_id=long_commute_pct&from_year=2023&to_year=2023
- Why it works: Everyone commutes. Southeast and Southwest side wards 7, 9, 18, 10, 8 top the list, while downtown wards have the shortest.
- Fairness caveat: ACS 2023 medium. Share of workers over 45 minutes, not average time.

## 17. Chicago's 5 most rent-burdened wards
- Metric: `rent_burdened_households_pct` (Rent Burden), direction: lower is better, confidence: medium, wards: 50
- Year: 2023
- Top 5: W18 63.1%, W7 58.5%, W37 58.4%, W15 57.2%, W24 56.3%
- Bottom 3: W32 30.5%, W1 31.8%, W47 33.6%
- Call: https://www.wardwise.org/api/metrics/delta?metric_id=rent_burdened_households_pct&from_year=2023&to_year=2023
- Why it works: Ward 18 at 63% (rent takes 30%+ of income) is a surprise.
- Fairness caveat: ACS 2023 medium. Share of renter households only, so wards with few renters have small samples.

## 18. How far is each ward from the Bean?
- Metric: `bean_distance_miles` (Bean Proximity), direction: lower is better, confidence: unrated, wards: 50
- Year: single snapshot (latest)
- Top 5: W42 0.4 mi, W34 1.2 mi, W2 1.8 mi, W27 2.7 mi, W43 2.9 mi
- Bottom 3: W41 16.3 mi, W10 14.1 mi, W9 13.4 mi
- Call: https://www.wardwise.org/api/metrics/comparison?metrics=bean_distance_miles
- Why it works: Fun and viral map. Ward 41 is 16 miles away.
- Fairness caveat: Confidence unrated. Distance from ward center. Playful, not a quality ranking.

## 19. Chicago's 5 wards with the highest school spending per student
- Metric: `per_pupil_spending` (Per-Pupil Spending), direction: higher is better, confidence: medium, wards: 50
- Year: 2025
- Top 5: W24 $23,663, W21 $23,247, W25 $22,961, W8 $22,597, W28 $22,583
- Bottom 3: W39 $17,135, W47 $17,158, W43 $17,303
- Call: https://www.wardwise.org/api/metrics/delta?metric_id=per_pupil_spending&from_year=2025&to_year=2025
- Why it works: Spending does not follow wealth: Ward 43 and 47 are near the bottom.
- Fairness caveat: Medium confidence. School attendance areas do not line up with ward lines. Includes selective-enrollment effects.

## 20. Chicago's 5 wards getting the least sleep
- Metric: `short_sleep_pct` (Short Sleep), direction: lower is better, confidence: medium, wards: 50
- Year: 2022
- Top 5: W17 47.7%, W16 47.6%, W24 47.6%, W6 47.1%, W20 46.8%
- Bottom 3: W44 29.7%, W43 29.9%, W2 30.1%
- Call: https://www.wardwise.org/api/metrics/delta?metric_id=short_sleep_pct&from_year=2022&to_year=2022
- Why it works: Quirky and relatable. Wards 17, 16, 24 are the weariest.
- Fairness caveat: Modeled CDC estimates (2022, medium), not a survey of each ward. Differences are narrow.

## Alternates (not in the 20)
- open_late_per_10000_residents (2026: Wards 42, 27, 1, 34, 44)
- basement_flooding_complaints_per_10000_residents (volatile: top 5 changes every year, so only as a one-year storm story)
- new_residential_construction_permits_count (2025: only 48 wards, Ward 20 leads with 86)
- nearest_cta_rail_station_miles (farthest: Wards 10, 19, 7)
- nonroutine_bills_sponsored_current_session (Ward 36 leads with 221)
- licensed_coffee_shops_per_10000_residents

## Broken-looking metrics
See `broken_metrics.json` (73 entries) for the full list. Summary:
- All zeros: `c311_repeats_abandoned_vehicle`.
- Fewer than 45 wards (9): licensed_pawnbrokers (31), summer_night_air_temp_c (35), summer_day_sensor_temp_c (33, also low confidence), summer_night_humidity_pct (35), pm25_sensor_annual_ugm3 (32), cta_l_station_entries (36), designated_landmarks_count (43), nrhp_listings_count (41). Also `tif_increment_usd` has 49 and is low confidence.
- Mostly zeros, so a map would be mostly blank (10): museum_count, menu_lighting/parks/cameras/schools_share, participatory_budgeting (2 distinct values), ej_rmp_site_proximity, metrics_submitted_count, colleges_count, trade_schools_count, purpleair_sensors.
- Partial-year latest value (current-year to date, ends 2026-10-13): traffic_crash_injuries_count, pedestrian_cyclist_crashes_count, divvy_rides_count, real_estate_sales_usd, five permit metrics plus demolition permits, building_permit_processing_days, cta_l_station_entries. Use 2025 via /api/metrics/delta?...&from_year=2025&to_year=2025. All c311_* metrics end 2026-09-29, so 2026 is partial.
- Year-volatile (top 5 changes each year): basement/street flooding complaints, pothole days, summer surface temp (top 3 stable). Only state the year on screen.
