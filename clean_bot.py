
def calc_distance(coords=[], x=0, y=0) -> list:
    # returns a list of distances from x, y to distance
    dists = [] 
    for element in coords:
       dists.append(abs(element[0] - x) + abs(element[1] - y))

    return dists

def get_ds(board=[]) -> list:
    
    d_coords = []
    for i, row in enumerate(board):
        for j, col in enumerate(row):
            if col == 'd':
                d_coords.append([i, j])
   
    return d_coords 

def print_move(coords, posr, posc):
    x, y = coords

    if x < posr




def next_move(posr, posc, board):
    if board[posr][posc] == 'd':
        print("CLEAN")
        return
    # get coords of d
    l = get_ds(board)
    m = calc_distance(l, posc, posr)
    n = m.index(min(m))
    dest_coords = l[n]
    print_move(coords, posr, posc)

    print("")


if __name__ == "__main__":
    # pos = [int(i) for i in input().strip().split()]
    # board = [[j for j in input().strip()] for i in range(5)]
    
    pos = [0, 0]
    board = [['b', 'd', '-', '-', '-'], ['-', 'd', '-', '-', '-'], ['-', '-', '-', 'd', '-'], ['-', '-', '-', 'd', '-'], ['-', '-', 'd', '-', 'd']]
    next_move(pos[0], pos[1], board)
