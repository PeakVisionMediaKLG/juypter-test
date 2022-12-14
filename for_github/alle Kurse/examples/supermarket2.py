import random

supermarket = { "milk": {"quantity": 20, "price": 1.19},
               "biscuits":  {"quantity": 32, "price": 1.45},
               "butter":  {"quantity": 20, "price": 2.29},
               "cheese":  {"quantity": 15, "price": 1.90},
               "bread":  {"quantity": 15, "price": 2.59},
               "cookies":  {"quantity": 20, "price": 4.99},
               "yogurt": {"quantity": 18, "price": 3.65},
               "apples":  {"quantity": 35, "price": 3.15},
               "oranges":  {"quantity": 40, "price": 0.99},
               "bananas": {"quantity": 23, "price": 1.29}            
              }



customers = ["Frank", "Mary", "Paul"]
shopping_lists = { "Frank" : [('milk', 5), ('apples', 5), ('butter', 1), ('cookies', 1)],
   "Mary":  [('apples', 2), ('cheese', 4), ('bread', 2), ('pears', 3), ('bananas', 4), ('oranges', 1), ('cherries', 4)],
   "Paul":  [('biscuits', 2), ('apples', 3), ('yogurt', 2), ('pears', 1), ('butter', 3), ('cheese', 1), ('milk', 1), ('cookies', 4)]}

    
# filling the carts
carts = {}
for customer in customers:
    carts[customer] = []
    for article, quantity in shopping_lists[customer]:
        if article in supermarket:
            if supermarket[article]["quantity"] < quantity:
                quantity = supermarket[article]["quantity"]
            if quantity:
                supermarket[article]["quantity"] -= quantity
                carts[customer].append((article, quantity))
for customer in customers:                            
     print(carts[customer])
            
            
print("checkout")
for customer in customers:
    print("\ncheckout for " + customer + ":")
    total_sum = 0
    for name, quantity in carts[customer]:
        unit_price = supermarket[name]["price"]
        item_sum = quantity * unit_price
        print( "{0:3d} {1:12s} {2:8.2f} {3:8.2f}".format(quantity, name, unit_price, item_sum))
        total_sum += item_sum
    print("{0:22s} {1:11.2f}".format("total_sum:", total_sum))
