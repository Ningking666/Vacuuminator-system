def distance_to_wall(world):
    row=len(world)
    col=len(world[0])

    walls=[]
    min_distance=[]
    for r in range(row):
        for c in range(col):
            if world[r][c]=='w':
                walls.append((r,c))

    if not walls:
        return None
    for  r in range(row):
        for c in range(col):
            if world[r][c]=='X':
               v_dis=(r,c)
               break
    for pos in walls:
        distance=abs(pos[0]-v_dis[0])+abs(pos[1]-v_dis[1])
        min_distance.append(distance)
    return min(min_distance)

#Make a move 

# Direction constants as specified in the problem
DIR_UP = "u"
DIR_DOWN = "d"
DIR_LEFT = "l"
DIR_RIGHT = "r"

# Tile characters as specified in the problem
DIRTY_TILE = 'D'
EMPTY_TILE = 'E'
WALL_TILE = 'W'
ROBOT_TILE = 'X'

# Tuple representations for directions, allows easier movement calculation
UP_MOVE = (-1, 0)
RIGHT_MOVE = (0, 1)
DOWN_MOVE = (1, 0)
LEFT_MOVE = (0, -1)

# Index positions for X and Y axis
X_INDEX = 0
Y_INDEX = 1

def find_cleaner(world):
    """ 
    Returns a tuple containing the position of the Vacuuminator in the world
    """
    for row in range(len(world)):
        for col in range(len(world[0])):
            if world[row][col] == ROBOT_TILE:
                return (row, col)

            
def text_move_to_tuple(direction):
    """
    Converts from text to tuple representation of a move
    """   
    move_dict = {}
    move_dict[DIR_UP] = UP_MOVE 
    move_dict[DIR_DOWN] = DOWN_MOVE
    move_dict[DIR_RIGHT] = RIGHT_MOVE
    move_dict[DIR_LEFT] = LEFT_MOVE
    
    return move_dict[direction]


def find_new_pos(cleaner_pos, direction):
    """
    Locates the cleaner after a move is made
    """
    movement = text_move_to_tuple(direction)
    return (cleaner_pos[X_INDEX] + movement[X_INDEX], 
            cleaner_pos[Y_INDEX] + movement[Y_INDEX])


def in_world(world, new_pos):
    """
    Checks whether a given position is within the bounds of the world
    """
    if (0 <= new_pos[X_INDEX] < len(world)
        and 0 <= new_pos[Y_INDEX] < len(world[0])):
        return True
    return False



def legal_move(world, new_pos):
    """
    Checks if a move can legally be made
    """
    
    # Move would take cleaner outside of the world
    if not in_world(world, new_pos):
        return False 
    
    # Move would take cleaner into a wall
    if world[new_pos[X_INDEX]][new_pos[Y_INDEX]] == WALL_TILE:
        return False
    
    return True


"""
Executes a move in a given direction
"""
def make_move(world, direction):
    cleaner_pos = find_cleaner(world)
    new_pos = find_new_pos(cleaner_pos, direction)
    
    # Only change the state of the world if the move is legal
    if legal_move(world, new_pos):
        world[cleaner_pos[X_INDEX]][cleaner_pos[Y_INDEX]] = EMPTY_TILE
        world[new_pos[X_INDEX]][new_pos[Y_INDEX]] = ROBOT_TILE
    
    return world


def tuple_move_to_text(moves):
    """
    Converts from tuple to text representation of a move
    """
    move_dict = {}
    move_dict[UP_MOVE] = DIR_UP
    move_dict[DOWN_MOVE] = DIR_DOWN
    move_dict[RIGHT_MOVE] = DIR_RIGHT
    move_dict[LEFT_MOVE] = DIR_LEFT
    
    text_moves = []
    for move in moves:
        text_moves.append(move_dict[move])
    return text_moves


def in_world(world, new_pos):
    """
    Checks whether a given position is within the bounds of the world
    """
    if (0 <= new_pos[X_INDEX] < len(world) 
        and 0 <= new_pos[Y_INDEX] < len(world[0])):
        return True
    return False


def find_cleaner(world):
    """ 
    Returns a tuple containing the position of the Vacuuminator in the world
    """
    for row in range(len(world)):
        for col in range(len(world[0])):
            if world[row][col] == ROBOT_TILE:
                return (row, col)

#Finding dirt
            
