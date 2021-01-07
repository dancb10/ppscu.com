package com.ppscu;

public class Main {

    public static void main(String[] args) {
        System.out.println(hasTeen(9, 99, 19));
        System.out.println(hasTeen(23, 15, 42));
        System.out.println(hasTeen(22, 23, 34));
    }

    public static boolean hasTeen(int first, int second, int third) {
        if (first >= 13 && first <= 19) {
            return true;
        }
        else if (second >= 13 && second <= 19) {
            return true;
        }
        else if (third >= 13 && third <= 19) {
            return true;
        }
        else {
            return false;
        }
    }
}
