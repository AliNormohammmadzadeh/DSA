
#Using Brute-Force
def FindPair(nums , target):
    for i in range(len(nums)-1):
        for j in range(i+1 ,len(nums)):
            if nums[i] + nums[j] == target:
                print("Pair Found in index : ",i,j)
                print("Pair Found at value of : ",nums[i],nums[j])
                return
    
    print("Paring not found")

#Using Sorting
def FindPair1(nums,target):
    nums.sort()
    (low , high) = (0 , len(nums)-1)
    
    while low < high:
        if nums[low] + nums[high] == target:
            print("Pair Found at value of : ",nums[low],nums[high])
            return

        if nums[low] + nums[high] < target:
            low += 1
        else:
            high -= 1
    
    print("Pair not found !")

#Using hash table

def FindPair2(nums,target):
    d = {}
    for i,e in enumerate(nums):
        if target - e in d :
            print("Pair found ",(nums[d.get(target-e)],nums[i]))
            return
        d[e] = i
    print("Pair not found")


if __name__ == "__main__":
    nums = [8, 7, 2, 5, 3, 1]
    target = 10
 
 
    FindPair2(nums, target)
 