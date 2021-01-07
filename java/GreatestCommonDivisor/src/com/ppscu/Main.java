package com.ppscu;

public class Main {

    public static void main(String[] args) {
        System.out.println(getGreatestCommonDivisor(12, 30));
    }

    public static int getGreatestCommonDivisor(int x, int y) {

        if (x < 10 || y < 10) {
            return -1;
        }

        while(y != 0) {
            if (x > y) {
                x = x - y;
            }
            else {
                y = y - x;
            }
        }
        return x;
    }
}
