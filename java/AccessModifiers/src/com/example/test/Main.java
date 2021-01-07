package com.example.test;

public class Main {

    public static void main(String[] args) {

        Account thimsAccount = new Account("Tim");
        thimsAccount.deposit(1000);
        thimsAccount.withdraw(500);
        thimsAccount.withdraw(-200);
        thimsAccount.deposit(-20);
        thimsAccount.calculateBalance();
        thimsAccount.balance = 5000;

        System.out.println("Balance on account is " + thimsAccount.getBalance());
        thimsAccount.transactions.add(4500);
        thimsAccount.calculateBalance();

    }
}
