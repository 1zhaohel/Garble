# from printy import printy

# def select_colour():
#   while True:
#     print("What colour would you like to use?")
#     print("\nred \tgreen \tyellow \tblue \torange \tpurple \n")
#     colour = input()

#     if colour.lower() == "red":
#       return "r"
#     elif colour.lower() == "green":
#       return "n"
#     elif colour.lower() == "yellow":
#       return "y"
#     elif colour.lower() == "blue":
#       return "b>"
#     elif colour.lower() == "orange":
#       return "o"
#     elif colour.lower() == "purple":
#       return "p"
#     else:
#       print("That is not an acceptable colour. Please pick from the given list.")

# def display_colour(colour):
#    if colour == "r":
#      return (255, 0, 0)
#    elif colour == "n":
#      return (0, 255, 0)
#    elif colour == "y":
#      return (255, 215, 0)
#    elif colour == "b>":
#      return (100, 149, 237)
#    elif colour == "o":
#      return (255, 128, 0)
#    else:
#      return (127, 0, 255)

# def colourer(sequence, guess, c2, c1):
#   index = 0
#   for num in sequence:
#     if num == 2:
#       printy(guess[index], c2, end=" ")
#     elif num == 1:
#       printy(guess[index], c1, end=" ")
#     else:
#       print(guess[index], end=" ")
#     index += 1