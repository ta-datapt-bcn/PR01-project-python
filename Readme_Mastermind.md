<img src="https://bit.ly/2VnXWr2" alt="Ironhack Logo" width="100"/>

# Title of Your Project
*[Gloria Camp]*

*[Data Analysis, Barcelona & 27 Feb 2021]*

## Content
- [Project Description](#project-description)
- [Rules](#rules)
- [Workflow](#workflow)
- [Organization](#organization)
- [Links](#links)

## Project Description
In this project I have created the **game Mastermind** where the user interacts with the computer.  My game will be able to take an input from the user and provide an output from the computer. 

## Rules

Goal: to guess a secret code consisting of a series of 4 colored pegs. Each guess results in feedback narrowing down the possibilities of the code. 

Number of players: 2 (the player and the computer)

Game pieces: 

- A set of colored pegs (yellow, red, blue, green, pink, orange)
- A set of white and black answer pegs
- Board: 8 X 10

Players: 

- Code maker (the computer): 
    1. The computer will place any combination of 4 colored pegs on a line. 
    2. In response to the player's choice:
        The computer will use the white pegs to indicate how many pegs are the correct color but wrong position.
        The computer will use a black peg to indicate how many pegs are in a correct position and are the right color. 
        If neither are true, then no peg should be placed. 
- Code guesser (the player):
    1. The player will have to place 4 color pegs in every round (colors can be repeated)
    2. The code guesser only

Note: The code maker may place these pegs in any order. 

Number of guesses = 10

End of the game: Play continues until the code is discovered by the code guesser or there are no remaining guesses.

## Workflow

1. I researched the game rules
2. I designed the game structure 
3. I coded the game, first different functions and then I joined it all in a class
4. I created a .py document

## Organization
I used trello, please see link further down. 

My repository contains the following files: 
- Read_Mastermind.me 
- Mastermindfinal.py 
- Mastermindparts.ipynb (contains the different functions separately)
- Mastermindfinal.ipynb (contains the code in a class)


## Links

[Repository]https://github.com/Glory85/PR01-project-python.git  
[Trello] https://trello.com/invite/b/XUo4npN2/9ac21bf88fa0e38aa954f2e0a3450a38/project-1-build-your-own-game-mastermind
