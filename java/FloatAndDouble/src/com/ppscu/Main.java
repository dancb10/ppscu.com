package com.ppscu;

public class Main {

    public static void main(String[] args) {

        // width of int = 32 (4 bytes)
        int myIntValue = 5 / 2;
        // width of float = 32 (4 bytes)
        float myFloatValue = 5f / 3f;
        // width of double = 64 (8 bytes)
        double myDoubleValue = 5d / 2d;
        System.out.println("myIntValue = "+ myIntValue);
        System.out.println("myFloatValue = "+ myFloatValue);
        System.out.println("myDoubleValue = "+ myDoubleValue);


        double nrOfPounds = 200d;
        double nrOfKilograms = nrOfPounds * 0.45359237;
        System.out.println("nrOfKilograms: "+ nrOfKilograms);

        double pi = 3.141_592_7d;
        System.out.println("Pi number: "+pi);
    }
}
