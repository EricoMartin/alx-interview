#!/usr/bin/python3
""" code to determine the fewest number of
    coins needed to meet a given amount.
"""


def makeChange(coins, total):
    """
        code to make change breaking the problem
        into subproblems and caching them with DP
    """

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
#    if (total < 1):
#        return 0

#    return changeCoin(coins, total, [0] * (total + 1))


'''def changeCoin(coins, total, nextCoin):
    """
        code to make change breaking the problem
        into subproblems and caching them with DP
    """
    if (total < 0):
        return -1

    if (total == 0):
        return 0

    if (nextCoin[total] != 0):
        return nextCoin[total]

    minim = sys.maxsize

    for coin in coins:
        change = changeCoin(coins, total - coin, nextCoin)
        if (change >= 0 and change < minim):
            minim = 1 + change

    if (minim == sys.maxsize):
        nextCoin[total] = -1
    else:
        nextCoin = minim
    return nextCoin[total]'''
