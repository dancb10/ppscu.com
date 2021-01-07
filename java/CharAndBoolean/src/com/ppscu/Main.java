package com.ppscu;

public class Main {

    public static void main(String[] args) {

        // width of char = 16 (2 bytes)
        char myChar = '\u00A9';
        System.out.println("Unicode character is: " + myChar);

        boolean myBoolean = true;

        char myChar2 = '\u00AE';
        System.out.println("My second char is: " + myChar2);
    }
}
