package com.ppscu;
import java.util.Arrays;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the desired number of items: ");
        int numbers = scanner.nextInt();
        int[] arrays = readIntegers(numbers);
        System.out.println("Array is: " + Arrays.toString(arrays));
        System.out.println("Minimum element from array is: " + findMin(arrays));
    }

    public static int findMin(int[] arrays) {
        int min = arrays[0];
        for(int i=1; i<arrays.length; i++) {
            if(arrays[i] < min) {
                min = arrays[i];
            }
        }
        return min;
    }

    public static int[] readIntegers(int count) {
        Scanner scanner = new Scanner(System.in);
        int[] arrays = new int[count];
        for(int i=0; i<count; i++) {
            arrays[i] = scanner.nextInt();
        }
        return arrays;
    }
}
