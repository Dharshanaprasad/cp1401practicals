import random


def main():
    """Main function to check the score and print result."""
    score = float(input("Enter your score: "))
    result = determine_score_result(score)
    print(f"Your score is {score}, which is {result}")

    # Random score generation
    random_score = random.randint(0, 100)
    result = determine_score_result(random_score)
    print(f"Random score: {random_score} - {result}")


def determine_score_result(score):
    """Determine the result for a given score."""
    if score < 0 or score > 100:
        return "Invalid"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
