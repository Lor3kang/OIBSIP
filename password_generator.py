import random
import string

def generate_password(length, include_letters=True, include_numbers=True, include_symbols=True):
    """
    Generate a random password based on user-defined criteria.
    """
    characters = ''
    if include_letters:
        characters += string.ascii_letters
    if include_numbers:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    if not characters:
        print("Error: At least one character type (letters, numbers, symbols) must be included.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Random Password Generator")
    length = int(input("Enter password length: "))
    include_letters = input("Include letters? (y/n): ").lower() == 'y'
    include_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    include_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    password = generate_password(length, include_letters, include_numbers, include_symbols)
    if password:
        print("Generated Password:", password)

if __name__ == "__main__":
    main()
