import csv
from pathlib import Path
import os
from PIL import Image


def first():

    input = "lab9photos"
    output = "lab9photosoutput"

    for filename in os.listdir(input):
        input_path = os.path.join(input, filename)
        if os.path.isfile(input_path) and filename.lower().endswith((".jpg, .jpeg, .png, .gif")):
            try:
                with Image.open(input_path) as img:
                    img = img.convert("CMYK")
                    output_path = os.path.join(output, filename)
                    img.save(output_path)
                    print(f"Ready {output_path}")
            except Image.UnidentifiedImageError:
                print(f"Unidentified image error: {input_path}")
            except Exception as e:
                print(f"Could not process image {input_path}: {e}")

    print("Your images are converted")



def second():

    input = "lab9photos"
    output = "lab9photosoutput"

    for filename in os.listdir(input):
        input_path = os.path.join(input, filename)
        if os.path.isfile(input_path) and filename.lower().endswith((".jpg, .png")):
            try:
                with Image.open(input_path) as img:
                    img = img.convert("CMYK")
                    output_path = os.path.join(output, filename)
                    img.save(output_path)
                    print(f"Ready {output_path}")
            except Image.UnidentifiedImageError:
                print(f"Unidentified image error: {input_path}")
            except Exception as e:
                print(f"Could not process image {input_path}: {e}")

    print("Your images are converted")




def third():

    result = 0
    print('Нужно купить')
    with open('data.csv') as f:
        file = csv.reader(f)
        for i in file:
            name = i[0]
            count = int([1])
            price = int(i[2])
            result += count * price
            print(f"{name} - {count} шт. за {price} руб.")
        print (f"Итоговая сумма: {result} руб.")

third()
