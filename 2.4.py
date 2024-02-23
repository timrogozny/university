import random

colornumber = ("red","blue","yellow")

color1 = random.choice(colornumber)
color2 = random.choice(colornumber)


print(color1,"+", color2, "=")
if (color1 == "red" and color2 =="blue") or (color1 =="blue" and color2 =="red"):
    print ("violet")
elif (color1 == "blue" and color2 =="yellow") or (color1 =="yellow" and color2 =="blue"):
    print ("green")
elif (color1 == "red" and color2 =="yellow") or (color1 =="yellow" and color2 =="red"):
    print ("orange")
elif (color1 == "yellow" and color2 =="yellow"):
    print ("yellow")
elif (color1 == "blue" and color2 == "blue"):
    print("blue")
elif (color1 == "red" and color2 =="red"):
    print ("red")
else:
    print ("enter ONLY red/blue/yellow colors to mix")