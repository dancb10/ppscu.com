package com.example.test;
import static com.example.test.ThreadColor.ANSI_PURPLE;
import static com.example.test.ThreadColor.ANSI_GREEN;
import static com.example.test.ThreadColor.ANSI_RED;

public class Main {

    public static void main(String[] args) {

        System.out.println(ANSI_PURPLE + "Hello from the main thread");
        Thread anotherThread = new AnotherThread();
        anotherThread.setName("=== ANOTHER THREAD ===");
        anotherThread.start();

        new Thread() {
            public void run() {
                System.out.println(ANSI_GREEN + "Hello from the anonymous class thread");
            }
        }.start();

        Thread myRunnableThread = new Thread(new MyRunnable() {
            @Override
            public void run() {
                System.out.println(ANSI_RED + "Hello from anonymous runnable class");
                try {
                    anotherThread.join();
                    System.out.println(ANSI_RED + "Another thread has terminated. I'm running again");
                } catch (InterruptedException e) {
                    System.out.println(ANSI_RED + "I couldn't wait after all. I was interrupted");
                }
            }
        });
        myRunnableThread.start();
//        anotherThread.interrupt();


        System.out.println("Hello again from the main thread");

    }
}
