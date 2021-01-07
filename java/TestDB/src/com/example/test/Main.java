package com.example.test;

import java.sql.*;

public class Main {

    public static final String DB_NAME = "testjava.db";
    public static final String CONNECTION_STRING = "jdbc:sqlite:/Users/dapopesc/mystuff/programming/java/TestDB/" + DB_NAME;

    public static final String TABLE_CONTACTS = "contacts";

    public static final String COLUMN_NAME = "name";
    public static final String COLUMN_PHONE = "phone";
    public static final String COLUMN_EMAIL = "email";


    public static void main(String[] args) {

//         try (Connection conn = DriverManager.getConnection("jdbc:sqlite:/Users/dapopesc/mystuff/programming/java/TestDB/testjava.db");
//              Statement statement = conn.createStatement()
//         ) {

         try {
//             Class.forName("org.sql.JDBC");
             Connection conn = DriverManager.getConnection(CONNECTION_STRING);
//             conn.setAutoCommit(false);
             Statement statement = conn.createStatement();

             statement.execute("DROP TABLE IF EXISTS " + TABLE_CONTACTS);

             statement.execute("CREATE TABLE IF NOT EXISTS " + TABLE_CONTACTS +
                                    " (" + COLUMN_NAME + " text, " +
                                           COLUMN_PHONE + " integer, " +
                                           COLUMN_EMAIL + " text" +
                                    ")");

             insertContact(statement ,"Tim", 545346, "tim@email.com");
             insertContact(statement ,"Ralu", 97921231, "ralu@email.com");
             insertContact(statement ,"Bisi", 48927492, "bisi@email.com");
             insertContact(statement ,"Jane", 42423, "jane@email.com");

             statement.execute("UPDATE " + TABLE_CONTACTS + " SET " +
                     COLUMN_PHONE + "=6543543" +
                     " WHERE " + COLUMN_NAME + "='Jane'");

             statement.execute("DELETE FROM " + TABLE_CONTACTS +
                     " WHERE " + COLUMN_NAME + "='Joe'");

//             statement.execute("INSERT INTO contacts (name, phone, email)" +
//                                    "VALUES('Joe','234255362','joe@email.com')");
//
//             statement.execute("INSERT INTO contacts (name, phone, email)" +
//                     "VALUES('Jane','428468','jane@email.com')");
//
//             statement.execute("INSERT INTO contacts (name, phone, email)" +
//                     "VALUES('Dan','31971','dan@email.com')");

//             statement.execute("UPDATE contacts SET phone=92828 WHERE name='Jane'");
//             statement.execute("DELETE FROM contacts WHERE name='Joe'");

//             statement.execute("SELECT * FROM contacts");
//             ResultSet results = statement.getResultSet();

             ResultSet results = statement.executeQuery("SELECT * FROM " + TABLE_CONTACTS);
             while (results.next()) {
                 System.out.println(results.getString(COLUMN_NAME) + " " +
                                    results.getInt(COLUMN_PHONE) + " " +
                                    results.getString(COLUMN_EMAIL));
             }
             results.close();

             statement.close();
             conn.close();
         } catch (SQLException e) {
             System.out.println("Something went wrong " + e.getMessage());
             e.printStackTrace();
         }
    }

    private static void insertContact(Statement statement, String name, int phone, String email) throws SQLException {
        statement.execute("INSERT INTO " + TABLE_CONTACTS +
                " (" + COLUMN_NAME + ", " +
                COLUMN_PHONE + ", " +
                COLUMN_EMAIL +
                ")" +
                "VALUES('" + name + "'," + phone + ", '" + email + "')");
    }
}
