def main():
    """Main menu program for handling score-related tasks."""
    score = get_valid_score()
    while True:
        print("(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit")
        choice = input("Choose an option: ").upper()

        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print(f"Your result is: {determine_score_result(score)}")
        elif choice == "S":
            print('*' * int(score))
        elif choice == "Q":
            print("Farewell!")
            break
        else:
            print("Invalid choice. Please try again.")


def get_valid_score():
    """Get a valid score from the user (0-100 inclusive)."""
    score = float(input("Enter a valid score (0-100): "))
    while score < 0 or score > 100:
        print("Invalid score. Must be between 0 and 100.")
        score = float(input("Enter a valid score: "))
    return score


def determine_score_result(score):
    """Determine the result for a given score."""
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
