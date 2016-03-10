# -*- coding: utf-8 -*-
import Image
import os

# Static variables
supported_image_formats = [
"BMP", "DIB", "DCX", "EPS", "PS", "GIF", "IM", "JPG", "JPE", "JPEG", "PCD", "PCX", "PDF", "PNG", "PBM", "PBM", "PGM", "PPM", "PSD", "TIF", "TIFF", "XBM", "XPM"
]

#Functions
def image_manipulation(changes):
    #if changes == 1:
        #Function
    if changes == 2:
        new_image_format = input("Please enter your new image format: ").upper.replace(".", None)
        if new_image_format not in supported_image_formats:
            print "%s not supported, choose another image format." % (new_image_format)
            image_manipulation(changes)
        else:
            change_format(img, new_image_format)
    else:
        raise Exception("Program recieved unexpected value")

def change_format(img, new_image_format):
    new_image = Image.open("img")
    new_image.save("img", ".", "new_image_format".lower)

# Variables
path = raw_input("Please input path to folder: ")
print "For downscaling: 1"
print "For image format conversion: 2"
changes = input("Pick one option: ") #Add functionality so that we can say "or more" at the end.
to_be_manipulated = []

for file in os.listdir(path):
	if file.endswith(".txt"): #NOTE NOTE NOTE NOTE NOTE Change .txt to a variable someday NOTE NOTE NOTE NOTE NOTE
		to_be_manipulated.append(file)
print to_be_manipulated

input("Finished")
