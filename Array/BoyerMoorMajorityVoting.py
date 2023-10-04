def FindMajority(arr, n):
    candidate = -1
    vote = 0
    
    for i in range(n):
        if(vote == 0):
            candidate = arr[i]
            vote = 1 
        else:
            if(arr[i] == candidate):
                vote += 1
            else :
                vote -= 1
    count = 0
    
    for i in range(n):
        if(arr[i] == candidate):
            count += 1
            
    if(count > n // 2):
        return candidate
    else:
        return "No Element Higher than Avrage"


#test Cases
arr = [ 1,1,1,1,2,3,4,4,5]
arr2 = [ 1,1,1,1,2,1,2,1,1,4,4,5]
arr3 = [ 1,1,1,1,2,3,4,4,5,2,5,1,1,1]
arr4 =[ 1,1,2]
n4 = len(arr4)
n = len(arr)
n1 =len(arr2)
n2 =len(arr3)
majority = FindMajority(arr,n)
print(" The Majority Element is : " ,majority) 
majority = FindMajority(arr2,n1)
print(" The Majority Element is : " ,majority) 
majority = FindMajority(arr3,n2)
print(" The Majority Element is : " ,majority) 
majority = FindMajority(arr4,n4)
print(" The Majority Element is : " ,majority) 
