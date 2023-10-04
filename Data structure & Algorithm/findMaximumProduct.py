import sys

def findMaximumProduct(nums):
    if len(nums)< 2:
        return
    
    max_product = - sys.maxsize
    max_i = max_j = -1
    
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if max_product < nums[j] * nums[i]:
                max_product = nums[j] * nums[i]
                (max_i, max_j) = (i, j)
    
    print("Pair is " ,(nums[max_i], nums[max_j]))  
    
    
### second one ###
def findMaximumProduct2(nums):
    n = len(nums)
    if n < 2 :
        return
    
    nums.sort()
    if (nums[0] * nums[1] < nums[n-1] * nums[n-2]):
        print("Pair is ", (nums[n-1], nums[n-2]))
    else:
        print("Pair is ", (nums[0], nums[1]))
    



if __name__ == "__main__":
    A = [-10, -3, 5, 6, -2]
    findMaximumProduct2(A)
 