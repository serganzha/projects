menu = ["coffee", "muffin", "sandwich", "tea"]
# list of items in the cafe
stock = {"coffee": 200, "muffin": 200, "sandwich": 100, "tea": 1200}
# dictionary containing stock values for each item
price = {"coffee": 3.2, "muffin": 2.0, "sandwich": 4.6, "tea": 2.0}
# dictionary containing price values for each item
total_stock = 0
# initial stock value will be set to 0, and formula below will add the total stock value to it, showing total
for items in menu:
    item_value = stock[items] * price[items]
    total_stock += item_value

print("The total stock worth in the cafe is: ", total_stock)
