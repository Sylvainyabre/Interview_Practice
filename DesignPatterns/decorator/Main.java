package DesignPatterns;

public class Main {
    public static void main(String[]args){
    Pizza customizedPizza = new ParmesanCheese(new ChickenMeat(new GarlicSauce(new PlainPizza())));
    System.out.println(customizedPizza.getDescription());
    System.out.println("TOTAL COST: " + customizedPizza.getCost());
    }
}
