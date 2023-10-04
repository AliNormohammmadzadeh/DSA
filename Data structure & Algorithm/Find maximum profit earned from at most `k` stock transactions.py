import sys

def findMaxProfit(price,k):
    n = len(price)
    if n <= 1:
        return 0
    
    profit = [[0 for x in range(n+1)] for y in range(k+1)]
    for i in range(k+1):
        prev_diff = -sys.maxsize
        for j in range(n):
            if i == 0 or j == 0:
                profit[i][j] = 0
            else:
                prev_diff = max(prev_diff,profit[i-1][j-1] - price[j-1])
                profit[i][j] = max(profit[i][j-1],price[j] + prev_diff)
    
    return profit[k][n-1]

if __name__ == '__main__':
 
    price = [1, 5, 2, 3, 7, 6, 4, 5]
    k = 3
 
    print('The maximum possible profit is', findMaxProfit(price, k))