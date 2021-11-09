def nextMove(n,r,c,grid):
    """
    Determine what direction bot should move in to reach princess
    
    Parameters
    ----------
    n : int
        size of square matrix
    r: int
        row where bot is placed
    c: int
        col where bot is placed
    grid: 
        square matrix containing location
        of bot 'm', princess 'p', and empty '-'

    Returns
    -------
    direction: string
        single direction (UP, DOWN, LEFT, RIGHT)
        which will move bot closer to princess

    Updates grid with new bot location
    """
    bot = [r, c]
    princess = [None] * 2
    direction = ""
    # find location of princess
    for i in range(n):
        if 'p' in grid[i]:
            princess[0] = i
            princess[1] = grid[i].index('p')
            break
    # Error Check
    if grid[r][c] != 'm':
        print("Error: bot location mismatch")
        return direction
    if princess[0] == None and princess[1] == None:
        print("Error: Princess not found")
        return direction
    if princess[0] == bot[0] and princess[1] == bot[1]:
        print("Error: bot shares same location of princess")
        return direction
    # determine horizontal and vertical moves to reach princess
    rows = princess[0] - bot[0]
    cols = princess[1] - bot[1]
    # move in greater direction to reduce distance
    if abs(rows) > abs(cols):
        if rows > 0:
            direction = "DOWN"
        else:
            direction = "UP"
    else:
        if cols > 0:
            direction = "RIGHT"
        else:
            direction = "LEFT"
    return direction

if __name__ == "__main__":
    n = int(input("Enter matrix size: "))
    r,c = [int(i) for i in input("Enter bot coords: ").strip().split()]
    grid = []
    for i in range(0, n):
        grid.append(input("Enter row: "))

    print(nextMove(n,r,c,grid))
    print(grid)