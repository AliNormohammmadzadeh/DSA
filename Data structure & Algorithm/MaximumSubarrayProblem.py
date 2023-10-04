import sys 

def kadaneNeg(A):
    max_so_far = - sys.maxsize
    max_ending_here = 0 
    for i in range(len(A)):
        max_ending_here = max_ending_here + A[i]
        max_ending_here = max(max_ending_here, A[i])
        max_so_far = max(max_so_far,max_ending_here)
    
    return max_so_far

if __name__ == '__main__':
    A = [-8, -3, -6, -2, -5, -4]
    B = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print("The sum of contiguous sublist with the largest sum is", kadaneNeg(A))
    print("The sum of contiguous sublist with the largest sum is", kadaneNeg(B))