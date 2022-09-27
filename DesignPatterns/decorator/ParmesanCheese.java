package DesignPatterns;

public class ParmesanCheese extends ToppingDecorator {

    public ParmesanCheese(Pizza newPizza) {
        super(newPizza);

    }

    public double getCost(){
        //We are able to access the tempPizza variable here because it's' protected
        return tempPizza.getCost() + 1.23;
    }

    public String getDescription(){
        return tempPizza.getDescription ()+ "\n- Italian Parmesan Cheese";
    }
}
