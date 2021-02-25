import random
import pandas as pd

class Mastermind():
    def __init__(self):
        self.column_names = ["P1", "P2", "P3", "P4","C1", "C2", "C3","C4"]
        self.board = pd.DataFrame(columns = self.column_names)
        self.colorpegs = ["yellow", "red", "blue", "green", "pink", "orange"]
        self.tips = []
        
    def codemaker_choice(self):
        return random.choices(self.colorpegs,k=4)

    def codeguesser_choice(self):
        while True:
            try:
                self.choice = input ("""Enter four colors separated by a space(you can repeat them): 
                Remember, your options are: yellow red blue green pink orange: """).split()
                if not (all([i in self.colorpegs for i in self.choice]) and len(self.choice) == 4):
                    raise ValueError
                break
            except: 
                print("you need to put 4 colors from the list, an example would be: green yellow blue red")
        return self.choice
        
    def codemaker_r(self,x,y):
        for i, j in zip(x, y): 
            if i == j:
                self.tips.append("black")
            elif i in y and i!=j:
                self.tips.append("white")
            else:
                self.tips.append("none")
                
    def run(self):
        print("""Welcome to mastermind! You can start the game!!
            
        Today we'll play with the following colors: yellow red blue green pink orange.
        
        The rules are as follows:
            
            Black:indicates how many pegs are in a correct position and are the right color
            White: indicates how many pegs are the correct color but wrong position
            None: indicates that both the color and the position are incorrect
            
        You only have 10 guesses!!
        
        Ready?? Let's begin!
        
        """)
        self.computerchoice = self.codemaker_choice()
        self.numberofguesses = 0
        while True:
            self.numberofguesses += 1
            self.mychoice = self.codeguesser_choice()
            self.codemaker_r(self.mychoice,self.computerchoice)
            random.shuffle(self.tips)
            if self.tips == ["black","black","black","black"]:
                print("you guessed the colors!")
                break
            elif self.numberofguesses > 11:
                print("Game Over")
                break
            else:
                self.round = self.mychoice + self.tips
                self.board.loc[len(self.board)]= self.round
                print(self.board.iloc[:,:])
                self.tips.clear()
                
if __name__ == "__main__":
    Mastermind().run()