"""
Developers: Helen, Chris, Alex, and Fisher
File: main.py
Date finished: Jan 20, 2023.
About Program: Garble - Word Game
A program to allow users to play Garble. Users interact with pygame 
window as well as the console to guess a randomly generated 5-letter
word. 

The program features a colour selector and a leaderboard in addition 
to the gameplay. 

This file contains all classes and functions required to run the game. 
Uses graphics and colour libraries to create a visually appealing output.
"""

import pygame, pygame_menu, sys, random
from colorama import Fore # used to print coloured text onto console
pygame.init()

class Colour:
    """
    A class representing the different colours used in the game.
    Includes default colors and options for user to choose from.
    
    Attributes
    ----------
    GREY : tuple
        RGB value of grey
    BLACK : tuple
        RGB value of black
    WHITE : tuple
        RGB value of white
    GREEN : tuple
        RGB value of green
    YELLOW : tuple
        RGB value of yellow
    RED : tuple
        RGB value of red
    BLUE : tuple
        RGB value of blue
    MAGENTA : tuple
        RGB value of magenta
        
    Methods
    -------
    options()
        Prints out an explanation of the colour options
    
    enter_colour()
        Takes in the user's colour choice
    
    assign_colour(c):
        Assigns the user's colour choice to the instance variables
        
    get_colour() 
        Returns the colour chosen by the user in the form of rgb 
        and colorama.
    """
    
    GREY = (128, 128, 128)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    YELLOW = (255, 215, 0)
    RED = (255, 0, 0)
    BLUE = (100, 149, 237)
    MAGENTA = (127, 0, 255)

    def __init__(self):
        """Colour Class Constructor to initialize the object.
        
        Initializes instance variables rgb and fore as empty strings.
        """
       
        self.rgb = ""
        self.fore = ""
    
    def options():
        """Prints default colours and colour options."""
        
        print("Default Colours:")
        print("Correct Letter Placement In Word = " + Fore.GREEN + "GREEN" + Fore.RESET)
        print("Incorrect Letter Placement In Word = " + Fore.YELLOW + "YELLOW" + Fore.RESET)
        print("\nOptions:")
        print(Fore.GREEN + "GREEN\n" + Fore.YELLOW + "YELLOW\n" + Fore.RED + "RED\n" + Fore.BLUE + "BLUE\n" + Fore.MAGENTA + "MAGENTA" + Fore.RESET)

    def enter_colour(self):
        """Takes in the user's desired colour.

        The method repeats until the user enters a valid colour option. 
        """
        
        while self.rgb == "":
            print("Enter Desired Colour: ", end="")
            colour = input().upper()
            self.assign_colour(colour)
    
    def assign_colour(self, c):
        """Assigns the user's desired colour to the instance variables rgb
        and fore.

        Parameters
        ----------
        c : str
            The desired colour
        """
        
        if c == "GREEN":
            self.rgb = Colour.GREEN
            self.fore = Fore.GREEN
        elif c == "YELLOW":
            self.rgb = Colour.YELLOW
            self.fore = Fore.YELLOW   
        elif c == "RED":
            self.rgb = Colour.RED
            self.fore = Fore.RED   
        elif c == "BLUE":
            self.rgb = Colour.BLUE
            self.fore = Fore.BLUE  
        elif c == "MAGENTA":
            self.rgb = Colour.MAGENTA
            self.fore = Fore.MAGENTA
        else:
            print("Select a given colour option.")

    def get_colour(self):
        """Returns the desired colour.
        
        Returns
        -------
        self.rgb
            rgb value of colour
        self.fore
            fore value of colour
        """
        
        return self.rgb, self.fore

class Guess:
    """
    A class used to handle all methods related to guesses.
    
    ...
    
    Methods
    -------
    get_guess()
        Returns guess
    
    get_sequence()
        Returns sequence
    
    input_guess()
        Retrieves input from user, ensures input is five characters long, 
        then converts the string input to list
        
    compare()
        Compares guess list to answer list and creates a sequence comparison
    """
  
    def __init__(self, answer):
        """Guess Class Constructor to initialize the object.

        Parameters
        ----------
        answer : list
            The word to be guessed; each item in the list is a 
            character
            
        Instance Attributes
        -------------------
        self.answer : list
            Randomly generated word to be guessed
        
        self.answer_copy : list
            A copy of answer; used for comparisons
        
        self.guess : str
            An empty string; later a guess list will be stored
        
        self.sequence : list
            A list of five '0' items; later will be the result of 
            the comparison between answer and guess
                2 means correct letter in correct place, 
                1 means letter is found in answer,
                0 means letter is not found in answer
            """
        
        self.answer = answer
        self.answer_copy = answer[:]
        self.guess = ""
        self.sequence = [0, 0, 0, 0, 0]

    def get_guess(self):
        """Returns instance variable guess"""
        
        return self.guess

    def get_sequence(self):
        """Returns instance variable sequence"""
        
        return self.sequence

    def input_guess(self):
        """Retrieves input from the user
        
        Ensures guess is five characters long, in the guessables file,
        then converts the string input to a list. Continues to run until
        the user enters a valid guess.
        """
        
        while True:
            self.guess = input("Enter Guess: ").lower()
            if len(self.guess) == 5:
                guessables_file = open("guessables.txt")
                if (self.guess + "\n") in guessables_file.readlines():
                    self.guess = list(self.guess)
                    break
                else:
                    print("Guess is not a word! \n")
            else:
                print("Guess must be 5 letters! \n")

    def compare(self):
        """Compares the guess list to answer list.
        
        Creates sequence comparison. Each item represents the similarities 
        between the guess and the answer for the mirrored letter
            2 means correct letter in correct place, 
            1 means letter is found in answer,
            0 means letter is not found in answer
        """
        
        for i in range(5):
            if self.guess[i] == self.answer[i]:
                self.sequence[i] = 2
                self.answer_copy[i] = None
        for i in range(5):
            if (self.guess[i] in self.answer_copy) and (self.sequence[i] == 0):
                self.sequence[i] = 1
                self.answer_copy.remove(self.guess[i])

