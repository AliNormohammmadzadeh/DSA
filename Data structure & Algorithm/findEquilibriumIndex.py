import iniconfig
from numpy import indices


def findEquilibriumIndex(A):
    left = [0] * len(A)
    right = 0 
    for i in range(1,len(A)):
        left[i] = left[i-1] + A[i-1]
        print((i,left[i]))
    
    indices = []
    for i in reversed(range(len(A))):
        if left[i] == right:
            indices.append(i)
        right += A[i]
    print(left)
    print("Equilibrium Index found at", indices)
 
### second oen ###
def findEquilibriumIndex2(A):
    total = sum(A)
    right = 0 
    andices = []
    for i in reversed(range(len(A))):
        if right == total - (A[i] + right):
            andices.append(i)
        right += A[i]
    
    print("Equilibrium Index found at", andices)
 
if __name__ == '__main__':
 
    A = [0, -3, 5, -4, -2, 3, 1, 0]
 
    findEquilibriumIndex2(A)
    for i in reversed(range(len(A))):
        print(i)