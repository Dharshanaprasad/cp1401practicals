# Part 1: Write name to file
name = input("What is your name? ")
with open("name.txt", "w") as file:
    file.write(name)

# Part 2: Read name from file and print greeting
with open("name.txt", "r") as file:
    name = file.read().strip()
    print(f"Hi {name}!")

# Part 3: Add the first two numbers from numbers.txt
with open("numbers.txt", "r") as file:
    num1 = int(file.readline())
    num2 = int(file.readline())
    print(f"The sum of the first two numbers is {num1 + num2}")

# Part 4: Sum all numbers in numbers.txt
total = 0
with open("numbers.txt", "r") as file:
    for line in file:
        total += int(line)
    print(f"The total of all numbers is {total}")
