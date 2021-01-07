package com.ppscu;

public class Main {

    public static void main(String[] args) {
        System.out.println(sumFirstAndLastDigit(372629));
    }

    public static int sumFirstAndLastDigit(int number) {
        if (number < 0) {
            return -1;
        }

        int firstNumber = 0;
        int lastNumber = number % 10;

        while (number > 0) {
            firstNumber = number % 10;
            number = number / 10;

        }
        System.out.println(firstNumber);
        System.out.println(lastNumber);
        return firstNumber + lastNumber;
    }
}
