def findProduct(A):
    n = len(A)
    if n == 0 :
        return 
    
    left = [None] * n
    right = [None] * n
    
    left[0] = 1 
    right[n-1] = 1
    for i in range(1, n):
        left[i] = left[i-1] * A[i-1]
    
    for i in reversed(range(n-1)):
        right[i] = right[i+1] * A[i+1]
    
    for j in range(n):
            A[j] = left[j] * right[j]
            
### seconde one is more efficient ###
def findProduct1(A, n , left=1,i=0):
    if i == n :
        return 1
    
    curr = A[i]
    
    right = findProduct1(A,n,left * A[i],i+1)
    print("this is right  : ",right)
    print("this is left :" ,left)
    A[i] = left * right
    
    return curr * right
    

if __name__ == "__main__":
    A = [5, 3, 4, 2, 6, 8]
    findProduct1(A,len(A))
 
    # print the modified list
    print(A)