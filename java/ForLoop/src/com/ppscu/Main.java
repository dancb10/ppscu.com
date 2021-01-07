package com.ppscu;

public class Main {

    public static void main(String[] args) {
//        System.out.println(("10.000 at 2% interest " + calculateInterest(10000.0, 2.0)));

//        for(int i=0; i<5; i++) {
//            System.out.println("Loop " + i + " hello!");
//        }
//
//        for(int i=2; i<=8; i++) {
//
//            System.out.println(String.format("%.2f",calculateInterest(10000.0, (double) i)));
//        }
//
//        for(int i=8; i>=2; i--) {
//
//            System.out.println(String.format("%.2f",calculateInterest(10000.0, (double) i)));
//        }

        int counter = 0;
        for(int i=2; i< 100; i++) {
            if (isPrime(i)) {
                counter++;
                System.out.println("Prime number found: " + i);
                if (counter == 10) {
                    break;
                }
            }
        }
    }

    public static boolean isPrime(int n) {
        if (n == 1) {
            return false;
        }

        for(int i=2; i<=n/2; i++) {
            if (n%i == 0) {
                return false;
            }
        }
        return true;
    }

    private static double calculateInterest(double amount, double interestRate) {

        return (amount * (interestRate / 100));
    }
}
