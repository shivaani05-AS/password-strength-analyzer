
import re
import getpass

COMMON_PASSWORDS = {
    "password", "password123", "12345678",
    "qwerty123", "admin123", "letmein"
}


def analyze_password(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters.")

    if len(password) >= 12:
        score += 1
    else:
        feedback.append("Consider using 12 or more characters.")

    if re.search(r"[a-z]", password) and re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Use a mix of uppercase and lowercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Consider including a number.")

    if re.search(r"[^A-Za-z0-9]", password):
        score += 1
    else:
        feedback.append("Consider including a special character.")

    if password.lower() in COMMON_PASSWORDS:
        return "Very Weak", ["Avoid common or easily guessed passwords."]

    if score <= 2:
        strength = "Weak"
    elif score <= 3:
        strength = "Moderate"
    elif score == 4:
        strength = "Strong"
    else:
        strength = "Very Strong"

    return strength, feedback


def main():
    print("=== Password Strength Analyzer ===")
    print("Your password is checked locally; it is not transmitted.")
    password = getpass.getpass("Enter a sample password: ")

    if not password:
        print("Please enter a password to analyze.")
        return

    strength, feedback = analyze_password(password)

    print("\nPassword Strength:", strength)

    if feedback:
        print("\nSuggestions:")
        for item in feedback:
            print("-", item)
    else:
        print("Good character variety and length!")

    print("\nNote: This is a basic educational checker,")
    print("not a guarantee of password security.")


if __name__ == "__main__":
    main()
