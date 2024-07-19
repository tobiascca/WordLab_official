import pygame as py
import sys

import pygame.locals
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
        
# Class to create buttons with images
class ImageButton:
    def __init__(self, image, pos):
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.hovered = False

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

# Sounds
switch_sound = pygame.mixer.Sound("assets/switch_sound.mp3")
switch_sound.set_volume(0.6)
button_sound = pygame.mixer.Sound("assets/brightness_sound.mp3")
button_sound.set_volume(0.6)

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
SWITCH_ON = py.image.load("assets\SWITCH_ON.png")
SWITCH_OFF = py.image.load("assets\SWITCH_OFF.png")

# Play music indefinitely
pygame.mixer.music.play(loops=-1)

#-----------------------------
#       Window events
#-----------------------------

MN_BTTN_SPACING = 23

def main_menu():    # Main menu screen
    # Toggle states for SFX and music buttons
    sfx_on = True

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
                    if sfx_on:
                        button_sound.play()
                    else:
                        button_sound.stop()
                if CREDITS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    credits()
                    if sfx_on:
                        button_sound.play()
                    else:
                        button_sound.stop()
                if EXIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    if sfx_on:
                        button_sound.play()
                    else:
                        button_sound.stop()
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
    # Toggle states for SFX and music buttons
    sfx_on = True
    music_on = True

    # Default brightness value
    brightness_value = 50

    while True:
        screen.fill(NAVY_BLUE)      # Fills window with a color
        screen.blit(SETTINGS_BACKGROUND, SETTINGS_BACKGROUND_RECT)      # Sets the background image

        SETTINGS_BACK = Button(image=None, pos=(19+30, 23+30))
        SETTINGS_BRIGHTNESS_DOWN = Button(image=None, pos=(300, 340))
        SETTINGS_BRIGHTNESS_UP = Button(image=None, pos=(600, 340))
        SETTINGS_SFX_SWITCH = ImageButton(image=SWITCH_ON if sfx_on else SWITCH_OFF, pos=(435, 421))
        SETTINGS_MUSIC_SWITCH = ImageButton(image=SWITCH_ON if music_on else SWITCH_OFF, pos=(435, 505))
        
        # Variables to get mouse position and left click
        settings_mouse_pos = py.mouse.get_pos()
        settings_mouse_pressed = py.mouse.get_pressed()
        
        # Display brightness value
        font = pygame.font.Font(None, 60)
        brightness_text = font.render(f'{brightness_value}', True, (0, 0, 0))
        brightness_text_rect = brightness_text.get_rect(center=(435, 314))
        screen.blit(brightness_text, brightness_text_rect)

        settings_buttons = [SETTINGS_BACK, SETTINGS_BRIGHTNESS_DOWN, SETTINGS_BRIGHTNESS_UP,
                            SETTINGS_SFX_SWITCH, SETTINGS_MUSIC_SWITCH]

        # Checks for hovering
        hovered = False
        for button in settings_buttons:
            if button.checkForHover(settings_mouse_pos):
                hovered = True

        # If hovering is true, sets cursor to pointing hand
        if hovered:
            py.mouse.set_cursor(py.SYSTEM_CURSOR_HAND)
        else:
            py.mouse.set_cursor(py.SYSTEM_CURSOR_ARROW)

        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                sys.exit()
            if event.type == py.MOUSEBUTTONDOWN:
                if SETTINGS_BACK.checkForInput(settings_mouse_pos):
                  main_menu()
                if SETTINGS_BRIGHTNESS_DOWN.checkForInput(settings_mouse_pos):
                    print("Brightness Down button clicked")
                    brightness_value = max(0, brightness_value - 10)  # Decrease brightness by 10 (minimum 0)
                    if sfx_on:
                        button_sound.play()
                    else:
                        button_sound.stop()
                if SETTINGS_BRIGHTNESS_UP.checkForInput(settings_mouse_pos):
                    print("Brightness Up button clicked")
                    brightness_value = min(100, brightness_value + 10)  # Increase brightness by 10 (maximum 100)
                    if sfx_on:
                        button_sound.play()
                    else:
                        button_sound.stop()
                if SETTINGS_SFX_SWITCH.checkForInput(settings_mouse_pos):
                    sfx_on = not sfx_on
                    SETTINGS_SFX_SWITCH.image = SWITCH_ON if sfx_on else SWITCH_OFF
                    print("SFX switch button clicked")
                    switch_sound.play()
                    if sfx_on != True:
                        switch_sound.set_volume(0)
                    else:
                        switch_sound.set_volume(0.6)
                if SETTINGS_MUSIC_SWITCH.checkForInput(settings_mouse_pos):
                    music_on = not music_on
                    switch_sound.play()
                    SETTINGS_MUSIC_SWITCH.image = SWITCH_ON if music_on else SWITCH_OFF
                    if music_on != True:
                        pygame.mixer.music.stop()
                    else:
                        pygame.mixer.music.play(-1)
                    print("Music switch button clicked")

        # Redraw everything
        screen.blit(SETTINGS_SFX_SWITCH.image, SETTINGS_SFX_SWITCH.rect)
        screen.blit(SETTINGS_MUSIC_SWITCH.image, SETTINGS_MUSIC_SWITCH.rect)

        py.display.update()

def reset():
    # Loop for reset window
    while True:
        # Set window background
        screen.fill(NAVY_BLUE)
        screen.blit(RESET_BG, RESET_BG_RECT)

        RESET_MOUSE_POS = py.mouse.get_pos()

        # Reset buttons definition
        RESET_NO = Button(image=None, pos=(560, 593.5))
        RESET_YES = Button(image=None, pos=(40, 593.5))
        reset_buttons = [RESET_NO, RESET_YES]       # Array containing all buttons

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

# main_menu()