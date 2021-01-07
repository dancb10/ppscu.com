package com.ppscu;

public class Main {

    public static void main(String[] args) {
	    printMegaBytesAndKiloBytes(2050);
    }

    public static void printMegaBytesAndKiloBytes(int kiloBytes) {

        if (kiloBytes < 0) {
            System.out.println("Invalid Value");
        }
        else {
            int transformedMB = kiloBytes / 1024;
            int transformedKB = kiloBytes % 1024;
            System.out.println(kiloBytes + " KB = " + transformedMB + " MB and " + transformedKB + " KB");
        }
    }
}
