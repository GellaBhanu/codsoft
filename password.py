import secrets
import string
def generate(length):
    ch= string.ascii_letters + string.digits + string.punctuation
    password = [
        secrets.choice(string.ascii_uppercase),  # At least one uppercase letter
        secrets.choice(string.ascii_lowercase),  # At least one lowercase letter
        secrets.choice(string.digits),           # At least one digit
        secrets.choice(string.punctuation)       # At least one symbol
    ]
    for _ in range(length - 4):
        password.append(secrets.choice(ch))
    secrets.SystemRandom().shuffle(password)
    return ''.join(password)
length = int(input("Enter the desired password length: "))
if length < 4:
    print("Password length must be at least 4 for security. Please try again.")
else:
    password = generate(length)
    print("Generated password:", password)
