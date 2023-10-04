def findPairs(nums):
 
    # create an empty dictionary
    # key —> sum of a pair of elements in the list
    # value —> list storing an index of every pair having that sum
    d = {}
 
    # consider every pair (nums[i], nums[j]), where `j > i`
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            # calculate the sum of the current pair
            total = nums[i] + nums[j]
 
            # if the sum is already present on the dictionary
            if total in d:
                # check every pair for the desired sum
                for m, n in d[total]:
 
                    # if pairs don't overlap, print and return them
                    if (m != i and m != j) and (n != i and n != j):
                        print('First Pair', (nums[i], nums[j]))
                        print('Second Pair', (nums[m], nums[n]))
                        return
 
            # insert the current pair into the dictionary
            d.setdefault(total, []).append((i, j))
 
    print('No non-overlapping pairs present')
 
 
if __name__ == '__main__':
 
    nums = [3, 4, 7, 9, -2]
    findPairs(nums)