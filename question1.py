def maximize_profit(stock_prices):
    buy_day = 0
    sell_day = 0
    max_profit = 0

    for i in range(len(stock_prices)):
        for j in range(i + 1, len(stock_prices)):
            profit = stock_prices[j] - stock_prices[i]
            if profit > max_profit:
                max_profit = profit
                buy_day = i + 1
                sell_day = j + 1

    return buy_day, sell_day
# Example usage
stock_prices = [100, 180, 260, 310, 40, 535, 695]
buy_day, sell_day = maximize_profit(stock_prices)
print("Buy stock on day:", buy_day)
print("Sell stock on day:", sell_day)
