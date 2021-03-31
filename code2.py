"""
All coordinates assume a screen resolution of 1920 x 1080
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
import pytesseract

import pynput
from pynput.keyboard import Key, Controller
from pynput.mouse import Controller

import time

from numpy import *
import numpy
import win32api, win32con

# Ab Optical Character Roegnition (OCR) tool for python
import pytesseract
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
    retry_button = (935, 524)
    
    # Coords of buttons while in login screen
    login_button = (756, 706)

    # Coords found in main menu screen
    setting_button = (1779, 36)
    log_out = (778, 534)
    exit_game = (796, 489)
    ok_button = (930, 519)

    # Coords in main menu screen
    play_button = (1308, 796)  # Bottom right button in main menu
    all_play_button = (978, 100)

    # Cords to move cursor to deck after pressing 'play' button
    deck = (1388, 630)

    # Coords of deck shown in the right side nav bar menu
    deck_right_side_menu = (981, 598)

    # Coords of buttons/images while playing a match
    keep_button = (854, 702)
    
    click_cont = (691, 394, 843, 845)

    # The middle cords of each card in your hand
    hand = {
        1: (346, 845),
        2: (486, 845),
        3: (635, 845),
        4: (784, 845),
        5: (915, 845),
        6: (1046, 845),
        7: (1177, 845),
        }

    #Cords for deck position
    decks = {0: (366, 230),
             1: (618, 192),
             2: (840, 197),
             3: (1121, 198),
             4: (145, 337)
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
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

    im = ImageGrab.grab(image)

    #resize_im = im.resize((830, 55), resample=Image.NEAREST) #(width, height)

    text = pytesseract.image_to_string(cv2.cvtColor(numpy.array(im), cv2.IMREAD_GRAYSCALE),
                                           lang='eng')
    
    #im.show()
    print(text)
    split_text = text.split()
    print(split_text)
    

    return split_text

def CordsToImage(y1, x1, y2, x2):
    time.sleep(1)               # almost works(108, 769, 200, 826)
    #box = (1608, 896, 1878, 950) #best working cords (5, 769, 200, 826)
    box = (y1, x1, y2, x2)
    
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

    im = ImageGrab.grab(box)

    if box != (1608, 896, 1878, 950):
        resize_im = im.resize((170, 139), resample=Image.NEAREST) #(170, 139) The values work when resizing image for
                                                                # the amount of cards in hand

        text = pytesseract.image_to_string(cv2.cvtColor(numpy.array(resize_im), cv2.IMREAD_GRAYSCALE),
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
        text = pytesseract.image_to_string(cv2.cvtColor(numpy.array(im), cv2.IMREAD_GRAYSCALE),
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
    time.sleep(3)               # almost works(108, 769, 200, 826)
    #box = (1608, 896, 1878, 950) #best working cords (5, 769, 200, 826)
    box = (108, 789, 200, 826)
    
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

    im = ImageGrab.grab(box)

    
    resize_im = im.resize((170, 139), resample=Image.NEAREST) #(170, 139) The values work when resizing image for
                                                                # the amount of cards in hand

    text = pytesseract.image_to_string(cv2.cvtColor(numpy.array(resize_im), cv2.IMREAD_GRAYSCALE),
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
    '''
    use this function to get a picture of whatever coordinates you need from the
    screen
    will need to adjust the numbers of the box variable below
    '''
    time.sleep(5)               # almost works(108, 769, 200, 826)
    box = (266, 630, 430, 1048) #best working cords (5, 769, 200, 826)
    
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

    im = ImageGrab.grab()
    pixel = im.getpixel((428, 629))
    
    print(pixel)
    resize_im = im.resize((170, 139), resample=Image.NEAREST)

    text = pytesseract.image_to_string(cv2.cvtColor(numpy.array(im), cv2.IMREAD_GRAYSCALE),
                                           lang='eng')

    #text = pytesseract.image_to_string(cv2.cvtColor(numpy.array(resize_im), cv2.IMREAD_GRAYSCALE),
     #                                      lang='eng')
    #resize_im.show()
    im.show()
    print(text)
    print()

    split_text = text.split()
    print(split_text)
#########################################################################
    
def check_hand_size():
    mousePos((170, 654))
    time.sleep(2)
    leftClick()

    mousePos((170, 754))

        
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
        ##box = (683, 711, 842, 765)
        time.sleep(3)
        im = ImageGrab.grab()
        color = im.getpixel((220, 816))
            
        reference_color = im.getpixel((220, 816))
        
        print(color)

        while color == reference_color:
            time.sleep(3)
            im = ImageGrab.grab()
            reference_color = im.getpixel((220, 816))
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
            name = CordsToImage(1608, 896, 1878, 950)

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
        box = (871, 843, 985, 888)

        decks = ((366, 230),
                 (618, 192),
                 (840, 197),
                 (1121, 198),
                 (145, 337)
                 )

        colors = []
        DeckFound = False
        no_color_quest = False

        pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

        im = ImageGrab.grab(box)

        resize_im = im.resize((200, 50), resample=Image.NEAREST)

        text = pytesseract.image_to_string(cv2.cvtColor(numpy.array(im), cv2.IMREAD_GRAYSCALE),
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
        mousePos((1311, 253)) #'Play' the button found under "Find Match"
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
        ##box = (1267, 765, 1389, 797)

        ##box = (1446, 861, 1653, 906)
        box = (1674, 923, 1880, 975)

        # the path to use tesseract in program. May be different depending on location of file
        pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

        im = ImageGrab.grab(box)

        resize_im = im.resize((250, 70), resample = Image.NEAREST)
        #im.show()

        #resize_im.show()

        
        #cv2.cvtColor takes a numpy ndarray as an argument
        # convereted the image to grayscale for it to be easily read by the OCR and obrained the output string
        text = pytesseract.image_to_string(cv2.cvtColor(numpy.array(resize_im), cv2.IMREAD_GRAYSCALE),
                                           lang = 'eng')
        
        #print(text)
        print(text.split())
        return text.split()

    def CheckMyTurn(self):
        #will check if the button on bottom right is orange, indicating
        #its the bots turn
        box = (1504, 923, 1684, 933)
        
        im = ImageGrab.grab()
        #im.show()
        pixel = im.getpixel((1684, 933))
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
            0: (346, 845),
            1: (486, 845),
            2: (635 + pointer, 845),
            3: (784 + pointer, 845),
            4: (915 + pointer, 845),
            5: (1046 + pointer, 845),
            6: (1177 + pointer, 845),
            7: (1226 + pointer, 845)
        }

        AreaOfEnlargedCards = {
            0: (428, 632),
            1: (568, 632),
            2: (708, 632),
            3: (848, 632),
            4: (988, 632),
            5: (1128, 632),
            6: (1268, 632),
            7: (1408, 632),
            }

        '''
        method will first check if YOU are playing first or second
        this will be determined when the game asks if you are gonna keep or mulligan your hand
        '''
        """
        text = CordsToImage(628, 51, 977, 124)

        time.sleep(2)
        if text == 'opponent' or text == 'Opponent' \
           or text == "opponent\n" or text == "Opponent\n":
            pointer -= 48
            print("You play second")
        else:
            print("You play first")
        time.sleep(5)

        mousePos(Cords.keep_button)
        time.sleep(2)

        leftClick()
        time.sleep(8)
        """

        # while loop will check if the background is the same throughout the whole match
        # if its not, the screen is probably displaying the screen indicating you won or lost
        im = ImageGrab.grab()
        
        color = im.getpixel((40, 1048)) #get cords of an area of the background during a match

        reference_color = im.getpixel((40, 1048))

        print(reference_color)
        print(color)
        count = 0
        print()

        #HandDuration = len(hand)
        #start = 0
        
        
        while color == reference_color or sum(reference_color) in range(302, 315):

            #this section checks if the background is blue.
            #if it is, it will concede the match
            # blue background messes with the program
            
            im = ImageGrab.grab()
            concede_color = im.getpixel((535, 64))
            #print(concede_color)
            if concede_color[2] >= 190:
                mousePos((1506, 28))
                leftClick()
                time.sleep(1.5)
                mousePos((770, 508))
                leftClick()

            Broken = False
            
            pixel = self.CheckMyTurn() # returns pixel color of bottom right button
            
            if sum(pixel) in range(300, 490):
                """
                CardsInHand = CordsToImage(5, 769, 200, 826)
                if not CardsInHand or type(CardsInHand) != int:
                    start = hand[0]
                elif type(CardsInHand) == int and CardsInHand <= 8:
                    start = hand[-CardsInHand]
                """
                
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
                            mousePos((1376, 768))
                            leftClick()
                            time.sleep(1)
                            leftClick()
                            mousePos((22, 598))
                            break
                        

                        elif (j == 'Blocks')\
                             or (j == 'NoBlocks')\
                             or (j == 'Block'):
                            mousePos((1376, 768))
                            leftClick()
                            time.sleep(1)
                            leftClick()
                            mousePos((22, 598))
                            break
                        elif (j == "Opponent's Turn") or\
                             (j == "Opponent") or\
                             (j == "Opponent's"):
                            print("part 1")
                            print("breaking out of loop")
                            mousePos((1518, 525))
                            time.sleep(1)
                            leftClick()
                            mousePos((22, 598))
                            Broken = True
                            break

                    if Broken == True:
                        break
                    
                    #predefined area to click on to start moving the cursor
                    mousePos((1518, 525)) 
                    ##leftClick()
                    
                    mousePos(hand[i])
                    time.sleep(1)
                    # will grab an image of the whole screen
                    im = ImageGrab.grab() #(266, 630, 430, 1048)

                    # will get the pixel of defined cords
                    aura = im.getpixel(AreaOfEnlargedCards[i])
                    #im.show()
                    print(aura)
                    time.sleep(1.2)
                    #aura = sum(aura)

                    # if the sum of the pixel is within this range...
                    #if aura in range(379, 629):
                    if aura[2] >= 102 or sum(aura) in range(379, 670):
                        doubleClick()
                        time.sleep(.5)
                        mousePos((22, 598))
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
                            mousePos((1376, 768))
                            leftClick()
                            time.sleep(1)
                            leftClick()
                            mousePos((22, 598))
                            break
                        elif j == 'Next' or j == "`Next":
                            pass
                        
                        elif j == "Opponent's Turn" or\
                           j == "Opponent" or\
                           j == "Opponent's":
                            
                            print("breaking out of loop")
                            mousePos((1518, 525)) 
                            Broken = True
                            break

                    if Broken == True:
                        break
                        
                      
                    if i >= 7:               
                        # will double click the bottom right button
                        mousePos((1376, 768))
                        leftClick()
                        time.sleep(1)
                        #leftClick()
                        mousePos((22, 598))

                    pointer = 0
                        
            time.sleep(3)
            im = ImageGrab.grab()
            # reference_color will be used to compare with 'color' 
            reference_color = im.getpixel((40, 1048))
            #print(color)
            #print(reference_color)
            count += 1
            print(count)

        print("game done")
        time.sleep(2)
        leftClick()
        return


bot1 = bot(email, password)
bot2 = bot(email, password)
bot3 = bot(email, password)
bot4 = bot(email, password)

accounts = [bot1, bot2, bot3, bot4]
#"""
for account in accounts:
    time.sleep(5)
    account.login_screen()
    account.getdeck()
    account.gameplay()
    time.sleep(7)
    account.logout()
#"""
