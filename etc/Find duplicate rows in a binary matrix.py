from unicodedata import decimal


class Trie:
    def __init__(self):
        self.characters = [None] * 2
        self.isLeaf = False

    def __str__(self):
        return "{self.characters}".format(self=self)

def insert(head , A):
    cur = head 
    
    for i in A:
        if cur.characters[i] is None:
            cur.characters[i] = Trie()
        
        cur = cur.characters[i]
    
    if cur.isLeaf:
        return False
    
    cur.isLeaf = True
    return True    

 
if __name__ == '__main__':
    mat = [
        [1, 0, 0, 1, 0],
        [0, 1, 1, 0, 0],
        [1, 0, 0, 1, 0],
        [0, 0, 1, 1, 0],
        [0, 1, 1, 0, 0]
    ]
    
    s = set()
    
    for i in range(len(mat)):
        decimal = 0
        
        for j in range(len(mat[i])):
            decimal += mat[i][j] * pow(2,j)
        
        if decimal in s :
            print("Duplicate row found: Row", (i + 1))
        else :
            s.add(decimal)
            
    # *********************************************************OR*********************************************************
    # head = Trie()
    
    # for i ,e in enumerate(mat):
    #     if not insert(head,e):
    #         print(f'uplicate row found: Row #{i+1}')
