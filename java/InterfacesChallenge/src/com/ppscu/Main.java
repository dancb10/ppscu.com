package com.ppscu;

import java.util.ArrayList;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

//        Player tim = new Player("Tim", 10, 15);
//        System.out.println(tim.toString());
//        saveObject(tim);
//
//        tim.setHitPoints(8);
//        System.out.println(tim);
//        tim.setWeapon("Stormbringer");
//        saveObject(tim);
//        loadObject(tim);
//        System.out.println(tim);

        ISavable warewolf = new Monster("Warewolf", 20, 40);
        System.out.println(((Monster) warewolf).getStrength());
//        Monster warewolf = new Monster("Warewolf", 20 ,40);
//
//        System.out.println(warewolf.getStrength());
        saveObject(warewolf);
    }

    public static ArrayList<String> readValues() {
        ArrayList<String> values = new ArrayList<String>();

        Scanner scanner = new Scanner(System.in);
        boolean quit = false;
        int index = 0;
        System.out.println("Choose\n" +
                "1 to enter a string\n" +
                "0 to quit");
        while(!quit) {
            System.out.println("Choose an option: ");
            int choice = scanner.nextInt();
            scanner.nextLine();
            switch (choice) {
                case 0:
                    quit = true;
                    break;
                case 1:
                    System.out.println("Enter a string: ");
                    String stringInput = scanner.nextLine();
                    values.add(index, stringInput);
                    index++;
                    break;
            }
        }
        return values;
    }

    public static void saveObject(ISavable objectToSave) {
        for(int i=0; i < objectToSave.write().size(); i++) {
            System.out.println("Saving " + objectToSave.write().get(i) + " to storage device");
        }
    }

    public static void loadObject(ISavable objectToLoad) {
        ArrayList<String> values = readValues();
        objectToLoad.read(values);
    }
}
