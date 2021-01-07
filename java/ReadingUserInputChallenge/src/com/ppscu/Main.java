package com.ppscu;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        int i = 0;
        int sum  = 0;
        Scanner scanner = new Scanner(System.in);
        while(i < 10) {

            System.out.print("Enter number #" + (i+1) +": ");
            boolean hasNextInt = scanner.hasNextInt();
            if(hasNextInt) {
                sum += scanner.nextInt();
            }
            else {
                System.out.println("Invalid number");
                return;
            }
            i++;
        }
        scanner.close();
        System.out.println("The sum of numbers is: " + sum);
    }
}
