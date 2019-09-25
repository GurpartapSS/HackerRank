bot_x, bot_y = list(map(int, input().split()))
grid = []
for i in range(3):
    grid.append(list(map(str, input())))

def distance(bot,binn):
  return(abs(bot[0]-binn[0])+abs(bot[1]-binn[1]))

ararara = []
for i in range(3):
  for j in range(3):
    if grid[i][j] == 'b':
      bot = [bot_x,bot_y]
      binn = [i,j]
      ararara.append([i,j,distance(bot,binn)])

def keyy(boom):
  return(boom[2])
ararara.sort(keyy)
