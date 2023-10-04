def swap(A,i,j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp


def revers(A,i , j):
    if A[i] >= j :
        return
    swap(A,i,j)
    revers(A,i+1,j-1)



def rev(A, beg ,end , m):
    if m <= 0:
        return
    if m > end -beg + 1:
        return
    
    for i in range(beg ,end +1 ,m):
        if i + m - 1 <= end:
            revers(A,i,i+m-1)

if __name__ == '__main__':
 
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    m = 3
 
    (beg, end) = (1, 8)
 
    # reverse
    rev(A, beg, min(end, len(A) - 1), m)
 
    # print the modified
    print(A)