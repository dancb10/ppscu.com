package com.example.test;

import java.util.ArrayList;
import java.util.List;

public class Departament {

    private String name;
    private List<Employee> employees;

    public Departament(String name) {
        this.name = name;
        employees = new ArrayList<>();
    }

    public void addEmployee(Employee employee) {
        employees.add(employee);
    }

    public List<Employee> getEmployees() {
        return employees;
    }
}
