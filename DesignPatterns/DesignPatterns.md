# Notes on Software Design Patterns from Head First Design Patterns

## **Principle of Object Oriented Programming:** 
Program to an interface, not to an implementation. Separate the aspects of the application that change and separate them from the aspects that remain the same. The changing behaviour can be turned into an interface and the main class can encapsulate it in the form of member variables.

```java
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
};

```
In the example above, the `Duck` class, `quacking` and `flying` are changing behaviors. To avoid changes in the `Duck` class due to the possible introduction of new duck types, the changing behaviors have been extracted and turned into separate classes that are encapsulated by the main class.The interfaces may be replaced by abstract classes to serve the same purpose. This technique is known as `Composition`.

## **The Strategy Pattern**:
 The strategy pattern defines a family of algorithms, encapsulates each one, and make them interchangeable. An example is the multiple duck behaviors defined and encapsulated above.The algorithm can vary independently from the client that uses it and the client can change without changing the algorithms.

 ## **The Observer Pattern**:
It depends a one-to-many dependency between objects such that when one object changes state, all of its dependents are notified and updated automatically.

![](observer.png)

below is a general implementation of the observer pattern:

```java
public interface Subject {
    public void registerObserver(Observer o);

    public void removeObserver(Observer o);

    public void notifyObserver();

};
public class ConcreteSubject implements Subject {
    private ArrayList<Observer> observers;

    // additional member variables
    public ConcreteSubject() {
        // constructor
        observers = new ArrayList<Observer>();
    }

    public void registerObserver(Observer o) {
        observers.add(o);
    };

    public void removeObserver(Observer o) {
        observers.remove(o);
    };

    public void notifyObserver() {
        for (Observer o : observers) {
            o.update();
        }
    }

};

public interface Observer {
    public void update();
    
};


public class ConcreteObserver  implements Observer{

    public void update(){
        //Implementation
    }
    
}
```
The observer pattern allows for loose coupling of software components. When two or more components are loosely coupled, they can interact but with very little knowledge of each other.In the context of OOP, loose coupling allows for the design of flexible OO systems that can handle change because they minimize the interdependence between objects.

## **The Decorator Pattern**:
This pattern attaches new responsibilities to an object dynamically.It provides flexible alternative to subclassing for extending functionality.
The Open-CLosed Principle: Classes should be closed for modification but open for extension.


Say we are designing software for ordering pizza online. We want the customer to be able to customize their pizza by adding as many various toppings as they want and for our up to be able to easily display a description of the order and also computer the total cost.


### Doing it the wrong way:
We create and an abstract class that all the pizzas can extend like the one below:
```java
public abstract class Pizza {
   
   public abstract void setDescription(String description);
   public abstract void setCost(double cost);
   public abstract String getDescription();
   public abstract double getCost();  
}
```
### Issues with this approach
- every customized pizza with have to extend this class; we will therefore end up with a lot of classes to manage
- In the concrete Pizza class, if the cost of any topping changes, we have to also go into the code and change the cost, which is inefficient.

### Doing it the right way
- Create interface called ``Pizza`` with the methods ``getDescription`` and ``getCost ``.
- Create a ``PlainPizza`` class that implements the ``Pizza``interface. PlainPizza is the object that will be decorated at runtime.
- Create a ``ToppingDecorator`` that also implements the ``Pizza`` interface
- To extend the behaviour of the object, i.e to decorate our pizza, create a new topping class that extends the Decorator class. In the methods of the topping class, call the method needed and extend it . Below is the full implementation of the Decorator Pattern for the Pizza Ordering example

```java
//Pizza Interface
public interface Pizza {

   public abstract String getDescription();
   public abstract double getCost();

    
}
```

```java
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
```

```java
public abstract class ToppingDecorator implements Pizza {
    protected Pizza tempPizza;

    public ToppingDecorator(Pizza newPizza) {
        tempPizza = newPizza;
    }

    public String getDescription() {
        return tempPizza.getDescription();
    }

    public double getCost() {
        return tempPizza.getCost();
    }
}
```

