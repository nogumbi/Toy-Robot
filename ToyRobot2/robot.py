def get_robot_name():
    """
    Gets robot name and stores it to use it later
    """
    name = input('What do you want to name your robot? ')
    if name == '' or name == ' ':
        return get_robot_name()
    print(f'{name}: Hello kiddo!')
    return name


def get_command_input(name):
    """
    Gets all the commands and outputs from the function called
    """
    command_list = ['OFF', 'HELP', 'FORWARD', 'BACK', 'RIGHT', 'LEFT', 'SPRINT']
    coordinates = {
        "x" : 0,
        "y" : 0
    }
    direction = ['forward']
    while True:
        command = input(f'{name}: What must I do next? ')
        user_list = command.split(' ')
        if command.upper() == 'OFF':
            print(f'{name}: Shutting down..')
            break
        elif command.upper() == 'HELP':
            help_command = get_help()
            print(help_command)
        elif user_list[0].upper() == 'FORWARD':
            coordinates = move_forward(name, int(user_list[1]), coordinates, direction)
            robot_position(name, coordinates)
        elif user_list[0].upper() == 'BACK':
            coordinates = move_back(name, int(user_list[1]), coordinates, direction)
            robot_position(name, coordinates)
        elif user_list[0].upper() == 'RIGHT':
            move_right(name, coordinates, direction)
            robot_position(name, coordinates)
        elif user_list[0].upper() == 'LEFT':
            move_left(name, coordinates, direction)
            robot_position(name, coordinates)
        elif user_list[0].upper() == 'SPRINT':
           sprint(name, int(user_list[1]), coordinates, direction) 
           robot_position(name, coordinates)
        elif command not in command_list:
            print(f"{name}: Sorry, I did not understand '{command}'.")


def robot_position(name, coordinates):
    """
    Function handles for the position one is currenntly in
    """
    print(f" > {name} now at position ({str(coordinates['x'])},{str(coordinates['y'])}).") 


def get_help():
    """
    Returns the help command which includes a list of all valid commands.
    FORWARD - Moves forward by a number of steps
    BACK - Moves back
    RIGHT - Changes the direction to right
    LEFT - Changes the direction to left
    SPRINT - It starts by going forward the number of steps indicated, until it counted down to zero steps
    """
    help_command = """I can understand these commands:
OFF  - Shut down robot
HELP - provide information about commands
     """
    return help_command


def move_forward(name, steps, coordinates, direction):
    """
    Moves forward by a number of steps

        Args:
        name : name of the robot
        coordinates ([dictionary]): X and y axis on the cartesian plane
        direction ([list]]): where it should move next

    Returns:
        [bool]: returns the old coordinates if the robot is out of the restricted area, else if returns the coordinates
    """
    old_coordinates = coordinates.copy()
    if direction[0] == 'forward':
        coordinates['y'] += steps
    elif direction[0] == 'back':
        coordinates['y'] -= steps
    elif direction[0] == 'left':
        coordinates['x'] -= steps
    elif direction[0] == 'right':
        coordinates['x'] += steps

    holder = limited_area(name, coordinates)
    if holder is True:
        print(f' > {name} moved forward by {steps} steps.')
        return coordinates
    else:
        return old_coordinates


def move_back(name, steps, coordinates, direction):
    """
    Moves back by a number of steps
    
        Args:
        name : name of the robot
        coordinates ([dictionary]): X and y axis on the cartesian plane
        direction ([list]]): where it should move next

    Returns:
        [bool]: returns the old coordinates if the robot is out of the restricted area, else if returns the coordinates
    """
    old_coordinates = coordinates.copy()
    if direction[0] == 'back':
        coordinates['y'] += steps
    elif direction[0] == 'forward':
        coordinates['y'] -= steps
    elif direction[0] == 'left':
        coordinates['x'] += steps
    elif direction[0] == 'right':
        coordinates['x'] -= steps

    holder = limited_area(name, coordinates)
    if holder is True:
        print(f' > {name} moved back by {steps} steps.')
        return coordinates
    else:
        return old_coordinates


def move_right(name, coordinates, direction):
    """
    Changes the direction to right

    Args:
        name : name of the robot
        coordinates ([dictionary]): X and y axis on the cartesian plane
        direction ([list]]): where it should move next

    Returns:
        [bool]: returns the old coordinates if the robot is out of the restricted area, else if returns the coordinates
    """
    old_coordinates = coordinates.copy()
    print(f' > {name} turned right.')
    if direction[0] == 'forward':
        direction[0] = 'right'
    elif direction[0] == 'back':
        direction[0] = 'left'
    elif direction[0] == 'left':
        direction[0] = 'forward'
    elif direction[0] == 'right':
        direction[0] = 'back'

    holder = limited_area(name, coordinates)
    if holder is True:
        return coordinates
    else:
        return old_coordinates


def move_left(name, coordinates, direction):
    """
    Changes the direction to the left

    Args:
        name : name of the robot
        coordinates ([dictionary]): X and y axis on the cartesian plane
        direction ([list]]): where it should move next

    Returns:
        [bool]: returns the old coordinates if the robot is out of the restricted area, else if returns the coordinates
    """
    old_coordinates = coordinates.copy()
    print(f' > {name} turned left.')
    if direction[0] == 'forward':
        direction[0] = 'left'
    elif direction[0] == 'back':
        direction[0] = 'right'
    elif direction[0] == 'left':
        direction[0] = 'back'
    elif direction[0] == 'right':
        direction[0] = 'forward'

    holder = limited_area(name, coordinates)
    if holder is True:
        return coordinates
    else:
        return old_coordinates
        
def limited_area(name, coordinates):
    """
    Check the restriction of the area.

    Args:
        name : name of the robot
        coordinates ([dictionary]): X and y axis on the cartesian plane

    Returns:
        [bool]: if the robot is within the area, then return true, else it should state that it is out of the area and return the command 
    """
    check = (-100 <= (coordinates['x']) <= 100) and (-200 <= (coordinates['y']) <= 200)
    if check:
        return True
    else:
        print(f'{name}: Sorry, I cannot go outside my safe zone.')
        return False

def sprint(name, steps, coordinates, direction):
    """
    Sprint gives it a short burst of speed and some extra distance
    Args:
        name : name of the robot
        coordinates ([dictionary]): X and y axis on the cartesian plane
        steps (integer): number of steps taken
        direction ([list]]): where it should move next
    """
    #print(f' > {name} moved forward by {steps} steps.')
    while steps > 0:
        forward = move_forward(name, steps, coordinates, direction)
        steps -= 1
    
def robot_start():
    """This is the entry function, do not change"""
    name = get_robot_name()
    get_command_input(name)

if __name__ == '__main__':
    robot_start()
