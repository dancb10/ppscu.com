package com.ppscu;

public class Main {

    public static void main(String[] args) {

        long sum = 0;
        int counter = 0;
        for(int i=1; i<1000; i++) {

            if (i % 3 == 0 && i % 5 ==0) {
                System.out.println("Number divisible with 3 and 5 is: " + i);
                counter += 1;
                sum += i;
                if (counter == 5) {
                    break;
                }
            }
        }
        System.out.println("The sum is: " + sum);
    }
}
