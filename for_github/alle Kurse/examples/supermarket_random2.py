import random 

supermarket = { "milk": {"quantity": 5, "price": 1.19},
               "biscuits":  {"quantity": 3, "price": 1.45},
               "butter":  {"quantity": 10, "price": 2.29},
               "cheese":  {"quantity": 5, "price": 1.90},
               "bread":  {"quantity": 5, "price": 2.59}             
              }

available_articles = list(supermarket.keys()) + ["beans", "eggs"]
print(supermarket)

customers = ["Frank", "Mary", "Paul", "Jennifer"]
shopping_lists = {}
for customer in customers:
    items =random.randint(3, 10)
    shopping_lists[customer] = []
    for item in range(items):
        article_name = random.choice(available_articles)
        quantity = random.randint(1, 3)
        shopping_lists[customer].append((article_name, quantity))

for customer in customers:     
    print(customer + ":  " + str(shopping_lists[customer]))
    
print("shopping:")
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
            
            
            