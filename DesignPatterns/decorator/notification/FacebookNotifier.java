package DesignPatterns.decorator.notification;

public class FacebookNotifier  extends NotificationDecorator{

    public FacebookNotifier(Notifier newNotifier) {
        super(newNotifier);
       
    }
    public void sendNotification(){
        tempNotifier.sendNotification();;
        System.out.println("Notifying you from Facebook");
    }
    
}
