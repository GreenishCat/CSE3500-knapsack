# Ananya Sripathi

def knapsack_greedy(capacity, items):
  #sort the items in the profit to weight ratio, from highest to lowest
  items.sort(key=lambda item: item[1] / item[0], reverse=True)
  total_profit = 0.0
  #checks each item's profit and weight in a loop
  for weight, profit in items:
    #if we can take it fully, then keep adding it to the knapsack
    while capacity >= weight:
      total_profit += profit
      capacity -= weight
    
    #do not allow fractional items (only whole multiple copies are allowed)
    if capacity == 0:
      break
  return total_profit

#example test case - multiple items in the knapsack
items = [(60, 10), (100, 20), (48, 12)]
capacity = 50
print(knapsack_greedy(items, capacity))

#example test case - capacity = 0
items = [(120, 40)]
capacity = 0
print(knapsack_greedy(items, capacity))

#example test case - no items in the knapsack
items = []
capacity = 60
print(knapsack_greedy(items, capacity))

#example test case - single item in the knapsack
items = [(80, 10)]
capacity = 10
print(knapsack_greedy(items, capacity))
