def dpMakeChange(coinValueList, change, minCoins, coinsUsed):
    for cents in range(change+1):
        coinCount = cents
        for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents-j] + 1 < coinCount:
                coinCount = minCoins[cents-j]+1
        minCoins[cents] = coinCount

    return minCoins[change]

def printCoins(coinsUsed, change):
    coin = change
    while coin > 0:
        thisCoin = coinsUsed[coin]
        print(thisCoin)
        coin = coin - thisCoin


def main():
    amount = 63
    clist = [1,5,10,21,25]
    coinsUsed = [0]*(amount+1)
    coinCount = [0]*(amount+1)

    print('Making change for ', amount, 'requires')
    print(dpMakeChange(clist, amount, coinCount, coinsUsed), 'coins')
    print('They are: ')
    printCoins(coinsUsed, amount)
    print('The used list is as follows: ')
    print(coinsUsed)

main()
