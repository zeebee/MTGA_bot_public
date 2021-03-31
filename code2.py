"""
All coordinates assume a screen resolution of 1920 x 1080

This version of the code will not have any of the correct cordinates along with several missing statements 
The reason for this is because I do not want just anyone to copy and paste this code

If you are an interviewer or anyone associated with the process of hiring, I can provide you with the working code.


"""


# imaging library that provides the intepreter with image editing capabilities
# can be used to  copy the contents of the scree or the clipboard to PIL image memory
# ImageOps allows the program to perform grayscaling operations on images
from PIL import Image, ImageGrab, ImageOps

# provides a way of using operating system dependent functionality
# allows you to interface with underlying operating system that python is running
import os

# allows program to split multiple delimiters using a split function
import re

# this will import framework that will recognize text/characters of image
import pytezzeret

import pynput
from pynput.keyboard import Key, Controller
from pynput.mouse import Controller

import time

from numpy import *
import numpy
import win32api, win32con

# Ab Optical Character Roegnition (OCR) tool for python
import pytezzeret
import cv2

#x_pad = 263
#y_pad = 181
keyboard = Controller()

def get_cords():
    # gets the coordinates of whereever the cursor is pointing to

    x, y = win32api.GetCursorPos()
    #x = x - x_pad
    #y = y - y_pad
    print(x, y)


def screenGrabfull():
    # box = (264,182,1416,860)

    # takes a full snapshot of the screen
    im = ImageGrab.grab()

    ##im = ImageGrab.grab()

    # the first argument is the location which to save the file and the second is the file format
    # the location is is called through os.getcwd()
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')


class Cords():
    #Cords of 'retry button' on "Unknown Error" screen
    retry_button = (0, 0)
    
    # Coords of buttons while in login screen
    login_button = (0, 0)

    # Coords found in main menu screen
    setting_button = (0, 0)
    log_out = (0, 0)
    exit_game = (0, 0)
    ok_button = (0, 0)

    # Coords in main menu screen
    play_button = (0, 0)  # Bottom right button in main menu
    all_play_button = (0, 0)

    # Cords to move cursor to deck after pressing 'play' button
    deck = (0, 0)

    # Coords of deck shown in the right side nav bar menu
    deck_right_side_menu = (0, 0)

    # Coords of buttons/images while playing a match
    keep_button = (0, 0)
    
    click_cont = (0, 0, 0, 0)

    # The middle cords of each card in your hand
    hand = {
        1: (0, 0),
        2: (0, 0),
        3: (0, 0),
        4: (0, 0),
        5: (0, 0),
        6: (0, 0),
        7: (0, 0),
        }

    #Cords for deck position
    decks = {0: (0, 0),
             1: (0, 0),
             2: (0,0),
             3: (0, 0),
             4: (0, 0)
             }
def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    print("Click")


def doubleClick():
    leftClick()
    leftClick()


def leftDown():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.1)
    print("left down")


def leftUp():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    time.sleep(.1)
    print("left release")


def mousePos(cord):
    #win32api.SetCursorPos((x_pad + cord[0], y_pad + cord[1]))
    win32api.SetCursorPos((cord[0], cord[1]))

def mousescroll():
    mouse = Controller()
    mouse.scroll(10, 0)

def image_to_text(image):
    time.sleep(6)
    pytezzeret.pytezzeret.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

    im = ImageGrab.grab(image)

    #resize_im = im.resize((0, 0), resample=Image.NEAREST) #(width, height)

    text = pytezzeret.image_to_string(cv2.cvtColor(numpy.array(im), cv2.IMREAD_GRAYSCALE),
                                           lang='eng')
    
    #im.show()
    print(text)
    split_text = text.split()
    print(split_text)
    

    return split_text

