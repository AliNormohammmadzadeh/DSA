import sys 

def findSublist(A,k):
    if not len(A) or len(A) <= k:
        return
    
    window_sum = 0 
    last = 0
    min_winow = sys.maxsize
    
    for i in range(len(A)):
        window_sum += A[i]
        if i + 1 >= k:
            if min_winow > window_sum:
                min_winow = window_sum
                last = i
            window_sum -= A[i+1-k]
    
    print("The minimum sum sublist is :" ,(last-k+1,last))
    
if __name__ == '__main__':
 
    A = [10, 4, 2, 5, 6, 3, 8, 1]
    k = 3
 
    findSublist(A, k)