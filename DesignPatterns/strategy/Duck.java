package DesignPatterns.strategy;

public abstract class Duck {
    private String name;
    private int age;
    private FlyBehaviour flyBehaviour;
    private QuackBehaviour quackBehaviour;

    public Duck(String name, int age) {
        this.name = name;
        this.age = age;
       
    }

    public void performQuack() {
        quackBehaviour.quack();
    }

    public void performFlying() {
        flyBehaviour.fly();
    }

};

interface FlyBehaviour {
    public void fly();

}

class FlyWithWings implements FlyBehaviour {
    public void fly() {
        System.out.println("FLying");
    }
}

class flyNoWay implements FlyBehaviour {
    public void fly() {
        // DO nothing
    }
}

interface QuackBehaviour {
    public void quack();
}

class Quack implements QuackBehaviour {
    public void quack() {
        System.out.println("Quacking...");
    }
}

class MuteQuack implements QuackBehaviour {
    public void quack() {
        // Do nothing
    }
}

class Squeak implements QuackBehaviour {
    public void quack() {
        System.out.println("Squeaking...");
    }
}