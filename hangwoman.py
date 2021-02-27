import random

words = ["apple","chair","computer","animal","pencil","yogurt","water","medicine","kitchen","table","watch","vacuum","movies","telephone","shower","work"]

words_upper = list(map(lambda i: i.upper(), words))
pictures = [
 """
  __________
  |        |
  |       \😀/
  |        |
  |       / \ 
 _|____
 """,

 """
  __________
  |        |
  |       \😀/
  |        |
  |       / 
 _|____
 """,

 """
  __________
  |        |
  |       \😀/
  |        |
  |      
 _|____
  """,
 """
  __________
  |        |
  |       \😀
  |        |
  |      
 _|____
 """,
 """
  __________
  |        |
  |        😀
  |        |
  |     
 _|____
 """,
 """
  __________
  |        |
  |        😀
  |        
  |     
 _|____
 """,
 """
  __________
  |        |
  |        
  |        
  |     
 _|____
 """]

word= (random.choice(words_upper))
print(word)
to_guess = "-" * len(word)

print( "Hi! let's play Hangwomen!")
player = input("What is your name? \n")
print(f"Ok {player}, below are the rules: \n ""1. I will choose a word and you need to guess the word \n 2. You have a total of 6 tries, you can either try to guess a letter or a word \n Let's start!")

n = 6
stage = pictures[n]

def check_game_over():
    global n

    if n == 0:
        print(f"Auch! your hangman is dead, you lost! \n The word {word}")

    else:
        print(pictures[n])
    
    print(to_guess)

    return n > 0

# Game execution

def ask_user_guess():
    guess = input("Please input the letter you want to guess: \n").upper()
    return guess[0]

def update_cypher(guess):
    global word
    global to_guess
    chars = []
    for i in range(len(word)):
        if word[i] == guess:
            chars.append(guess)
        else:
            chars.append(to_guess[i])
    to_guess = "".join(chars)

while check_game_over() > 0:
    user_letter = ask_user_guess() 
    if user_letter in word:    
        update_cypher(user_letter)
        print(f"Great! the letter {user_letter} is part of the word")

        if to_guess ==  word:
            print("Congratulations, you guesses your mother fucker! ")
            break
    else:
        n = n - 1