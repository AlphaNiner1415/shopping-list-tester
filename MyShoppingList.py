class ShoppingList(object):
    def __init__(self, customerName, items, cart,bill):
        self.customerName = customerName
        self.items = items
        self.cart = cart
        self.bill = bill
    def addToCart (self, items, cart):
        user_choice = input("Enter which items you'd like to add to cart")
        if user_choice in cart:
            print("You already have that item in your cart!")
        elif user_choice in items:
            cart = cart.append(user_choice)
            items.remove(user_choice)
            print("That item has been added to your cart!")
        else:
            print("Plese enter another item!! That item is not available!!")
    def checkOut (self, cart, items, bill):
        for i in cart:
            if i == "Ham"

## Items = Ham 20
## bacon 40
## Beans 30
items = ["Ham": 20, "Bacon": 40, "beans":30]
