package com.ppscu;

class Car {

    private boolean engine;
    private int cylinders;
    private String name;
    private int wheels;

    public Car(int cylinders, String name) {
        this.cylinders = cylinders;
        this.name = name;
        this.engine = true;
        this.wheels = 4;
    }

    public int getCylinders() {
        return cylinders;
    }

    public String getName() {
        return name;
    }

    public String startEngine() {
        return "Car -> startEngine()";
    }

    public String accelerate() {
        return "Car -> accelerate()";
    }

    public String brake() {
        return "Car -> brake()";
    }
}

class Mitshubishi extends Car {

    public Mitshubishi(int cylinders, String name) {
        super(cylinders, name);
    }

    @Override
    public String startEngine() {
        return "Mitshubishi -> startEngine()";
    }

    @Override
    public String accelerate() {
        return "Mitshubishi -> accelerate()";
    }

    @Override
    public String brake() {
        return "Mitshubishi -> brake()";
    }
}

public class Main {

    public static void main(String[] args) {

        Car car = new Car(8, "Base car");
        System.out.println(car.startEngine());
        System.out.println(car.accelerate());
        System.out.println(car.brake());

        Mitshubishi mitshubishi = new Mitshubishi(6, "Outlander VRW 4WD");
        System.out.println(mitshubishi.startEngine());
        System.out.println(mitshubishi.accelerate());
        System.out.println(mitshubishi.brake());

        Ford ford = new Ford(6, "Ford Focus");
        System.out.println(ford.startEngine());
        System.out.println(ford.accelerate());
        System.out.println(ford.brake());
    }

    static class Ford extends Car {

        public Ford(int cylinders, String name) {
            super(cylinders, name);
        }

        @Override
        public String startEngine() {
            return "Ford -> startEngine()";
        }

        @Override
        public String accelerate() {
            return "Ford -> accelerate()";
        }

        @Override
        public String brake() {
            return "Ford -> brake()";
        }
    }
}
