package DesignPatterns.decorator.notification;

public abstract class NotificationDecorator implements Notifier {
    protected Notifier tempNotifier;

    public NotificationDecorator(Notifier newNotifier) {
        tempNotifier = newNotifier;
    }

    public void sendNotification() {
        tempNotifier.sendNotification();
    }
}
