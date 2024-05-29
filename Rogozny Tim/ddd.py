import csv

cnt=0
with open('9lab.csv', newline='', encoding='cp1251') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        product, k, price = row
        k = int(k)
        price = int(price)
        cnt += k * price
        print(product,"-",k," шт. за", price," руб.")

print("Итоговая сумма: ",cnt,"руб." )