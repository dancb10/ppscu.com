package com.ppscu;

public class Main {

    public static void main(String[] args) {

        // int has a width of 32
        int myMinValue= -2_147_483_648;
        int myMaxValue= 2_147_483_647;
        int myTotal = (myMinValue / 2);
        System.out.println(myTotal);

        // has a width of 8
        byte myByteValueMin = -128;
        byte myByteValueMax = 127;
        byte myNewByteValue = (byte) (myByteValueMax / 2);
        System.out.println("My total byte value equals:" + myNewByteValue);

        // has a width of 16
        short myShortValueMin = -32768;
        short myShortValueMax = 32767;
        short myNewShortValue = (short) (myShortValueMax /2 );
        System.out.println(myNewShortValue);

        // has a width of 64
        long myLongValue = 100L;


        byte byteVal = 10;
        short shortVal = 20;
        int intVal = 30;
        long longVal = (50000L + 10L ) * (byteVal + shortVal + intVal);
        short shortTotal = (short) (5000 + 10 * (byteVal + shortVal + intVal));
        System.out.println("LongVal "+ longVal);
        System.out.println("ShortVal "+ shortTotal);
    }
}
