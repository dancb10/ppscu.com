package com.ppscu;

public class Main {

    public static void main(String[] args) {

        Bank bank = new Bank("National Australia Bank");
        bank.addBranch("Adelaide");
        bank.addCustomer("Adelaide", "Tim", 50.05);
        bank.addCustomer("Adelaide", "Mike", 23.10);
        bank.addCustomer("Adelaide", "Logan", 20.3);

        bank.addBranch("Sydeny");
        bank.addCustomer("Sydeny", "Bob", 501.05);

        bank.addCustomerTransaction("Adelaide", "Tim", 44.22);
        bank.addCustomerTransaction("Adelaide", "Tim", 24.22);
        bank.addCustomerTransaction("Adelaide", "Mike", 64.22);

        bank.listCustomers("Adelaide", true);
    }
}
