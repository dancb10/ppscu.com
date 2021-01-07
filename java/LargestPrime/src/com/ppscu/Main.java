package com.ppscu;

public class Main {

    public static void main(String[] args) {
//        System.out.println(getLargestPrime2(63));
//        System.out.println(getLargestPrime(217));
        System.out.println(getLargestPrime(217));
        System.out.println(getLargestPrime(7));
        System.out.println(getLargestPrime(21));
    }


//    public static boolean isPrime(int n) {
//
//        for(int i=2; i <= n/2; i++) {
//            if(n % i == 0) {
//                return false;
//            }
//        }
//        return true;
//    }
//
//    public static int getLargestPrime2(int number) {
//
//        int largestPrime = -1;
//        if(number <= 1) {
//            return -1;
//        }
//        if (isPrime(number)) {
//            return number;
//        }
//
//        for(int i=number/2; i > 1; i--) {
//            if(number % i == 0 && isPrime(i)) {
//                largestPrime = i;
//                break;
//            }
//        }
//        return largestPrime;
//    }

    public static int getLargestPrime(int number) {

        int largestPrime = -1;
        if(number <= 1) {
            return -1;
        }

        for(int i=number; i > 1; i--) {
            if(number % i == 0) {
                boolean isPrime = true;
                for(int k=2; k <= i/2; k++) {
                    if(i % k == 0) {
                        isPrime = false;
                    }
                }
                if (isPrime) {
                    return i;
                }
            }
        }
        return largestPrime;
    }

//    public static int getLargestPrime(int n)
//    {
//        int maxPrime = -1;
//        while (n % 2 == 0) {
//            maxPrime = 2;
//            n /= 2;
//        }
//
//        for (int i = 3; i <= Math.sqrt(n); i += 2) {
//            while (n % i == 0) {
//                maxPrime = i;
//                n = n / i;
//            }
//        }
//        if (n > 2)
//            maxPrime = n;
//
//        return maxPrime;
//    }
}
