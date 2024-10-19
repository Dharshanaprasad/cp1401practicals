def main():
    email_to_name = {}
    email = input("Email: ")

    while email != "":
        name = get_name_from_email(email)
        is_correct = input(f"Is your name {name}? (Y/n) ").lower()

        if is_correct != "y" and is_correct != "":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")

    for email, name in email_to_name.items():
        print(f"{name} ({email})")

def get_name_from_email(email):
    name = email.split('@')[0]
    parts = name.split('.')
    return " ".join(parts).title()

if __name__ == "__main__":
    main()
