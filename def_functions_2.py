stock_prices = [34.68, 36.09, 34.94, 33.97, 34.68, 35.82, 43.41, 44.29, 44.65, 53.56, 49.85, 48.71, 48.71, 49.94, 48.53, 47.03, 46.59, 48.62, 44.21, 47.21]
def price_at(x):
  day_price = stock_prices[x-1]
  return day_price
def max_price(a,b):
  maximum_price = max(stock_prices[a],stock_prices[b])
  return maximum_price
def min_price(a,b):
  minimum_price = min(stock_prices[a],stock_prices[b])
  return minimum_price
print(price_at(5))
print(max_price(5,12))
print(min_price(3,10))
