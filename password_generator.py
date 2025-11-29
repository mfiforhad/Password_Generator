import random
import string

"""
User Input to choose what kind of password needs

"""
print("choose options to generate password\nOption 1: Low\nOption 2: Medium\nOption 3: Hard")

user_choice = int(input("> "))
password_limit = int(input("Limits: "))

if user_choice == 1:
    low_password = "".join(set(random.choices(
        string.ascii_letters, k=password_limit)))
    print(
        f"Your expected password for Option {user_choice}: Low \nPassword: {low_password}")
elif user_choice == 2:
    medium_password = "".join(set(random.choices(
        (string.ascii_letters + string.digits), k=password_limit)))
    print(
        f"Your expected password for Option {user_choice}: Medium \nPassword: {medium_password}")
elif user_choice == 3:
    hard_password = "".join(set(random.choices(
        (string.ascii_letters + string.digits + string.punctuation), k=password_limit)))
    print(
        f"Your expected password for Option {user_choice}: Hard \nPassword: {hard_password}")
else:
    print("Please choose between 1/2/3")
