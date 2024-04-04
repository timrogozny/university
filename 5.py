import random

def first():
    rnd_numbers = [random.randint(1,10) for _ in range(1,6)]

    number = int(input("Enter number"))
    if number in rnd_numbers:
        print("Congrats! You guessed it!")
    else:
        print("There is no such number in the list.")
    print(rnd_numbers)

first()

def second():
    rnd_numbers = [random.randint(1, 55) for _ in range(1, 21)]
    print(rnd_numbers)
    for item in rnd_numbers:
        if rnd_numbers.count(item) > 1:
            print(item)


second()

def third():
    a =( "Monday", "Tuesday", "Wednesday","Thursday","Friday", "Saturday","Sunday")
    off=int(input("How many days off you want?"))
    print(a[-off:7])
    print(a[1:-off])

third()


def fourth():
    spisok1 = ["rogozny", "rogov", "ben","ronin","dude", "folk","jey"]
    spisok2 = ["fan", "gen", "rex", "flint", "grand", "enfant", "linda"]
    sport = []
    for _ in range(5):
        rnd = random.choice([spisok1,spisok2])
        choose = random.choice(rnd)
        sport.append(choose)
    length =  len(sport)
    sort = sorted(sport)
    print(spisok1,spisok2,sport, length,sort)
    elem = "ivanov"
    if elem in sort:
        print("Ivanov in team")
    else:
        print("Ivanov isnt in team")
    count = sport.count(elem)
    print(count)


fourth()