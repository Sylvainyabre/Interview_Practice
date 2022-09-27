package DesignPatterns;

public class ChickenMeat extends ToppingDecorator {

    public ChickenMeat(Pizza newPizza) {
        super(newPizza);

    }

    public String getDescription() {
        return tempPizza.getDescription() + "\n - Shredded chicken breast ";
    }

    public double getCost() {
        return tempPizza.getCost() + 2.35;
    }

}
