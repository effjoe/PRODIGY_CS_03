import re

def check_password_strength(password):
    score = 0
    feedback = []

    # Rule 1: Check length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Rule 2: Check for lowercase letter
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    # Rule 3: Check for uppercase letter
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    # Rule 4: Check for digit
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add at least one number.")

    # Rule 5: Check for special character
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add at least one special character (e.g., @, #, $, etc.).")

    # Determine strength
    if score == 5:
        strength = "Strong 💪"
    elif score >= 3:
        strength = "Medium 🔐"
    else:
        strength = "Weak ❌"

    return strength, feedback


# === Loop the program ===
while True:
    password = input("\nEnter your password (or type 'exit' to quit): ")
    
    if password.lower() == 'exit':
        print("Goodbye!")
        break

    strength, feedback = check_password_strength(password)

    print(f"\nPassword Strength: {strength}")
    if feedback:
        print("Suggestions:")
        for f in feedback:
            print(f" - {f}")