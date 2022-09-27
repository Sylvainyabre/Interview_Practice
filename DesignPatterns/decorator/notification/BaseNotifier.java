package DesignPatterns.decorator.notification;

public class BaseNotifier  implements Notifier {
   

    @Override
    public void sendNotification() {
        System.out.println("Notifying you from the Base Notification Service");
        
    }

    
}
