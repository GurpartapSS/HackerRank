pac_x, pac_y = list(map(int, input().split()))
Dest_x, Dest_y = list(map(int, input().split()))
n, m = list(map(int, input().split()))

grid = []
for i in range(n):
    grid.append(list(map(str, input())))

visited = []
final_route = None
queue = []

PossibleMoves = [[-1, 0], [0, -1], [0, 1], [1, 0]]

queue.append([pac_x, pac_y, []])
while len(queue)>0:
    x, y, temp = queue.pop(0)
    routes = list(temp)
    routes.append([x, y])
    
    if x == Dest_x and y == Dest_y:
        if final_route == None:
            final_route = routes
            break
    
    moves = []
    for move in PossibleMoves:
        next_x, next_y = x + move[0], y + move[1]
        if next_x < 0 or next_x >= n or next_y < 0 and next_y >= m:
            continue

        if grid[next_x][next_y] == "-" or grid[next_x][next_y] == ".":
            grid[next_x][next_y] = "="
            moves.append([next_x, next_y , 0 if grid[next_x][next_y] == "." else 1])

    moves.sort(key = lambda x: x[2]) # use the third element of the list to sort
    for move in moves:
        queue.append([move[0], move[1], routes])

print(str(len(final_route)-1))
for node in final_route:
    print(str(node[0])+ " " + str(node[1]))
