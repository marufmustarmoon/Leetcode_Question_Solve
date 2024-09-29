def maxProfit(prices):

    left = 0
    right = 1
    maxprofit = 0

    while right < len(prices):

        if  prices[left] < prices[right] :

            maxprofit = max (maxprofit,prices[right] - prices[left])

        else:
            left = right

        right = right + 1

    return maxprofit

        




prices = [7,1,5,3,6,4]

result = maxProfit(prices)
print(result)