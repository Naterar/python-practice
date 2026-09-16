flight_hours = [2.4, 1.7, 3.1, 4.1, 5.5, 3.6, 8.3, 13.5]

total_flight_hours = 0
for hours in flight_hours:
    total_flight_hours += hours
print(f"Total flight hours this week: {total_flight_hours}")

longest_flight = 0
for hours in flight_hours:
    if hours > longest_flight:
        longest_flight = hours
print(f"Longest flight this week: {longest_flight}")

avg_flight_hours = total_flight_hours / len(flight_hours)
print(f"Average flight hours this week: {avg_flight_hours}")

total_long_flights = 0
for hours in flight_hours:
    if hours >= 2:
        total_long_flights += 1
print(f"Total long flights (over 2 hours) this week: {total_long_flights}")
