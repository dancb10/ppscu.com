package com.ppscu;

import java.lang.reflect.Array;
import java.util.Arrays;

public class Main {

    public static void main(String[] args) {

        int[] array = {1, 2, 6, 9, 3, 4, 5, 10};
        reverse(array);
    }

    public static void reverse(int[] array) {
        int n = array.length - 1;
        System.out.println(n);
        int i = 0;
        int tmp;
        while(i < n) {
            tmp = array[i];
            array[i] = array[n];
            array[n] = tmp;
            i++;
            n--;
        }
        System.out.println("Reversed array is " + Arrays.toString(array));
    }
}
