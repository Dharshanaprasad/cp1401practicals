# Dictionary of colour names and their hex codes
HEX_COLOURS = {
    "AliceBlue": "#f0f8ff",
    "AntiqueWhite": "#faebd7",
    "Aqua": "#00ffff",
    "Aquamarine": "#7fffd4",
    "Azure": "#f0ffff",
    "Beige": "#f5f5dc",
    "Black": "#000000",
    "BlueViolet": "#8a2be2",
    "Brown": "#a52a2a",
    "CadetBlue": "#5f9ea0"
}

def main():
    # Keep asking the user for colour names until they enter a blank input
    while True:
        colour_name = input("Enter colour name (or press Enter to quit): ").title()
        if colour_name == "":
            break
        # Look  and display the hex code for the colour
        if colour_name in HEX_COLOURS:
            print(f"The hex code for {colour_name} is {HEX_COLOURS[colour_name]}")
        else:
            print("Invalid colour name. Please try again.")

if __name__ == "__main__":
    main()
