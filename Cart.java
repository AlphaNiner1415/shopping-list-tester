import java.util.ArrayList;
public class Cart{
  protected ArrayList<Item> items = new ArrayList<Item>();
  private double total;
  // private boolean isIn = false;

  public Cart(){
    items.clear();
    this.total = 0;
  }
  public void addToCart(Item myItem){
    this.items.add(new Item(myItem.name, myItem.unique_id, myItem.price));
  }
  public void getNumberofItems(){
    System.out.println(items.size());
  }
  public void printCart(){
    System.out.println();
  }
  public double getTotal(){
    return total;
  }
  public void setTotal(double r){
    total = r;
  }
  public void removeFromCart(Item myItem){

    items.remove(items.indexOf(myItem));
  }
  
}
