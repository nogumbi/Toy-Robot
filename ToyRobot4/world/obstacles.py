import random

#Empty list
obstacles = []

def get_obstacles():
    """
    Randomly places obstacles up to 10
    """
    global obstacles
    obstacles = []
    obstacle_count = random.randint(1,10)
    for i in range(0,obstacle_count):
       (x, y) = random.randint(-100, 100), random.randint(-200, 200)
       obstacles.append((x, y))
    return obstacles


def obstacles_list(i):
    the_list = []
    for x in range(i[0],i[0]+5):
        for y in range(i[1],i[1] +5):
            co_ord = x,y
            the_list.append(co_ord)
    return the_list


def is_position_blocked(x, y):
    """
    checkes if the position is blocked
    """
    global obstacles
    block_list = []
    for i in obstacles:
        block =obstacles_list(i)
        block_list += block
    postion_tuple = x,y
    for i in block_list:
        if postion_tuple == i:
            return True
    return False
   

def is_path_blocked(x1,y1, x2, y2):
    """
    Checks if the block is in the path of where the robot is headed
    """
    global obstacles
    
    # for coordinates in obstacles:
    #     if x1 == x2:
    #         if y1 in range(coordinates[1], coordinates[1] + 5):
    #             return True     
    #     elif y1 == y2:
    #         if x1 in range(coordinates[0], coordinates[0] + 5):
    for x in range(x1,x2+1):
        for y in range(y1,y2+1):
            if is_position_blocked(x,y):
                return True
    return False