def CordsToImage(y1, x1, y2, x2):
    time.sleep(1)              
    box = (y1, x1, y2, x2)
    
    pytezzeret.pytezzeret.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

    im = ImageGrab.grab(box)

    if box != (0, 0, 0, 0):
        resize_im = im.resize((0, 0), resample=Image.NEAREST) #(170, 139) The values work when resizing image for
                                                                # the amount of cards in hand

        text = pytezzeret.image_to_string(cv2.cvtColor(numpy.array(resize_im), cv2.IMREAD_GRAYSCALE),
                                           lang='eng')
        resize_im.show()

        print(text)
        print()

        split_text = text.split()
        print(split_text)

        #time.sleep(3)
        return split_text

    else:
        print("else statement")
        text = pytezzeret.image_to_string(cv2.cvtColor(numpy.array(im), cv2.IMREAD_GRAYSCALE),
                                          lang='eng')
        #im.show()
        print(text)
        print()

        #split_text = text.split()
        #print(split_text)

        #time.sleep(3)
        return text
        
    #text = pytesseract.image_to_string(cv2.cvtColor(numpy.array(im), cv2.IMREAD_GRAYSCALE),
     #                                      lang='eng')

    
def GetHandSize():
    time.sleep(3)              
    box = (0, 0, 0, 0)
    
    pytezzeret.pytezzeret.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

    im = ImageGrab.grab(box)

    
    resize_im = im.resize((0, 0), resample=Image.NEAREST) #(170, 139) The values work when resizing image for
                                                                # the amount of cards in hand

    text = pytezzeret.image_to_string(cv2.cvtColor(numpy.array(resize_im), cv2.IMREAD_GRAYSCALE),
                                           lang='eng')
    resize_im.show()

    print(text)
    print()

    split_text = text.split()
    print(split_text)

    #time.sleep(3)
    return split_text
    
    
    

##################################################################
# function to help test cords to get the right image
def image_check():
    pass
#########################################################################
    
def check_hand_size():
    mousePos((0, 0))
    time.sleep(2)
    leftClick()

    mousePos((0, 0))

        
