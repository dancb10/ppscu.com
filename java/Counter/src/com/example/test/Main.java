package com.example.test;

public class Main {

    public static void main(String[] args) {

        Countdown countdown = new Countdown();

        CountdownTread t1 = new CountdownTread(countdown);
        t1.setName("Thread 1");

        CountdownTread t2 = new CountdownTread(countdown);
        t2.setName("Thread 2");

        t1.start();
        t2.start();
    }
}

class Countdown {

    private int i;

    public void doCountDown() {
        String color;

        switch (Thread.currentThread().getName()) {
            case "Thread 1":
                color = ThreadColor.ANSI_CYAN;
                break;
            case "Thread 2":
                color = ThreadColor.ANSI_PURPLE;
                break;
            default:
                color = ThreadColor.ANSI_GREEN;
                break;
        }

        synchronized (this) {
            for (i=10; i>0; i--) {
                System.out.println(color + Thread.currentThread().getName() + ": i =" + i);
            }
        }

    }
}

class CountdownTread extends Thread {
    private Countdown threadCountdown;

    public CountdownTread(Countdown countdown) {
        threadCountdown = countdown;
    }

    public void run() {
        threadCountdown.doCountDown();
    }
}
