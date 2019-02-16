import random
def minesweeper_board(rows, columns, mines):
    temp = []
    temp2 = []
    for i in range(0, rows):
        for j in range(0, columns):
            #add element at the end of the temp list
            temp.append([i,j,0])
    for k in range (0, mines):
        #randomly select item from temp list
        newmine = random.choice(temp)
        #where there's mine = 1
        newmine[2]=1
        #add element at the end of the temp2 list
        temp2.append(newmine)
        #remove element from temp list
        temp.remove(newmine)
    #if temp is not empty list
    while temp:
        #add rest elements at the end of the temp2 list
        newmine = temp[-1]
        temp2.append(newmine)
        temp.remove(newmine)
    #classify temp2 list
    board = sorted(temp2, key = lambda x: (x[0], x[1]))
    return board

def main():
    rows = int(input("Enter #rows: "))
    columns = int(input("Enter #columns: "))
    mines = int(input("Enter #mines: "))
    board = minesweeper_board(rows, columns, mines)  
    #print(board)
    for i in range(0, rows):
        for j in range(0, columns):
            #check for mines
            if board[i*columns+j][2]==1:
                print('X', end=' ', flush=True)
            else:
                print('_', end=' ', flush=True)
        #creates rectangular
        print(" ")
        
main()
