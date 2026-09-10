print("Welcome to the Ready Room Callsign Generator")
pilot_name = input("What's your first name or nickname? ")
aircraft_type = input(
    "What type of aircraft do you fly? (e.g., F-16, F/A-18, A-10, etc.) ")
callsign = pilot_name + " " + aircraft_type

print(f"{pilot_name}, your callsign is {callsign}")
