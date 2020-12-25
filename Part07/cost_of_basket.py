## Compute cost of a basket, given prices and quantities
#
# | Good      | **Price**       | **Quantity** |
# | :-------- | :------------:  | :----------: |
# | Cola      | 1.25            | 5            |
# | Water     | 0.75            | 7            |
# | Chocolate | 3               | 4            |

# Compute cost of individual goods and store them in a variables
cost_cola      = 1.25 * 5
cost_water     = 0.75 * 7
cost_chocolate = 3 * 4

# Finally, use the previously created variables to store the cost of the basket
cost_basket = cost_cola + cost_water + cost_chocolate

# Notice that when you create a new variable, it does not show automatically
# Use the print() function to do this
print(cost_basket)
