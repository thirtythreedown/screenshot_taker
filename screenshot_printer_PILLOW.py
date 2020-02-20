#! python3

##PILLOW library - https://pypi.org/project/Pillow/

import os
##importing os module (sending to printer)

import keyboard
##Importing keyboard module (detecting keypresses)

import time
#Importing time module (filename generation)

from PIL import Image
##Importing the Image module from the PILLOW library

from PIL import ImageGrab
##Importing the ImagGrab module from the PILLOW library

print("Welcome to the Automatic Screen Capturator 3000")
print("Push CTRL+S anytime to capture the screen")
print("Push Q anytime to quit")

def file_saver(screenshot):
    """Saves file after cropped"""
    timestr = time.strftime("%Y%m%d-%H%M%S")
    ##Composing timestring and assigning to timestr variable
    ##print("The timestring is " + timestr)
    ##DIAGNOSTIC TOOL - Checking timestring content, will be used as filename ingredient later
    filename = 'csc' + timestr + '.bmp'
    ##Creating filename variable and assembling filename elements
    screenshot.save(filename, format='bmp')
    ##Saving cropped_screenshot to folder with save() method using filename
    print("Screenshot saved at " + filename + " !")
    ##Confirming saved file
    saved_screenshot_local = filename
    return saved_screenshot_local
    ##Returning saved_screenshot_local

def screenshot_printer(saved_screenshot):
    """Sends the screenshot to the default printer"""
    os.system("start " + saved_screenshot)
    ##Loading the saved screenshot in the default Photos app
    print("Screenshot ready to send to printer !")

while True:
##Starting main loop
    if keyboard.is_pressed('ctrl+s'):
    ##If detection: CTRL+S key pres
        screenshot = ImageGrab.grab(bbox=(0,0,1600,900)) #Dimensions for Bee's dev laptop
        ##screenshot.show()
        ##DIAGNOSTIC TOOL - Display screenshot
        screenshot_width, screenshot_height = screenshot.size
        ##Getting dimensions from screenshot
        print("Grabbing dimensions from screenshot")
        #Collecting dimensions from screenshot content
        ##print(screenshot_width, screenshot_height)
        ##Printing the dimensions obtained from screenshot just for kicks
        saved_screenshot = file_saver(screenshot)
        ##Passing cropped_screenshot to file_saver() function for saving
        screenshot_printer(saved_screenshot)
        ##Passing saved_screenshot to screenshot_printer() for printing
        ##print("Ready to take the next screenshot!")
        ##DIAGNOSTIC TOOL - Confirming ready to print
    elif keyboard.is_pressed('q'):
        print("Hope everything worked out. See you later!")
        break
