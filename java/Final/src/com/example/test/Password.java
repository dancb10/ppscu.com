package com.example.test;

public class Password {

    private static final int key = 74829572;
    private final int enryptedPassowrd;

    public Password(int passowrd) {
        this.enryptedPassowrd = encryptDecrypt(passowrd);
    }

    private int encryptDecrypt(int password) {
        return password ^key;
    }

    public final void storePassword() {
        System.out.println("Saving password as " + this.enryptedPassowrd);
    }

    public boolean letMeIn(int password) {
        if(encryptDecrypt(password) == this.enryptedPassowrd) {
            System.out.println("Welcome");
            return true;
        } else {
            System.out.println("Nop, you cannot come in");
            return false;
        }
    }
}
