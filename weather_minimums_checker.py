print('Welcome to the Go / No-Go Weather Minimums Checker')
ceiling = float(input('Enter the ceiling in feet: '))
visibility = float(input('Enter the visibility in statute miles: '))
crosswind = float(input('Enter the crosswind in knots: '))

if ceiling < 1000 or visibility < 3:
    print('Poor weather condition. Decision: NO-GO')
elif crosswind > 25:
    print('Crosswind winds too high; over the aircraft limitation. Decision: NO-GO')
elif ceiling < 3000:
    print('IFR pilot rating required. CAUTION - IFR CONDITIONS')
else:
    print('VFR CONDITIONS')
