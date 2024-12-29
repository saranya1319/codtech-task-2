import re


def password_strength(password):
    """
    Function to evaluate the strength of a given password based on length,
    presence of uppercase letters, lowercase letters, digits, special characters, and uniqueness.
    """
    # Criteria for password evaluation
    length_criteria = len(password) >= 8  # At least 8 characters
    has_uppercase = any(char.isupper() for char in password)  # Contains uppercase
    has_lowercase = any(char.islower() for char in password)  # Contains lowercase
    has_digit = any(char.isdigit() for char in password)  # Contains digits
    has_special = bool(re.search(r"[@$!%*?&#]", password))  # Contains at least one special character
    is_unique = len(set(password)) > len(password) // 2  # Uniqueness (more than half the characters are unique)

    # Strength feedback
    strength_score = sum([length_criteria, has_uppercase, has_lowercase, has_digit, has_special, is_unique])
    feedback = []

    if not length_criteria:
        feedback.append("Password should be at least 8 characters long.")
    if not has_uppercase:
        feedback.append("Password should include at least one uppercase letter.")
    if not has_lowercase:
        feedback.append("Password should include at least one lowercase letter.")
    if not has_digit:
        feedback.append("Password should include at least one digit.")
    if not has_special:
        feedback.append("Password should include at least one special character (@, $, !, %, *, ?, & or #).")
    if not is_unique:
        feedback.append("Password should contain a large variety of unique characters.")

    # Final result
    if strength_score == 6:
        strength = "Strong"
    elif 4 <= strength_score < 6:
        strength = "Moderate"
    else:
        strength = "Weak"

    return strength, feedback


# Test the function
if __name__ == "__main__":
    print("Welcome to the Password Strength Checker!")
    user_password = input("Enter a password to check its strength: ")
    strength, suggestions = password_strength(user_password)
    print(f"\nPassword Strength: {strength}")
    if suggestions:
        print("Suggestions to improve your password:")
        for tip in suggestions:
            print(f"- {tip}")
