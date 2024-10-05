def main():
    """Main function to convert between Celsius and Fahrenheit."""
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = convert_celsius_to_fahrenheit(celsius)
    print(f"{celsius}°C is {fahrenheit:.2f}°F")

    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = convert_fahrenheit_to_celsius(fahrenheit)
    print(f"{fahrenheit}°F is {celsius:.2f}°C")


def convert_celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return celsius * 9.0 / 5 + 32


def convert_fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5.0 / 9


main()
