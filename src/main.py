import pygame as py
import sys
from game_loop import *

import pygame as py

# Class to create buttons
class Button:
    def __init__(self, image, pos):
        self.image = image if image is not None else self.create_default_button()
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.hovered = False

    def create_default_button(self):
        surface = py.Surface((298, 68))
        return surface

    def checkForInput(self, position):
        return self.rect.collidepoint(position)
    
    def checkForHover(self, position):
        if self.checkForInput(position):
            return True
        else:
            return False

# Initialize py
py.init()

# Constants
WIDTH = 600
HEIGHT = 800

# Set up the display
screen = py.display.set_mode((WIDTH, HEIGHT))
py.display.set_caption('WordLab')

# Set up icon of window
ICON = py.image.load("assets/Icon.png")
py.display.set_icon(ICON)

# Font
def get_font(size):
    return py.font.Font("assets/.FreeSansBold.otf", size)

# Menu Background
MENU_BG = py.image.load("assets\MENU.png")
MENU_BG_RECT = MENU_BG.get_rect(center=(WIDTH / 2, HEIGHT / 2))

# Options Background
OPTIONS_BACKGROUND = py.image.load("assets\OPTIONS.png")
OPTIONS_BACKGROUND_RECT = MENU_BG.get_rect(center=(WIDTH / 2, HEIGHT / 2))

# How To Background
HOWTO_BACKGROUND = py.image.load("assets\HOWTO.png")
HOWTO_BACKGROUND_RECT = MENU_BG.get_rect(center=(WIDTH / 2, HEIGHT / 2))

# Settings Background
SETTINGS_BACKGROUND = py.image.load("assets\SETTINGS.png")
SETTINGS_BACKGROUND_RECT = MENU_BG.get_rect(center=(WIDTH / 2, HEIGHT / 2))

# Are You Sure Background
RESET_BG = py.image.load("assets\RESET.png")
RESET_BG_RECT = MENU_BG.get_rect(center=(WIDTH / 2, HEIGHT / 2))

# Credits background
CREDITS_BACKGROUND = py.image.load("assets\CREDITS.png")
CREDITS_BACKGROUND_RECT = MENU_BG.get_rect(center=(WIDTH / 2, HEIGHT / 2))

# Color definitions
NAVY_BLUE = (39, 48, 67)
WHITE = (255, 255, 255)

# Load button images
SWITCH_ON = py.image.load("assets\SWITCH_ON.png").convert_alpha(),
SWITCH_OFF = py.image.load("assets\SWITCH_OFF.png").convert_alpha()



#-----------------------------
#       Window events
#-----------------------------

MN_BTTN_SPACING = 23

def main_menu():    # Main menu screen
    while True:
        screen.fill(NAVY_BLUE)      # Fills window with a color
        screen.blit(MENU_BG, MENU_BG_RECT)      # Sets the background image

        MENU_MOUSE_POS = py.mouse.get_pos()     # To get position of mouse
        
        # Buttons definition
        PLAY_BUTTON = Button(image=None, pos=(WIDTH/2, 235+34))
        OPTIONS_BUTTON = Button(image=None, pos=(WIDTH/2, 326+34))
        CREDITS_BUTTON = Button(image=None, pos=(WIDTH/2, 417+34))
        EXIT_BUTTON = Button(image=None, pos=(WIDTH/2, 508+34))
        
        buttons = [PLAY_BUTTON, OPTIONS_BUTTON, CREDITS_BUTTON, EXIT_BUTTON]
        
        # Variables to get mouse position and left click
        mouse_pos = py.mouse.get_pos()
        mouse_pressed = py.mouse.get_pressed()

        # Checks for hovering
        hovered = False
        for button in buttons:
            if button.checkForHover(mouse_pos):
                hovered = True

        # If hovering is true, sets cursor to pointing hand
        if hovered:
            py.mouse.set_cursor(py.SYSTEM_CURSOR_HAND)
        else:
            py.mouse.set_cursor(py.SYSTEM_CURSOR_ARROW)
        
        if mouse_pressed[0]:  # Check if left mouse button is pressed
            if PLAY_BUTTON.checkForInput(mouse_pos):
                print("Start Game button clicked")
            if OPTIONS_BUTTON.checkForInput(mouse_pos):
                print("Options button clicked")
            if CREDITS_BUTTON.checkForInput(mouse_pos):
                print("Credits button clicked")

        # Handles event detection
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                sys.exit()
            if event.type == py.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play_game()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if CREDITS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    credits()
                if EXIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    py.quit()
                    sys.exit()
        
        py.display.flip()

