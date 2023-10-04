def validCoord(x, y, n ,m):
  if x < 0 or  y < 0:
    return 0
  if x >= n or y >= m :
    return 0
  return 1


def BFS(n,m , data , X , Y , Color):
  vis = [[0 for i in range(101)] for j in range(101)]
  obj = []
  obj.append([X,Y])
  vis[X][Y] = 1
  
  while len(obj) > 0 :
    coord = obj[0]
    x = coord[0]
    y = coord[1]
    preColor = data[x][y]
    data[x][y] = Color
    obj.pop(0)
    
    if validCoord(x + 1, y, n , m) == 1 and vis[x+1][y] == 0 and data[x+1][y] == preColor:
      obj.append([x+1,y])
      vis[x+1][y] = 1
      
    if validCoord(x -1, y, n , m) == 1 and vis[x-1][y] == 0 and data[x-1][y] == preColor:
      obj.append([x-1,y])
      vis[x-1][y] = 1
      
    if validCoord(x , y+1, n , m) == 1 and vis[x][y+1] == 0 and data[x][y+1] == preColor:
      obj.append([x,y+1])
      vis[x][y+1] = 1
      
    if validCoord(x , y-1, n , m) == 1 and vis[x][y-1] == 0 and data[x][y-1] == preColor:
      obj.append([x,y-1])
      vis[x][y-1] = 1

  for i in range(n):
    for j in range(m):
      print(data[i][j] ,end=" ")
    print()
  print()

n = 8
m = 8
 
data = [
  [ 1, 1, 1, 1, 1, 1, 1, 1 ],
  [ 1, 1, 1, 1, 1, 1, 0, 0 ],
  [ 1, 0, 0, 1, 1, 0, 1, 1 ],
  [ 1, 2, 2, 2, 2, 0, 1, 0 ],
  [ 1, 1, 1, 2, 2, 0, 1, 0 ],
  [ 1, 1, 1, 2, 2, 2, 2, 0 ],
  [ 1, 1, 1, 1, 1, 2, 1, 1 ],
  [ 1, 1, 1, 1, 1, 2, 2, 1 ],
]
 
x, y, color = 4, 4, 3
print("before change") 
print("**********************************************")
print("**********************************************")
print("**********************************************")
for i in range(n):
  for j in range(m):
    print(data[i][j] ,end=" ")
  print()
  
print("**********************************************")
print("**********************************************")
print("**********************************************")
  
print("after change")

BFS(n, m, data, x, y, color)  
    