import random
import string

def gen():
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    punctuation = string.punctuation

    all_characters = uppercase_letters + lowercase_letters + digits + punctuation

    passlen = int(input("Enter password length: "))
    password = ''.join(random.choice(all_characters) for _ in range(passlen))

    print("Password:", password)

gen()
