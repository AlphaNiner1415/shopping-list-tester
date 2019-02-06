items2 ={}
items2['ham'] =20
items2['bacon'] = 40
items2['beans'] = 20
print(items2)
class ShoppingList(object):
    def __init__(self, customerName, items, cart,bill):
        self.customerName = customerName
        self.items = items
        self.cart = cart
        cart = {}
        self.bill = bill
    def addToCart (self, items, cart, userinp):
        
        if user_choice not in items:
            print("Plese enter another item!! That item is not available!!")
            return cart, items
        else:
            print(items[userinp])
            cart.update(items[userinp])
            print(cart)
            items.pop(userinp)
            print("That item has been added to your cart!")
            return cart, items
        print(cart)
    def checkOut (self, cart, items, bill):
        for i in cart:
            if i == "ham":
                bill += items.get('ham')
            if i == "bacon":
                bill += items.get('bacon')
            if i == "beans":
                bill += items.get('beans')
        print("Here is your total bill: $",bill)
bobList = ShoppingList("Bob",items2,{},0)
bobList.items = items2
user_choice = input("Enter which items you'd like to add to your cart ")
bobList.addToCart(items2,bobList.cart,user_choice)
print(bobList.cart)
bobList.checkOut(bobList.cart,bobList.items, bobList.bill)

## Items = Ham 20
## bacon 40
## Beans 30
