def findDuplicate(nums):
    visited = [False] * (len(nums) )
    for i in nums:

        if visited[i]:
            return i
        
        visited[i] = True
    return -1

#second one and useless
def findDuplicate(nums):
 
    xor = 0
 
    # take xor of all list elements
    for i in range(len(nums)):
        xor ^= nums[i]
        print(xor)
    print(xor)
 
    # take xor of numbers from 1 to `n-1`
    for i in range(1, len(nums)):
        xor ^= i
        print(xor)
    print(xor)
 
    # same elements will cancel each other as a ^ a = 0,
    # 0 ^ 0 = 0 and a ^ 0 = a
 
    # `xor` will contain the missing number
    return xor

if __name__ == "__main__":
    nums = [1,2,3,4,4]
    print('the duplicate element is : ', findDuplicate(nums))