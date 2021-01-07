package com.ppscu;

public class Main {

    public static void main(String[] args) {
        System.out.println(getEvenDigitSum(123456789));
    }

    public static int getEvenDigitSum(int number) {

        int sum = 0;
        if(number < 0) {
            return  -1;
        }

        while(number > 0) {

            if ((number % 10) % 2 == 0 ) {
                sum += number % 10;
            }
            number = number / 10;
        }
        return sum;
    }
}
