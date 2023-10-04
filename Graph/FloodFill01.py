N = 8 
M = 8

def FloodFillUntil(screan, x,y, OColor, NColor):
    if (x < 0 or x >=8  or y<0 or y >=N or screan[x][y] != OColor or screan[x][y] == NColor):
        return
    screan[x][y] = NColor
    FloodFillUntil(screan, x+1 , y, OColor, NColor)
    FloodFillUntil(screan, x-1 , y, OColor, NColor)
    FloodFillUntil(screan, x , y+1, OColor, NColor)
    FloodFillUntil(screan, x , y-1, OColor, NColor)
    
def FloodFill(screan , x ,y,NColor):
    OColor = screan[x][y]
    if(OColor == NColor):
        return
    FloodFillUntil(screan,x,y,OColor , NColor)


screen = [[1, 1, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 1, 0, 0],
          [1, 0, 0, 1, 1, 0, 1, 1],
          [1, 2, 2, 2, 2, 0, 1, 0],
          [1, 1, 1, 2, 2, 0, 1, 0],
          [1, 1, 1, 2, 2, 2, 2, 0],
          [1, 1, 1, 1, 1, 2, 1, 1],
          [1, 1, 1, 1, 1, 2, 2, 1]]
 
x = 4
y = 4
newC = 3

print("screen before call the floodfill :")
for i in range(M):
    for j in range(N):
        print(screen[i][j] , end=' ')
    print()
FloodFill(screen, x, y, newC)
print("Update screen after call the floodfill :")
for i in range(M):
    for j in range(N):
        print(screen[i][j] , end=' ')
    print()

