import sys

def findSmallestSublistLen(A,k):
    windowSum = 0
    length = sys.maxsize
    left = 0
    for right in range(len(A)):
        windowSum += A[right]
        while windowSum > k and left <= right:
            length = min(length, right - left + 1)
            windowSum -= A[left]
            left += 1
    
    if length == sys.maxsize:
        return 0
    
    return length







if __name__ == '__main__':
 
    # a list of positive numbers
    A = [1, 2, 3, 4, 5, 6, 7, 8]
    k = 21
 
    # find the length of the smallest sublist
    length = findSmallestSublistLen(A, k)
 
    if length != sys.maxsize:
        print("The smallest sublist length is", length)
    else:
        print("No sublist exists")