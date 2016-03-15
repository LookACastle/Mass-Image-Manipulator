# -*- coding: utf-8 -*-
from PIL import Image
import os
import re

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
def image_manipulation(changes, to_be_manipulated, input_image_format, new_image_format, jpg_quality, jpg_subsampling):
    #if changes == "1":
        #Function

    if changes == "2":
        if new_image_format not in supported_image_formats and new_image_format not in write_only_image_formats:
            print(new_image_format, "not supported, choose another image format.")
            print("I have support for these image formats: ", supported_image_formats, "And I have write only support for: ", write_only_image_formats)
            image_manipulation(changes, to_be_manipulated)
        else:
            change_format(to_be_manipulated, new_image_format, input_image_format, jpg_quality, jpg_subsampling)
    else:
        raise Exception("Function image_manipulation recieved unexpected value")

    if delete_old_files:
        os.remove(to_be_manipulated)

def change_format(img, new_image_format, input_image_format, jpg_quality, jpg_subsampling):
    new_image = Image.open(img)
    file_name, file_extension = re.split('\.', img)
    if new_image_format == "JPG" and advanced_jpg == True:
        new_image.save(img.replace( "." + file_extension, "_MIM." + new_image_format.lower()), quality = jpg_quality, subsampling = jpg_subsampling)
    else:
        new_image.save(img.replace("." + file_extension, "_MIM." + new_image_format.lower()))

def string_true(string):
    if string == "True" or string == "true":
        string = True
    elif string == "False" or string == "false":
        string = False
    else:
        raise Exception("string_true recieved a string that isn't false or true.")
    return string

def _only_specific_format(supported_image_formats, read_only_image_formats):
    input_image_format = input("Which format?: ").upper()
    if input_image_format == None:
        input_image_format = read_only_image_formats, supported_image_formats
    if input_image_format not in supported_image_formats and input_image_format not in read_only_image_formats:
        print(input_image_format, "not supported, choose another image format.")
        print("I have support for these image formats: ", supported_image_formats, "And I have write only support for: ", read_only_image_formats)
        _only_specific_format(supported_image_formats, read_only_image_formats)
    else:
        return input_image_format

# Variables
to_be_manipulated = []
input_image_format = None
path = input("Please input path to folder: ")
print("For downscaling: 1")
print("For image format conversion: 2")
changes = input("Pick one option: ") #Add functionality so that we can say "or more" at the end.
jpg_quality = None
jpg_subsampling = None

if changes == "2":
    new_image_format = input("Please enter your new image format: ").upper()

delete_old_files = string_true(input("Should I delete the old version of the images(True/False)?: "))
only_specific_format = string_true(input("Do you only want to change images with a specific format? (True/False): "))

if only_specific_format:
    input_image_format = _only_specific_format(supported_image_formats, read_only_image_formats)

if new_image_format == "JPG" and changes == "2":
    advanced_jpg = string_true(input("Do you want advanced jpg control?(True/False): "))
    if advanced_jpg:
        jpg_quality = int(input("How high quality should the jpgs be?(0-100): "))
        jpg_subsampling = int(input("Which subsampling should the jpgs use?(0: equivalent to 4:4:4, 1: equivalent to 4:2:2, 2: equivalent to 4:1:1): "))
    else:
        jpg_quality = 75
        jpg_subsampling = 1

for file in os.listdir(path):
    if only_specific_format:
        if file.endswith(input_image_format.upper()) or file.endswith(input_image_format.lower()):
             to_be_manipulated.append(file)
    else:
        for string in supported_image_formats:
            if file.endswith(string.upper()) or file.endswith(string.lower()):
                to_be_manipulated.append(file)

# Not variables anymore (find a better name)
for x in range(len(to_be_manipulated)):
    image_manipulation(changes, path + "\\" + to_be_manipulated[x], input_image_format, new_image_format, jpg_quality, jpg_subsampling)

input("Finished")



# Counter for ammount of times LookACastle thought changes was an integer: 3
# Still not sure why we don't make changes an integer though...