class Display:
    """
    A class used to handle all methods related to the display of guesses on 
    the game window.
    
    ...
    
    Methods
    --------
    to_console()
        Directs player's attention to the console
        
    guess(sequence, all_guesses)
        Displays the player's guess onto the game window 
        with the correct colour
        
    """
    
    def __init__(self, c2, c1):
        """Display Class Constructor to initialize the object.

        Displays the tiles onto the game window.
        
        Parameters
        ----------
        c2 : tuple
            RGB value of the colour for letters in the correct position

        c1 : tuple
            RGB value of the colour for letters in the word, but in the 
            incorrect position

        Instance Attributes
        -------------------
        self.letter_y_spacing : int
            The pixel distance from the top of the game window at which the 
            first letter in the round should be displayed at
        """
        
        screen.fill(Colour.WHITE)
        screen.blit(tiles, tiles_rect)
        pygame.display.flip()
        self.c2 = c2
        self.c1 = c1
        self.letter_y_spacing = 27

    
    def to_console():
        """Directs player's attention to the console."""
        
        screen.fill(Colour.WHITE)
        font = pygame.font.SysFont("chalkduster.ttf", 50)
        text = font.render("<Go to Console>", True, Colour.BLACK)
        text_rect = text.get_rect()
        text_rect.center = (WIDTH/2, HEIGHT/2)
        screen.blit(text, text_rect)
        pygame.display.flip()

    def guess(self, sequence, all_guesses):
        """Displays the characters in colour on the game window
        
        Parameters
        ----------
        sequence : list
            Items indicate the similarities between answer and player's guess. 
            Item 0 means letter is not in the word. Item 1 means letter is 
            present in the word, but in the wrong place. Item 2 means letter
            is present in the word and in the right place.
            
        all_guesses : 2D array
            Contains all of the player's guesses in the round. Each item in the 
            outer array represents a guess. Each item in the inner array represents 
            a character in that specific guess. 
        """
        
        letter_x_spacing = 76
        font = pygame.font.SysFont("chalkduster.ttf", 65)
        
        for i in range(5):
            letter = all_guesses[-1][i].upper()
            if sequence[i] == 2:
                letter = font.render(letter, True, self.c2)
            elif sequence[i] == 1:
                letter = font.render(letter, True, self.c1)
            else:
                letter = font.render(letter, True, Colour.GREY)

            screen.blit(letter, (letter_x_spacing, self.letter_y_spacing))
            letter_x_spacing += 60
            pygame.display.flip()
        self.letter_y_spacing += 73

class Console:
    """
    A class used to represent the display of the Console.

    ...

    Methods
    -------
    guess(sequence, all_guesses)
        Prints the updated coloured keyboard based on user's guess. 
    """

    def __init__(self, fore2, fore1):
        """Console Class Constructor to initialize the object.
        
        Parameters
        ----------
        fore2 : str
            The colour for correct letter placement in word
            
        fore1 : str
            The colour for incorrect letter placement in word

        Instance Attributes
        -------------------
        self.keybaord : str
            String of a keybaord

        self.guessed_letters : list    
            Empty list; later user's past guessed letters are 
            added
        """
        
        self.fore2 = fore2
        self.fore1 = fore1
        self.keyboard = "\nQ W E R T Y U I O P\n A S D F G H J K L\n   Z X C V B N M"
        self.guessed_letters = []

    def guess(self, sequence, all_guesses):
        """Prints out a coloured keyboard based on player's guess.

        If the player guesses a correct letter placement, the letter
        will appear in the fore2 colour for the rest of the round. If 
        the player guesses an incorrect letter placement, the letter will 
        appear in the fore1 colour. If the user guesses a letter which 
        is not in the word, the letter is replaced by an underscore.

        Parameters
        ----------
        sequence : list
            Items indicate the similarities between answer and player's guess. 
            Item 0 means letter is not in the word. Item 1 means letter is 
            present in the word, but in the wrong place. Item 2 means letter
            is present in the word and in the right place.
            
        all_guesses : 2D array
            Contains all of the player's guesses in the round. Each item in the 
            outer array represents a guess. Each item in the inner array represents 
            a character in that specific guess. 
        """
        
        for i in range(5):
            letter = all_guesses[-1][i].upper()
            index = self.keyboard.find(letter)
            if sequence[i] == 2:
                self.keyboard = self.keyboard[:index] + self.fore2 + self.keyboard[index] + Fore.WHITE + self.keyboard[index+1:]
                
            elif (sequence[i] == 1) and (letter not in self.guessed_letters):
                self.keyboard = self.keyboard[:index] + self.fore1 + self.keyboard[index] + Fore.WHITE + self.keyboard[index+1:]
                
            elif letter not in self.guessed_letters:
                self.keyboard = self.keyboard[:index] + "_" + self.keyboard[index+1:]
            self.guessed_letters.append(letter)
        print(self.keyboard)

