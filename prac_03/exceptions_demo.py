try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    result = numerator / denominator
    print(f"The result is {result}")
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Numerator and denominator must be valid numbers!")

# Answering the questions in comments:
# 1. A ValueError will occur when the input is not an integer.
# 2. A ZeroDivisionError occurs when the denominator is zero.
# 3. Yes, we can avoid the ZeroDivisionError by adding a condition before division.
