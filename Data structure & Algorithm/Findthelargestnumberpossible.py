from functools import cmp_to_key

@cmp_to_key
def custom_compare(a,b):
    value1 = str(a) + str(b)
    value2 = str(b) + str(a)
    print("value1 =" ,value1)
    print("value2 =" ,value2)
    
    if value1 < value2:
        print("1")
        return 1
    if value1 > value2:
        print("-1")
        return -1
    else:
        print("0")
        return 0
    
  
def findLargestNumber(nums):
    nums.sort(key=custom_compare)
      
    return ''.join(map(str,nums))

  

if __name__ == '__main__':
    numbers = [10, 68, 97, 9, 21, 12]
 
    largestNumber = findLargestNumber(numbers)
    print('The largest number is', largestNumber)