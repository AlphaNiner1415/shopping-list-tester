public class Item {
  protected String name;
  protected int unique_id;
  protected Double price;

  public Item(String s1, Integer i1, Double d1) {
    this.name = s1;
    this.unique_id = i1;
    this.price = d1;
  }
  public double getPrice(){
    return price;
  }
  public String getName(){
    return name;
  }
  public int getId(){
    return unique_id;
  }
  public String toString(){
    return "name= " + name + " price= $" + price;
  }
}
