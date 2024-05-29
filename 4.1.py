def first():
    number = int(input("enter number"))
    if number % 3 == 0:
        print("The number is divisible by 3")
    else:
        print("Try again!")
first()

def second():
    try:
        hundred = 100
        number = int(input("enter number"))
        print (hundred / number)
    except(ZeroDivisionError):
        print("division by zero!")
second()

