import random

class Mastermind():
    
    def __init__(self):
    
        """
        Starts the game and provides instructions
        
        """

        print("Welcome to Mastermind! There's a secret code composed of 4 digits between 0 and 5, \nand your goal is to guess the code. To begin, insert 4 digits and the machine will tell you \nhow many of the numbers you inserted are in the code and in the right position with a black peg ('B'). \nYou will get a white peg ('W') for each number that is in the code, but in the wrong position. \nRemember you can repeat numbers (the code may be 0000 or 1122). \nLet's begin! \n\n")
    
    def computer_choice(self):

        """
        Returns the random code that the player will need to break.
        Numbers can be between 0 and 5 and can be repeated.
        
        """      
        
        return random.choices(range(0,6), k=4)
                    
    def player_choice(self):

        """
        Asks the player for input (guessing the code). Returns the code.
        Displays different error messages for the following cases: 
        The user inserts more or less than 4 digits
        Some of the numbers are not between 0 and 5
        The characters inserted were not numbers
        
        """      
        
        while True:
            try:
                self.choice = [int(i) for i in list(input("Insert 4 numbers between 0 and 5 (you can repeat numbers): "))]
                if len(self.choice) != 4:
                    self.choice = [int(i) for i in list(input("You must insert 4 numbers. Try again: "))]

                elif any([x > 5 for x in self.choice]):
                    self.choice = [int(i) for i in list(input("All numbers must be between 0 and 5. Try again: "))]
                else: 
                    break
            except: 
                print("You didn't insert a number.")
                
        return self.choice
    
    def comparing(self, player_input, real_code):
        
        """
        Compares the code vs. the player input
        Returns a list with:
        A white peg 'W' for each number that's in the code and in the right place
        A black peg 'B' for each number that's in the code but in the wrong place
        
        """
        
        for p_input, r_code in zip(player_input, real_code):
            if p_input == r_code:
                self.cpu_response.append("B")
            elif p_input != r_code:
                if p_input in real_code: 
                    self.cpu_response.append("W")
        return self.cpu_response

    def run(self):
        
        """
        We set the variables: 
        round counter at 0
        an empty list to be filled with the player choice
        the code of the computer
        
        """
        
        self.rounds = 0
        self.your_choice = [] 
        self.code = self.computer_choice()

        """
        Main loop:
        
        """

        
        while True:
            self.cpu_response = []
            self.rounds += 1
            self.your_choice = self.player_choice()
            self.cpu_response = self.comparing(self.your_choice, self.code)
            
            print("Your guess: ", ''.join([str(digit) for digit in self.your_choice],))
            print("The computer says:", ' '.join([str(digit) for digit in random.sample(self.cpu_response, len(self.cpu_response))]), "\n") 
            
            """
            We define the winning combination and the end of the game:

            """

            if self.cpu_response == ['B', 'B', 'B', 'B']:
                print("You broke the code, yay!")
                break
            elif self.rounds > 11:
                print("Game over :( The code was", ''.join([str(digit) for digit in self.code]))
                break

    
def main():
    Mastermind().run()

if __name__ == "__main__":
    main()