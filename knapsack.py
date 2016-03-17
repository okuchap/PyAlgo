#Knapsack

items = [1,2,3,4,5]
weights = [2,3,4,5,9]
values = [3,4,8,8,10]
bag = [0]*len(items)

def dpMakeBag(coinValueList,change,minCoins,coinsUsed):
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

def itemsInBag(items,weights,values,capacity,value=0):
    #Base cases:
    if capacity == 2:
        bag[0] = 2
        items[0] = 0
        value += 3

    if capacity == 3:
        bag[0] = 3
        item[1] = 0
        value += 4

    if capacity == 4:
        bag[0] = 4
        item[2] = 0
        value += 8

    if capacity == 5:
        bag[0] = 5
        item[3] = 0
        value += 8

    #Step case:
    else:
        for k in [weight in weights if weight<=capacity]:



