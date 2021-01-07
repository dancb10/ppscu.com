package com.ppscu;

import java.util.ArrayList;

class IntClass {

    private int myValue;

    public IntClass(int myValue) {
        this.myValue = myValue;
    }

    public int getMyValue() {
        return myValue;
    }

    public void setMyValue(int myValue) {
        this.myValue = myValue;
    }
}

public class Main {

    public static void main(String[] args) {

        String[] strArray = new String[10];
        int[] intArray = new int[10];

        ArrayList<String> stringArrayList = new ArrayList<String>();
        stringArrayList.add("Tim");

        ArrayList<IntClass> intClassArrayList = new ArrayList<IntClass>();
        intClassArrayList.add(new IntClass(54));

        Integer integer = new Integer(54);
        Double doubleValue = new Double(54.3);

        ArrayList<Integer> integerArrayList = new ArrayList<Integer>();
//        for(int i=0; i<=10; i++) {
//            integerArrayList.add(Integer.valueOf(i));
//        }
//        for(int i=0; i<=10; i++) {
//            System.out.println(i + " --> " + integerArrayList.get(i).intValue());
//        }

        Integer myIntValue = 56; // Integer.valueOf(56);
        int myint = myIntValue; // myInt.intValue();

        ArrayList<Double> myDoubleValue = new ArrayList<Double>();
        for(double dbl=0.0; dbl<=10.0;dbl += 0.5) {
            myDoubleValue.add(Double.valueOf(dbl));
        }

        for(int i=0; i<myDoubleValue.size(); i++) {
            double value = myDoubleValue.get(i);
            System.out.println(i + " --> " + value);

        }
    }
}
