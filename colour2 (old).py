# import pygame

# class ColorSelector:
#   def init(self):
#   self.color_map = {"red": "r", "green": "n", "yellow": "y", "blue": "b", "orange": "o", "purple": "p"}
#   def select_color(self):
#       while True:
#           print("What color would you like to use?")
#           print("\nred \tgreen \tyellow \tblue \torange \tpurple \n")
#           color = input()
  
#           if color.lower() in self.color_map:
#               return self.color_map[color.lower()]
#           else:
#               print("That is not an acceptable color. Please pick from the given list.")
  
#   def display_color(self, color):
#       color_rgb = {"r": (255, 0, 0), "n": (0, 255, 0), "y": (255, 215, 0), "b": (100, 149, 237), "o": (255, 128, 0), "p": (127, 0, 255)}
#       return color_rgb.get(color, None)
  
#   def colourer(self, sequence, guess, c2, c1):
#       index = 0
#       for num in sequence:
#           if num == 2:
#               printy(guess[index], c2, end=" ")
#           elif num == 1:
#               printy(guess[index], c1, end=" ")
#           else:
#               print(guess[index], end=" ")
#           index += 1