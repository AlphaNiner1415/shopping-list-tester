class Item(object):
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
    def __eq__(self, other):
        myName = self.name
        hisName = other.name
        if myName == hisName:
            return True
        else:
            return False

    def __repr__(self):
        return '{id: '+str(self.unique_id)+', name: '+self.name+', price: '+str(self.price)+ '}'

Banana = Item(1,"Banana",20)
Apple = Item(2,"Apple",30)
Cherries = Item(3,"Cherries",40)
# print(repr(item3))
class Cart(object):
    def __init__(self, shoppingList):
        self.shoppingList = shoppingList

    def addToCart(self, item, mallStand):
        willAdd = not (self.checkIfIn(item))
        print(willAdd)
        if willAdd == True:
            print("ADDING " + item.getName() + " to your cart.")
            self.shoppingList.append(item)
            mallStand.shoppingList.remove(item)
        elif willAdd == False:
            print("ERROR! UNABLE to add item to cart.")
    # def removeFromCart(self, item):

    def checkIfIn(self,item):
        isIn = False
        for i in self.shoppingList:

            if i.getName() == item.getName():
                print("Items already in your cart: " + item.getName())
                isIn = True
            else:
                print("Nope")
                isIn = False
        return isIn
    def removeFromCart(self,item):
        for i in self.shoppingList:
            if i in self.shoppingList:
                self.shoppingList.remove(i)
        return self.shoppingList


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
mallStand = Cart([Apple,Banana, Cherries])

print("WELCOME TO THE SHOPPING MALL!!!!!! THE MALL STAND CONTAINS")
print(mallStand.getCart())




#print(repr(myCart))
