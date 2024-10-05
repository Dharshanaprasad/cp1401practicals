def main():
    """Main function to get and check password, then print stars."""
    password = get_password()
    print_stars(password)


def get_password():
    """Get a valid password of a certain length from the user."""
    password = input("Enter your password: ")
    while len(password) < 8:
        print("Password must be at least 8 characters long.")
        password = input("Enter your password: ")
    return password


def print_stars(password):
    """Print the password as asterisks."""
    print('*' * len(password))


main()
