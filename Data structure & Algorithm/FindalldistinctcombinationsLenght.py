def findCombinations(A, n , k , subarray, out=()):
    if len(A) == 0 or k > n:

        return

    if k == 0:
        print(out)
        subarray.add(out)
        return 
    
    for i in reversed(range(n)):
        findCombinations(A, i , k -1 , subarray , out +(A[i],))




def getDisticntSubarrays(A,k):
    subarrays = set()
    findCombinations(A, len(A) , k , subarrays)
    return subarrays




if __name__ == "__main__":
    A = [1 ,2,3,4,5,6,3,4,6,7,3]
    k = 5
    
    subarrays = getDisticntSubarrays(A, k)
    print(subarrays)
    