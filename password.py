import string
import random

def generate_password(length, use_uppercase, use_lowercase, use_numbers, use_symbols):
    """Generate a random password based on user input."""
    password_characters = ""
    
    if use_uppercase:
        password_characters += string.ascii_uppercase
    if use_lowercase:
        password_characters += string.ascii_lowercase
    if use_numbers:
        password_characters += string.digits
    if use_symbols:
        password_characters += string.punctuation

    if not password_characters:
        raise ValueError("At least one character type must be selected.")

    password = ''.join(random.choice(password_characters) for _ in range(length))
    
    return password