def path_to_next(world):
    """ 
    Identifies the path to the nearest located dirt
    """
    
    # Ideally, the function should not change the state of the world. The
    # codeblock below ensures this behavior.  Note that a single line
    # world = world.copy() is not sufficient, as it would copy the outer list
    # only and not the individual rows.  An alternative solution is to use
    # the deepcopy function in the copy library, i.e. world = deepcopy(world)
    new_world = []
    for row in world:
        row_copy = row.copy()
        new_world.append(row_copy)
    world = new_world
    
    cleaner_pos = find_cleaner(world)
    all_moves = [UP_MOVE, RIGHT_MOVE, DOWN_MOVE, LEFT_MOVE]
    legal_moves = [UP_MOVE, RIGHT_MOVE, DOWN_MOVE, LEFT_MOVE]
    distance = 0
    
    # Begin with closest squares
    while True:
        distance += 1
        for move in all_moves:
            if move in legal_moves:
                
                # Identifies the location of the square being scanned
                new_row = cleaner_pos[X_INDEX] + move[X_INDEX] * distance
                new_col = cleaner_pos[Y_INDEX] + move[Y_INDEX] * distance
                if in_world(world, (new_row, new_col)):
                    
                    # Dirty square found
                    if world[new_row][new_col] == DIRTY_TILE:
                        world[cleaner_pos[X_INDEX]][cleaner_pos[Y_INDEX]] \
                            = EMPTY_TILE
                        world[new_row][new_col] = ROBOT_TILE
                        return tuple_move_to_text([move]  * distance)
                    
                    # Cannot see through walls, remove this direction
                    elif world[new_row][new_col] == WALL_TILE:
                        legal_moves.remove(move)
                
                # Do not continue to search outside the world
                else:
                    legal_moves.remove(move)
            
            # All directions are outside house or blocked by wall
            if len(legal_moves) == 0:
                return []

#Task 4: Cleaning all the dirt located

def find_cleaner(world):
    """ 
    Returns a tuple containing the position of the Vacuuminator in the world
    """
    for row in range(len(world)):
        for col in range(len(world[0])):
            if world[row][col] == ROBOT_TILE:
                return (row, col)

            
def make_moves(world, moves): 
    """
    Modifies the world to reflect the execution of a move sequence
    """
    # Execute moves in the sequence, one at a time
    for move in moves:
        cleaner_pos = find_cleaner(world)
        world[cleaner_pos[X_INDEX]][cleaner_pos[Y_INDEX]] = EMPTY_TILE
        world[cleaner_pos[X_INDEX] + move[X_INDEX]][cleaner_pos[Y_INDEX] 
            + move[Y_INDEX]] = ROBOT_TILE
    return


def reversed_move(move):
    """
    Calculates the opposite of a given movement
    """
    return (move[X_INDEX] * -1, move[Y_INDEX] * -1)


def text_move_to_tuple(text_moves):
    """
    Converts from text to tuple representation of a move
    """
    move_dict = {}
    move_dict[DIR_UP] = UP_MOVE 
    move_dict[DIR_DOWN] = DOWN_MOVE
    move_dict[DIR_RIGHT] = RIGHT_MOVE
    move_dict[DIR_LEFT] = LEFT_MOVE
    
    moves = []
    for text_move in text_moves:
        moves.append(move_dict[text_move])
    return moves
 
    
def tuple_move_to_text(moves):
    """
    Converts from tuple to text representation of a move
    """
    move_dict = {}
    move_dict[UP_MOVE] = DIR_UP
    move_dict[DOWN_MOVE] = DIR_DOWN
    move_dict[RIGHT_MOVE] = DIR_RIGHT
    move_dict[LEFT_MOVE] = DIR_LEFT
    
    text_moves = []
    for move in moves:
        text_moves.append(move_dict[move])
    return text_moves


def clean_path(world):
    """
    Returns a list of moves the Vacuuminator will use to clean the world
    """
    all_moves = []
    moves = []

    # Continue as long as there any dirt found or movements to backgrack
    while moves or path_to_next(world):
        
        # Identify next dirt to seek if any is visible
        next_moves = text_move_to_tuple(path_to_next(world))
        
        # Seek dirt from the current position
        if next_moves:
            make_moves(world, next_moves)
            moves = moves + next_moves
            all_moves = all_moves + next_moves
        
        # Backtrack from current position
        else:
            rev_move = reversed_move(moves.pop())
            make_moves(world, [rev_move])
            all_moves.append(rev_move)
        
    return tuple_move_to_text(all_moves)