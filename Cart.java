import java.util.ArrayList;
public class Cart{
  ArrayList<String> items;
  double total;
  // private boolean isIn = false;

  public Cart(){
    items = new ArrayList<String>();
  }
  public void addToCart(String item){
    items.add(item);
  }
  public void getNumberofItems(){
    System.out.println(items.size());
  }
  public void removeFromCart(String item){
    items.remove(item);
  }
  
}
