# for this program open new terminal and add path to this folder or it will be complicated

# to run cd to 1_image-processing folder then type : python jpg_to_png.py pokedex gg
# gg is new folder where converted file will be stored

from PIL import Image
import sys
import os

# greab first and second argument
first = sys.argv[1]
second = sys.argv[2]

# check if new exist, if not create
if not os.path.exists(second):
    os.makedirs(second)

# lopp through pokedex
for filename in os.listdir(first):
    if filename.endswith(".jpg"):
        # convert images to png
        im1 = Image.open(f'{first}/{filename}')
        # save them to new folder
        # temp = filename.split('.')
        # or
        # split name and extension like '.jpg'
        clean_name = os.path.splitext(filename)[0]
        # print(clean_name)
        im1.save(f'{second}/{clean_name}.png', 'png')
        print('all done!')
