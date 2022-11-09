# name = input("Enter your name")
# age = int(input("Enter your age "))
# print("Hello,",name, age)

# a = "Hello,"
# b = "world"
# с = a + b
# print(с)
#
# concat

# #cписок
# a = ["2", "hello", "45", "bye"]
# print(a)
# b = "*".join(a)
# print(b)

import random
import time
a = "abcdefghijklmnopqrstuvwxyz"
b = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
с = "0123456789"
d = "{}[]*/,!?"

all = a + b + с + d
# length = int(input("Enter expected password length"))
while True:
    try:
        length = int(input("Enter expected password length: "))
        if length <5:
            print("We recommend to choose from 5 to 12 symbols")
            time.sleep(1)
            continue
        elif length >15:
            print("It`s too long password, we recommend the length about 12 symbols")
            time.sleep(1)
            continue
        else:
            password = "".join(random.sample(all, length))
            print("Generation is going...")
            time.sleep(2)
            print("Your password is ready")
            print(password)
            break
    except ValueError:
        print("Please enter the integer")
        continue