<img src="https://bit.ly/2VnXWr2" alt="Ironhack Logo" width="100"/>

# Project 01 - Python Project: Mastermind
*[Borja Teruelo Vázquez]*

*[DAPT Feb 2021, Barcelona & 27/02/2021]*

## Content
- [Project Description](#project-description)
- [Rules](#rules)
- [Workflow](#workflow)
- [Organization](#organization)
- [Links](#links)

## Project Description
In this project I decided to build Mastermind, a game in which I could practice the recently acquired skills about iteration, lists, tuples, etc. and combine them with functions and classes.

## Rules
The rules of the game are simple: you just need to guess a 4-digit number with the only constraint that these digits cannot be repeated in the number. I.e. '4227' wouldn't be a good guess because the digit '2' appears twice in it.

The objective of the game is to guess the number with the least posible number of attempts and the way to do that is by interpreting the output the machine will provide: on one hand, you'll be provided with the number of digits of your attempt that are contained in the right answer; on the other hand, you'll be provided with the number of digits of your attempt that are not only contained in the right answer but also in the same position.

## Workflow
First I created the game engine just to be executed as a solitaire in the file "Mastermind (solitaire).ipynb". Once tested, I applied it to the approach I had in mind: create 2 classes - one for the human player and another one for the computer player - and create the functions needed so each instance of any class interacts with the game engine. This more complex approach is in the file "Mastermind with classes.ipynb".

## Organization
The project has been organized in a Trello board. All tasks have been achieved except for the improvement of computer AI, which is currently just generating random numbers, which makes it almost impossible to win because it's not taking into account the output. This task included in the "Backlog / nice to have" folder.

Since the game is already thought to be played only 1 human player against the computer, another line was created in the jupyter notebook file "Mastermind with classes.ipynb" creating one instance of each class - one human player and one computer player.

All information in the jupyter notebook file "Mastermind with classes.ipynb" has been copied into the file "Mastermind.py" so the game can be executed from anywhere. The fastest way to execute it would be to import this file in Python, you can do that by running the code in the file "Execution.ipynb".

## Links

[Repository](https://github.com/borjatv/PR01-project-python.git)  
[Slides](https://www.canva.com/design/DAEW4POL-9M/DoJR_4oZhsVJEnP-AZp-yQ/view?utm_content=DAEW4POL-9M&utm_campaign=designshare&utm_medium=link&utm_source=sharebutton  
[Trello](https://trello.com/b/10y0xG4H/mastermind-borja-teruelo)  
