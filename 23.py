import random

a = ["красный", "синий", "желтый"]
color_1 = random.choice(a)
color_2 = random.choice(a)

print(color_1, color_2)
if (color_1 == "красный" and color_2 == "синий") or (color_2 == "красный" and color_1 == "синий"):
    print("фиолетовый")
elif (color_1 == "красный" and color_2 == "желтый") or (color_2 == "красный" and color_1 == "желтый"):
    print("ораньжевый")
elif (color_1 == "синий" and color_2 == "желтый") or (color_2 == "синий" and color_1 == "желтый"):
    print("зеленый")
else:
    print("Зачем мешал")

