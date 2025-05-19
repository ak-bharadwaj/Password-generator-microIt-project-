import random
import string

def generate_password(length=12, use_uppercase=True, use_lowercase=True, use_numbers=True, use_special=True):
    characters = ""
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_numbers:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if not characters:
        return "Error: Please select at least one character type."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Example usage
if __name__ == "__main__":
    print("Password Generator")
    length = int(input("Enter password length: "))
    upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
    lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
    nums = input("Include numbers? (y/n): ").lower() == 'y'
    special = input("Include special characters? (y/n): ").lower() == 'y'

    password = generate_password(length, upper, lower, nums, special)
    print("Generated Password:", password)