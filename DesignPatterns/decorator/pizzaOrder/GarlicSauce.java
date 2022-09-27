package DesignPatterns.decorator.pizzaOrder;

public class GarlicSauce extends ToppingDecorator {

    public GarlicSauce(Pizza newPizza) {
        super(newPizza);

    }

    public String getDescription() {
        return tempPizza.getDescription() + "\n - Homemade white garlic sauce";
    }

    public double getCost() {
        return tempPizza.getCost() + 0.45;
    }

}
