package com.ppscu;

public class Main {

    public static void main(String[] args) {

        System.out.println(canPack(1,0,4));
        System.out.println(canPack(1,0,5));
        System.out.println(canPack(0,5,4));
        System.out.println(canPack(2, 2 ,12));
        System.out.println(canPack(-3, 2 ,12));

    }

    public static boolean canPack(int bigCount, int smallCount, int goal){
        if(bigCount < 0 || smallCount < 0 || goal < 0)
            return false;
        if(bigCount * 5 + smallCount * 1 < goal)
            return false;

        while(bigCount > 0 && goal >= 5){
            goal -= 5;
            bigCount -= 1;
        }
        while(smallCount > 0 && goal >= 1){
            smallCount --;
            goal --;
        }
        return goal == 0;
    }

}
