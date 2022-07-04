import random

class Minesweeper:
    #class contains the dim and bomb count, the function that makes the board and another function that assigns values to the each cell
    def __init__(self, dim, bombs):
        self.dim = dim
        self.bombs = bombs
        
        self.board = self.make_board()
        self.assign_to_board()

        self.dug = set()


    
    def make_board(self):
        board = [[None for _ in range(self.dim)] for _ in range(self.dim)] #creating the empty board
        #plant the bombs randomly
        planted_bombs = 0
        while planted_bombs < self.bombs:
            bomb_row = random.randint(0,self.dim-1)
            bomb_col = random.randint(0,self.dim-1)
            if board[bomb_row][bomb_col] == "*":
                continue
            board[bomb_row][bomb_col] = "*"
            planted_bombs += 1

        return board      

    def assign_to_board(self):
        #assigning values to the board
        for r in range(self.dim):
            for c in range(self.dim):
                if self.board[r][c] == "*":
                    continue
                self.board[r][c] = self.get_neighbors(r,c)  

    def get_neighbors(self,row,col):
        #calculate the values of each locations
        neighbors = 0
        for r in range(max(0,row-1), min(row+1, self.dim-1)+1):
            for c in range(max(0,col-1), min(col+1, self.dim-1)+1):
                if self.board[r][c] == "*":
                    neighbors += 1
        return neighbors


 
           
def print_board(visible_board):
    #printing the board that is visible to the user
    count = 0
    print("   ",end="")
    for j in range(len(visible_board)):
        print(f"{j} |",end="")
    print("")
    print("--------------------------------")    
    for i in visible_board:
        print(count, end="|")
        for k in range(len(i)):
            print(f"{i[k]} |", end="")
        count +=1
        print("")


def main(dim=10, bombs=10):
    #run the app
    global visible_board
    board = Minesweeper(dim,bombs)
    visible_board = [[" " for _ in range(dim)] for _ in range(dim)]
    gameRunning = True
    def check_around(row, col):
        if (row,col) not in board.dug:
            for y in range(max(0,row-1), min(row+1, dim-1)+1):
                for z in range(max(0,col-1), min(col+1, dim-1)+1):
                    board.dug.add((row,col))
                    if y == row and z == col:
                        pass
                    else:
                        visible_board[y][z] = board.board[y][z]  
                        if board.board[y][z] == 0:
                            check_around(y,z)   
                                                             
                            
    while gameRunning:
        """for x in board.board:
            print(x)
        print("kiki do you love me")"""  
        print_board(visible_board)
        row = int(input("enter the row: "))
        col = int(input("enter the column: "))
        if board.board[row][col] == 0:
            visible_board[row][col] = board.board[row][col]
            check_around(row,col)
            win_variable = 0
            for k in range(dim):
                for l in range(dim):
                    if visible_board[k][l] == " ":
                        win_variable += 1
            if win_variable == 10:
                gameRunning=False
                print("You Won!")     
        elif board.board[row][col] == "*":
            for r in range(dim):
                for c in range(dim):
                    if board.board[r][c] == "*":
                        visible_board[r][c] = "*"
            print("Game Over!")
            print_board(visible_board)
            gameRunning = False
        else:
            visible_board[row][col] = board.board[row][col]
            board.dug.add((row,col))
            win_variable = 0
            for k in range(dim):
                for l in range(dim):
                    if visible_board[k][l] == " ":
                        win_variable += 1
            if win_variable == 10:
                gameRunning=False
                print("You Won!")
        """print(board.dug)"""


if __name__ == "__main__":
    main()