def play_game():
    while True:

        screen.fill(WHITE)
        screen.blit(PLAY_BACKGROUND, PLAY_BACKGROUND_RECT)

        START_MOUSE_POS = py.mouse.get_pos()

        START_BACK = Button(image=None, pos=(19+30, 23+30))
        START_OPTIONS = Button(image=None, pos=(550, 43.53))

        play_buttons = [START_BACK, START_OPTIONS]

        # Variables to get mouse position and left click
        play_mouse_pos = py.mouse.get_pos()
        play_mouse_pressed = py.mouse.get_pressed()

        # Checks for hovering
        hovered = False
        for button in play_buttons:
            if button.checkForHover(play_mouse_pos):
                hovered = True

        # If hovering is true, sets cursor to pointing hand
        if hovered:
            py.mouse.set_cursor(py.SYSTEM_CURSOR_HAND)
        else:
            py.mouse.set_cursor(py.SYSTEM_CURSOR_ARROW)

        GameLoop()

def options():
    while True:
        screen.fill(NAVY_BLUE)      # Fills window with a color
        screen.blit(OPTIONS_BACKGROUND, OPTIONS_BACKGROUND_RECT)      # Sets the background image

        OPTIONS_MOUSE_POS = py.mouse.get_pos()

        OPTIONS_BACK = Button(image=None, pos=(19+30, 23+30))
        OPTIONS_HOWTO = Button(image=None, pos=(151+298/2, 289+34))
        OPTIONS_SETTINGS = Button(image=None, pos=(151+298/2, 403+34))
        OPTIONS_RESET = Button(image=None, pos=(151+298/2, 517+34))

        options_buttons = [OPTIONS_BACK, OPTIONS_HOWTO, OPTIONS_SETTINGS, OPTIONS_RESET]

        # Checks for hovering
        hovered = False
        for button in options_buttons:
            if button.checkForHover(OPTIONS_MOUSE_POS):
                hovered = True

        # If hovering is true, sets cursor to pointing hand
        if hovered:
            py.mouse.set_cursor(py.SYSTEM_CURSOR_HAND)
        else:
            py.mouse.set_cursor(py.SYSTEM_CURSOR_ARROW)

        # Checks for events
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                sys.exit()
            # Checks for click events
            if event.type == py.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()
                if OPTIONS_HOWTO.checkForInput(OPTIONS_MOUSE_POS):
                    how_to()
                if OPTIONS_SETTINGS.checkForInput(OPTIONS_MOUSE_POS):
                    settings()
                if OPTIONS_RESET.checkForInput(OPTIONS_MOUSE_POS):
                    reset()

        py.display.update()

def how_to():
    while True:
        screen.fill(NAVY_BLUE)      # Fills window with a color
        screen.blit(HOWTO_BACKGROUND, HOWTO_BACKGROUND_RECT)      # Sets the background image
        HOWTO_MOUSE_POS = py.mouse.get_pos()

        # Buttons definition and array containing buttons
        HOWTO_BACK = Button(image=None, pos=(19+30, 23+30))
        howto_buttons = [HOWTO_BACK]

        # Checks for hovering
        hovered = False
        for button in howto_buttons:
            if button.checkForHover(HOWTO_MOUSE_POS):
                hovered = True

        # If hovering is true, sets cursor to pointing hand
        if hovered:
            py.mouse.set_cursor(py.SYSTEM_CURSOR_HAND)
        else:
            py.mouse.set_cursor(py.SYSTEM_CURSOR_ARROW)

        # Handles event detection
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                sys.exit()
            if event.type == py.MOUSEBUTTONDOWN:
                if HOWTO_BACK.checkForInput(HOWTO_MOUSE_POS):
                  main_menu()

        py.display.update()

