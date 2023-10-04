def DFS(graph, start , visited = None):
    if visited is None :
        visited = set()
    visited.add(start)
    print(start)
    for next in graph[start] - visited:
        print('graph start is : ' + str(graph[start]))
        print('visited is  : ' + str(visited))
        print('next is : ' + str(next))
        DFS(graph, next, visited)
    return visited 

graph = {'0': set(['1', '2']),
         '1': set(['0', '3', '4']),
         '2': set(['0']),
         '3': set(['1']),
         '4': set(['2', '3'])}

DFS(graph,'0')