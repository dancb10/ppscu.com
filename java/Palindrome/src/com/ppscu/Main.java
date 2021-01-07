package com.ppscu;

public class Main {

    public static void main(String[] args) {
        System.out.println(isPalindrome(12321));
        System.out.println(isPalindrome(707));
        System.out.println(isPalindrome(-1221));
        System.out.println(isPalindrome(11212));
    }

    public static boolean isPalindrome(int number) {

        int buffer = number;
        int reversed = 0;
        while(buffer != 0) {
            reversed = reversed * 10 + buffer % 10;
            buffer = buffer / 10;
        }

        if (reversed == number) {
            return true;
        }
        else {
            return false;
        }
    }
}
