class node:
    def __init__(self,freq, symbol,left=None, right=None):
        self.freq = freq
        self.symbol = symbol
        self.right = right 
        self.left = left 
        self.huff = ""
        
def PrintNodes(node,val=""):
    newVal = val + str(node.huff)
    if(node.left):
        PrintNodes(node.left, newVal)
    if(node.right):
        PrintNodes(node.right, newVal)
    if(not node.left and not node.right):
        print(f"{node.symbol} ==> {newVal}")

        
chars = ['a', 'b', 'c', 'd', 'e', 'f']
 
# frequency of characters
freq = [ 5, 9, 12, 13, 16, 45]
 
# list containing unused nodes
nodes = []
 
# converting characters and frequencies
# into huffman tree nodes
for x in range(len(chars)):
    nodes.append(node(freq[x], chars[x]))
# for i in range(len(nodes)):
#     print(nodes[i].freq, nodes[i].symbol , nodes[i].left , nodes[i].right, nodes[i].huff ) 
        
while len(nodes) > 1 :
    nodes = sorted(nodes, key=lambda x: x.freq)
    left = nodes[0]
    right = nodes[1]
    right.huff = 1
    left.huff = 0
    
    newnode = node(left.freq+right.freq , left.symbol + right.symbol, left , right)
    nodes.remove(left)
    nodes.remove(right)
    nodes.append(newnode)

PrintNodes(nodes[0])
    
    