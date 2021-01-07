package com.example.test;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class Main {

    public static void main(String[] args) {

        List<String> someBingNumbers = Arrays.asList(
          "N40", "N36",
          "B13", "B40",
          "G53", "G49", "G60", "G50", "g64",
          "I26", "I27", "I29",
          "O71"
        );

        List<String> gNumbers = new ArrayList<>();


//        someBingNumbers.forEach(number -> {
//            if(number.toUpperCase().startsWith("G")) {
//                gNumbers.add(number);
////                System.out.println(number);
//            }
//        });
//
//        gNumbers.sort((String s1, String s2) -> s1.compareTo(s2));
//        gNumbers.forEach((String s) -> System.out.println(s));

        someBingNumbers.stream()
                .map(String::toUpperCase)
                .filter(s-> s.startsWith("G"))
                .sorted()
                .forEach(System.out::println);

        Stream<String> ioNumberStream = Stream.of("I26", "I17", "I29", "O71");
        Stream<String> inNumberStream = Stream.of("N40", "N36", "I26", "I17", "I29", "O71");
        Stream<String> concatStream = Stream.concat(inNumberStream, ioNumberStream);
        System.out.println("=============================");
        System.out.println(concatStream
                .distinct()
                .peek(System.out::println)
                .count());

        Employee john = new Employee("John Doe", 30);
        Employee jack = new Employee("Jack Man", 25);
        Employee jane = new Employee("Jane Blue", 40);
        Employee snow = new Employee("Snow White", 22);

        Departament hr = new Departament("Human Resources");
        hr.addEmployee(jane);
        hr.addEmployee(jack);
        hr.addEmployee(snow);

        Departament accounting = new Departament("Accounting");
        accounting.addEmployee(john);

        List<Departament> departaments = new ArrayList<>();
        departaments.add(hr);
        departaments.add(accounting);

        departaments.stream()
                .flatMap(departament -> departament.getEmployees().stream())
                .forEach(System.out::println);

        System.out.println("========================");
//        List<String> sortedGNumbers = someBingNumbers
//                .stream()
//                .map(String::toUpperCase)
//                .filter(s->s.startsWith("G"))
//                .collect(Collectors.toList());

        List<String> sortedGNumbers = someBingNumbers
                .stream()
                .map(String::toUpperCase)
                .filter(s->s.startsWith("G"))
                .collect(ArrayList::new, ArrayList::add, ArrayList::addAll);

        for(String s: sortedGNumbers) {
            System.out.println(s);
        }

        Map<Integer, List<Employee>> grouppedByAge = departaments.stream()
                .flatMap(departament -> departament.getEmployees().stream())
                .collect(Collectors.groupingBy(employee -> employee.getAge()));

        departaments.stream().flatMap(departament -> departament.getEmployees().stream())
                .reduce((e1,e2) -> e1.getAge() < e2.getAge() ? e1 : e2)
                .ifPresent(System.out::println);

        Stream.of("ABC","AC","BAA","CCC","XY","ST")
                .filter(s -> {
                    System.out.println(s);
                    return s.length() == 3;
                })
                .count();

    }
}
