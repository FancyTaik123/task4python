from random import randint

random_number = randint(1,10)

user_input = int(input("Enter a random number from 1 - 10: "))

if (user_input) and (user_input == random_number):
    print(f"{user_input} is the correct number!")
else:
    print(f"{user_input} is not the number! The number was {random_number}!")