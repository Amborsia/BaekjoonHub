def solution(park, routes):
    height = len(park)
    width = len(park[0])

    for i in range(height):
        for j in range(width):
            if park[i][j] == 'S':
                start_x, start_y = i,j
                break

    direction_map = {
        'N': (-1, 0),
        'S': (1, 0),
        'W': (0, -1),
        'E': (0, 1)
    }
    current_x, current_y = start_x, start_y

    for route in routes:
        direction, distance = route.split()
        distance = int(distance)

        dx, dy = direction_map[direction]
        new_x, new_y = current_x, current_y

        can_move = True
        for _ in range(distance):
            new_x+=dx
            new_y+=dy
            if not(0<=new_x<height and 0<= new_y<width and park[new_x][new_y] != 'X'):
                can_move = False
                break
        if can_move:
            current_x, current_y = new_x, new_y

    

    return [current_x,current_y]