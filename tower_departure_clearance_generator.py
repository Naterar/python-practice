import random

runways = [
    "8L",
    "8R",
    "16L",
    "16R",
    "9",
    "27",
    "12",
    "30",
]
taxi_instructions = [
    "Alpha",
    "Bravo",
    "Charlie",
    "Delta",
]

callsign = input("Welcome to Miami International, what is your callsign? ")

assigned_runway = random.choice(runways)
assigned_taxi_instruction = random.choice(taxi_instructions)

squawk1 = random.randint(0, 7)
squawk2 = random.randint(0, 7)
squawk3 = random.randint(0, 7)
squawk4 = random.randint(0, 7)

print(
    f"{callsign}, Miami clearance, you are cleared to taxi runway {assigned_runway}, via Taxi to holding point {assigned_taxi_instruction}, squawk {squawk1}{squawk2}{squawk3}{squawk4}. Contact Miami ground on 118.9.")
