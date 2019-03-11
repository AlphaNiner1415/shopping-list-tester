class Item:
    def __init__(self, unique_id, name, price):
        self.unique_id = unique_id
        self.name = name
        self.price = price
    def getPrice(self):
        return self.price
    def getName(self):
        return self.name
    def getId(self):
        return self.unique_id
    def __repr__(self):
        return '{id: '+str(self.unique_id)+', name: '+self.name+', price: '+str(self.price)+ '}'

item1 = Item(1,"Banana",20)
item2 = Item(2,"Apple",30)
item3 = Item(3,"Cherries",40)
# print(repr(item3))
class Cart:
    def __init__(self, shoppingList):
        self.shoppingList = shoppingList

    def addToCart(self, item):
        print(self.checkIfIn(item))
        print("ADDING " + item.getName() + " to your cart.")
        self.shoppingList.append(item)

    def checkIfIn(self,item):
        temp = False
        for i in self.shoppingList:

            if i.getName() == item.getName():
                print("Items already in your cart: " + item.getName())
                temp = True
            else:
                print("Nope")
                temp = False
        if temp:
            return temp #Item really is in the cart
        else:
            return temp  # item not in cart.



    ## One way to get the price and name of items
    ## Here the method returns the object Item at the specified index
    ##And that Item instance returns itself through the __repr__ function.
    def getItem(self,index):
        return self.shoppingList[index-1]

    def getPrice(self):
        total = 0
        for item in self.shoppingList:
            price = item.getPrice()
            total += price
        return total

    def getCartList(self):
        for item in self.shoppingList:
            print(item)
            # print("\n")

    def getCart(self):
        ItemInCart = ""
        for item in self.shoppingList:
            ItemInCart = ItemInCart +" "+ item.getName()
        return ItemInCart
myCart = Cart([])
myCart.addToCart(item1)
print("___________________________________________________________________________________________________________________________________")
myCart.checkIfIn(item1)
myCart.addToCart(item2)
myCart.checkIfIn(item2)
myCart.getCartList()
print(myCart.getPrice())

#print(repr(myCart))
