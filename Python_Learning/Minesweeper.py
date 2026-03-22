import random

def check():
    tile_value = 0
    directions = [(-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(-1,1)]
    for dr, dc, in directions:
        try:
            if board[dr+r][dc+c] == -1:
                tile_value += 1
        except:
            pass
    board[r][c] = tile_value

while True:
    board = []
    row_board = []
    mine_in_brd = 0
    rows = int(input("Board Height : "))
    collum = int(input("Board Length : "))
    mine_amnt = int(input("Amount of Mines : "))
    for i in range(rows):
        for i in range (collum):
            row_board.append(0)
        board.append(row_board)
        row_board = []

    while mine_in_brd < mine_amnt:
        r = random.randint(0, rows-1)
        c = random.randint(0, collum-1)
        if board[r][c] != -1:
            board[r][c] = -1
            mine_in_brd += 1

    for i in board[r]:
        if i == 0:
            check()

    for i, v in enumerate(board):
        print(board[i])