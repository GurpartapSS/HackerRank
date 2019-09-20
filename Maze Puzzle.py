pac_x, pac_y = list(map(int, input().split()))
Dest_x, Dest_y = list(map(int, input().split()))
n, m = list(map(int, input().split()))

grid = []
for i in range(n):
    grid.append(list(map(str, input())))

explore = []
node_visited = []
final_route = None

PossibleMoves = [[-1, 0], [0, -1], [0, 1], [1, 0]]

explore.append([pac_x, pac_y, []])

while len(explore) > 0:
    x, y, temp = explore.pop()
    routes = list(temp)
    routes.append([x, y])
    node_visited.append([x, y])

    if x == Dest_x and y == Dest_y:
        if final_route == None:
            final_route = routes
            break

    for move in PossibleMoves:
        next_x, next_y = x + move[0], y + move[1]
        if next_x < 0 or next_x >= m or next_y < 0 and next_y >= n:
            continue

        if grid[next_x][next_y] == '-' or grid[next_x][next_y] == '.':
            grid[next_x][next_y] = '='
            explore.append([next_x, next_y, routes])
print(str(len(node_visited)))
for nodes in node_visited:
    print(str(nodes[0]) + " " +str(nodes[1]))

print(str(len(final_route)-1))
for nodes in final_route:
    print(str(nodes[0]) + " " +str(nodes[1]))
