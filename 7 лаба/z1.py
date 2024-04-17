def z1():
    from PIL import Image
    img = Image.open(r'Z:\more.jpg')
    img.show()
    print(img.size)
    print(img.format)
    print(img.mode)
z1()

def z2():
    from PIL import Image
    img = Image.open(r'Z:more.jpg')
    img1 = img.reduce(3)
    img2 = img.transpose(Image.FLIP_LEFT_RIGHT)
    img3 = img.transpose(Image.FLIP_TOP_BOTTOM)
    img1.save(r'Z:umenmore.jpg')
    img2.save(r'Z:gormore.jpg')
    img3.save(r'Z:vertmore.jpg')
z2()

def z3():
    from PIL import Image, ImageFilter
    images = [r'Z:1v.jpg', r'Z:2v.jpg', r'Z:3v.jpg', r'Z:4v.jpg', r'Z:5v.jpg']
    for img in images:
        image = Image.open(img)
        imgcont = image.filter(ImageFilter.CONTOUR)
        imgcont.save(r'Z:1viz.jpg')
        imgcont.save(r'Z:2viz.jpg')
        imgcont.save(r'Z:3viz.jpg')
        imgcont.save(r'Z:4viz.jpg')
        imgcont.save(r'Z:5viz.jpg')
z3()