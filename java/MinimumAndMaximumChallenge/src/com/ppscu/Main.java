package com.ppscu;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        int maximum = 0;
        int minimum = 0;

        int test = Integer.MAX_VALUE; // maximum of Integer
        int test2 = Integer.MIN_VALUE; // minimum of Integer
        boolean first = true;

        while(true) {

            System.out.print("Enter number: ");
            boolean hasNextInt = scanner.hasNextInt();

            if(hasNextInt) {
                int number = scanner.nextInt();

                if(first) {
                    maximum = number;
                    minimum = number;
                    first = false;
                }

                if(number > maximum ) {
                    maximum = number;
                }
                if(number < minimum) {
                    minimum = number;
                }
                scanner.nextLine();
            }
            else {
                break;
            }
        }
        System.out.println("minimum: " +minimum + ", maximum: " +maximum);
        scanner.close();
    }
}
