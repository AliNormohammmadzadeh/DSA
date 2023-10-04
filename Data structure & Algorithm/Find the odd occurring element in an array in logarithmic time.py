def findOddOccuring(nums):
    xor= 0 
    for i in nums:
        xor = xor ^ i
    return xor


def findOddOccuring(nums, low, high):
 
    # base case
    if low == high:
        return low
 
    # find the middle index
    mid = (low + high) // 2
 
    # if `mid` is odd
    if mid % 2 == 1:
 
        # if the element before `mid` is the same as the middle element, the odd
        # element lies on the right side; otherwise, it lies on the left side
        if nums[mid] == nums[mid - 1]:
            return findOddOccuring(nums, mid + 1, high)
        else:
            return findOddOccuring(nums, low, mid - 1)
 
    # `mid` is even
    else:
 
        # if the element next to `mid` is the same as the middle element, the odd
        # element lies on the right side; otherwise, it lies on the left side
        if nums[mid] == nums[mid + 1]:
            return findOddOccuring(nums, mid + 2, high)
        else:
            return findOddOccuring(nums, low, mid)
 
 
if __name__ == '__main__':
 
    nums = [0, 2, 1, 1, 3, 3, 2, 2, 4, 4, 3, 0, 0]
 
    index = findOddOccuring(nums, 0, len(nums) - 1)
    print('The odd occurring element is', nums[index])

# if __name__ == '__main__':
 
#     nums = [2, 2, 1, 1, 3, 3, 2, 2, 4, 4, 3, 1, 1]
 
#     print('The odd occurring element is', findOddOccuring(nums))