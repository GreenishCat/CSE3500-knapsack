# Alice Chen

def knapsack(W, items):
    """
    W = maximum weight capacity 
    items = list of tuples (weights, profits)
    weight = list of item weights
    value = list of item profits/values
    """
    weight = [w for w, _ in items]
    value = [v for _, v in items]

    n = len(items) # number of items 
    
    # initializing 2D DP table (W+1 * n+1) with 0s
    # stores the maximum value we can get using i items such that the knapsack capacity is w
    dp = [[0 for _ in range(W+1)] for _ in range(n+1)]

    # Build table dp[i][w] using bottom-up tabulation 
    for i in range(n+1):
        for w in range(W+1):

            # if there is no item or the knapsack's capacity is 0
            if i == 0 or w == 0:
                dp[i][w] = 0
            else:
                pick = 0 

                # pick ith item if it does not exceed the capacity of knapsack
                if weight[i-1] <= w: 
                    pick = value[i - 1] + dp[i - 1][w - weight[i - 1]]

                # don't pick
                notPick = dp[i - 1][w]

                dp[i][w] = max(pick, notPick)

    return dp[n][W]

    # O(n*W) time and space (tabulation)
    # O(W) space for 1D dp table
    # handles large n but not large W

# add test cases
