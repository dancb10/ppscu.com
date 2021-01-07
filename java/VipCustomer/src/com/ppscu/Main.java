package com.ppscu;

public class Main {

    public static void main(String[] args) {

        VipCustomer c1 = new VipCustomer();
        System.out.println(c1.getCreditLimit());
        System.out.println(c1.getCustomerName());
        System.out.println(c1.getEmailAddress());

        VipCustomer c2 = new VipCustomer("Dan", 100);
        System.out.println(c2.getCreditLimit());
        System.out.println(c2.getCustomerName());
        System.out.println(c2.getEmailAddress());

        VipCustomer c3 = new VipCustomer("Dan", 100, "dapopesc@g.com");
        System.out.println(c3.getCreditLimit());
        System.out.println(c3.getCustomerName());
        System.out.println(c3.getEmailAddress());
    }
}
