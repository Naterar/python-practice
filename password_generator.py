import random
import string

lowercase_letters = list(string.ascii_lowercase)
uppercase_letters = list(string.ascii_uppercase)
numbers = list(string.digits)
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_lowercase = int(input("How many lowercase letters would you like?\n"))
nr_uppercase = int(input("How many uppercase letters would you like?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

password_list = []

for _ in range(nr_lowercase):
    password_list.append(random.choice(lowercase_letters))

for _ in range(nr_uppercase):
    password_list.append(random.choice(uppercase_letters))

for _ in range(nr_symbols):
    password_list.append(random.choice(symbols))

for _ in range(nr_numbers):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)
password = "".join(password_list)

print(f"Your password is: {password}")
