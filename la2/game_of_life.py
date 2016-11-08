from graphics import * 
from time import sleep


def create_grid(width, height):
    """ 
    Creates and returns a grid with given height and width
    with each cell dead (represented as False)
    """
    grid = []

    for row in range(height):
        grid.append([])
        for column in range(width):
            grid[row].append(False)

    return grid


def is_on_grid(grid, column, row):
    """
    Returns whether the coordinates (x, y) are valid coordinates in grid
    """
    if column < 0 or row < 0:
        return False
    if column >= len(grid[0]) or row >= len(grid):
        return False
    return True


def live_neighbours(grid, column, row):
    """
    Returns the number of live neighbours to the cell with coordinates (x, y)
    Cells outside the board is seen as dead
    """
    alive = 0
    for r in range(-1, 2):
        for c in range(-1, 2):
            if not (c == 0 and r == 0): # Make sure you dont count yourself
                if is_on_grid(grid, column + c, row + r) and grid[row + r][column + c]:
                    alive += 1
    
    return alive


def evolve(grid):
    """
    Returns the next state of a grid based on Conway's Game of Life
    in a new grid
    """
    width = len(grid[0])
    height = len(grid)

    new_grid = create_grid(width, height)

    for row in range(height):
        for column in range(width):
            alive = live_neighbours(grid, column, row)
            if alive == 3:
                new_grid[row][column] = True
            elif alive == 2:
                new_grid[row][column] = grid[row][column]
            else:
                new_grid[row][column] = False

    return new_grid
    
# Yes I was a bit lazy if you want me to I can fix so it only uses win and grid
def paint(target_window, grid, cell_size):
    """ Paints the given grid in given window """
    height = len(grid)
    width = len(grid[0])

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] != 0:
                cell = Rectangle(Point(i*cell_size, j*cell_size), Point((i+1)*cell_size, (j+1)*cell_size))
                cell.setFill('black')
            else:
                cell = Rectangle(Point(i*cell_size, j*cell_size), Point((i+1)*cell_size, (j+1)*cell_size))
                cell.setFill('white')
            cell.draw(target_window)

    target_window.update()


def main():
    grid = example_grid()
    
    print(len(grid))
    print(len(grid[0]))

    """
    To read a grid from a file, download a file from www.conwaylife.com/wiki and place it in 
    the same folder as this file and uncomment the following line
    """
    #grid = read_file('example.rle')

    height = len(grid)
    width = len(grid[0])

    cell_size = 20 # Size of graphical representation of each cell

    my_window = GraphWin('Game of Life', width * cell_size, height * cell_size, autoflush=False)

    while my_window.checkMouse() == None:
        paint(my_window, grid, cell_size)
        grid = evolve(grid)

        sleep(0.1)
    my_window.close()


def example_grid():
    grid = create_grid(18, 17)
    grid[7][4:14] = [False, False, True, False, False, False, False, True, False, False]
    grid[8][4:14] = [True, True, False, True, True, True, True, False, True, True]
    grid[9][4:14] = [False, False, True, False, False, False, False, True, False, False]
    grid[1][1:4] = [True, True, True]
    grid[2][0:3] = [True, True, True]
    return grid


def read_file(file_name):
    """ 
    Reads a file containing a Game of Life pattern
    where 'O' means alive and '.' means dead
    Rows starting with '!' will be ignored 
    """
    content = open(file_name, 'r')

    # Calculate width and height of grid needed
    width = 0
    height = 0
    for line in content:
        if line[0] == '!':
            continue #ignore line
        height += 1
        if len(line) > width:
            width = len(line)

    # add extra space around pattern
    width += 10
    height += 10

    grid = create_grid(width, height)

    # Distance of pattern from edge
    offset_row = 5
    offset_col = 5

    content.seek(0) # reset file pointer

    row = 0

    for line in content:
        if line[0] == '!':
            continue # ignore line
        for col in range(len(line)):
            if line[col] == 'O':
                grid[row + offset_row][col + offset_col] = True
        row += 1
    
    return grid
   

# -----------------------------------------------------------------------------
# You do not need to worry about this code. 
# What it does is that it checks if you're running this as a script, or 
# imported (eg from the answer key/facit scripts).
if __name__== "__main__":
    main()
