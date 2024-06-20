#!/usr/bin/python3
''' Find prime numbers from 1 upto n
    using the seive of eratoshtesis
'''


def findPrimes(n):

    primeList = [True] * (n + 1)
    p = 2

    while (p * p <= n):
        if primeList[p]:
            for i in range(p * p, n + 1, p):
                primeList[p] = False

        p += 1

    primeArray = [p for p in range(2, n + 1) if primeList[p]]
    return primeArray


def simulateGame(x, n):
    ''' Players take turns to play '''

    turns = 0

    numList = list(range(1, n + 1))
    primesList = [False] * (n + 1)

    for i in x:
        if i > n:
            break
        primesList[i] = True

    for num in numList:
        if primesList[num]:
            turns = 1 - turns

    return 'Maria' if turns == 1 else 'Ben'


def isWinner(x, nums):
    ''' Find winner of the game '''

    if not nums or x <= 0:
        return None

    numMax = max(nums)
    highPrime = findPrimes(numMax)
    maria = 0
    ben = 0

    for num in nums:
        gameWinner = simulateGame(highPrime, num)

        if gameWinner == 'Maria':
            maria += 1
        elif gameWinner == 'Ben':
            ben += 1

    if maria > ben:
        return 'Maria'
    elif ben > maria:
        return 'Ben'
    else:
        return None
