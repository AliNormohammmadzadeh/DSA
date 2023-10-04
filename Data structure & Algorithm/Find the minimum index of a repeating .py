def findMinIndex(A):
    minIndex = len(A)
    s = set()
    for i in reversed(range(len(A))):
        if A[i] in s:
            minIndex = i
        else :
            s.add(A[i])
        
    if minIndex == len(A):
        return -1

    return minIndex


if __name__ == '__main__':
 
    A = [5, 6, 3, 4, 3, 6, 4]
    A = [1, 2, 3, 4, 5, 6]
 
    minIndex = findMinIndex(A)
 
    if minIndex != len(A):
        print("The minimum index of the repeating element is", minIndex)
    else:
        print("Invalid Input")