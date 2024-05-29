import csv

def third():

    items= []
    with open('9lab.csv', newline='', encoding='cp1251' ) as file:
        reader = csv.reader(file)
        co = 0
        for row in reader:
            if len(row) == 3:
                prod = row[0]
                quant = int(row[1])
                price = int(row[3])
                quant = int(quant)
                price = int(price)
                items.append((prod, quant, price))


    print(prod)