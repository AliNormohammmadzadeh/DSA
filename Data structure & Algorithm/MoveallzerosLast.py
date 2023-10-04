def swap(A, i,j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

def reorder(A):
    k = 0
    for i in A:
        if i:
            A[k] = i 
            k += 1
    for i in range(k, len(A)):
        A[i] = 0

def partition1(A):
    j = 0 
    for i in range(len(A)):
        if A[i]:
            swap(A, i, j)
            j += 1
        
if __name__ == "__main__":
    A = [6, 0, 8, 2, 3, 0, 4, 0, 1]
 
    reorder(A)
    print(A)
    
    partition1(A)
    print(A)
 

 