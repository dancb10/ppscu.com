package com.ppscu;

public class BankAccount {

    private int number;
    private double balance = 0;
    private String customerName;
    private String email;
    private String phoneNumber;

    public BankAccount() {
        this(0001, 0000, "No name", "Default email", "Default number");
        System.out.println("Empty constructor called");
    }

    public BankAccount(int number, double balance, String customerName, String email, String phoneNumber) {
        System.out.println("BankAccount constructor called with parameters");
//        this.number = number;
        setNumber(number);
        this.balance = balance;
        this.customerName = customerName;
        this.email = email;
        this.phoneNumber = phoneNumber;
    }

    public BankAccount(String customerName, String email, String phoneNumber) {
        this(9999,100.55, customerName, email, phoneNumber);
    }

    public void setNumber(int number) {
        this.number = number;
    }
    public int getNumber() {
        return this.number;
    }

    public void setBalance(double balance) {
        this.balance = balance;
    }
    public double getBalance() {
        return this.balance;
    }

    public void setCustomerName(String customerName) {
        this.customerName = customerName;
    }
    public String getCustomerName() {
        return this.customerName;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getEmail() {
        return this.email;
    }

    public void setPhoneNumber(String phoneNumber) {
        this.phoneNumber = phoneNumber;
    }
    public String getPhoneNumber() {
        return this.phoneNumber;
    }

    public void depositFunds(double funds) {
        this.balance += funds;
        System.out.println("Balance has changed, new balance is: " + this.balance);
    }

    public void withdrawFunds(double funds) {
        if(funds < this.balance) {
            this.balance -= funds;
            System.out.println("Funds have been withdrawn, new balance is: " + this.balance);
        }
        else {
            System.out.println("Insuficient funds for "+ this.customerName + " (" + this.number + ")" + ", current balance is: " +this.balance);
        }
    }
}
