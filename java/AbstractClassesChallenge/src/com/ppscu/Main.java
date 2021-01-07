package com.ppscu;

public class Main {

    public static void main(String[] args) {

        SearchTree tree = new SearchTree(null);
        tree.traverse(tree.getRoot());

        String stringData = "5 7 3 8 9 2 4 0 6";

        String[] data = stringData.split(" ");
        for (String s : data) {
            tree.addItem(new Node(s));
        }


        tree.traverse(tree.getRoot());
//        list.removeItem(new Node("5"));
//        list.removeItem(new Node("9"));
//        list.traverse(list.getRoot());

    }
}
