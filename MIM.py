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
    if delete_old_files:
        os.remove(to_be_manipulated)
    else:
        raise Exception("Function image_manipulation recieved unexpected value")

def change_format(img, new_image_format, input_image_format):
    new_image = Image.open(img)
    new_image.save(img.replace(input_image_format,  new_image_format.lower()))

# Variables
to_be_manipulated = []
path = input("Please input path to folder: ")
print("For downscaling: 1")
print("For image format conversion: 2")
changes = input("Pick one option: ") #Add functionality so that we can say "or more" at the end.
if changes == "2":
    new_image_format = input("Please enter your new image format: ").upper()
delete_old_files = input("Should I delete the old version of the images(True/False)?: ")
only_specific_format = input("Do you only want to change images with a specific format? (True/False): ")
if only_specific_format:
    input_image_format = input("Which format?: ")
for file in os.listdir(path):
    if only_specific_format:
        if file.endswith(input_image_format):
             to_be_manipulated.append(file)
    else:
        to_be_manipulated.append(file)

for x in range(len(to_be_manipulated)):
    image_manipulation(changes, path + "\\" + to_be_manipulated[x], input_image_format, new_image_format)

input("Finished")
