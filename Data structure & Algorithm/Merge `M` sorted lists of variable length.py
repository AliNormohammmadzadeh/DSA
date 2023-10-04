import heapq
from heapq import heappop , heappush

class Node:
    def __init__(self,value ,list_num,index):
        self.value = value
        self.list_num = list_num
        self.index = index
        
    def __lt__(self,other):
        return self.value < other.value

def print_sorted(lists):
    pq = [Node(lists[i][0],i,0) for i in range(len(lists)) if len(lists[i]) >= 1]
    heapq.heapify(pq)
    
    while pq:
        min = heappop(pq)
        print(min.value,end=' ')
        if min.index + 1 < len(lists[min.list_num]):
            min.index = min.index + 1
            min.value = lists[min.list_num][min.index]
            heappush(pq,min)
            
if __name__ == '__main__':
 
    list = [[10, 20, 30, 40], [15, 25, 35], [27, 29, 37, 48, 93], [32, 33]]
    print_sorted(list)