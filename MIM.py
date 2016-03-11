# -*- coding: utf-8 -*-
from PIL import Image
import os

# Static variables
supported_image_formats = [
"BMP", "EPS", "GIF", "ICNS", "IM", "JPG", "J2K", "MSP", "PCX", "PNG", "PPM", "SPIDER", "TIFF", "WEBP", "XBM", "XPM"
]

read_only_image_formats = [
"CUR", "DCX", "FLI", "FPX", "GBR", "GD", "ICO", "IMT", "IPTC", "NAA", "MCIDAS", "MIC", "MPO", "PCD", "PIXAR", "PSD", "SGI", "TGA", "WAL", "XPM"
]

write_only_image_formats = [
"PALM", "PDF", "XVPICS"
]

#Functions
def image_manipulation(changes, to_be_manipulated, input_image_format, new_image_format):
    #if changes == "1":
        #Function
    if changes == "2":
        if new_image_format not in supported_image_formats and new_image_format not in write_only_image_formats:
            print(new_image_format, "not supported, choose another image format.")
            print("I have support for these image formats: ", supported_image_formats, "And I have write only support for: ", write_only_image_formats)
            image_manipulation(changes, to_be_manipulated)
        else:
            change_format(to_be_manipulated, new_image_format, input_image_format)
    else:
        raise Exception("Program recieved unexpected value")

def change_format(img, new_image_format, input_image_format):
    new_image = Image.open(img)
    new_image.save(img.replace(input_image_format, "." + new_image_format.lower()))

# Variables
path = input("Please input path to folder: ")
print("For downscaling: 1")
print("For image format conversion: 2")
changes = input("Pick one option: ") #Add functionality so that we can say "or more" at the end.
if changes == "2":
    new_image_format = input("Please enter your new image format: ").upper()
to_be_manipulated = []
input_image_format = ".jpg" #Make it an input or something

for file in os.listdir(path):
	if file.endswith(input_image_format):
		to_be_manipulated.append(file)

for x in range(len(to_be_manipulated)):
    image_manipulation(changes, path + "\\" + to_be_manipulated[x], input_image_format, new_image_format)

input("Finished")
