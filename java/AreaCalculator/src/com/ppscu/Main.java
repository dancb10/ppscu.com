package com.ppscu;

public class Main {

    public static final double PI = 3.14159;
    public static void main(String[] args) {

        System.out.println(area(5.0));
        System.out.println(area(-1));
        System.out.println(area(5.0, 4.0));
        System.out.println(area(-1.0, 4.0));
    }

    public static double area(double radius) {
        if (radius < 0) {
            return -1d;
        }

        return  radius * radius * PI;
    }

    public static double area(double x, double y) {
        if (x < 0 || y < 0) {
            return -1d;
        }

        return x * y;
    }
}
