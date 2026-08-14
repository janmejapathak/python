import random
import string


def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))


def check_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1

    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Medium"
    else:
        return "Strong"


print("=== PASSWORD GENERATOR ===")

length = int(input("Enter password length: "))

password = generate_password(length)

print("\nGenerated Password:", password)
print("Password Strength:", check_strength(password))
