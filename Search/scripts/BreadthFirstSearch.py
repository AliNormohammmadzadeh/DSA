graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

visited = []
queue = []

def BFS(visited, graph , node):
    visited.append(node)
    queue.append(node)
    print("****** ")
    print(visited)
    print("****** ")
    print(queue)
    print("****** ")
    print(graph)
    
    while queue:
        print("this is queue : " +str(queue))
        m = queue.pop(0)
        print(m, end=" ")
        
        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
        
    print("this is queue : "+str(queue))
    print("*********************")
    print("*********************")
    print("*********************")
    print("result is : " +str(visited))
    
             
print("Following is the Breadth-First Search")
BFS(visited, graph, '5')        