def word_generator():
    """Picks a 5-letter word from the wordlist file."""
    
    answer = []
    x = random.randint(1, 2315)
    wordlist_file = open("wordlist.txt").readlines()
    for i in wordlist_file[x][:5]:
        answer.append(i) 
    return answer

def write_score(name, num_guesses):
    """Records player's name and number of guesses. 

    Writes score down only if player is new or number of guesses
    is lower than the number of guesses recorded previously.
    
    Parameters
    ----------
    name : str
        User inputted name
        
    num_guesses : int
        Number of guesses the user used to guess the word
    """
    
    guesses = num_guesses
    file = open("score.txt", "r")
    new = ""
    flag = False
    for i in file:
        if name not in i:
            new += i
        elif name in i and int(i[-2]) > guesses:
            new += name + ", Guesses: " + str(guesses) + "\n"
            flag = True
        elif name in i:
            new += i
            flag = True 
    file.close()
    file = open("score.txt", "w")
    file.write(new)
    file.close()
    file = open("score.txt", "a")
    if flag == False:
        file.write(name + ", Guesses: " + str(guesses) + "\n" )
      
def menu():
    """Runs the menu."""
    
    menu = pygame_menu.Menu('GARBLE', WIDTH, HEIGHT, theme=pygame_menu.themes.THEME_GREEN)
    menu.add.button("Play", main)
    menu.add.button("Select Colour", select_colour)
    menu.add.button("Leaderboard", leaderboard)
    menu.add.button("Exit", exit)
    menu.mainloop(screen)

def select_colour():
    """Lets users choose correct letter and incorrect letter placement colours."""
    
    global c2, c1, fore2, fore1
    Display.to_console()
    Colour.options()
    
    print("For Correct Letter Placement In Word...")
    correct_colour = Colour()
    correct_colour.enter_colour()
    c2, fore2 = correct_colour.get_colour()

    print("For Incorrect Letter Placement In Word...")
    incorrect_colour = Colour()
    incorrect_colour.enter_colour()
    c1, fore1 = incorrect_colour.get_colour()

def leaderboard():
    """Displays players' names and their best number of guesses.
    
    Displays in order from lowest number of guesses to highest.
    """

    filename = r"score.txt"
    with open(filename) as file:
        lines = file.readlines()
    
    sortedList = []
    for number, line in enumerate(lines, 1):
        for i in range(5):
            score = i+1
            if str(score) in line:
                name = line.split(",")[0]
                sortedList.append("Number of Guesses: " + str(score) + " --- " + name)
    print("="*50)
    
    sortedList = sorted(sortedList)
    for i in sortedList:
        print(i)

def exit():
    """Terminates the program."""
    
    pygame.quit()
    sys.exit()
    exit()

WIDTH, HEIGHT = 420, 460
c2, c1 = Colour.GREEN, Colour.YELLOW
fore2, fore1 = Fore.GREEN, Fore.YELLOW

screen = pygame.display.set_mode((WIDTH, HEIGHT))
tiles = pygame.image.load("StartingTiles.png")
tiles = pygame.transform.scale(tiles, (293, 428))
tiles_rect = tiles.get_rect(center=(WIDTH/2, HEIGHT/2))

def main():    
    """Main function for running the guessing game. 
    
    Handles the overall flow of the game, using methods for initializing 
    and displaying the game screen, accepting user input for guesses, 
    and keeping track of the number of remaining guesses.
    """
    
    global c2, c1, fore2, fore1
    running = True
    while running:
        num_guesses = 6
        all_guesses = []
        name = input("Enter Name: ")
        answer = word_generator()
        show_screen = Display(c2, c1)
        show_console = Console(fore2, fore1)
        
        while num_guesses > 0:
            current_guess = Guess(answer)
            current_guess.input_guess()
            current_guess.compare()
    
            all_guesses.append(current_guess.get_guess())
            sequence = current_guess.get_sequence()

            show_screen.guess(sequence, all_guesses)
            show_console.guess(sequence, all_guesses)
            
            num_guesses -= 1
            if sequence == [2, 2, 2, 2, 2]:
                break
        write_score(name, 6 - num_guesses)
        print("The word was: " + "".join(answer))
        play_again = input("Continue playing? (Y/N) ").upper()
        if play_again == "N":
            running = False

menu()