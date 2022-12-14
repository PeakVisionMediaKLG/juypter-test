def number_of_neighbours(board, row, col):
    """ counts the numbers of an array_element with
    the position row and column. It is assumed,
    that i,j > 0 and i,< < len(board)-1"""
    counter = 0
    for i in [row-1,row,row+1]:
        for j in [col-1,col,col+1]:
             counter += board[i][j]
    counter -= board[row][col]
    return counter

board = [ [0,0,0,0,0,0,0,0,0,0,0,0],
          [0,1,0,1,0,0,0,0,1,0,1,0],
          [0,1,0,1,0,1,0,1,0,0,0,0],
          [0,1,1,0,0,0,0,0,1,1,1,0],
          [0,0,0,1,1,0,0,0,0,0,0,0],
          [0,1,0,1,0,0,0,0,1,0,1,0],
          [0,0,0,0,0,0,0,0,0,0,0,0]]
while True:
    r = int(input("row: "))  # Python2: raw_input
    if r == 0:
        break
    c = int(input("col: "))  # Python2: raw_input
    print("neighbours: ", number_of_neighbours(board, r,c))
