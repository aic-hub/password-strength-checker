import re

def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters")

    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("❌ Add at least one uppercase letter (A-Z)")

    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("❌ Add at least one lowercase letter (a-z)")

    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9)")

    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        feedback.append("❌ Add at least one special character (!@#$...)")

    if score <= 2:
        strength = "🔴 Weak"
    elif score <= 4:
        strength = "🟡 Medium"
    else:
        strength = "🟢 Strong"

    return strength, feedback


if __name__ == "__main__":
    pwd = input("Enter a password to check: ")
    strength, feedback = check_password_strength(pwd)

    print(f"\nPassword strength: {strength}\n")

    if feedback:
        print("Suggestions:")
        for item in feedback:
            print(item)
    else:
        print("✅ Your password is strong!")
