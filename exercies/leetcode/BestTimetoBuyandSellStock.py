def max_profit(prices):
    max_profit, min_price = 0, float('inf')
    for price in prices:
        min_price = min(min_price, price)
        print("min price {}".format(min_price))
        profit = price - min_price
        print("profit {}".format(profit))
        max_profit = max(max_profit, profit)
        print("max_profit {}".format(max_profit))
    return max_profit

myinput = [7,1,5,3,6,4]
print(max_profit(myinput))
