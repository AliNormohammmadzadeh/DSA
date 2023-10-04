def findSublist(nums,target):
    d = {0 : -1}
    sum_so_far = 0
    for i in range(len(nums)):
        sum_so_far += nums[i]
        print(sum_so_far)
        if (sum_so_far - target) in d:
            
            print("Sublist found ",(d.get(sum_so_far - target)+1,i))
            return
        
        d[sum_so_far] = i
        print(d)

### second one ### 
def findSublist(nums, target):
 
    # maintains the sum of the current window
    windowSum = 0
 
    # maintain a window [low, high-1]
    (low, high) = (0, 0)
 
    # consider every sublist starting from `low` index
    for low in range(len(nums)):
 
        # if the current window's sum is less than the given sum,
        # then add elements to the current window from the right
        while windowSum < target and high < len(nums):
            windowSum += nums[high]
            high = high + 1
 
        # if the current window's sum is equal to the given sum
        if windowSum == target:
            print('Sublist found', (low, high - 1))
            return
 
        # At this point, the current window's sum is more than the given sum.
        # Remove the current element (leftmost element) from the window
        windowSum -= nums[low]


if __name__ == '__main__':
 
    # a list of integers
    nums = [0, 5, -7, 1, -4, 7, 6, 1, 4, 1, 10]
    target = 15
 
    findSublist(nums, target)