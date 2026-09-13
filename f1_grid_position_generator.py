import random

teams = [
    "Mercedes",
    "Red Bull",
    "Ferrari",
    "McLaren",
    "Alpine",
    "AlphaTauri",
    "Aston Martin",
    "Williams",
]
tyre_compounds = [
    "Hard",
    "Medium",
    "Soft",
    "Extra Soft"
]
grid_position = random.randint(1, 20)

team_selection = random.choice(teams)
tyre_selection = random.choice(tyre_compounds)

driver = input("Welcome to the F1 grid, what is your name? ")

print(
    f"Hello {driver}, you are driving for {team_selection} on {tyre_selection} tyres; starting from grid position {grid_position}.")
