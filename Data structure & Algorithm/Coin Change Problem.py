def count(S,target):
    if target == 0 :
        return 1
    
    if target < 0:
        return 0
    result = 0
    for c in S:
        result += count(S,target-c)
    return result




if __name__ == '__main__':
 
    # `n` coins of given denominations
    S = [1, 2, 3]
 
    # total change required
    target = 4
 
    print('The total number of ways to get the desired change is', count(S, target))