package DesignPatterns.decorator.notification;

public class WhatsappNotifier extends NotificationDecorator{

    public WhatsappNotifier(Notifier newNotifier) {
        super(newNotifier);
        
    }
    public void sendNotification(){
        tempNotifier.sendNotification();
        System.out.println("Notifying you from Whatsapp");
    }
    
}
