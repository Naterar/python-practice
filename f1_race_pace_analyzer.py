lap_times = [
    91.824,
    91.835,
    91.964,
    92.013,
    92.019,
    92.149,
    92.294,
    92.316,
    92.903,
    93.041
]

total_stint_time = 0
for lap in lap_times:
    total_stint_time += lap
print(
    f"Kimi Antonelli's total time for the final 10 laps was: {total_stint_time:.3f} seconds")

fastest_lap = float("inf")
for lap in lap_times:
    if lap < fastest_lap:
        fastest_lap = lap
print(
    f"Kimi Antonelli's fastest lap in the final 10-lap stint was: {fastest_lap:.3f} seconds")

average_pace = total_stint_time / len(lap_times)
print(
    f"Kimi Antonelli's average lap pace over the final 10 laps was: {average_pace:.3f} seconds")

laps_below_average = 0
for lap in lap_times:
    if lap < average_pace:
        laps_below_average += 1
print(
    f"Kimi Antonelli set {laps_below_average} laps faster than his average pace in the final stint.")
