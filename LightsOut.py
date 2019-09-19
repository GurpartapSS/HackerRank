def nextMove(player,board):
    y = 0
    for i in board:
        x = 0
        for j in i:
            if j == "1":
                print (y,x)   
                return
            x+=1
        y+=1
#If player is 1, I'm the first player.
#If player is 2, I'm the second player.
player = input()

#Read the board now. The board is a 8x8 array filled with 1 or 0.
board = []
for i in range(8):
    board.append(input())

nextMove(player,board)