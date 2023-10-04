def printAllSublist(nums):
    for i in range(len(nums)):
        total = 0
        for j in range(i,len(nums)):
            total += nums[j]
            if total == 0 :
                print("sublist " ,(i ,j)) 
                
### second One ###
# Utility function to insert <key, value> into the dictionary
def insert(d, key, value):
 
    # if the key is seen for the first time, initialize the list
    d.setdefault(key, []).append(value)
 
 
# Function to print all sublists with a zero-sum present in a given list
def printallSublists(nums):
 
    # create an empty dictionary to store the ending index of all
    # sublists having the same sum
    d = {}
 
    # insert (0, -1) pair into the dictionary to handle the case when
    # sublist with zero-sum starts from index 0
    insert(d, 0, -1)
 
    total = 0
 
    # traverse the given list
    for i in range(len(nums)):
 
        # sum of elements so far
        total += nums[i]
 
        # if the sum is seen before, there exists at least one
        # sublist with zero-sum
        if total in d:
 
            list = d.get(total)
 
            # find all sublists with the same sum
            for value in list:
                print('Sublist is', (value + 1, i))
 
        # insert (sum so far, current index) pair into the dictionary
        insert(d, total, i)

if __name__ == '__main__':
 
    nums = [3, 4, -7, 3, 1, 3, 1, -4, -2, -2]
    printAllSublist(nums)