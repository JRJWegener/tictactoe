

class tictactoe:
    '''Tictactoe game (object oriented) with 5 methods: display_grid, player_symbol, fill_grid, win_condition,and the function 'game' itself'''
    def __init__(self):
        #establishing the main variables used in the game    
        self.grid_board = [[1,2,3],[4,5,6],[7,8,9]] #the game board
        self.inx_dict = {1:[0, 0], 2:[0, 1], 3:[0, 2], 4:[1, 0], 5:[1, 1], 6:[1, 2], 7:[2, 0], 8:[2, 1],9:[2, 2]} # for translating between shown positions and the indices
        self.players_dict = {"player_1": "", "player_2": ""} # for saving the player symbols

    
    def display_grid(self):
        '''method for displaying the game grid in 3 print statements'''x^
        print(self.grid_board[0])
        print(self.grid_board[1])
        print(self.grid_board[2])



    def player_symbol(self):
        '''method for choosing a player symbol as first player'''
        self.players_dict["player_1"] = (input("player_1 please choose X or O: ")).upper() saving the input of player 1 in players_dict and capitalizing it
        if self.players_dict["player_1"] == "X": #if loop, giving the other player the remaining symbol
            self.players_dict["player_2"] = "O" 
        elif self.players_dict["player_1"] == "O":
            self.players_dict["player_2"] = "X"
        else:
            print("incorrect letter") #feedback if player doesn't put in x or o and restarts the method
            self.player_symbol()
            

    def fill_grid(self, player_key):
        '''method for putting input into grid_board'''
        self.display_grid() #first show the grid
        try: #try except loop to make sure input is a integer
            player_input = int(input(f"{player_key}, Which field do you want to choose?")) # ask for the number of the field
            if not player_input in range(1,10): #if not a number between 1 and 9 -> restart the method
                print("invalid number") 
                self.fill_grid(player_key)
            else:
                played_field = self.inx_dict[player_input] #translate given number into indices
                if isinstance((self.grid_board[played_field[0]][played_field[1]]), int): #if field is still integer, no player used it previously
                    self.grid_board[played_field[0]][played_field[1]] = self.players_dict[player_key]
                else:
                    print("position is already filled, please choose another") #restart the method if value is already a string (filled by player previously)
                    self.fill_grid(player_key)        
        except: 
            print("ATTENTION! take a valid number!") #if input is not a integer -> restart the method
            self.fill_grid(player_key)


    def win_condition(self, player_key):
        '''method to check for win conditions'''
        player_symbol = self.players_dict[player_key] #symbol of player whose move is being checked
        win_combo=[player_symbol,player_symbol,player_symbol] # winning combo = 3x the same symbol
        #horizontal conditions:
        for row in self.grid_board:
            if row == win_combo:
                return True
        #vertical conditions:
        helper_list=[]
        for column in range(0,3): #cycling through the columns
            for row in range(0,3): #cycling through the rows
                helper_list.append(self.grid_board[row][column]) #temporarily saving the values in a list for checking
            if helper_list == win_combo:
                return True
        #diagonal descending condition:
        helper_list2=[]
        for column in range(0,3):
            for row in range(0,3):
                if row == column: # all indices in the descending diagonal are 0:0,1:1,2:2
                    helper_list2.append(self.grid_board[row][column])
                if helper_list2 == win_combo:
                    return True       
        #diagonal ascending condition
        helper_list3 =[]
        for column in range(0,3):
            for row in range(0,3):
                if row + column == 2: # all indices in the descending diagonal equal 2
                    helper_list3.append(self.grid_board[row][column])
                if helper_list3 == win_combo:
                    return True
        return False
                        
    # Tic-tac-toe game
    def game(self):
        '''method to start a round of tic tac toe'''
        self.player_symbol() # choose player 1 symbol
        round_counter = 1 # to check if there is a draw after 9 round
        while round_counter < 10:
            if round_counter %2 != 0: #player 1 has uneven round counter
                self.fill_grid("player_1")
                if round_counter > 4: #only start checking for wins after player 1 has done 3 inputs
                    if self.win_condition("player_1"):
                        self.display_grid()
                        print ("player_1 won the game")
                        break
                round_counter += 1
            else: #player 2 has even round counter
                self.fill_grid("player_2")
                if round_counter > 5: #only start checking for wins after player 2 has done 3 inputs
                    if self.win_condition("player_2"):
                        self.display_grid()
                        print("player_2 won the game")
                        break
                round_counter += 1
        if not self.win_condition("player_1") and not self.win_condition("player_2"): #draw condition after 9 rounds
            print("Steve wins!")        

if __name__ == "__main__":

    ticgame = tictactoe()
    ticgame.game()

