class Node():
    def __init__(self,d):
        self.data = d 
        self.next = None
    def __str__(self) :
        return str(self.data)
        

head = None

def detectLoop(head):
    slowPointer = head
    fastPointer = head 
    
    while(slowPointer != None
          and fastPointer != None
          and fastPointer.next != None):
        slowPointer = slowPointer.next
        fastPointer = fastPointer.next.next
        if(slowPointer == fastPointer):
            return 1
        
    return 0 

head = Node(10)        
head.next = Node(20)        
head.next.next = Node(30)        
head.next.next.next = Node(40)        
head.next.next.next.next = Node(50)   
print(head)   

temp = head 
while(temp.next != None):
    print("this is temp .next : " +str(temp.next))
    temp = temp.next

temp.next = head 

if (detectLoop(head)):
    print("Loop exists in the linked List !!")
else:
    print("Loop does not in the linked List ! :##")