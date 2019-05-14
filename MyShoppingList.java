import java.util.Scanner;
public class MyShoppingList{
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    String userInput;
    do {
      System.out.print("Welcome to the shopping mall what do you want to do? ");
      userInput = sc.next();
    } while (userInput != "Exit");
    Cart myCart = new Cart();
    Item Banana = new Item("Banana",1,40.0);
    Item Apple = new Item("Apple",2,30.0);
    myCart.addToCart(Banana);
    myCart.printCart();
    System.out.println(myCart.getTotal());
  }
}
