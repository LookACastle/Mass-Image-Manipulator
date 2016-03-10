# -*- coding: utf-8 -*-
import Image
import os

def image_manipulation(changes):
    if changes = 1:
        # Function
    elif changes = 2:
        # Function
    else:
        raise Exception("Program recieved unexpected value")


path = input("Please input path to folder")
print "For downscaling: 1"
print "For image format conversion: 2"
changes = input("Pick one option: ") #Add functionality so that we can say "or more" at the end.

to_be_manipulated = os.listdir(path)
