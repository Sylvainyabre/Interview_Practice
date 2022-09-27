package DesignPatterns.observer;

import java.util.ArrayList;

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

}
