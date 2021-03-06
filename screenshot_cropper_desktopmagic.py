#! python3

##PILLOW library - https://pypi.org/project/Pillow/
##DesktopMagic library - https://pypi.org/project/Desktopmagic/

import os
##importing os module (sending to printer)

import keyboard
##Importing keyboard module (detecting keypresses)

import time
#Importing time module (filename generation)

from PIL import Image
##Importing the Image module from the PILLOW library

from desktopmagic.screengrab_win32 import getRectAsImage
##Importing DesktopMagic module's getRectAsTimage

print("Welcome to the Automatic Screen Capturator 3000")
print("Push CTRL+S anytime to capture the screen")
print("Push Q anytime to quit")

def screenshot_cropper(screenshot, screenshot_width, screenshot_height):
    """Crops the screenshot down to printing size"""
    left = (screenshot_width-1000)/2
    ##Defining position of leftmost pixel
    top = (screenshot_height-750)/2
    ##Defining position of topmost pixel
    right = screenshot_width-((screenshot_width-1000)/2)
    ##Defining position of rightmost pixel
    bottom = screenshot_height-((screenshot_height-750)/2)
    ##Defining position of bottom pixels
    cropped_screenshot_local = screenshot.crop((left, top, right, bottom))
    ##Cropping screenshot
    ##cropped_screenshot_local.show()
    ##DIAGNOSTIC TOOL - Displays the cropped screenshot
    print("Screenshot cropped!")
    ##Confirming cropping
    return cropped_screenshot_local

def file_saver(cropped_screenshot):
    """Saves file after cropped"""
    timestr = time.strftime("%Y%m%d-%H%M%S")
    ##Composing timestring and assigning to timestr variable
    ##print("The timestring is " + timestr)
    ##DIAGNOSTIC TOOL - Checking timestring content, will be used as filename ingredient later
    filename = 'csc' + timestr + '.bmp'
    ##Creating filename variable and assembling filename elements
    cropped_screenshot.save(filename, format='bmp')
    ##Saving cropped_screenshot to folder with save() method using filename
    print("Screenshot saved at " + filename + " !")
    ##screenshot.show(filename) #Shows the screenshot, but uncropped
    ##Confirming saved file
    saved_screenshot_local = filename
    ##screenshot.show(saved_screenshot_local) #Shows a screenshot, uncropped
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
    ##If detection: CTRL+S key press
        screenshot = getRectAsImage((1920,0,3840,1080))
        ##Using getRectAsImage to capture the right-hand screen on a dual screen setup at 1920x1080
        ##screenshot.show()
        ##DIAGNOSTIC TOOL - Display screenshot
        screenshot_width, screenshot_height = screenshot.size ##Getting dimensions
        print("Grabbing dimensions from screenshot") #Collecting dimensions from raw_screenshot content
        print(screenshot_width, screenshot_height) #Printing the dimensions obtained from raw_screenshot just for kicks
        cropped_screenshot = screenshot_cropper(screenshot, screenshot_width, screenshot_height)
        ##Passing raw_screenshot to screenshot_cropper() function for cropping
        saved_screenshot = file_saver(cropped_screenshot)
        ##Passing cropped_screenshot to file_saver() function for saving
        screenshot_printer(saved_screenshot)
        ##Passing saved_screenshot to screenshot_printer() for printing
        ##print("Ready to take the next screenshot!")
        ##DIAGNOSTIC TOOL - Confirming ready to print
    elif keyboard.is_pressed('q'):
    ##If detection - Q press
        print("Hope everything worked out. See you later!")
        ##Goodbye message
        break
        ##Exit program
