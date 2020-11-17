lookup_path = []
history_path = []

maze = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
             [0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
             [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]



def up(location):
    # Get the top of maze
    if location[0] == 0:
        return False
    else:
        new_location = [location[0] - 1, location[1]]
        # Visited, do no visit
        if new_location in history_path:
            return False
        # When meet wall, do not visit
        elif maze[new_location[0]][new_location[1]] == 1:
            return False
        else:
            lookup_path.append(new_location)
            history_path.append(new_location)
            return True


def down(location):
    # The end of maze, do not visit
    if location[0] == len(maze) - 1:
        return False
    else:
        new_location = [location[0] + 1, location[1]]
        # Visited, do no visit
        if new_location in history_path:
            return False
        # When meet wall, do not visit
        elif maze[new_location[0]][new_location[1]] == 1:
            return False
        else:
            history_path.append(new_location)
            lookup_path.append(new_location)
            return True


def left(location):
    # The leftmost of the maze
    if location[1] == 0:
        return False
    else:
        new_location = [location[0], location[1] - 1]
        # Visited, do no visit
        if new_location in history_path:
            return False
        # When meet wall, do not visit
        elif maze[new_location[0]][new_location[1]] == 1:
            return False
        else:
            history_path.append(new_location)
            lookup_path.append(new_location)
            return True


def right(location):
    # The rightmost of the maze
    if location[1] == len(maze[0]) - 1:
        return False
    else:
        new_location = [location[0], location[1] + 1]
        # Visited, do no visit
        if new_location in history_path:
            return False
        # When meet wall, do not visit
        elif maze[new_location[0]][new_location[1]] == 1:
            return False
        else:
            history_path.append(new_location)
            lookup_path.append(new_location)
            return True


def upright(location):
    # Get the most upright of maze
    if location[0] == 0 or location[1] == len(maze[0]) - 1:
        return False
    else:
        new_location = [location[0] - 1, location[1] + 1]
        # Visited, do no visit
        if new_location in history_path:
            return False
        # When meet wall, do not visit
        elif maze[new_location[0]][new_location[1]] == 1:
            return False
        else:
            lookup_path.append(new_location)
            history_path.append(new_location)
            return True


def upleft(location):
    # Get the most upright of maze
    if location[0] == 0 or location[1] == 0:
        return False
    else:
        new_location = [location[0] - 1, location[1] -1]
        # Visited, do no visit
        if new_location in history_path:
            return False
        # When meet wall, do not visit
        elif maze[new_location[0]][new_location[1]] == 1:
            return False
        else:
            lookup_path.append(new_location)
            history_path.append(new_location)
            return True

def downright(location):
    # The end of maze, do not visit
    if location[0] == len(maze) - 1 or location[1] == len(maze[0]) - 1:
        return False
    else:
        new_location = [location[0] + 1, location[1] + 1]
        # Visited, do no visit
        if new_location in history_path:
            return False
        # When meet wall, do not visit
        elif maze[new_location[0]][new_location[1]] == 1:
            return False
        else:
            history_path.append(new_location)
            lookup_path.append(new_location)
            return True

def downleft(location):
    # The end of maze, do not visit
    if location[0] == len(maze) - 1 or location[1] == 0:
        return False
    else:
        new_location = [location[0] + 1, location[1] - 1]
        # Visited, do no visit
        if new_location in history_path:
            return False
        # When meet wall, do not visit
        elif maze[new_location[0]][new_location[1]] == 1:
            return False
        else:
            history_path.append(new_location)
            lookup_path.append(new_location)
            return True


start = [17, 10]
end = [2, 10]
lookup_path.append(start)
history_path.append(start)

while lookup_path[-1] != end:
    now = lookup_path[-1]
    # print("retry:%s, Lookup path:%s" % (now, route_stack))
    if up(now) or down(now) or left(now) or right(now) or upleft(now) or upright(now) or downleft(now) or downright(now):
        continue

    lookup_path.pop()

print (lookup_path)