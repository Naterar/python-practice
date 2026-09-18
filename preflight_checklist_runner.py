def welcome_banner():
    print("Welcome to the Preflight Checklist Runner!")


def preflight_checklist():
    print("Battery: CHECKED")
    print("Tire pressure: CHECKED")
    print("Oil level: CHECKED")
    print("Brake system: CHECKED")
    print("Lights: CHECKED")


def engine_start_checklist():
    print("Ignition: CHECKED")
    print("Fuel level: CHECKED")
    print("Temperature: CHECKED")
    print("Oil pressure: CHECKED")


welcome_banner()

while True:
    command = input("Command (preflight / start / quit): ")

    if command == "preflight":
        preflight_checklist()
    elif command == "start":
        engine_start_checklist()
    elif command == "quit":
        print("Exiting the checklist runner.")
        break
    else:
        print("Invalid command. Please try again.")
