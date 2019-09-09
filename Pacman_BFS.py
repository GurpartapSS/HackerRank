pac_x, pac_y = list(map(int, input().split()))
Dest_x, Dest_y = list(map(int, input().split()))
n, m = list(map(int, input().split()))

grid = []
for i in range(n):
	g.append(list(map(str, input())))

node_visited = []
queue = []
final_route = None
