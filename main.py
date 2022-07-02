import random

class Minesweeper:
    def __init__(self, dim, bombs):
        self.dim = dim
        self.bombs = bombs
        
        self.board = self.make_board()
        self.assign_to_board()

        self.dug = set()
        #dug locations are recorded


    
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
    for i in visible_board:
        print(i)
    #this will be upgraded to a better board with the numbers that represent the rows and cols


def main(dim=10, bombs=10):
    #run the app
    global visible_board
    board = Minesweeper(dim,bombs)
    visible_board = [[" " for _ in range(dim)] for _ in range(dim)]
    gameRunning = True
    def check_around(row, col):
        #return visible_board yerine fonksiyonun direk visible_board üzerinde işlem yapması daha mı kolay olur
        for y in range(max(0,row-1), min(row+1, dim-1)+1):
            for z in range(max(0,col-1), min(col+1, dim-1)+1):
                if y != row and z != col:
                    if board.board[y][z] == 0:
                        visible_board[y][z] = board.board[y][z]
                        check_around(y,z)
                    else:
                        visible_board[y][z] = board.board[y][z]
    while gameRunning:
        for x in board.board:
            print(x)
        print_board(visible_board)
        row = int(input("enter the row: "))
        col = int(input("enter the column: "))
    

        if board.board[row][col] == 0:
            visible_board[row][col] = board.board[row][col]
            check_around(row,col)
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
            #check if the game is over   we probably will need a new variable for this


if __name__ == "__main__":
    main()
