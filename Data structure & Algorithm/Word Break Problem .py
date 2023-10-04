CHAR_SIZE = 26

class Node:
    next = [None] * CHAR_SIZE
    exist = False

def insertTrie(head , s):
    node = head 
    for c in s :
        index = ord(c) - ord('a')
        if node.next[index] is None:
            node.next[index] = Node()
        node = node.next[index]
    node.exist = True
    
def WordBreak(head, s):
    n = len(s)
    good = [None] * (n+1)
    good[0] = True
    for i in range(n):
        if good[i]:
            node = head
            for j in range(i , n):
                if node is None:
                    break
                index = ord(s[j]) - ord('a')
                node = node.next[index]
                if node and node.exist:
                    good[j+1] = True
    return good[n]


if __name__ =="__main__":
    words = [
        'self', 'th', 'is', 'famous', 'word', 'break', 'b', 'r',
        'e', 'a', 'k', 'br', 'bre', 'brea', 'ak', 'prob', 'lem'
    ]
    s = 'wordbreakproblem'
    t = Node()
    for word in words:
        insertTrie(t,word)
    
    if WordBreak(t,s):
        print("string can be sagemented")
    else:
        print("the string can\'t be segmented")