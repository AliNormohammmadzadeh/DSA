from collections import defaultdict

class Graph():
    def __init__(self):
        self.graph = defaultdict(list)
    
    def addEdge(self, u , v):
        self.graph[u].append(v)
        
    def BFS(self,s):
        visited = [False] * (max(self.graph) + 1)
        print("this is self.graph :"  +str(self.graph))
        print("this is max self.graph :" +str(max(self.graph)))
        print("this is visited :" +str(visited))
        queue = []
        queue.append(s)
        visited[s] = True
        print(visited)
        
        while queue:
            print("this is queue : "+str(queue))
            s  = queue.pop(0)
            print(s,end=" ")
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

g = Graph()

#test tree
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,3)
g.addEdge(1,4)
g.addEdge(2,4)
g.addEdge(3,4)
g.addEdge(3,5)
g.addEdge(4,5)
g.addEdge(1,0)
g.addEdge(2,0)
g.addEdge(3,1)
g.addEdge(4,1)
g.addEdge(4,2)
g.addEdge(5,3)
g.addEdge(5,3)
g.addEdge(5,4)
g.BFS(0)

 
print ("Following is Breadth First Traversal"
                  " (starting from vertex 2)")
g.BFS(0)
# g.BFS(2)        


# #test one 
# g.addEdge(0,1)
# g.addEdge(0,2)
# g.addEdge(0,3)
# g.addEdge(0,4)
# g.addEdge(1,5)
# g.addEdge(1,6)
# g.addEdge(2,7)
# g.addEdge(1,0)
# g.addEdge(2,0)
# g.addEdge(3,0)
# g.addEdge(4,0)
# g.addEdge(5,1)
# g.addEdge(6,1)
# g.addEdge(7,2)

#test tow 
# g.addEdge(0, 1)
# g.addEdge(0, 2)
# g.addEdge(1, 2)
# g.addEdge(2, 0)
# g.addEdge(2, 3)
# g.addEdge(3, 3)