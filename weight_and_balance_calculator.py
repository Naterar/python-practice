aircraft_weight = float(input("Enter aircraft weight in pounds: "))
fuel_quantity = float(input("Enter fuel quantity in gallons: "))
passenger_weight = float(input("Enter passenger weight in pounds: "))
cargo_weight = float(input("Enter cargo weight in pounds: "))

onboard_fuel = fuel_quantity * 6.8
ramp_weight = aircraft_weight + onboard_fuel + passenger_weight + cargo_weight

print(
    f"Total ramp weight: {ramp_weight} pounds")
