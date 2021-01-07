package com.ppscu;

public class Main {

    public static void main(String[] args) {
        String numberAsString = "2018.125";
        System.out.println("numberAsString= " + numberAsString);

//        int number = Integer.parseInt(numberAsString);
//        System.out.println("number = " + number);

        double number = Double.parseDouble(numberAsString);
        System.out.println("number = " + number);

        numberAsString += 1;
        number += 1;

        System.out.println("numberAsString= " + numberAsString);
        System.out.println("number= " + number);

        int number2 = 1000;
        String ab = String.valueOf(number2);
        System.out.println(ab);
    }
}
