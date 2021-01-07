package com.ppscu;

public class Main {

    public static void main(String[] args) {

        ITelephone timsPhone;
//        DeskPhone timsPhone;
        timsPhone = new DeskPhone(123456);
        timsPhone.powerOn();
        timsPhone.callPhone(123456);
        timsPhone.answer();

        timsPhone = new MobilePhone(1234789);
        timsPhone.powerOn();
        timsPhone.callPhone(1234789);
        timsPhone.answer();
    }
}
