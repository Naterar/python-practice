lap_remaining = float(
    input("Enter the number of laps remaining in the race: "))
fuel_burn_per_lap = float(input("Enter fuel burn per lap in gallons: "))
current_fuel_in_the_car = float(
    input("Enter current fuel in the car in gallons: "))
fuel_needed = (
    fuel_burn_per_lap * lap_remaining) - current_fuel_in_the_car
print(f"Fuel needed to finish the race: {fuel_needed} gallons")
