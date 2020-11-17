from collections import deque

def bfs():

    x = deque([])  # x value
    y = deque([])  # y value
    s = deque([])  # step value

    a = [[0 for col in range(20)] for row in range(20)]  # Array a contain maze
    b = [[0 for col in range(20)] for row in range(20)]  # Array b serve as temporary

    next_step = [[0, 1], [1, 0], [0, -1], [-1, 0], [-1, 1], [-1, -1], [1, 1], [1, -1]]  # Direction of Movement

    start_x = 17  # Start
    start_y = 10  # Start
    end_x = 2  # Destination
    end_y = 10  # Destination
    map_array = [
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
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
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                 ]

    for i in range(len(map_array)):
        for j in range(len(map_array)):
            a[i][j] = map_array[i][j]  # Save maze into Array a

    head = 0  # Head of the queue
    tail = 0  # Tail of the queue

    # Add the start point into path
    x.append(start_x)
    y.append(start_y)
    s.append(0)
    tail += 1

    b[start_x][start_y] = 1  # The start point has been visited, set 1

    flag = 0  # Destination flag, if reach, flag set 1, else set 0

    while head < tail:
        for i in range(len(next_step)):
            next_x = x[head] + next_step[i][0]
            next_y = y[head] + next_step[i][1]
            if next_x < 0 or next_y < 0 or next_x > 19 or next_y > 19:  # Go out of the maze
                continue
            if a[next_x][next_y] == 0 and b[next_x][next_y] == 0:  # Next point is not wall/terrain and has not visited
                b[next_x][next_y] = 1
                x.append(next_x)
                y.append(next_y)
                s.append(s[head] + 1)  # Add this point into the list
                tail += 1
            if next_x == end_x and next_y == end_y:
                flag = 1
                break
        if flag == 1:
            break
        head += 1  # Continue to search


    tuple = list(zip(x,y))
    return tuple

print (bfs())