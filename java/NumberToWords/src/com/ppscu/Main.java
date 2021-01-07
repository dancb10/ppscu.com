package com.ppscu;

public class Main {

    public static void main(String[] args) {

//        System.out.println(getDigitCount(0));
//        System.out.println(getDigitCount(123));
//        System.out.println(getDigitCount(-12));
//        System.out.println(getDigitCount(5200));
//        System.out.println("\n");
//        System.out.println(reverse(-121));
//        System.out.println(reverse(1212));
//        System.out.println(reverse(100));
//        System.out.println(reverse(1234));
//        System.out.println(reverse(-98347));
//        System.out.println("\n");
        numberToWords(10);
//        numberToWords(100);
    }

    public static void numberToWords(int number) {

        if (number < 0) {
            System.out.println("Invalid Value");
        }

        int reversedNumber = reverse(number);
        int numberCount = 0;

        while(reversedNumber > 0) {
            int nr = reversedNumber % 10;
            switch (nr) {
                case 0: {
                    System.out.println("Zero");
                    break;
                }
                case 1: {
                    System.out.println("One");
                    break;
                }
                case 2: {
                    System.out.println("Two");
                    break;
                }
                case 3: {
                    System.out.println("Three");
                    break;
                }
                case 4: {
                    System.out.println("Four");
                    break;
                }
                case 5: {
                    System.out.println("Five");
                    break;
                }
                case 6: {
                    System.out.println("Fix");
                    break;
                }
                case 7: {
                    System.out.println("Seven");
                    break;
                }
                case 8: {
                    System.out.println("Eight");
                    break;
                }
                case 9: {
                    System.out.println("Nine");
                    break;
                }
            }
            reversedNumber /= 10;
            numberCount += 1;
        }

        for(int i=numberCount; i < getDigitCount(number); i++)
            System.out.println("Zero");
    }

    public static int getDigitCount(int number) {
        if (number < 0) {
            return -1;
        }
        if (number == 0) {
            return 1;
        }

        int count = 0;
        while(number > 0) {
            number /= 10;
            count++;
        }
        return count;
    }

    public static int reverse(int number) {

        int reversedNumber = 0;
        while(true) {
            if(number != 0) {
                reversedNumber = ((reversedNumber * 10) + (number % 10));
                number /= 10;
            }
            else {
                break;
            }
        }
        return reversedNumber;
    }
}