def settings():
    while True:
        screen.fill(NAVY_BLUE)      # Fills window with a color
        screen.blit(SETTINGS_BACKGROUND, SETTINGS_BACKGROUND_RECT)      # Sets the background image

        SETTINGS_BACK = Button(image=None, pos=(19+30, 23+30))
        SETTINGS_BRIGHTNESS_DOWN = Button(image=None, pos=(300, 340))
        SETTINGS_BRIGHTNESS_UP = Button(image=None, pos=(600, 340))
        SETTINGS_SFX = Button(image=None, pos=(435.5, 422))
        SETTINGS_MUSIC = Button(image=None, pos=(435.5, 505))

        SETTINGS_MOUSE_POS = py.mouse.get_pos()

        settings_buttons = [SETTINGS_BACK, SETTINGS_BRIGHTNESS_DOWN, SETTINGS_BRIGHTNESS_UP,
                            SETTINGS_SFX, SETTINGS_MUSIC]

        # Checks for hovering
        hovered = False
        for button in settings_buttons:
            if button.checkForHover(SETTINGS_MOUSE_POS):
                hovered = True

        # If hovering is true, sets cursor to pointing hand
        if hovered:
            py.mouse.set_cursor(py.SYSTEM_CURSOR_HAND)
        else:
            py.mouse.set_cursor(py.SYSTEM_CURSOR_ARROW)
        
            

        # Handles event detection
        clicked = False
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                sys.exit()
            if event.type == py.MOUSEBUTTONDOWN:
                if SETTINGS_BACK.checkForInput(SETTINGS_MOUSE_POS):
                  main_menu()
                if SETTINGS_SFX.checkForInput(SETTINGS_MOUSE_POS):
                  clicked = True
                  click_pos = py.mouse.get_pos()
                if SETTINGS_MUSIC.checkForInput(SETTINGS_MOUSE_POS):
                  clicked = True
                  click_pos = py.mouse.get_pos()
            
            if clicked:
                screen.blit(SWITCH_OFF, (362, 390))
                clicked = False

        py.display.update()

def reset():
    while True:
        screen.fill(NAVY_BLUE)
        screen.blit(RESET_BG, RESET_BG_RECT)

        RESET_MOUSE_POS = py.mouse.get_pos()

        RESET_NO = Button(image=None, pos=(600, 593.5))
        RESET_YES = Button(image=None, pos=(0, 593.5))
        reset_buttons = [RESET_NO, RESET_YES]

        # Checks for hovering
        hovered = False
        for button in reset_buttons:
            if button.checkForHover(RESET_MOUSE_POS):
                hovered = True

        # If hovering is true, sets cursor to pointing hand
        if hovered:
            py.mouse.set_cursor(py.SYSTEM_CURSOR_HAND)
        else:
            py.mouse.set_cursor(py.SYSTEM_CURSOR_ARROW)

        # If hovering is true, sets cursor to pointing hand
        if hovered:
            py.mouse.set_cursor(py.SYSTEM_CURSOR_HAND)
        else:
            py.mouse.set_cursor(py.SYSTEM_CURSOR_ARROW)

        # Handles event detection
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                sys.exit()
            if event.type == py.MOUSEBUTTONDOWN:
                if RESET_NO.checkForInput(RESET_MOUSE_POS):
                  options()
                if RESET_YES.checkForInput(RESET_MOUSE_POS):
                  main_menu()

        py.display.update()

def credits():
    while True:
        screen.fill(NAVY_BLUE)      # Fills window with a color
        screen.blit(CREDITS_BACKGROUND, CREDITS_BACKGROUND_RECT)      # Sets the background image

        CREDITS_MOUSE_POS = py.mouse.get_pos()

        CREDITS_BACK = Button(image=None, pos=(19+30, 23+30))

        credits_buttons = [CREDITS_BACK]

        # Checks for hovering
        hovered = False
        for button in credits_buttons:
            if button.checkForHover(CREDITS_MOUSE_POS):
                hovered = True

        # If hovering is true, sets cursor to pointing hand
        if hovered:
            py.mouse.set_cursor(py.SYSTEM_CURSOR_HAND)
        else:
            py.mouse.set_cursor(py.SYSTEM_CURSOR_ARROW)

        # If hovering is true, sets cursor to pointing hand
        if hovered:
            py.mouse.set_cursor(py.SYSTEM_CURSOR_HAND)
        else:
            py.mouse.set_cursor(py.SYSTEM_CURSOR_ARROW)

        # Handles event detection
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                sys.exit()
            if event.type == py.MOUSEBUTTONDOWN:
                if CREDITS_BACK.checkForInput(CREDITS_MOUSE_POS):
                  main_menu()

        py.display.update()



#-----------------------------
#         Main Loop
#-----------------------------

main_menu()