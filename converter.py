import requests

base = input("enter base value code(e.g. EUR):")
out = input("enter base value code(e.g. RUB):")

amount = float(input("enter amount of value:"))

rep = requests.get(f"https://v6.exchangerate-api.com/v6/latest/{base}")
rate = rep.json()["rates"]
targ = rate[out]
converted = amount*targ
print(converted,out)
