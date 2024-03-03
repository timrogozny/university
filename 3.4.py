print("----- Maths for kids -----")

import random

number = ("1","2","3","4","5","6","7","8","9","0",)
n = 2
counter = 0
counter2 = 0

while counter2 <= n:

    number1 = int(random.choice(number))
    number2 = int(random.choice(number))

    print(number1, "+", number2, "=")

    correct = number1 + number2
    answer = int(input("Enter your answer"))
    if answer == correct:
        print("Congrats! You are right!")
        counter += 1
    else:
        print("Sad... You are wrong")
        counter2 += 1

print("Game over. The number of correct answers is", counter, "Game over((((")


