def merge(X, Y, m, n):
    k = m + n + 1
    while m >= 0 and n >= 0:
        if X[m] > Y[n]:
            X[k] = X[m]
            m -= 1 
            k -= 1
        else:
            X[k] = Y[n]
            n -= 1
            k -= 1
    while n >= 0:
        X[k] = Y[n]
        n -= 1
        k -= 1
        
    for i in range(len(Y)):
        Y[i] = 0



def rerange(X,Y):
    if not len(X):
        return
    
    k = 0
    for i in range(len(X)):
        if X[i]:
            X[k] = X[i]
            k += 1
    
    
    merge(X, Y, k - 1, len(Y) - 1)

if __name__ == '__main__':
 
    # vacant cells in `X[]` is represented by 0 
    X = [0, 2, 0, 3, 0, 5, 6, 0, 0]
    Y = [1, 8, 9, 10, 15]

    ''' Validate input before calling `rearrange()`
        1. Both lists `X[]` and `Y[]` should be sorted (ignore 0's in `X[]`)
        2. Size of list `X[]` >= size of list `Y[]` (i.e., `m >= n`)
        3. Total number of vacant cells in list `X[]` = size of list `Y[]` '''
 
    # merge `Y` into `X`
    rerange(X, Y)
 
    # print merged list
    print(X)
    print(Y)