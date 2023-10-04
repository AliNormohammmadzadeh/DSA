import sys
 
 
# Function to find the smallest window in a list, sorting which will
# make the entire list sorted
def findSublist(A):
 
    leftIndex = rightIndex = -1
 
    # traverse from left to right and keep track of maximum so far
    max_so_far = -sys.maxsize
    for i in range(len(A)):
        if max_so_far < A[i]:
            max_so_far = A[i]
 
        # find the last position that is less than the maximum so far
        if A[i] < max_so_far:
            rightIndex = i
 
    # traverse from right to left and keep track of the minimum so far
    min_so_far = sys.maxsize
    for i in reversed(range(len(A))):
        if min_so_far > A[i]:
            min_so_far = A[i]
 
        # find the last position that is more than the minimum so far
        if A[i] > min_so_far:
            leftIndex = i
 
    if leftIndex == -1:
        print("Array is already sorted")
        return
 
    print("Sort list from index", leftIndex, "to", rightIndex)
 
 
if __name__ == '__main__':
 
    A = [1, 3, 2, 7, 5, 6, 4, 8]
    findSublist(A)