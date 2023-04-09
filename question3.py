import csv
def calculate_high_low_prices(csv_file):
 stock_prices = {}
 with open(csv_file, 'r') as file:
 csv_reader = csv.reader(file)
 next(csv_reader) # Skip the header row
 for row in csv_reader:
 ticker = row[0]
 price = float(row[2])
 if ticker not in stock_prices:
 stock_prices[ticker] = [price] # Initialize with the first price as both high and 
low
 else:
 # Update the high and low prices if necessary
 if price > stock_prices[ticker][0]:
 stock_prices[ticker][0] = price # Update the high price
 elif price < stock_prices[ticker][1]:
 stock_prices[ticker][1] = price # Update the low price
 return stock_prices
