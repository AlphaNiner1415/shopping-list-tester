class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def getPrice(self):
        return self.price
    def getName(self):
        return self.name
    def __repr__(self):
        return '{name:'+self.name+', price:'+str(self.price)+ '}'

item1 = Item("Banana",20)
item2 = Item("Apple",30)
print(item1.getName())
class Cart:
    def __init__(self, shoppingList):
        self.shoppingList = shoppingList
    def addToCart(self, item):
        self.shoppingList.append(item)
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
    def getCart(self):
        ItemInCart = ""
        for item in self.shoppingList:
            ItemInCart = ItemInCart +" "+ item.getName()
        return ItemInCart
myCart = Cart([])

myCart.addToCart(item1)
myCart.addToCart(item2)
print(myCart.getPrice())
print(myCart.getCart())
#print(repr(myCart))
