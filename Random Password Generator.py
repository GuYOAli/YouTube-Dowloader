import string
import random

char = string.ascii_letters + string.digits + "!@#$%^&*()"

while True:

    user_input = int(input("Enter the length of your password: "))
    if user_input == 0:
        break

    lis = []

    for i in range(user_input):
        lis.append(random.choice(char))

    password = ''.join(lis)

    print("Your Password is: {} ".format(password))

    user_answer = input("Do You want to continue ? (Y/N)").upper()

    if user_answer == 'N':
        break
    else:
        continue
