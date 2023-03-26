"""
TODO:
- DONE | add tiles to game window 
- DONE | implement previous guesses list (try to use a 2D array) 
- DONE | make console inputs display on tiles 
- DONE | background squares for correct placement or in word 
- DONE | colourblind mode? 
- DONE | score keeping with persistent file data? 
- DONE | organise code into classes 
- DONE | create some sort of keyboard for users to keep track of their letter guesses
- internal documentation like docstrings
- DONE | make a return button
- DONE | leaderboard sorted by least guesses taken

- - - FIX printy.exceptions.InvalidFlag: '[' is not a valid flag WHEN WINNING

"""
import pygame, pygame_menu, sys, random, colour
from printy import printy

pygame.init()

# Constants
WIDTH, HEIGHT = 420, 460
DIVIDER = "—" * 65
HEADER = "=" * 65

WHITE = (255, 255, 255)
GREY = (128, 128, 128)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Screen
pygame.display.set_caption("GARBLE.CO")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
tiles = pygame.image.load("StartingTiles.png")
tiles = pygame.transform.scale(tiles, (293, 428))
tiles_rect = tiles.get_rect(center=(WIDTH/2, HEIGHT/2))

# Global Variables
c2, c1 = "n", "y"

def generate_word():
  """
  Picks a random word from wordlist.txt as the word to guess

    Returns:
      chosen_word (list): list of individual characters in the word
  """
  x = random.randint(1, 2315)
  file = open("wordlist.txt").readlines()
  chosen_word = []
  for i in file[x][:5]:
    chosen_word.append(i)

  print(chosen_word)
  
  return chosen_word


def get_guess():
  """
  Retrieves a valid guess from the user.

    Return:
      guess (list): guess is returned as a list. each item of the list is a character.
  """
  while True:
    guess = input("What is your guess? ").lower()
    if len(guess) == 5:
      file = open("guessables.txt")
      if guess + "\n" in file.readlines():
        return list(guess)
      else:
        print("Not a word! \n")
    else:
      print("Guess is not 5 letters! \n")


def guess_comparer(guess, answer, keyboard, c2, c1):
  sequence = [0, 0, 0, 0, 0]
  copy = answer[:]
  green = "[" + c2 + "]"
  yellow = "[" + c1 + "]"
  
  for i in range(5):
    if guess[i] == answer[i]:
      sequence[i] = 2
      copy[i] = None
      if green + guess[i] + "@" not in keyboard:
        if yellow + guess[i] + "@" in keyboard:
          keyboard = keyboard.replace(yellow + guess[i] + "@", green + guess[i] + "@")
        else:
          keyboard = keyboard.replace(guess[i], green + guess[i] + "@")
          
  for i in range(5):
    if guess[i] in copy and sequence[i] == 0:
      sequence[i] = 1
      copy.remove(guess[i]) 
      if green + guess[i] + "@" not in keyboard:
        if yellow + guess[i] + "@" not in keyboard:
          keyboard = keyboard.replace(guess[i], yellow + guess[i] + "@")

  for i in range(5):
    if sequence[i] == 0:
      if green + guess[i] + "@" not in keyboard:
        if yellow + guess[i] + "@" not in keyboard:
          keyboard = keyboard.replace(guess[i], " ")
  printy(keyboard + "\n")
  return sequence, keyboard


def display_guesses(letter_y_spacing, sequence):
  letter_x_spacing = 76
  font = pygame.font.SysFont('chalkduster.ttf', 65)
  correct_colour = colour.display_colour(c2)
  in_word_colour = colour.display_colour(c1)

  for i in range(5):
    letter = past_guesses[-1][i].upper()
    if sequence[i] == 2:
      letter = font.render(letter, True, correct_colour)
    elif sequence[i] == 1:
      letter = font.render(letter, True, in_word_colour)
    else:
      letter = font.render(letter, True, GREY)

    screen.blit(letter, (letter_x_spacing, letter_y_spacing))
    pygame.display.update()
    letter_x_spacing += 60


def display_console():
  screen.fill(BLACK)
  font = pygame.font.SysFont('chalkduster.ttf', 50)
  text = font.render("< Go to Console >", True, GREEN)
  text_rect = text.get_rect()
  text_rect.center = (WIDTH // 2, HEIGHT // 2)
  screen.blit(text, text_rect)
  pygame.display.flip()


def menu():
  menu = pygame_menu.Menu('GARBLE', WIDTH, HEIGHT, theme=pygame_menu.themes.THEME_GREEN)
  
  menu.add.button('Play', start_the_game)
  menu.add.button('Colour Selector', colours)
  menu.add.button('Leaderboard', leaderboard)
  menu.add.button('Quit', close)
  menu.mainloop(screen)


def start_the_game():
  running = True 
  while running:
    screen.fill(WHITE)
    screen.blit(tiles, tiles_rect)
    pygame.display.flip()
    main(c2, c1)
    again = input("Continue playing? (Y/N) ").upper()
    if again == "N":
      break

    
def colours():
  global c2, c1
  display_console()
  
  print(HEADER)
  print("Type in the colour you would like displayed for correct letters in the correct position.", end = " ")
  c2 = colour.select_colour()
  print(DIVIDER)
  
  print("Type in the colour you would like displayed for  correct letters in the wrong position.", end = " ")
  c1 = colour.select_colour()
  print(HEADER)


def write_score(name, guesses):
  guesses = guesses + 1
  file = open("score.txt", "r")
  new = ""
  flag = False
  for i in file:
    if name not in i:
        new += i
    elif name in i and int(i[-2]) > guesses:
        new += name + ", Guesses: " + str(guesses)
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


def leaderboard():  
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


def close():
  pygame.quit()
  sys.exit()
  exit()

  
def main(green, yellow):
  global past_guesses
  past_guesses = [] 
  letter_y_spacing = 27
  answer = generate_word()  
  currentKeyboard = "q w e r t y u i o p\n a s d f g h j k l\n   z x c v b n m"
  name = input("What is your name? ")
  
  for i in range(6):
    guess = get_guess()
    past_guesses.append(guess)
    
    sequence, currentKeyboard = guess_comparer(guess, answer, currentKeyboard, green, yellow)
    
    display_guesses(letter_y_spacing, sequence)
    letter_y_spacing += 73
    colour.colourer(sequence, guess, green, yellow)

    if sequence == [2, 2, 2, 2, 2]:
      print("Correct. You win!")
      write_score(name, i)
      break
    else:
      print("\n")

  printy("The word was: ", end=" ")
  printy(" ".join(answer), "n", end="\n\n")
  
menu()