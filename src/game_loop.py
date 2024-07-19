import pygame   # Main library that helps with GUI
import sys      # Library that allows accesing files
import random   # Library that randomizes selection
from words import *     # Python file containing words available
from PyDictionary import PyDictionary   # Library that retrieves the definition of the words
dictionary = PyDictionary()     # Initializing the function that retrieves definitions

# Initializes pygame library
pygame.init()

# Constants

# Dimensions of the window
WIDTH, HEIGHT = 600, 800

# Title of the window
pygame.display.set_caption('WordLab')

# Set up icon of window
ICON = pygame.image.load("assets/Icon.png")
pygame.display.set_icon(ICON)

# Loads sound effect when entering keys and pressing buttons
keys_sound_effect = pygame.mixer.Sound("assets/Tick.mp3")
keys_sound_effect.set_volume(0.6)

# Load music
music = pygame.mixer.music.load("assets/music.mp3")

# Sets the screen dimensions
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Start Game Background
PLAY_BACKGROUND = pygame.image.load("assets/START_GAME.png")
PLAY_BACKGROUND_RECT = PLAY_BACKGROUND.get_rect(center=(WIDTH/2, HEIGHT/2))

# Color definitions
GREEN = "#6aaa64"
YELLOW = "#c9b458"
GREY = "#787c7e"
OUTLINE = "#d3d6da"
FILLED_OUTLINE = "#878a8c"

# Selects a random word from a selected array that is used for testing
CORRECT_WORD = random.choice(CORRECT_WORDS)

# Array containing alphabet
ALPHABET = ["QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM"]

# Assigns fonts
GUESSED_LETTER_FONT = pygame.font.Font("assets/FreeSansBold.otf", 50)
AVAILABLE_LETTER_FONT = pygame.font.Font("assets/FreeSansBold.otf", 25)

# Fills screen with color and background
screen.fill("white")
screen.blit(PLAY_BACKGROUND, PLAY_BACKGROUND_RECT)
pygame.display.update()

LETTER_X_SPACING = 76.1
LETTER_Y_SPACING = 22.2
LETTER_SIZE = 70

# Global variables

guesses_count = 0

# guesses is a 2D list that will store guesses. A guess will be a list of letters.
# The list will be iterated through and each letter in each guess will be drawn on the screen.
guesses = [[]] * 6

current_guess = []
current_guess_string = ""
current_letter_bg_x = 110

# Indicators is a list storing all the Indicator object. An indicator is that button thing with all the letters you see.
indicators = []

game_result = ""    # Initializing the game result variable

# Class to create letters
class Letter:
    def __init__(self, text, bg_position):
        # Initializes all the variables, including text, color, position, size, etc.
        self.bg_color = "white"
        self.text_color = "black"
        self.bg_position = bg_position
        self.bg_x = bg_position[0]
        self.bg_y = bg_position[1]
        self.bg_rect = (bg_position[0], self.bg_y, LETTER_SIZE, LETTER_SIZE)
        self.text = text
        self.text_position = (self.bg_x + 36, self.bg_position[1] + 34)
        self.text_surface = GUESSED_LETTER_FONT.render(self.text, True, self.text_color)
        self.text_rect = self.text_surface.get_rect(center = self.text_position)

    def draw(self):
        # Puts the letter and text on the screen at the desired positions.
        pygame.draw.rect(screen, self.bg_color, self.bg_rect)
        if self.bg_color == "white":
            pygame.draw.rect(screen, FILLED_OUTLINE, self.bg_rect, 3)
        self.text_surface = GUESSED_LETTER_FONT.render(self.text, True, self.text_color)
        screen.blit(self.text_surface, self.text_rect)
        pygame.display.update()

    def delete(self):
        # Fills the letter's spot with the default square, emptying it.
        pygame.draw.rect(screen, "white", self.bg_rect)
        pygame.draw.rect(screen, OUTLINE, self.bg_rect, 3)
        pygame.display.update()

# Class to draw the keys down the grid as indicators
class Indicator:
    def __init__(self, x, y, letter):
        # Initializes variables such as color, size, position, and letter.
        self.x = x
        self.y = y
        self.text = letter
        self.rect = (self.x, self.y, 57, HEIGHT / 12)
        self.bg_color = OUTLINE

    def draw(self):
        # Puts the indicator and its text on the screen at the desired position.
        pygame.draw.rect(screen, self.bg_color, self.rect)
        self.text_surface = AVAILABLE_LETTER_FONT.render(self.text, True, "white")
        self.text_rect = self.text_surface.get_rect(center=(self.x+27, self.y+30))
        screen.blit(self.text_surface, self.text_rect)
        pygame.display.update()

# Drawing the indicators on the screen.
indicator_x, indicator_y = WIDTH / 31.65, HEIGHT / 1.34

# Loop that draws letter below
for i in range(3):
    for letter in ALPHABET[i]:
        new_indicator = Indicator(indicator_x, indicator_y, letter)
        indicators.append(new_indicator)
        new_indicator.draw()
        indicator_x += WIDTH / 10.55
    indicator_y += HEIGHT / 12.1
    if i == 0:
        indicator_x = WIDTH / 9.66
    elif i == 1:
        x = WIDTH / 105
        indicator_x = WIDTH / x

