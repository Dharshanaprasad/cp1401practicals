"""
Test UnreliableCar class
"""
from prac_09.unreliable_car import UnreliableCar

def main():
    """Test the UnreliableCar class."""
    unreliable_car = UnreliableCar("Dodgy", 100, 50)
    for i in range(10):
        print(f"Attempt {i + 1}:")
        distance_driven = unreliable_car.drive(10)
        print(f"Car tried to drive 10km and drove {distance_driven}km.")
        print(unreliable_car)

if __name__ == "__main__":
    main()
