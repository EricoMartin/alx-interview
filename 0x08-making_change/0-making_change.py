#!/usr/bin/python3
""" code to determine the fewest number of
    coins needed to meet a given amount.
"""


def makeChange(coins, total):
    """ main code """
    if (total < 1):
        return 0

    return changeCoin(coins, total, [0] * (total + 1))


def changeCoin(coins, total, nextCoin):
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
            minim = change + 1

    if (minim == sys.maxsize):
        nextCoin[total] = -1
    else:
        nextCoin = minim
    return nextCoin[total]
