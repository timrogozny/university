def first():
    number = int(input("Enter number:"))
    if number % 3 == 0:
        print("The number is divisible by 3")
    else:
        print("Try again!")
first()

def second():
    try:
        hundred = 100
        number = int(input("Enter number:"))
        print (hundred / number)
    except(ZeroDivisionError):
        print("Division by zero!")
    except(ValueError):
        print("Enter number!")
second()

def third():
    day = int(input("Enter day:"))
    month = int(input("Enter month:"))
    year = int(input("Enter year:"))
    last = year % 100
    dm = day * month
    if last == dm:
        print("Date is magic!")
    else:
        print("Date isnt magic(")
third()



def fourth():
    ticket = input("Enter ticket number:")
    if len(ticket) % 2 == 1:
        print("Enter an odd ticket number!")
    half = len(ticket) // 2
    half1 = ticket[:half]
    half2 = ticket[half:]
    s = sum(map(int, half1))
    s2 = sum(map(int, half2))
    if s == s2:
        print("Your ticket is lucky!!!")
    else:
        print("Sad( Your ticket isnt lucky.")

fourth()
