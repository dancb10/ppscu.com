package com.ppscu;

public class Main {

    public static void main(String[] args) {
        System.out.println(sumDigits(148));
        System.out.println(sumDigits(1));
    }

    public static int sumDigits(int number) {
        int sum = 0;
        if (number < 10) {
            return  -1;
        }
        while(number > 0) {
            sum += number % 10;
            number = number / 10;
        }
        return sum;
    }
}
