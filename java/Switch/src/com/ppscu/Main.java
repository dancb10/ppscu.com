package com.ppscu;

import java.util.logging.SocketHandler;

public class Main {

    public static void main(String[] args) {

        int value = 1;
//        if (value == 1) {
//            System.out.println("Value was 1");
//        }
//        else if (value == 2) {
//            System.out.println("Value was 2");
//        }
//        else {
//            System.out.println("Was not 1 or 2");
//        }

        int switchValue = 4;

        switch (switchValue) {
            case 1:
                System.out.println("Value was 1");
                break;

            case 2:
                System.out.println("Value was 2");
                break;

            case 3: case 4: case 5:
                System.out.println("Was a 3, or a 4, or a 5");
                break;

            default:
                System.out.println("Was not 1 or 2");
                break;
        }

        char sValue = 'D';
        switch (sValue) {

            case 'A':
                System.out.println("Found A");
                break;
            case 'B':
                System.out.println("Found B");
                break;
            case 'C': case 'D': case 'E':
                System.out.println("Found C, or D or E");
                break;
            default:
                System.out.println("Was not 1, 2, 3, 4 or 5");
                break;
        }

        String month = "jAnuary";

        switch (month.toLowerCase()) {

            case "january":
                System.out.println("Jan");
                break;
            case "june":
                System.out.println("Jun");
                break;
            default:
                System.out.println("Not sure");
        }
    }
}
