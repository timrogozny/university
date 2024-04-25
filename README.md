from PIL import Image, ImageFilter, ImageDraw, ImageFont

def previous():
    with Image.open('sun.jpg') as img:
        img.load()
    t = 'ROGOZNY'

    draw = ImageDraw.Draw(img)

    draw.text((500,500),t)
    img.show()



previous()


def first():
    img = Image.open('sun.jpg')
    img.show()
    crop = img.crop((100,200,300,400))
    crop.save('cropped.jpg')
    crop.show()
