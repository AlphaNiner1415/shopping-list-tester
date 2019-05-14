import java.util.ArrayList;
public class Cart{
  protected ArrayList<Item> items = new ArrayList<Item>();
  private double total;
  // private boolean isIn = false;

  public Cart(){
    items.clear();
    this.total = 0;
  }
  public Cart(ArrayList<Item> a, double t){
    items = a;
    total = t;
  }
  public void addToCart(Item myItem){
    this.items.add(myItem);
    total += myItem.getPrice();
  }
  public void getNumberofItems(){
    System.out.println(items.size());
  }
  public void printCart(){
    for(Item a : items){
      System.out.println(a.toString());
    }
  }
  public double getTotal(){
    return total;
  }
  public void setTotal(double r){
    total = r;
  }
  public void removeFromCart(Item myItem){

    items.remove(items.indexOf(myItem));
    total -= myItem.getPrice();
  }
  
}
