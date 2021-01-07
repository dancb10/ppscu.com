package com.ppscu;

public class Main {

    public static void main(String[] args) {
        System.out.println(hasEqualSum(1,1,1));
        System.out.println(hasEqualSum(1,1,2));
        System.out.println(hasEqualSum(1,-1,0));
    }

    public static boolean hasEqualSum(int first, int second, int third) {

        if (first + second == third) {
            return true;
        }
        else {
            return false;
        }
    }
}
