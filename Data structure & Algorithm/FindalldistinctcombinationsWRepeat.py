def findCombinations(A , k , i=0 , out=[]):
    if len(out) == k:
        print(out)
        return
    
    j = i 
    while j < len(A):
        out.append(A[j])
        findCombinations(A,k,j,out)
        out.pop()
        while j < len(A) -1 and A[j] == A[j+1]:
            j += 1
        j += 1

### with repeat ####
# Function to print all distinct combinations of length `k`, where the
# repetition of elements is allowed
def findCombinations(A, out, k, i, n):
 
    # base case: if the combination size is `k`, print it
    if len(out) == k:
        print(out)
        return
 
    # start from the previous element in the current combination
    # till the last element
    for j in range(i, n):
 
        # add current element `A[j]` to the solution and recur with the
        # same index `j` (as repeated elements are allowed in combinations)
        out.append(A[j])
        findCombinations(A, out, k, j, n)
 
        # backtrack: remove the current element from the solution
        out.pop()
 



if __name__ == "__main__":
    A = [1,2,1]
    k =2 
    
    
    A.sort()
    findCombinations(A,k)
