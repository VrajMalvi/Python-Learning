# here we have installed package named 'pillow'
# link : https://pillow.readthedocs.io/en/stable/installation.html
# pypi link : https://pypi.org/project/Pillow/
# wiki link : https://en.wikipedia.org/wiki/Python_Imaging_Library


# search proper package and the one most people use, find about package more in wikipedia


from PIL import Image, ImageFilter

# img = Image.open(
#     '17_Scripting-with-python/1_image-processing/pokedex/#pikachu.jpg')


# filtered_img = img.filter(ImageFilter.BLUR)  # blur the image a lil
# shart the image there is also command like smooth
# filtered_img = img.filter(ImageFilter.SHARPEN)


# we can also convert img into different form like gray with 'L'
# filtered_img = img.convert('L')
# creats gray pickachu

# here we save it to as png because png supports all this img filters it might give error if we use jpg/jpeg


# crooked = filtered_img.rotate(90)
# # as name suggests rotation 90 to left
# crooked.save(
#     '17_Scripting-with-python/1_image-processing/test.png', 'png')


# filtered_img.save(
#     '17_Scripting-with-python/1_image-processing/test.png', 'png')


# resize the image - resize accept tuple
# resize = filtered_img.resize((300, 300))
# resize.save(
#     '17_Scripting-with-python/1_image-processing/test.png', 'png')


# filtered_img.show()  #open image in image viewer


# to crop image
# box = (100, 100, 400, 400)
# # pixal of four corner
# region = filtered_img.crop(box)
# region.save('17_Scripting-with-python/1_image-processing/test.png', 'png')

# print(img)
# print(img.format)
# print(img.size)
# print(img.mode)


# ---------------------------------------------------------------------------------------------------
# size of img is 3.6MB
img = Image.open(
    '17_Scripting-with-python/1_image-processing/pokedex/astro.jpg')
# here size is not same so when resize to same value it compresses and change its aspact ratio
# print(img.size)
# new_img = img.resize((400, 200))


# we can avoid chaage in aspact ratio using thumbnail
# this method doesnt return anything and try to keep the aspact ration and do not resize to exact value
img.thumbnail((400, 200))

img.save('17_Scripting-with-python/1_image-processing/try.jpg')
print(img.size)  # as you can see size is not the exact what we gave

# new_img.save('17_Scripting-with-python/1_image-processing/try.jpg')
