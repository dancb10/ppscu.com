package com.ppscu;

public class Main {

    public static void main(String[] args) {

        BankAccount myaccount = new BankAccount(1456, 7000, "Dan Popescu", "dan_cb10@yahoo.co.uk", "0746210616");
        BankAccount account2 = new BankAccount();
        System.out.println("Customer " + myaccount.getCustomerName() + " has the following details");
        System.out.println("Email: " + myaccount.getEmail());
        System.out.println("Phone: " + myaccount.getPhoneNumber());
        System.out.println("Bank Number: " + myaccount.getNumber());
        System.out.println("Balance: " + myaccount.getBalance());

        myaccount.depositFunds(2560);
        myaccount.withdrawFunds(349586);

        System.out.println(account2.getCustomerName());

        BankAccount account3 = new BankAccount("Dan","dan@gmail.com","12345");
        System.out.println(account3.getNumber() + " name " + account3.getCustomerName());
    }
}
