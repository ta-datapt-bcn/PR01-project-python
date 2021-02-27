#Executing the game. 
def game():
        #Welcoming the player and explaining the rules. 
        def greeting():
                print("""

                    Welcome to Tic-Tac-Toe, player! The rules of this game are very simple: 

                    - You will take turns with the computer marking the spaces of the grid. 
                    - Whoever scores three marks in a vertical, horizontal or diagonal line wins. 
                    - If nobody wins or loses, it's a draw.

                    To play, you will have to type the position you'd like to mark following this chart:

                                                    1 | 2 | 3
                                                    ---------
                                                    4 | 5 | 6
                                                    ---------
                                                    7 | 8 | 9
                  """)
                import time
                time.sleep(0.2)

        #Generating the board for the current state of the game.
        def board_gen(board):
                print("""
                                                    {0} | {1} | {2}
                                                    ---------
                                                    {3} | {4} | {5}
                                                    ---------
                                                    {6} | {7} | {8} """.format(board["1"],board["2"],board["3"],board["4"],board["5"],
                                                    board["6"],board["7"],board["8"],board["9"]))   


        #Announcing the winner and asking for a new match.
        def win_announce(winner):
                print("The ", winner, "has won this match!\nBut we can keep playing for a while.")
                confirm() #Calling the function to confirm a new game.

        #Asking confirmation for a new match. 
        def confirm():    
                x = input("Would you like to generate a new match? Y/N") 
                if x=="Y":
                    print("\nGenerating new match...")
                    print("""

                                                      |   |  
                                                    ---------
                                                      |   |  
                                                    ---------
                                                      |   |  
                  """) #Printing a blank board, this could be skipped but is done for aesthetic reasons.
                    game_body()
                elif x=="N":
                    goodbye() #Quitting the game if the input is N.
                else:
                    print("I'm sorry but I couldn't understand you.")
                    confirm()    

        #Checking for a possible draw.      
        def draw(player, cpu):
                    if sum(player) + sum(cpu) == 45: #Checking for a draw if all positions are filled and there's no winner.
                        print("It's a draw!")
                        confirm() #Stopping the game if there's a draw.
                    else:
                        pass #If there's no draw, does nothing.  

        #Saying goodbye and closing the game.
        def goodbye():
                import time
                import sys
                print("GOODBYE!")
                time.sleep(5) #This makes the program wait 5s to properly display the goodbye message before closing.   
                sys.exit()            

        #Making the cpu move. It takes into account both the player moves, its own and the positions unckecked. 
        #Using a combination of 3 lists we can account for all possible winning combinations, and using a series
        #of loops the cpu will try to block any try to perform a winning move.
        def cpu_move(possible_moves, player, cpu):
                    val_1 = [1,1,1,2,2,3,3,3,4,4,5,5,5,5,6,6,7,7,7,8,8,9,9,9]
                    val_2 = [2,5,4,1,5,1,5,6,1,5,2,4,1,3,3,4,1,8,5,2,7,1,3,7]
                    val_3 = [3,9,7,3,8,2,7,9,7,6,8,6,9,7,9,5,4,9,3,5,7,5,6,8]
                    filled = player + cpu
                    possible = [] #List of all filled positions.
                    import random
                    for i in possible_moves:
                        if i not in filled: #Checking what moves are still available.
                            possible.append(i)
                    for i in range(24):
                        if val_1[i] in player: #Checking if the value is in the player moves.
                            if val_2[i] in player: 
                                if val_3[i] in possible:
                                    return val_3[i] #If both moves have been performed by the player, the cpu blocks the winning move.
                                else:
                                    pass
                            else:
                                pass
                        else:
                            pass      
                    else: 
                        return random.choice(possible) #Returning a random choice from the list of available moves.   

        #Checking if there's a winner.
        def wincheck(moves):
                winmoves = [{1,2,3},{4,5,6},{7,8,9},{1,4,7},{2,5,8},{3,6,9},{1,5,9},{7,5,3}] #Possible win combinations.
                if len(moves) >= 3: 
                    if {1,2,3}.issubset(moves):
                        return True #Checking for all winning conditions.
                    elif {4,5,6}.issubset(moves):
                        return True
                    elif {7,8,9}.issubset(moves):
                        return True
                    elif {1,4,7}.issubset(moves):
                        return True
                    elif {2,5,8}.issubset(moves):
                        return True
                    elif {3,6,9}.issubset(moves):
                        return True
                    elif {1,5,9}.issubset(moves):
                        return True
                    elif {7,5,3}.issubset(moves):
                        return True
                    else:
                        return False
                else:
                    return False

        #Executing the main game loop. 
        def game_body():
                board = {"1": " ", "2": " ", "3": " ", "4": " ", "5": " ", "6": " ", "7": " ", "8": " ", "9": " "}
                possible_moves = [1,2,3,4,5,6,7,8,9] #List of possible moves.
                player = [] #This list will hold the player's moves.
                cpu = [] #This one will contain the moves made by the computer.    
                import time

                while (wincheck(player) == False) and (wincheck(cpu) == False): #Asking for a new move if there's no winner yet.
                    player_move = int(input("Enter your move:"))
                    while player_move in (player or cpu) or (player_move not in possible_moves):
                            print("That's not a valid move, please try again.")
                            player_move = int(input("Enter your move:"))

                    board[str(player_move)] = "X" #Marking the move on the board.
                    board_gen(board) #Displaying a board with the new move.
                    player.append(player_move) #Appending the move to the list of mplayer moves.
                    if wincheck(player): #Checking for a winner.
                        win_announce("player") #Announcing a winner (if there's one).
                    else:
                        pass
                    draw(player, cpu) #There's no winner, so we'll check for a draw before re-launching the loop.

                    print("The cpu is making a move.")
                    time.sleep(2) #Waits 2 seconds before performing the cpu move.
                    cpu_var = cpu_move(possible_moves, player, cpu) #The cpu makes a move based on the current state.
                    board[str(cpu_var)] = "O" 
                    board_gen(board)
                    cpu.append(cpu_var) #Adding the cpu move to the list of its performed moves.
                    if wincheck(cpu):
                        win_announce("cpu")
                    else:
                        pass
                    draw(player, cpu)
            
        greeting()
        print("\n")
        confirm()