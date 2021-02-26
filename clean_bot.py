def next_move(posr, posc, board):
    if board[posr][posc] == 'd':
        print("CLEAN")
        return
    # get coords of d
    d_coords = get_ds(board, 'd')
    if not d_coords:
        d_coords = get_ds(board, 'o')

    # get a list of distances for each d coord
    dist_list = [abs(e[0] - posr) + abs(e[1] - posc) for e in d_coords]
    
    # get the smallest value's index
    index = dist_list.index(min(dist_list))
    

    x, y = d_coords[index]

    if x < posr: print('UP')
    elif x > posr: print('DOWN')
    elif y < posc: print('LEFT')
    elif y > posc: print('RIGHT')

    return

def get_ds(board, c):
    
    d_coords = []
    for i, row in enumerate(board):
        for j, col in enumerate(row):
            if col == c:
                d_coords.append([i, j])
   
    return d_coords


if __name__ == "__main__":
    # pos = [int(i) for i in input().strip().split()]
    # board = [[j for j in input().strip()] for i in range(5)]
    
    pos = [3, 2]
    #board = [['b', 'd', '-', '-', '-'], ['-', 'd', '-', '-', '-'], ['-', '-', '-', 'd', '-'], ['-', '-', '-', 'd', '-'], ['-', '-', 'd', '-', 'd']]
    board = [['-', '-', '-', '-', 'd'], ['-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-'], ['d', 'd', '-', '-', 'd']]
    next_move(pos[0], pos[1], board)

