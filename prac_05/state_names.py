STATE_NAMES = {
    "QLD": "Queensland",
    "NSW": "New South Wales",
    "NT": "Northern Territory",
    "WA": "Western Australia",
    "SA": "South Australia",
    "VIC": "Victoria",
    "TAS": "Tasmania"
}


def main():
    state = input("Enter short state (e.g., QLD, NSW): ").upper()

    if state in STATE_NAMES:
        print(f"{state} is {STATE_NAMES[state]}")
    else:
        print("Invalid short state. Please try again.")

    # Print all states and their full names
    print("\nAll states and their full names:")
    for abbreviation, name in STATE_NAMES.items():
        print(f"{abbreviation:3} is {name}")