```java
public class ParmesanCheese extends ToppingDecorator {

    public ParmesanCheese(Pizza newPizza) {
        super(newPizza);

    }

    public double getCost(){
        //We are able to access the tempPizza variable here because it's' protected
        return tempPizza.getCost() + 1.23;// the parmesan class decorates the plain pizza by adding its own cost to the total cost
    }

    public String getDescription(){
        // also adding the description of this ingredient to the overall description of this pizza
        return tempPizza.getDescription ()+ "\n- Italian Parmesan Cheese";
    }
}

```

```java
//Another decoration for the plain pizza
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
```

```java
//One more decoration for the plain pizza
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
```
For the Decorator Pattern to work properly, the creation of the object must be done recursively following the desired order as is done in the main function below.

```java
public class Main {
    public static void main(String[] args) {
        Pizza customizedPizza = new ParmesanCheese(new ChickenMeat(new GarlicSauce(new PlainPizza())));
        System.out.println("=============================");
        System.out.println("=============================");
        System.out.println("TOPPINGS");
        System.out.println(customizedPizza.getDescription());
        System.out.println("=============================");
        System.out.println("=============================");
        System.out.println("TOTAL COST: " + customizedPizza.getCost());
    }
```
```java
//The output after running the above code
- Plain dough
 - Homemade white garlic sauce
 - Shredded chicken breast 
- Italian Parmesan Cheese
=============================
=============================
TOTAL COST: 9.030000000000001
```
Looking back at this implementation, the benefit is huge: 
- If/when the price of an ingredient changes, we only need to ever-so slightly change the relevant decoration class to introduce this new change.
- If we want to add a new behaviour/new topping to our Pizza object, we only new to creation a new Decoration class to make it happen.

### Summary of the Decoration Pattern
- Create an interface representing the object to decorate along with the needed methods
- Create a Plain Object class to decorate, the subject of decoration also implements the Plain Object interface.
- Create an abstract Decorator class that implements the Plain Object interface
- The decorator class must maintain a protected instance of the subject of decoration having an apparent type set to the interface of the subject of decoration. That instance is used the call the needed method in every decoration class. 
- To add a new behaviour/decoration, create a new class that extends the Decorator class, call the needed method using the object instance and then extend that behaviour.


Another  example of the decorator pattern : 
A notification system that may need to add different ways of notifying its users later. The system can later be extended efficiently with this implementation.

```java
//interface of the object to decorate
public interface Notifier {
    public void sendNotification();
    
    
}
```

```java
//The plain object to decorate
public class BaseNotifier  implements Notifier {
   

    @Override
    public void sendNotification() {
        System.out.println("Notifying you from the Base Notification Service");
        
    }

    
}
```

```java
//The decorator abstract class 
public abstract class NotificationDecorator implements Notifier {
    protected Notifier tempNotifier; // the protected instance of the general object to be decorated. Take not of the apparent type.

    public NotificationDecorator(Notifier newNotifier) {
        tempNotifier = newNotifier;
    }

    public void sendNotification() {
        tempNotifier.sendNotification();
    }
}
```

```java
public class EmailNotifier  extends NotificationDecorator{

    public EmailNotifier(Notifier newNotifier) {
        super(newNotifier);
       
    }
    public void sendNotification(){
        tempNotifier.sendNotification();
        System.out.println("Notifying you by email");//extending the behaviour
    }
    
}
```

```java
public class FacebookNotifier  extends NotificationDecorator{

    public FacebookNotifier(Notifier newNotifier) {
        super(newNotifier);
       
    }
    public void sendNotification(){
        tempNotifier.sendNotification();;
        System.out.println("Notifying you from Facebook");
    }
    
}
```

```java
public class WhatsappNotifier extends NotificationDecorator{

    public WhatsappNotifier(Notifier newNotifier) {
        super(newNotifier);
        
    }
    public void sendNotification(){
        tempNotifier.sendNotification();
        System.out.println("Notifying you from Whatsapp");
    }
    
}
```

```java
public class Main {
    public static void main(String[] args){
    Notifier myNotifier = new FacebookNotifier(new WhatsappNotifier(new BaseNotifier()));
    myNotifier.sendNotification();
    }
}
```

```java
//output of the main method
Notifying you from the Base Notification Service
Notifying you from Whatsapp
Notifying you from Facebook
```













## **The Factor Pattern**




