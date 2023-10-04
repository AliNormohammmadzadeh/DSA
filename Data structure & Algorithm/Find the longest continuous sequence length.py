
def findMaxSublistLength(X, Y):
 
    # create an empty dictionary
    d = {}
 
    # to handle the case when the required sequence starts from index 0
    d[0] = -1
 
    # stores length of the longest continuous sequence
    result = 0
 
    # `sum_x` and `sum_y` stores the sum of elements of `X` and `Y`,
    # respectively, till the current index
    sum_x = sum_y = 0
 
    # traverse both lists simultaneously
    for i in range(len(X)):
 
        # update `sum_x` and `sum_y`
        sum_x += X[i]
        sum_y += Y[i]
 
        # calculate the difference between the sum of elements in two lists
        diff = sum_x - sum_y
 
        # if the difference is seen for the first time, store the
        # difference and current index in a dictionary
        if diff not in d:
            d[diff] = i
 
        # if the difference is seen before, then update the result
        else:
            result = max(result, i - d[diff])
 
    return result
 
 
if __name__ == '__main__':
 
    X = [0, 0, 1, 1, 1, 1]
    Y = [0, 1, 1, 0, 1, 0]
 
    print('The length of the longest continuous sequence with the same sum is',
        findMaxSublistLength(X, Y))