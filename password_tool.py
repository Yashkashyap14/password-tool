"""Password Generator and Strength Checker

A simple beginner Python project.
- Generates a strong random password
- Checks how strong any password is
Only built-in Python modules are used, so nothing needs to be installed.
"""

import secrets
import string


def generate_password(length=12):
    """Create a random password with letters, digits and symbols."""
    characters = string.ascii_letters + string.digits + "!@#$%&*?"
    return "".join(secrets.choice(characters) for _ in range(length))


def check_strength(password):
    """Give a score out of 5 and a list of tips to improve the password."""
    score = 0
    tips = []

    if len(password) >= 8:
        score += 1
    else:
        tips.append("Use at least 8 characters")

    if len(password) >= 12:
        score += 1
    else:
        tips.append("12 or more characters is even better")

    if any(c.islower() for c in password) and any(c.isupper() for c in password):
        score += 1
    else:
        tips.append("Mix uppercase and lowercase letters")

    if any(c.isdigit() for c in password):
        score += 1
    else:
        tips.append("Add at least one number")

    if any(c in string.punctuation for c in password):
        score += 1
    else:
        tips.append("Add a symbol like @ # $ !")

    return score, tips


def get_label(score):
    """Turn a score into a simple word."""
    if score <= 2:
        return "WEAK"
    if score <= 4:
        return "MEDIUM"
    return "STRONG"


def menu():
    print("\n=== Password Tool ===")
    print("1. Generate a password")
    print("2. Check password strength")
    print("3. Exit")


def main():
    while True:
        menu()
        choice = input("Choose 1, 2 or 3: ").strip()

        if choice == "1":
            text = input("Password length (default 12): ").strip()
            length = int(text) if text.isdigit() and int(text) >= 4 else 12
            print("Your password:", generate_password(length))

        elif choice == "2":
            password = input("Enter a password to check: ")
            score, tips = check_strength(password)
            print(f"Strength: {get_label(score)} ({score}/5)")
            for tip in tips:
                print(" - Tip:", tip)

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
