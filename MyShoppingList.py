class ShoppingList(object):
    def __init__(self, customerName, items, cart):
        self.customerName = customerName
        self.items = items
        self.cart = cart
    def addToCart (items, cart):
        user_choice = input("Enter which items you'd like to add to cart")
        if user_choice in cart:
            print("You already have that item in your cart!")
        elif user_choice in items:
            cart = cart.append(user_choice)
            items.remove(user_choice)
        else:
            print("Plese enter another item!! That item is not available!!")
