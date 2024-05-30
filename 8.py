from PIL import Image, ImageDraw

def first():
    img = Image.open('filted.jpg')
    img.show()
    crop = img.crop((100,200,300,400))
    crop.save('cropped.jpg')
    crop.show()


def second():

    a = {
    "1" : "filted.jpg",
    "2" : "filted1.jpg",
    "3": "filted2.jpg",
    }

    req = input("Enter celebration")



    if req in a:
        c = a[req]
        img = Image.open(c)
        img.show()
    else:
        print("Celebration was not found")




def third():


    a = {
    "1" : "filted.jpg",
    "2" : "filted1.jpg",
    "3": "filted2.jpg",
    }

    req = input("Enter celebration")
    name = str(input("Enter name"))
    tex= name+ ", celebrate!"

    if req in a:
        c = a[req]
        img = Image.open(c)
        draw = ImageDraw.Draw(img)
        draw.text((300,200),tex)
        img.show()
    else:
        print("Celebration was not found")



third()