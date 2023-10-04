def findLargestSublist(nums):
    d = {}
    d[0] = -1
    length = 0
    total = 0
    index_ending = -1
    for i in range(len(nums)):
        total += -1 if nums[i] == 0 else 1
        if total in d :
            if length < i - d.get(total):
                length = i - d.get(total)
                index_ending = i
        else:
            d[total] = i
    print(d)
    
    if index_ending != 1 :
        print((index_ending - length +1 ,index_ending ))
    else:
        print("No sublist found")

if __name__ == '__main__':
 
    nums = [0, 0, 1, 0, 1, 0, 0]
    findLargestSublist(nums)
    nums = [1, 0, 1, 0, 1, 0, 0]
    findLargestSublist(nums)
    nums = [0, 0, 1, 0, 1, 1, 0,0,0,0,1,1,1,1,1,1,]
    findLargestSublist(nums)