import random

def generate_password(length, complexity):
    password = ""
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '1234567890'
    symbols = '@#$%^&*()<>[]{}+_-!,'
    easy_choice = lower + numbers
    chars = lower + upper + numbers + symbols

    if complexity == "easy":
        for a in range(length):
            password += random.choice(easy_choice)
    else:
        for a in range(length):
            password += random.choice(chars)

    return password

while True:
    length = int(input("Enter length for your password: "))
    complexity = input("Enter your choice for complexity (easy/complex): ")

    password = generate_password(length, complexity)
    print("The Generated password is:", password)

    regenerate = input("Do you want to regenerate the password? (yes/no): ")
    if regenerate.lower() != "yes":
        break
