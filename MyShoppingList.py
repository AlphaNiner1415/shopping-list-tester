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
        return '{id:'+str(self.unique_id)+', name:'+self.name+', price:'+str(self.price)+ '}'

item1 = Item(1,"Banana",20)
item2 = Item(2,"Apple",30)
item3 = Item(3,"Cherries",40)
# print(repr(item3))
class Cart:
    def __init__(self, shoppingList):
        self.shoppingList = shoppingList
    def addToCart(self, item):
        self.shoppingList.append(item)
    # def checkIfIn(self,item):
    #     for i in self.shoppingList:
    #         if i.getName() == item.getName():
    #             print("already in")
    #         else:
    #             print("Nope")
    #             addToCart(self,item)


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
    def getCart(self):
        ItemInCart = ""
        for item in self.shoppingList:
            ItemInCart = ItemInCart +" "+ item.getName()
        return ItemInCart
myCart = Cart([])
myCart.addToCart(item1)
# myCart.checkIfIn(item2)
# myCart.checkIfIn(item1)
myCart.getCartList()

#print(repr(myCart))
