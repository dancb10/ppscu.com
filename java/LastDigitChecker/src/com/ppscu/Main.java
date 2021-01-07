package com.ppscu;

public class Main {

    public static void main(String[] args) {
        System.out.println(hasSameLastDigit(41, 22, 71));
        System.out.println(hasSameLastDigit(23, 32, 42));
        System.out.println(hasSameLastDigit(9, 99, 999));
        System.out.println(hasSameLastDigit(10, 11, 81));
    }

    public static boolean hasSameLastDigit(int x, int y, int z) {

        if ((x < 10 || x > 1000) || (y < 10 || y > 1000) || (z < 10 || z > 1000)) {
            return false;
        }
        if ((x % 10 == y % 10) || (y % 10 == z % 10) || (z % 10 == x % 10)) {
            return true;
        }
        return  false;
    }
}