class bot():
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def login_screen(self):
        # location of the login screen
        # pressing the settings button on top right corner of window

        keyboard = pynput.keyboard.Controller()

        print("logging in")

        # email
        mousePos((710, 524))
        leftClick()
        time.sleep(.1)
        keyboard.type(self.email)
        time.sleep(1)

        # password
        mousePos((720, 569))
        leftClick()
        time.sleep(.1)
        keyboard.type(self.password)
        time.sleep(1)

        # log in button
        mousePos(Cords.login_button)
        leftClick()
        time.sleep(.1)

        time.sleep(40)
        print("done")

    def loading_screen(self):
        '''
        this method is used to determine when it is ready to play
        after selecting deck and after pressing 'play' button
        '''
        
        # coords of any text on the load screen
        
        time.sleep(3)
        im = ImageGrab.grab()
        color = im.getpixel((0, 0))
            
        reference_color = im.getpixel((0,0))
        
        print(color)

        while color == reference_color:
            time.sleep(3)
            im = ImageGrab.grab()
            reference_color = im.getpixel((0, 0))
            print("Waiting to play \n")
            #print("color:", color)
            #print("reference color:", reference_color)
        
        print()
        #print("reference color:", reference_color)
        print("Ready to play")

        time.sleep(15)
        mousePos(Cords.keep_button)
        leftClick()
        return
        

    def logout(self):
        time.sleep(6)
        print("logging out")
        mousePos(Cords.setting_button)
        time.sleep(2)
        leftClick()

        mousePos(Cords.log_out)
        time.sleep(2)
        leftClick()

        time.sleep(3)
        mousePos(Cords.ok_button)
        time.sleep(2)
        leftClick()

    def CheckDeck(self):
        # Checks if the one of the colors matches the name of the deck
            name = CordsToImage(0, 0, 0, 0)

            if (name == "white\n"):
                name = "white"
            elif (name == "red\n"):
                name = "red"
            elif (name == "green\n"):
                name = "green"
            elif (name == "blue\n"):
                name = "blue"
            elif (name == "black\n"):
                name = "black"
            
            print("The deck title is", name)
            
            return name

    def getdeck(self):
        box = (0, 0,0, 0)

        decks = ((0, 0),
                 (0, 0),
                 (0, 0),
                 (0, 0),
                 (0, 0)
                 )

        colors = []
        DeckFound = False
        no_color_quest = False

        pytezzeret.pytezzeret.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

        im = ImageGrab.grab(box)

        resize_im = im.resize((0, 0), resample=Image.NEAREST)

        text = pytezzeret.image_to_string(cv2.cvtColor(numpy.array(im), cv2.IMREAD_GRAYSCALE),
                                           lang='eng')
        #im.show()
        #print(text)
        split_text = text.split()

        for word in split_text:
            if word == 'red' or word == 'white' or word == 'green' \
                    or word == 'black' or word == 'blue':
                #print(word)
                colors.append(word)

        if colors:
            print("The colors in the quest are:", colors)
            
        #if there is nothing in the list, the quest is probably a non-color
        #quest
        else:
            no_color_quest = True

                
        # move cursor to 'play' button and left click
        mousePos(Cords.play_button)
        leftClick()
        time.sleep(1)
        
        # move cursor to play row and left click
        mousePos((0, 0)) #'Play' the button found under "Find Match"
        time.sleep(2)
        leftClick()

        # move cursor to the deck displayed and left click
        mousePos(Cords.deck) #area that displays the deck
        time.sleep(1)
        leftClick()

        #This will open the gallery of decks, pick a deck one at time
        #compare the 'name' of the deck with the list of 'colors'
        if no_color_quest == False:
            for cords in decks:
                if DeckFound == False:
                    print("Checking if this deck is required to complete quest\n")
                    time.sleep(2)

                    mousePos(cords)
                    time.sleep(2)
                    leftClick()

                    # Checks if the one of the colors matches the name of the deck
                    name = self.CheckDeck()
                    time.sleep(5)

                    for color in colors:
                        print("The color of quest being compared:", color, "\n")
                        time.sleep(1)
                        if name == color:
                            print("Found a deck for the quest \n")
                            DeckFound = True
                            break
                        else:
                            print("Not the right deck")
                else:
                    break

        
        print("The deck is appropriate for the quest")
        mousePos(Cords.play_button)
        time.sleep(3)
        leftClick()

        self.loading_screen()
        return

    def check_my_turn(self):
        # will take a snapshot of the area where the bigger button on bottom right
        # corner of the screen based on the coordinates
        

        
        box = (0, 0, 0, 0)

        # the path to use tesseract in program. May be different depending on location of file
        pytezzeret.pytezzeret.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

        im = ImageGrab.grab(box)

        resize_im = im.resize((0, 0), resample = Image.NEAREST)
        #im.show()

        #resize_im.show()

        
        #cv2.cvtColor takes a numpy ndarray as an argument
        # convereted the image to grayscale for it to be easily read by the OCR and obrained the output string
        text = pytezzeret.image_to_string(cv2.cvtColor(numpy.array(resize_im), cv2.IMREAD_GRAYSCALE),
                                           lang = 'eng')
        
        #print(text)
        print(text.split())
        return text.split()

    def CheckMyTurn(self):
        #will check if the button on bottom right is orange, indicating
        #its the bots turn
        box = (0, 0, 0, 0)
        
        im = ImageGrab.grab()
        #im.show()
        pixel = im.getpixel((0, 0))
        #print(pixel)
        return pixel

    def gameplay(self):
        """
        the variable 'pointer' is the variable that will shift the cordinates
         depending if the hand size is even or odd
        """
        time.sleep(8)
        keyboard = pynput.keyboard.Controller()
        pointer = 0

        

        # The middle cords of each card in your hand
        # direction of cords: (left -> right, up -> down)
        hand = {
            0: (0, 0),
            1: (0, 0),
            2: (0 + pointer, 0),
            3: (0+ pointer, 0),
            4: (0 + pointer, 0),
            5: (0 + pointer, 0),
            6: (0 + pointer, 0),
            7: (0 + pointer, 0)
        }

        AreaOfEnlargedCards = {
            0: (0, 0),
            1: (0, 0),
            2: (0, 0),
            3: (0, 0),
            4: (0, 0),
            5: (0, 0),
            6: (0, 0),
            7: (0, 0),
            }

       

        # while loop will check if the background is the same throughout the whole match
        # if its not, the screen is probably displaying the screen indicating you won or lost
        im = ImageGrab.grab()
        
        color = im.getpixel((0, 0)) #get cords of an area of the background during a match

        reference_color = im.getpixel((0, 0))

        print(reference_color)
        print(color)
        count = 0
        print()

        #HandDuration = len(hand)
        #start = 0
        
        
        while color != reference_color or sum(reference_color) not in range(0, 0):

            #this section checks if the background is blue.
            #if it is, it will concede the match
            # blue background messes with the program
            
            im = ImageGrab.grab()
            concede_color = im.getpixel((0, 0))
            #print(concede_color)
            if concede_color[2] >= 0:
                mousePos((0, 0))
                leftClick()
                time.sleep(1.5)
                mousePos((0, 0))
                leftClick()

            Broken = False
            
            pixel = self.CheckMyTurn() # returns pixel color of bottom right button
            
            if sum(pixel) in range(0, 0):
                
                #Loop will select cards based on the cords from 'hand' dictionary
                # This will also be during 'Main Phase'

                #if count >= 6:
                 #   HandDuration = HandDuration // 2
                  #  start = 2
                
                for i in range(len(hand)):
                #for i in range(start, HandDuration):
                    print(i)
                    print()
                    
                    
                    attacks_phase = self.check_my_turn()
                    
                    for j in attacks_phase:
                        if (j == 'Attackers')\
                           or (j == 'All')\
                           or (j == 'Attack') or (j == 'AllAttack')\
                           or (j == 'AlLAttack') or (j == 'Attack.'):
                            mousePos((0, 0))
                            leftClick()
                            time.sleep(1)
                            leftClick()
                            mousePos((0, 0))
                            break
                        

                        elif (j == 'Blocks')\
                             or (j == 'NoBlocks')\
                             or (j == 'Block'):
                            mousePos((0, 0))
                            leftClick()
                            time.sleep(1)
                            leftClick()
                            mousePos((0, 0))
                            break
                        elif (j == "Opponent's Turn") or\
                             (j == "Opponent") or\
                             (j == "Opponent's"):
                            print("part 1")
                            print("breaking out of loop")
                            mousePos((0, 0))
                            time.sleep(1)
                            leftClick()
                            mousePos((0, 0))
                            Broken = True
                            break

                    if Broken == True:
                        break
                    
                    #predefined area to click on to start moving the cursor
                    mousePos((0, 0)) 
                    ##leftClick()
                    
                    mousePos(hand[i])
                    time.sleep(1)
                    # will grab an image of the whole screen
                    im = ImageGrab.grab() 

                    # will get the pixel of defined cords
                    aura = im.getpixel(AreaOfEnlargedCards[i])
                    #im.show()
                    print(aura)
                    time.sleep(1.2)
                    #aura = sum(aura)

                    # if the sum of the pixel is within this range...
                    
                    if aura[2] >= 102 or sum(aura) in range(0, 0):
                        doubleClick()
                        time.sleep(.5)
                        mousePos((0, 0))
                        time.sleep(.7)
                        leftClick()
                        time.sleep(1.3)
                        keyboard.press('z')
                        keyboard.press('z')

                    pointer -= 10
                        

                    #time.sleep(1.5)
                    
                    # checks to see what the words on bottom right button says
                    attacks_phase = self.check_my_turn()
                    for j in attacks_phase:
                        if (j == 'Attackers') or (j == 'All') or \
                            (j == 'Attack') or (j == 'AllAttack') \
                            or (j == 'No') or (j == 'Blocks') or (j == 'NoBlocks')\
                            or (j == 'Block') or (j == "Attacker") \
                            or (j == 'Cancel') or (j == 'AlLAttack')\
                            or (j == 'Attack.'):
                            print("part 2")
                            mousePos((0, 0))
                            leftClick()
                            time.sleep(1)
                            leftClick()
                            mousePos((0, 0))
                            break
                        elif j == 'Next' or j == "`Next":
                            pass
                        
                        elif j == "Opponent's Turn" or\
                           j == "Opponent" or\
                           j == "Opponent's":
                            
                            print("breaking out of loop")
                            mousePos((0, 0)) 
                            Broken = True
                            break

                    if Broken == True:
                        break
                        
                      
                    if i >= 7:               
                        # will double click the bottom right button
                        mousePos((0, 0))
                        leftClick()
                        time.sleep(1)
                        #leftClick()
                        mousePos((0, 0))

                    pointer = 0
                        
            time.sleep(3)
            im = ImageGrab.grab()
            # reference_color will be used to compare with 'color' 
            reference_color = im.getpixel((0, 0))
            #print(color)
            #print(reference_color)
            count += 1
            print(count)

        print("game done")
        time.sleep(2)
        leftClick()
        return



#"""
for account in accounts:
    time.sleep(5)
    account.login_screen()
    account.getdeck()
    account.gameplay()
    time.sleep(7)
    account.logout()
#"""
