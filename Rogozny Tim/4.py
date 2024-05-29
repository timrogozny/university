import random

colornumber = random.randint(1,3)
if colornumber == 1:
    color = ("red")
elif colornumber == 2:
    color = ("blue")
else:
    color = ("yellow")

color1 = random.choice(colornumber)
color2 = random.choice(colornumber)

print(color1, color2)
if (color1 == 1 and color2 ==2):
    print("violet")



else
    print ("enter ONLY this colors to mix")
