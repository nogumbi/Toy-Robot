from world import obstacles
import turtle


position_x = 0
position_y = 0
directions = ['forward', 'right', 'back', 'left']
current_direction_index = 0

# area limit vars
min_y, max_y = -200, 200
min_x, max_x = -100, 100


screen = turtle.Screen()

#Create a new turtle and call it 'robot'
robot = turtle.Turtle()
robot.penup()
robot.setposition(-101, -201)
robot.pendown()
robot.pencolor('red')
robot.pensize(3)
for i in range(4):
    if i%2 == 0:
        robot.forward(201)
        robot.left(90)
    else:
        robot.forward(401)
        robot.left(90)
robot.penup()


#Create obstacles
obstacles_list = obstacles.get_obstacles()
for square in obstacles_list:
    robot.pencolor("red")
    robot.begin_fill()
    robot.goto(square[0], square[1])
    robot.pendown()
    robot.goto(square[0] + 4, square[1])
    robot.goto(square[0] + 4, square[1] + 4)
    robot.goto(square[0], square[1] + 4)
    robot.goto(square[0], square[1])
    robot.penup()
robot.hideturtle()

move_robot = turtle.Turtle()
move_robot.setheading(90)


def show_position(robot_name):
    print(' > '+robot_name+' now at position ('+str(position_x)+','+str(position_y)+').')

    
def is_position_allowed(new_x, new_y):
    """
    Checks if the new position will still fall within the max area limit
    :param new_x: the new/proposed x position
    :param new_y: the new/proposed y position
    :return: True if allowed, i.e. it falls in the allowed area, else False
    """
    
    return min_x <= new_x <= max_x and min_y <= new_y <= max_y 

def is_path_allowed(new_x, new_y):
    if obstacles.is_path_blocked(position_x, position_y,new_x,new_y):
        return True
    elif obstacles.is_position_blocked(new_x,new_y):
        return True
    else:
        return False

def reset_position():
    global position_x, position_y, current_direction_index

    position_x = 0
    position_y = 0
    current_direction_index = 0

def update_position(steps):
    """
    Update the current x and y positions given the current direction, and specific nr of steps
    :param steps:
    :return: True if the position was updated, else False
    """

    global position_x, position_y
    new_x = position_x
    new_y = position_y

    if directions[current_direction_index] == 'forward':
        new_y = new_y + steps
    elif directions[current_direction_index] == 'right':
        new_x = new_x + steps
    elif directions[current_direction_index] == 'back':
        new_y = new_y - steps
    elif directions[current_direction_index] == 'left':
        new_x = new_x - steps
        

    if is_position_allowed(new_x, new_y):
        if is_path_allowed(new_x, new_y) == False:
            position_x = new_x
            position_y = new_y
            return True, ''
        else:
            return False, 'obstacle'
    return False, 'border'


def do_right_turn(robot_name):
    """
    Do a 90 degree turn to the right
    :param robot_name:
    :return: (True, right turn output text)
    """
    global current_direction_index
    move_robot.right(90)
    current_direction_index += 1
    if current_direction_index > 3:
        current_direction_index = 0
        

    return True, ' > '+robot_name+' turned right.'


def do_left_turn(robot_name):
    """
    Do a 90 degree turn to the left
    :param robot_name:
    :return: (True, left turn output text)
    """
    global current_direction_index
    move_robot.left(90)
    current_direction_index -= 1
    if current_direction_index < 0:
        current_direction_index = 3
        

    return True, ' > '+robot_name+' turned left.'


def do_forward(robot_name, steps):
    """
    Moves the robot forward the number of steps
    :param robot_name:
    :param steps:
    :return: (True, forward output text)
    """
    move = update_position(steps)

    if move[0] == True:
        move_robot.forward(steps)
        return True, ' > '+robot_name+' moved forward by '+str(steps)+' steps.'
    elif move[1] == 'obstacle':
        return True, ''+robot_name+': Sorry, There is an obstacle in my way.'
    else:
        return True, ''+robot_name+': Sorry, I cannot go outside my safe zone.'


def do_back(robot_name, steps):
    """
    Moves the robot forward the number of steps
    :param robot_name:
    :param steps:
    :return: (True, forward output text)
    """

    move = update_position(-steps)

    if move[0] == True:
        move_robot.back(steps)
        return True, ' > '+robot_name+' moved back by '+str(steps)+' steps.'
    elif move[1] == 'obstacle':
        return True, ''+robot_name+': Sorry, There is an obstacle in my way.'
    else:
        return True, ''+robot_name+': Sorry, I cannot go outside my safe zone.'

def do_sprint(robot_name, steps):
    """
    Sprints the robot, i.e. let it go forward steps + (steps-1) + (steps-2) + .. + 1 number of steps, in iterations
    :param robot_name:
    :param steps:
    :return: (True, forward output)
    """

    if steps == 1:
        return do_forward(robot_name, 1)
    else:
        (do_next, command_output) = do_forward(robot_name, steps)
        print(command_output)
        return do_sprint(robot_name, steps - 1)
