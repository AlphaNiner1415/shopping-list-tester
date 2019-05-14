public class MyShoppingList{
  public static void main(String[] args) {
    Cart myCart = new Cart();
    Item Banana = new Item("Banana",1,40.0);
    myCart.addToCart(Banana);
    myCart.printCart();
    System.out.println(myCart.getTotal());
  }
}
