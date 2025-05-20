menu = ['Muffin', 'Flapjack', 'Coffee', 'Brownie', 'Smoothie', 'Cookie', 'Yoghurt'] # Creates a list for menu items

stock_dict = {'Muffin': 15, # Store stock count in a dictionary
              'Flapjack': 13,
              'Coffee': 26,
              'Brownie': 9,
              'Smoothie': 14,
              'Cookie': 22,
              'Yoghurt': 7
              }
item = stock_dict.keys() # Determine variable for keys
count = stock_dict.values() # Determine variable for value

price_dict = {'Muffin': 3.49, # Store price in a dictionary
              'Flapjack': 1.79,
              'Coffee': 2.29,
              'Brownie': 2.59,
              'Smoothie': 3.99,
              'Cookie': 1.99,
              'Yoghurt': 1.29
              }

total_stock = sum(count) # Add all the stock value together
total_price = sum(stock_dict[item] * price_dict[item] for item in stock_dict) # Multiply stock count by stock value
print(f"The total stock is {total_stock}, which comes to the total value of £{total_price}.") # Print the calculation