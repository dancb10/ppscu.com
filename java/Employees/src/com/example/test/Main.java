package com.example.test;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.util.function.*;

public class Main {

    public static void main(String[] args) {

        Employee john = new Employee("John Doe", 30);
        Employee tim = new Employee("Tim Doe", 35);
        Employee dan = new Employee("Dan Popi", 27);
        Employee dany = new Employee("Dany", 23);
        Employee rad = new Employee("Rad dada", 43);
        Employee tfa = new Employee("tfs daa", 78);

        List<Employee> employees = new ArrayList<>();
        employees.add(john);
        employees.add(tim);
        employees.add(dan);
        employees.add(dany);
        employees.add(rad);
        employees.add(tfa);

        Function<Employee, String> getLastName = (Employee employee) -> {
            return employee.getName().substring(employee.getName().indexOf(' ') + 1);
        };

        Function<Employee, String> getFirstName = (Employee employee) -> {
          return employee.getName().substring(employee.getName().indexOf(' '));
        };

//        Random random = new Random();
//        for(Employee employee: employees) {
//            if(random.nextBoolean()) {
//                System.out.println(getAName(getFirstName, employee));
//            } else {
//                System.out.println(getAName(getLastName, employee));
//            }
//        }

        Function<Employee, String> upperCase = employee -> employee.getName().toUpperCase();
        Function<String, String> firstname = name -> name.substring(0, name.indexOf(' '));
        Function chainedFunction = upperCase.andThen(firstname);
        System.out.println(chainedFunction.apply(employees.get(0)));

        BiFunction<String, Employee, String> concatAge = (String name, Employee employee) -> {
          return name.concat(" " + employee.getAge());
        };

        String upperName = upperCase.apply(employees.get(0));
        System.out.println(concatAge.apply(upperName, employees.get(0)));

        IntUnaryOperator incBy5 = i -> i + 5;
        System.out.println(incBy5.applyAsInt(10));

        Consumer<String> c1 = s -> s.toUpperCase();
        Consumer<String> c2 = s -> System.out.println(s);
        c1.andThen(c2).accept("hello world");


//        String lastName = getLastName.apply(employees.get(2));
//        System.out.println(lastName);

//        printEmployeesByAge(employees, "Employees over 30", employee -> employee.getAge() > 30);
//        printEmployeesByAge(employees, "Employees under 30", employee -> employee.getAge() <= 30);
//
//        printEmployeesByAge(employees, "Employees younger than 25", new Predicate<Employee>() {
//            @Override
//            public boolean test(Employee employee) {
//                return employee.getAge() < 25;
//            }
//        });
//
//        IntPredicate greaterThan15 = i -> i > 15;
//        IntPredicate lesThan100 = i -> i < 100;
//
//        System.out.println(greaterThan15.test(10));
//        int a=20;
//        System.out.println(greaterThan15.test(a+5));
//
//        System.out.println(greaterThan15.and(lesThan100).test(50));
//        System.out.println(greaterThan15.and(lesThan100).test(15));
//
//        Random random = new Random();
//        Supplier<Integer> randomSupplier = () -> random.nextInt(1000);
//
//        for(int i = 0; i<10; i++) {
////            System.out.println(random.nextInt(1000));
//            System.out.println(randomSupplier.get());
//        }

//        employees.forEach(employee -> {
//            String lastName = employee.getName().substring(employee.getName().indexOf(' ') + 1);
//            System.out.println("Last name is: " + lastName);
//        });

//        employees.forEach(employee -> {
//            System.out.println(employee.getName());
//            System.out.println(employee.getAge());
//        });

//        System.out.println("Employees over 30");
//        System.out.println("=================");
//
//        employees.forEach(employee -> {
//            if(employee.getAge() > 30) {
//                System.out.println(employee.getName());
//            }
//        });

//        System.out.println("\nEmployees 30 and younger");
//        System.out.println("=================");
//
//        employees.forEach(employee -> {
//            if(employee.getAge() <= 30) {
//                System.out.println(employee.getName());
//            }
//        });

//        for(Employee employee: employees) {
//            if(employee.getAge() > 30) {
//                System.out.println(employee.getName());
//            }
//        }
    }

    private static String getAName(Function<Employee, String> getName, Employee employee) {
        return getName.apply(employee);
    }

    private static void printEmployeesByAge(List<Employee> employees,
                                            String ageText,
                                            Predicate<Employee> ageCondition) {
        System.out.println(ageText);
        System.out.println("=================");
        for(Employee employee: employees) {
            if(ageCondition.test(employee)) {
                System.out.println(employee.getName());
            }
        }
        System.out.println("\n");
    }
}
