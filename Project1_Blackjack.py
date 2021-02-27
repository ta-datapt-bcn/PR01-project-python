import random

class BlackJack():
    
    
    def __init__(self):
        self.numbers = [str(i) for i in range(2,11)] + ['J', 'Q', 'K', 'A']
        self.values = [i for i in self.numbers if i.isnumeric()] + ['10' for i in self.numbers if (i.isalpha() and i != "A")] + ['11' for i in self.numbers if i == "A"]
        self.deck1 = self.numbers * 4
        self.num_value = dict(zip(self.numbers, self.values))
        self.userhand = 0
        self.croupierhand = 0
        self.choices = ["H", "S"]
        self.again = ["Y", "N"]
        
       
    def welcome(self):
        # Welcome
        
        print("""Welcome to the Digital Casino. My name is Carlos Azagra and I will be acting
as your croupier. Tonight we will be playing the game of Black Jack. I will be playing in
name of the Digital Casino against you. I take for granted that you are familiar with the
rules of the game. Please take a sit, enjoy the game and good luck.""")
        
        user_choice0= (input("Would you like to start gambling? [Y]es or [N]o? ")).upper()
        while user_choice0 not in self.again:
            user_choice0 = (input("Would you like to start gambling? [Y]es or [N]o? ")).upper()
        if user_choice0 == "Y":
            self.game()
        else:
            print("""So why did you come here??????
Have a nice day""")
            pass
    
    
    
    
    def croupier(self):
          
        print("The value of croupier hand is {}.".format(self.croupierhand))
        
        random.shuffle(self.deck1)
        
        while self.croupierhand <= 16:
            croupier_card3 = self.deck1.pop()
            self.croupierhand += int(self.num_value[croupier_card3])
            print("Croupier card is {}. The value of croupier hand is {}.".format(croupier_card3, self.croupierhand))
        if self.croupierhand > 21:
            print("The value of croupier hand is {}. ".format(self.croupierhand))
            self.croupierhand = 0
        else:
            print("Croupier stands.")
        
        self.check_results()
    
    
    def check_results(self):
        
        if self.croupierhand < self.userhand:
            print("User {} - Croupier {}. User is the winner!".format(self.userhand,self.croupierhand))
        elif self.croupierhand > self.userhand:
            print("User {} - Croupier {}. Croupier is the winner!".format(self.userhand,self.croupierhand))
        else:
            print("User {} - Croupier {}. User and Croupier have tied the game!".format(self.userhand,self.croupierhand))
    
        self.play_other_hand()
        
        
        
    def play_other_hand(self):
        
        play_again = (input("Would you like to play again? [Y]es or [N]o? ")).upper()
        while play_again not in self.again:
            play_again = (input("Would you like to play again? [Y]es or [N]o? ")).upper()
        if play_again == "Y":
            if len(self.deck1) < 6:
                self.deck1 = self.numbers * 4
                self.game()
            else:
                self.game()
        else:
            print("Thank you for coming. We hope you have enjoyed your stay. Looking forward to see you again!")
    
    
    def game(self):
        
        self.userhand = 0
        self.croupierhand = 0
        
        # Mezclar las cartas
        random.shuffle(self.deck1)
        
        # Repartir cartas descubiertas para usuario y croupier
        user_card1 = self.deck1.pop()
        self.userhand += int(self.num_value[user_card1])
        print("Your 1st card is {}".format(user_card1))
        croupier_card1 = self.deck1.pop()
        self.croupierhand += int(self.num_value[croupier_card1])
        print("Croupier 1st card is {} ".format(croupier_card1))
        
              
        # Repartir carta descubierta para usuario y sin descubrir a croupier
        user_card2 = self.deck1.pop()
        self.userhand += int(self.num_value[user_card2])
        print("Your 2nd card is {}. The value of your hand is {}".format(user_card2, self.userhand))
        croupier_card2 = self.deck1.pop()
        self.croupierhand += int(self.num_value[croupier_card1])
        print("Croupier 2nd card is hidden")
        
        
        # Turno del usuario: 1a elección para pedir 3a carta o hacer Stand
        user_choice1= (input("What would be your next move, [H]it or [S]tand? ")).upper()
        while user_choice1 not in self.choices:
            user_choice1 = (input("What would be your next move, [H]it or [S]tand? ")).upper()
        if user_choice1 == "H":
            user_card3 = self.deck1.pop()
            self.userhand += int(self.num_value[user_card3])
      
        
        # Turno del usuario: 2a elección para pedir 4a carta o hacer Stand
            if self.userhand <= 21:
                print("Your 3rd card is {}. The value of your hand is {}.".format(user_card3, self.userhand))
                user_choice2= (input("What would be your next move, [H]it or [S]tand? ")).upper()
                while user_choice2 not in self.choices:
                    user_choice2 = (input("What would be your next move, [H]it or [S]tand? ")).upper()
                if user_choice2 == "H":
                    user_card4 = self.deck1.pop()
                    self.userhand += int(self.num_value[user_card4])
                        
        # Turno del usuario: 3a elección para pedir 5a carta o hacer Stand
                    if self.userhand <= 21:
                        print("Your 4th card is {}. The value of your hand is {}.".format(user_card4, self.userhand))
                        user_choice3= (input("What would be your next move, [H]it or [S]tand? ")).upper()
                        while user_choice3 not in self.choices:
                            user_choice3 = (input("What would be your next move, [H]it or [S]tand? ")).upper()
                        if user_choice3 == "H":
                            user_card5 = self.deck1.pop()
                            self.userhand += int(self.num_value[user_card5])
                            print("Your 5th card is {}. The value of your hand is {}. Now is croupier turn.".format(user_card5, self.userhand))
                        else:
                            print("Your final hand value is {}. Now is croupier turn.".format(user_card4, self.userhand))
                            self.croupier()
                    
                    else:
                        print("Your 4th card is {}. The value of your hand is {}. You have lost this hand." .format(user_card4, self.userhand))
                        self.play_other_hand()                            
                else:
                    print("Your final hand value is {}. Now is croupier turn.".format(self.userhand))
                    self.croupier()
            
            else:
                print("Your 3rd card is {}. The value of your hand is {}. You have lost this hand." .format(user_card3, self.userhand))
                self.userhand = 0
                self.play_other_hand()
                
        else:
            print("Your final hand value is {}. Now is croupier turn.".format(self.userhand))
            self.croupier()
            

if __name__=="__main__":
    BlackJack().welcome()

