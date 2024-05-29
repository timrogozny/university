import csv


def z1():
    with open("data.csv") as f:
        t_readed = csv.reader(f, delimiter = ",")

        c = 0
        print("Нужно купить")

        for row in t_readed:
            print(f'{row[0]} - {row[1]} шт. за {row[2]} руб.')
            c += 1
            print(c)


z1()