track_temp = float(input('Track temperature in °F: '))
laps_remaining = float(input('Lap remaining: '))
tyre_age = float(input('Current tyre age in laps: '))

if tyre_age > 25:
    print('BOX BOX BOX.')
elif track_temp > 145 and tyre_age > 18:
    print('Box now, new strategy; we are taking mediums.')
elif 10 < laps_remaining < 20:
    print('Consider a short stint on softs.')
else:
    print('Stay out is Hammer Time!')
