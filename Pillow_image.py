
"""
 Pictures Editing using python and pillow model

 Created by *Abdullah EL-Yamany*


 YouTube Channel = Abdelrahman Gamal - Application on the CS50 course
 Video Link => https://youtu.be/LVlsZdrzJMM
"""

from PIL import Image, ImageFilter


before = Image.open("before.jpeg") # Put an image next to this file with the name (before.jpeg) or change this name in the file according to the name and extension of the image that you put

blur = before.filter(ImageFilter.BoxBlur(8))  # Make a pixel for the picture, make it blurry #
blur.save("after_blur.bmp")

bw = before.convert("L")  # Make the picture black and white #
bw.save("after_b&w.bmp")

box = (120, 230, 330, 400)
crop = before.crop(box)  # Cut the picture #
crop.save("after_crop.bmp")

