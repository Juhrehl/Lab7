import random

characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcedfghijklmnopqrstuvwxyz0123456789!@#$%^&*()-=_+,./;'|:<>?"

def password_generator():
    while 1:
        length = int(input("How long would you like your password to be? Enter a length: "))
        count = int(input("How many password would you like? Enter a number: "))
        for i in range(0, count):
            password = ""
            for x in range(0, length):
                password_characters = random.choice(characters)
                password = password + password_characters
            print("Here is your password: ", password)

password_generator()