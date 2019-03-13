import java.util.ArrayList;
public class Cart{
  public ArrayList shoppingList = new ArrayList();
  private boolean isIn = false;

  public Cart(){
    shoppingList.add("");
  }
  public void addToCart(ArrayList item){
    shoppingList.add(item);
    System.out.println(shoppingList);
  }
  // public boolean checkIfIn(ArrayList shoppingList, item, boolean isIn){
  //   for(int i = 0; i< shoppingList.size();i++){
  //     if(item.unique_id ==
  //   }
  //   return isIn;
  // }
}