def check_guess(guess_to_check):
    # Goes through each letter and checks if it should be green, yellow, or grey.
    global current_guess, current_guess_string, guesses_count, current_letter_bg_x, game_result
    game_decided = False
    for i in range(5):
        lowercase_letter = guess_to_check[i].text.lower()
        if lowercase_letter in CORRECT_WORD:
            if lowercase_letter == CORRECT_WORD[i]:
                guess_to_check[i].bg_color = GREEN
                for indicator in indicators:
                    if indicator.text == lowercase_letter.upper():
                        indicator.bg_color = GREEN
                        indicator.draw()
                guess_to_check[i].text_color = "white"
                if not game_decided:
                    game_result = "W"
            else:
                guess_to_check[i].bg_color = YELLOW
                for indicator in indicators:
                    if indicator.text == lowercase_letter.upper():
                        indicator.bg_color = YELLOW
                        indicator.draw()
                guess_to_check[i].text_color = "white"
                game_result = ""
                game_decided = True
        else:
            guess_to_check[i].bg_color = GREY
            for indicator in indicators:
                if indicator.text == lowercase_letter.upper():
                    indicator.bg_color = GREY
                    indicator.draw()
            guess_to_check[i].text_color = "white"
            game_result = ""
            game_decided = True
        guess_to_check[i].draw()
        pygame.display.update()
    
    guesses_count += 1
    current_guess = []
    current_guess_string = ""
    current_letter_bg_x = 110

    if guesses_count == 6 and game_result == "":
        game_result = "L"

def wrap_text(text, font, max_width):
    words = text.split()
    lines = []
    current_line = []
    current_width = 0

    for word in words:
        word_width, _ = font.size(word + ' ')
        if current_width + word_width > max_width:
            lines.append(' '.join(current_line))
            current_line = [word]
            current_width = word_width
        else:
            current_line.append(word)
            current_width += word_width

    lines.append(' '.join(current_line))
    return lines


def play_again():
    # Puts the play again text on the screen.
    screen.fill(color=(255, 235, 210))

    global meaning
    meaning = dictionary.meaning(CORRECT_WORD)
    meaning_text = " ".join([f"{part}: {', '.join(defs)}" for part, defs in meaning.items()])

    play_again_font = pygame.font.Font("assets/FreeSansBold.otf", 40)
    play_again_text = play_again_font.render("Press ENTER to Play Again!", True, "black")
    play_again_rect = play_again_text.get_rect(center=(WIDTH/2, 700))
    word_was_text = play_again_font.render(f"The word was {CORRECT_WORD}!", True, "black")
    word_was_rect = word_was_text.get_rect(center=(WIDTH/2, 150))

    def_font = pygame.font.Font("assets/FreeSansBold.otf", 20)
    def_text = def_font.render(f"The definition of this word is:", True, "black")
    def_rect = def_text.get_rect(center=(WIDTH/2, 250))

    meaning_font = pygame.font.Font("assets/FreeSansBold.otf", 20)
    max_width = WIDTH - 20  # Adjust the width to fit within the screen
    wrapped_lines = wrap_text(meaning_text, meaning_font, max_width)
    line_height = meaning_font.get_height()
    max_height = HEIGHT - 300  # Adjust the height to fit within the screen
    y_offset = 300  # Start rendering from y=300

    for i, line in enumerate(wrapped_lines):
        if y_offset + line_height > max_height:
            break  # Stop rendering if we reach the maximum height
        meaning_text_surface = meaning_font.render(line, True, "black")
        meaning_rect = meaning_text_surface.get_rect(center=(WIDTH/2, y_offset))
        screen.blit(meaning_text_surface, meaning_rect)
        y_offset += line_height

    screen.blit(def_text, def_rect)
    screen.blit(word_was_text, word_was_rect)
    screen.blit(play_again_text, play_again_rect)
    pygame.display.update()

def reset():
    # Resets all global variables to their default states.
    global guesses_count, CORRECT_WORD, guesses, current_guess, current_guess_string, game_result
    screen.fill("white")
    screen.blit(PLAY_BACKGROUND, PLAY_BACKGROUND_RECT)
    guesses_count = 0
    CORRECT_WORD = random.choice(CORRECT_WORDS)
    guesses = [[]] * 6
    current_guess = []
    current_guess_string = ""
    game_result = ""
    pygame.display.update()
    for indicator in indicators:
        indicator.bg_color = OUTLINE
        indicator.draw()

def create_new_letter(key_pressed):
    keys_sound_effect.play()
    # Creates a new letter and adds it to the guess.
    global current_guess_string, current_letter_bg_x
    current_guess_string += key_pressed
    # Initial Y position for start drawing rows
    first_row_y = 56.8
    new_letter = Letter(key_pressed, (current_letter_bg_x, first_row_y + guesses_count * 88 + LETTER_Y_SPACING))
    current_letter_bg_x += LETTER_X_SPACING
    guesses[guesses_count].append(new_letter)
    current_guess.append(new_letter)
    for guess in guesses:
        for letter in guess:
            letter.draw()

def delete_letter():
    # Deletes the last letter from the guess.
    global current_guess_string, current_letter_bg_x
    guesses[guesses_count][-1].delete()
    guesses[guesses_count].pop()
    current_guess_string = current_guess_string[:-1]
    current_guess.pop()
    current_letter_bg_x -= LETTER_X_SPACING

def GameLoop():
    # Function to keep the game running
    # Play music indefinitely
    pygame.mixer.music.play(loops=-1)
    while True:
        if game_result != "":
            play_again()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if game_result != "":
                        reset()
                    else:
                        if len(current_guess_string) == 5 and current_guess_string.lower() in WORDS:
                            check_guess(current_guess)
                elif event.key == pygame.K_BACKSPACE:
                    if len(current_guess_string) > 0:
                        delete_letter()
                else:
                    key_pressed = event.unicode.upper()
                    if key_pressed in "QWERTYUIOPASDFGHJKLZXCVBNM" and key_pressed != "":
                        if len(current_guess_string) < 5:
                            create_new_letter(key_pressed)  

GameLoop()