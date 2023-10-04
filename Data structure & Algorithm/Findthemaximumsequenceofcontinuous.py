def findLongestSequence(A,k):
    left = 0 
    window = 0
    left_index= 0
    count = 0
    
    for right in range(len(A)):
        if A[right] == 0:
            count +=1
        
        while count > k:
            if A[left] == 0:
                count -=1
            left += 1
        
        if right - left + 1 > window:
            window = right - left + 1
            left_index = left
        
    if window == 0 :
        return

    print("The Longest sequence is:",window, "from index", left_index , "to index " ,(left_index+window-1))    
            




if __name__ == '__main__':
 
    A = [1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0]
    k = 2
 
    findLongestSequence(A, k)