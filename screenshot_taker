##Screenshots with PILLOW library - https://www.simplifiedpython.net/python-screenshot/#Taking_Screenshot_UsingPillow
##Filenames with date and time - https://stackoverflow.com/questions/10607688/how-to-create-a-file-name-with-the-current-date-time-in-python
##Keyboard presses in python outside of focused window - https://stackoverflow.com/questions/24072790/detect-key-press-in-python
##PILLOW documentation - https://pillow.readthedocs.io/en/3.1.x/reference/Image.html

##DONE
##Key press detection
##Filename based on time of recording
##Printer output
##Picture cropping
##General refactoring to functions
##Testing with Alienware laptop + TV output
##while True + clean exit loops
##Load files with Photos app

##TO DO
##All dooooooone

import os
##importing os module (sending to printer)

import keyboard
##Importing keyboard module (detecting keypresses)

import time
#Importing time module (filename generation)


from PIL import Image
from PIL import ImageGrab ##Trying something out here
##Importing the ImagGrab module from the PIL pillow library

##timestring = time.strftime("%Y%m%d-%H%M%S") 
##Creating timestring value and using .strftime() method from time to generate time value string

print("Welcome to the Automatic Screen Capturator 3000")
print("Push S anytime to capture the screen")
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
    ##cropped_screenshot_local.show() #This displays the picture but doesn't let us print it out :s
    ##Displaying cropped screenshot
    print("Screenshot cropped!")
    ##Confirming cropping
    return cropped_screenshot_local

def file_saver(cropped_screenshot):
    """Saves file after cropped"""
    timestr = time.strftime("%Y%m%d-%H%M%S")
    ##Composing timestring and assigning to timestr variable
    ##print("The timestring is " + timestr)
    ##Printing timestring for diagnostics and giggles
    filename = 'csc' + timestr + '.png'
    ##Creating filename variable and assembling filename elements
    cropped_screenshot.save(filename)
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
    ##os.startfile(saved_screenshot, "print")
    os.system("start " + saved_screenshot) ##Loading the saved screenshot in the default Photos app
    print("Sending screenshot to default printer !")

while True:
##Starting loop
    ##Starting try for exceptions handling
    if keyboard.is_pressed('s'):
    ##If detection: S key pres
        screenshot = ImageGrab.grab(bbox=(0,0,1920,1080)) #Appropriate dimensions for Alienware laptop
        ##screenshot = ImageGrab.grab(bbox=(0,0,1600,900)) #Appropriate dimensions for Thomas' dev laptop
        ##screenshot.show()
        ##Creating screenshot variable and capturing screenshot with ImageGrab.grab() method with display parameters (x origin, y origin, resolution)
        screenshot_width, screenshot_height = screenshot.size ##Getting dimensiosn
        print("Grabbing dimensions from screenshot") #Collecting dimensions from raw_screenshot content
        ##print(raw_screenshot_width, raw_screenshot_height) #Printing the dimensions obtained from raw_screenshot just for kicks
        cropped_screenshot = screenshot_cropper(screenshot, screenshot_width, screenshot_height)
        ##Passing raw_screenshot to screenshot_cropper() function for cropping
        saved_screenshot = file_saver(cropped_screenshot)
        ##Passing cropped_screenshot to file_saver() function for saving
        screenshot_printer(saved_screenshot)
        ##Passing saved_screenshot to screenshot_printer() for printing
        ##print("Ready to take the next screenshot!")
        ##Sending recorded screenshot to default printer
        ##print(saved_screenshot)
        ##show_image = Image.open(saved_screenshot) #Loading the saved screenshot and saving it to show_image
        ##show_image.show() #Displaying the loaded screenshot
    elif keyboard.is_pressed('q'):
        print("Hope everything worked out. See you later!")
        break
