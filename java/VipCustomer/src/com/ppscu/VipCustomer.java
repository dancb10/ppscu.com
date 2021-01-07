package com.ppscu;

public class VipCustomer {

    private String customerName;
    private int creditLimit;
    private String emailAddress;

    public VipCustomer() {
        this("Default Name", 0, "Unknown Email");
        System.out.println("Empty constructor called");
    }

    public VipCustomer(String customerName, int creditLimit) {
        this.customerName = customerName;
        this.creditLimit = creditLimit;
        this.emailAddress = "Default Email";
        System.out.println("Constructor with two parameters called");
    }

    public VipCustomer(String customerName, int creditLimit, String emailAddress) {
        this.customerName = customerName;
        this.creditLimit = creditLimit;
        this.emailAddress = emailAddress;
        System.out.println("Constructor with three parameters called");
    }

    public String getCustomerName() {
        return customerName;
    }

    public int getCreditLimit() {
        return creditLimit;
    }

    public String getEmailAddress() {
        return emailAddress;
    }
}
