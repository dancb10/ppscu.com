package com.ppscu;

import java.util.Scanner;

public class Main {

    private static Scanner scanner = new Scanner(System.in);
    public static void main(String[] args) {

        int[] myIntegers = getIntegers(5);
        for(int i=0;i<myIntegers.length;i++) {
            System.out.println("Element " +i+", value " + myIntegers[i]);
        }
        System.out.println("The average is:" + getAverage(myIntegers));

//        int[] myVariable;
//        myVariable = new int[25];
//
//        int[] myIntArray = new int[10];
////        myIntArray[5] = 50;
////        myIntArray[0] = 45;
//
//        double[] myDoubleArray = new double[10];
////        System.out.println(myIntArray[5]);
//
//        int[] myIntArray1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
//
//        int[] myIntArray2 = new int[25];
//        for(int i=0; i<myIntArray2.length;i++) {
//            myIntArray2[i] = i*10;
//        }
//        printArray(myIntArray2);
//
//    }
//
//    public static void printArray(int[] array) {
//        for(int i=0; i<array.length;i++) {
//            System.out.println("Element: " + i + " Value: " + array[i]);
//        }
    }

    private static int[] getIntegers(int number) {
        System.out.println("Enter " + number + " integer values.\r");
        int[] values = new int[number];
        for(int i=0;i<values.length;i++) {
            values[i] = scanner.nextInt();
        }
        return values;
    }

    private static double getAverage(int[] array) {
        int sum=0;
        for(int i=0;i<array.length;i++) {
            sum += array[i];
        }
        return (double) sum / (double) array.length;
    }
}
