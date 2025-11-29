import random
import secrets
import string

print("choose an option to generate password")
print("Press 1 : Low")
print("Press 2 : Medium")
print("Press 3 : Hard")

user_choice = input("Choose: ")

if user_choice not in ("1", "2", "3"):
    print("Please enter a number between 1/2/3")
    exit()

password_limit = input("Limits: ")

if not password_limit.isdigit():
    print("Please enter a number")
    exit()

password_limit = int(password_limit)

if user_choice == "1":
    charecter = string.ascii_letters
elif user_choice == "2":
    charecter = string.ascii_letters + string.digits
elif user_choice == "3":
    charecter = string.ascii_letters + string.digits + string.punctuation

password = "".join(secrets.choice(charecter) for _ in range(password_limit))  # generator expression

print("Your Password:")
print(password)