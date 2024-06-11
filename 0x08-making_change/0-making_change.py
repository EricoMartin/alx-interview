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
    nextCoin = [amount + 1] * (amount + 1)
    nextCoin[0] = 0

    for i in range(1, total + 1):
        for j in range(0, len(coins)):
            if coins[j] <= i:
                    nextCoin[i] = min(nextCoin[i], nextCoin[i - coins[j]] + 1)

    if nextCoin[total] > total:
        return -1
    return nextCoin[total]
