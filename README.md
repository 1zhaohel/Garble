# Garble
A game developed by Helen, Chris, Alex, and Fisher

## Game Description
Garble is a guessing word-based game which involves the player making guesses of 5-letter words until they have correctly guessed the word or attempted 6 guesses. After guessing a word, the game will display if any of the letters guessed are correct.  For example, by default, the pygame window will display green for a letter in the correct spot, yellow if the letter is in the word but in the incorrect spot, and grey if the letter is not in the word. 

## Standout Features
- The computer generates a 5-letter random word from a file of **2 315 words**. If a player played once every day, this would be enough to last them 6.43 years!
- Worry not! Obscure 5-letter words will be valid, the game has a separate file containing **12 973** 5-letter words to check the validity of the player's guess.
- A colour selector for the player to personalize their experience. Players can choose green, yellow, red, blue, or magenta!
- A leaderboard adds a competitive aspect to the game--players are rewarded for their quick-thinking. The leaderboard displays the players in order from lowest number of guesses to highest. 
- A keyboard which updates every time the player guesses. By default, if the letter is in the right spot, the letter will be displayed as green; if the letter is not in the right spot, the letter will be displayed as yellow; if the letter is not in the word, the letter will be replaced with an underscore ('_').
- A game window to view all of the player's past guesses in the round along with the letter colour indicating similarities between the guess and the answer for each guess.

## Game Instructions
1. When the game starts, players are greeted with a simple menu. They have the option to select Play, Colour Selector, Leaderboard, or Exit.
    - If they press Play immediately, they will begin with the default colours (green and         yellow).
    - If they choose to change the colours, they will have to choose 2 colours they would         like to use. After selection, the program will take them back to the main menu.
2. Once the player clicks play, a 5x6 grid will appear and the game will ask for the name of the player.
3. It will then ask for a valid 5-letter guess in the console. Click enter and it will reveal the correct placed letters, the incorrect placed letters, and letters not in the word.
4. The game will continue until players guess correctly or use all 6 attempts.
5. The player will then have the option to continue or go back to the main menu

## Input Specification
- Menu options are in the game window that players can click with a cursor. Everything else is to be typed in the console.
- When entering a colour, players must use one of the colours listed
- All guesses in the game must be a valid 5-letter word
- If these input specifications are not met, the game will let ask for a new input