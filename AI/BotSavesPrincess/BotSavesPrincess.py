def displayPathtoPrincess(n, grid):
    """
    Print out minimum moves for mario to reach peach
    
    Parameters
    ----------
    n : int
        size of square matrix
    grid:
        square matrix containing location 
        of mario 'm', peach 'p', empty '-'
    
    Returns
    -------
    print out of mimimum moves (UP, DOWN, LEFT, RIGHT)
    """
    princess = [None] * 2
    mario = [None] * 2
    # Find location of mario and peach
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 'p':
                princess[0] = i
                princess[1] = j
            if grid[i][j] == 'm':
                mario[0] = i
                mario[1] = j
    # number of horizontal and vertical moves to reach target
    rows = princess[0] - mario[0]
    cols = princess[1] - mario[1]
    for i in range(abs(rows)):
        if rows > 0:
            print("DOWN")
        else:
            print("UP")
    for i in range(abs(cols)):
        if cols > 0:
            print("RIGHT")
        else:
            print("LEFT")


if __name__ == '__main__':
    m = int(input('Enter grid size: '))
    grid = []
    for i in range(0, m): 
        grid.append(input('Enter Row values: ').strip())

    displayPathtoPrincess(m,grid)
