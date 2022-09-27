package DesignPatterns.decorator.pizzaOrder;

public class PlainPizza  implements Pizza{

    @Override
    public String getDescription() {
        
        return "\n- Plain dough";
    }

    @Override
    public double getCost() {
        
        return 5;
    }
    
}
