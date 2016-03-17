#Dynamic Programming

"""
#01.Extremely inefficient
def recMC(coinValueList,change):
    #change represents the amount of money you have to return

    minCoins = change
    
    if change in coinValueList:
        #you can pay change just using one coin
        return 1
    else:
        for i in [c for c in coinValueList if c <= change]:
        #the list contains the coins the amount of which is less than the value of change
            numCoins = 1 + recMC(coinValueList,change-i)
            if numCoins < minCoins:
                #update the optimal value
                minCoins = numCoins
    return minCoins
"""

"""
#02.remember past results(caching)
def recDC(coinValueList,change,knownResults):
    minCoins = change
    if change in coinValueList:
        knownResults[change] = 1
        return 1
    elif knownResults[change] > 0:
        return knownResults[change]
    else:
        for i in [c for c in coinValueList if c <= change]:
            numCoins = 1 + recDC(coinValueList,change-i,knownResults)
            if numCoins < minCoins:
                minCoins = numCoins
                knownResults[change] = minCoins
    return minCoins
"""
"""
#03.DP
def dpMakeChange(coinValueList,change,minCoins):
    for cents in range(change+1):
        #count from 0 to change
        #calculate how much coins you need to pay the present "cents" using the preceding results
        coinCount = cents

        for j in [c for c in coinValueList if c <= cents]:
            #using the preceding results
            if minCoins[cents-j] + 1 < coinCount:
                #check all cases and update the optimal value
                coinCount = minCoins[cents-j]+1
        #confirm the optimal value
        minCoins[cents] = coinCount
    return minCoins[change]
"""

#04.DP + show how to make change
def dpMakeChange(coinValueList,change,minCoins,coinsUsed):
    for cents in range(change+1):
        #count from 0 to change
        #calculate how much coins you need to pay the present "cents" using the preceding results
        coinCount = cents
        newCoin = 1

        for j in [c for c in coinValueList if c <= cents]:
            #using the preceding results
            if minCoins[cents-j] + 1 < coinCount:
                #check all cases and update the optimal value
                coinCount = minCoins[cents-j]+1
                #update the newly used coin
                newCoin = j
        #confirm the optimal value
        minCoins[cents] = coinCount
        #confirm the newly used coin
        coinsUsed[cents] = newCoin
    return minCoins[change]

def printCoins(coinsUsed,change):
    coin = change
    while coin > 0:
        thisCoin = coinsUsed[coin]
        print(thisCoin)
        coin = coin - thisCoin

def main():
    amnt = 63
    clist = [1,5,10,50]
    coinsUsed = [0]*(amnt+1)
    coinCount = [0]*(amnt+1)

    print("Making change for",amnt,"requires")
    print(dpMakeChange(clist,amnt,coinCount,coinsUsed),"coins")
    print("They are:")
    printCoins(coinsUsed,amnt)
    print("The used list is as follows:")
    print(coinsUsed)

main()




