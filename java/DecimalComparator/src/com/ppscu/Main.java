package com.ppscu;


public class Main {

    public static void main(String[] args) {
        System.out.println(areEqualByThreeDecimalPlaces(-3.1756,-3.175));
        System.out.println(areEqualByThreeDecimalPlaces(3.175,3.176));
        System.out.println(areEqualByThreeDecimalPlaces(3.0,3.0));
    }

    public static boolean areEqualByThreeDecimalPlaces(double firstNo, double secondNo) {
        firstNo = firstNo * 1000;
        secondNo = secondNo * 1000;
        int intFirstNo = (int) firstNo;
        int intSecondNo = (int) secondNo;
        if (intFirstNo == intSecondNo) {
            return true;
        }
        else {
            return false;
        }
    }
}
