package com.ppscu;

public class Main {

    public static void main(String[] args) {

        System.out.println(hasSharedDigit(12, 23));
        System.out.println(hasSharedDigit(9, 99));
        System.out.println(hasSharedDigit(15, 55));
    }

    public static boolean hasSharedDigit(int x, int y) {

        int comparex = 0;
        if ((x <= 10 || x >= 99) || (y <=10 || y >= 99)) {
            return false;
        }

        while(x > 0) {

            comparex = x % 10;
            while(y >0) {
                if (comparex == y % 10) {
                    return true;
                }
                y /= 10;
            }
            x /= 10;

        }
        return false;
    }
}
