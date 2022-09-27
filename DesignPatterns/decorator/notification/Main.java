package DesignPatterns.decorator.notification;

public class Main {
    public static void main(String[] args){
    Notifier myNotifier = new FacebookNotifier(new WhatsappNotifier(new BaseNotifier()));
    myNotifier.sendNotification();
    }
}
