from PIL import Image, ImageFilter, ImageDraw

def first():

    img = Image.open('imgnew.jpg')
    img.show()
    print(img.size)
    print(img.format)
    print(img.mode)


def sec():

    with Image.open('imgnew.jpg') as img:
        img.load()

    new_img = img.resize((img.width // 3, img.height // 3))
    new_img = img.rotate(180)
    new_img = img.transpose(Image.FLIP_LEFT_RIGHT)
    new_img.save('resize.jpg')
    new_img.show()



def third():

    with Image.open('1.jpg') as img:
        img.load()
    filt = img.filter(ImageFilter.CONTOUR)
    filt.show()
    filt.save('filted1.jpg')

    with Image.open('2.jpg') as img:
        img.load()
        filt = img.filter(ImageFilter.CONTOUR)
        filt.show()
        filt.save('filted2.jpg')

    with Image.open('3.jpg') as img:
        img.load()
        filt = img.filter(ImageFilter.CONTOUR)
        filt.show()
        filt.save('filted3.jpg')

    with Image.open('4.jpg') as img:
        img.load()
        filt = img.filter(ImageFilter.CONTOUR)
        filt.show()
        filt.save('filted4.jpg')

    with Image.open('5.jpg') as img:
        img.load()
    filt = img.filter(ImageFilter.CONTOUR)
    filt.show()
    filt.save('filted5.jpg')

third()
def previous():
    with Image.open('filted.jpg') as img:
        img.load()
    t = 'ROGOZNY'

    draw = ImageDraw.Draw(img)

    draw.text((200,200),t)
    img.show()




