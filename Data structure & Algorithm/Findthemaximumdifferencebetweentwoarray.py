import sys

def getMaxDiff(A):
    n = len(A)
    diff = - sys.maxsize
    
    if n == 0 :
        return diff
    
    max_so_far = A[n-1]
    for i in reversed(range(n-1)):
        if A[i] >= max_so_far:
            max_so_far = A[i]
        else:
            diff = max(diff , max_so_far - A[i])

    return diff
if __name__ == '__main__':
 
    A = [2, 7, 11, 5, 0, 3, 10]
    diff = getMaxDiff(A)
    if diff != -sys.maxsize:
        print("The maximum difference is", diff)