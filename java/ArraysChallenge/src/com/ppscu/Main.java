package com.ppscu;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        int numbers = 5;
        int[] arrays = getIntegers(numbers);
        printArray(arrays);
        System.out.println("\nSorted array is: ");
        printArray(sortArray(arrays));
    }

    public static int[] sortArray(int[] array) {

        boolean flag = true;
        int temp;
        while(flag) {
            flag = false;
            for(int i=0; i<array.length-1; i++) {
                if(array[i] < array [i+1]) {
                    temp = array[i];
                    array[i] = array[i+1];
                    array[i+1] = temp;
                    flag = true;
                }
            }
        }
        return array;
    }

    public static void printArray(int[] arrays) {
        for(int i=0;i<arrays.length;i++) {
            System.out.println("Element " + i + " has value " + arrays[i]);
        }
    }

    public static int[] getIntegers(int numbers) {
        Scanner scanner = new Scanner(System.in);
        int[] arrays = new int[numbers];
        System.out.println("Read from keyboard " + numbers + " numbers");
        for(int i=0; i<numbers; i++) {
            arrays[i] = scanner.nextInt();
        }
        return arrays;
    }
}
