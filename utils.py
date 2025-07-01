import random
import string

def generate_password(difficulty="medium"):
    length = {"easy": 6, "medium": 8, "hard": 10}[difficulty]
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(chars, k=length))
    return password

def generate_hint(password):
    hints = [
        f"Length: {len(password)}",
        f"First character: {password[0]}",
        f"Last character: {password[-1]}",
        f"Contains digits: {'Yes' if any(c.isdigit() for c in password) else 'No'}",
        f"Contains symbols: {'Yes' if any(c in string.punctuation for c in password) else 'No'}"
    ]
    return random.sample(hints, 3)