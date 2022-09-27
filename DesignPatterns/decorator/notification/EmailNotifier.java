package DesignPatterns.decorator.notification;

public class EmailNotifier  extends NotificationDecorator{

    public EmailNotifier(Notifier newNotifier) {
        super(newNotifier);
       
    }
    public void sendNotification(){
        tempNotifier.sendNotification();
        System.out.println("Notifying you by email");
    }
    
}
