package com.example.test;

import java.util.Random;

public class Main {

    public static void main(String[] args) {

        Message message = new Message();
        (new Thread(new Writer(message))).start();
        (new Thread(new Reader(message))).start();
    }
}

class Message {

    private String message;
    private boolean empty = true;

    public synchronized String read() {
        while(empty) {
            try {
                wait();
            } catch (InterruptedException e) {

            }
        }
        empty = true;
        notifyAll();
        return message;
    }

    public synchronized void write(String message) {
        while (!empty) {
            try {
                wait();
            } catch (InterruptedException e) {

            }
        }
        empty = false;
        this.message = message;
        notifyAll();
    }
}

class Writer implements Runnable {

    private Message message;

    public Writer(Message message) {
        this.message = message;
    }

    public void run() {
        String messages[] = {
                "Humpty Dumpty sat on a wall",
                "Humpty Dumpty had a great fall",
                "All the king's horses and all the king's men",
                "Couldn't put Humpty together again"
        };

        Random random = new Random();

        for(int i=0; i<messages.length; i++) {
            message.write(messages[i]);
            try {
                Thread.sleep(random.nextInt(2000));
            } catch (InterruptedException e) {

            }
        }
        message.write("Finished");
    }
}

class Reader implements Runnable {
    private Message message;

    public Reader(Message message) {
        this.message = message;
    }

    public void run() {
        Random random = new Random();
        for(String latestMesage = message.read(); !latestMesage.equals("Finished");
            latestMesage = message.read()) {
            System.out.println(latestMesage);
            try {
                Thread.sleep(2000);
            } catch (InterruptedException e) {

            }
        }
    }
}