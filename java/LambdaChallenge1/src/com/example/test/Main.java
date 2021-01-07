package com.example.test;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.function.Function;
import java.util.function.Supplier;

public class Main {

    public static void main(String[] args) {

        Runnable runnable1 = () -> {
            String mystring = "Let's split this up";
            String[] parts = mystring.split(" ");
            for(String part: parts) {
                System.out.println(part);
            }
        };

        Function<String, String > lambdaFunction = s -> {
            StringBuilder returnVal = new StringBuilder();
            for(int i=0; i < s.length(); i++) {
                if (i % 2 == 1) {
                    returnVal.append(s.charAt(i));
                }
            }
            return returnVal.toString();
        };
//        System.out.println(lambdaFunction.apply("1234567890"));

//        String character = everySecondCharacter(lambdaFunction,"123456789");
//        System.out.println(character);

//        Supplier<String> iLoveJava = () -> "I Love Java";
//        Supplier<String> iLoveJava = () -> { return "I Love Java"; };
//        String supplierResult = iLoveJava.get();
//        System.out.println(supplierResult);

        List<String> topName2015 = Arrays.asList(
          "Amelia",
          "Olivia",
          "emily",
          "Isla",
          "Ava",
          "olivier",
          "Jack",
          "Charlie",
          "harry",
          "Jacob"
        );

        List<String> sortedList = new ArrayList<>();
//        topName2015.forEach(name ->
//            sortedList.add(name.substring(0, 1).toUpperCase() + name.substring(1)));
//        sortedList.sort((s1, s2) -> s1.compareTo(s2));
//        sortedList.forEach(s -> System.out.println(s));
//        sortedList.sort(String::compareTo);
//        sortedList.forEach(System.out::println);

        topName2015.stream()
                .map(name -> name.substring(0, 1).toUpperCase() + name.substring(1))
                .sorted(String::compareTo)
                .forEach(System.out::println);

        long namesBeginingWithA = topName2015.stream()
                .map(name -> name.substring(0, 1).toUpperCase() + name.substring(1))
                .filter(name -> name.startsWith("A"))
                .count();
        System.out.println("Names beginning with A " + namesBeginingWithA);

        topName2015.stream()
                .map(name -> name.substring(0, 1).toUpperCase() + name.substring(1))
                .peek(System.out::println)
                .sorted(String::compareTo)
                .count();

    }

    public static String everySecondCharacter(Function<String, String> fun, String source) {
        return fun.apply(source);
    }
}
