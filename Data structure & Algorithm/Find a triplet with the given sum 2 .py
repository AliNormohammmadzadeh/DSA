def printAllTriplets(nums,target):
    nums.sort()
    n = len(nums)
    for i in range(n-2):
        k = target - nums[i]
        (low , high) = (i+1, n-1)
        while low < high :
            if nums[low] + nums[high] < k :
                low += 1
            elif nums[low] + nums[high] > k :
                high -= 1
            else:
                print((nums[i] , nums[low], nums[high]))
                low += 1
                high -= 1


if __name__ == '__main__':
 
    nums = [2, 7, 4, 0, 9, 5, 1, 3]
    target = 6
 
    printAllTriplets(nums, target)
 
