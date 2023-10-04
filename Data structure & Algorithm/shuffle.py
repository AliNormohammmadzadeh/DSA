from random import randrange 

def swap(A,i,j):
    tmp = A[i]
    A[i] = A[j]
    A[j] = tmp
    
def shuffle(A):
    for i in range(len(A)):
        j = randrange(i,len(A))
        swap(A,i,j)

if __name__ == '__main__':
 
    A = [1, 2, 3, 4, 5, 6]
 
    for i in range(5):
        shuffle(A)
 
    # print the shuffled list
        print(A)