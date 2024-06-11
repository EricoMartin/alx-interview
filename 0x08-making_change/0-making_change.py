#!/usr/bin/python3
""" code to determine the fewest number of
    coins needed to meet a given amount.
"""


def makeChange(coins, total):
    """
        code to make change breaking the problem
        into subproblems and caching them with DP
    """

    if total <= 0:
        return 0
    if not coins or coins is None:
        return -1

    minCoin = 0

    coins = sorted(coins)[::-1]
    for coin in coins:

        while(total >= coin):
            total -= coin
            minCoin += 1
        if (total == 0):
            return minCoin
    return -1

    ''' if total <= 0:
        return 0
    nextCoin = [total + 1] * (total + 1)
    nextCoin[0] = 0

    for i in range(1, total + 1):
        for j in range(0, len(coins)):
            if coins[j] <= i:
                nextCoin[i] = min(nextCoin[i], nextCoin[i - coins[j]] + 1)

    if nextCoin[total] > total:
        return -1
    else:
        return nextCoin[total]
    '''
