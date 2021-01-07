package com.example.test;

import java.util.Map;

public class Main {
    private static StockList stockList = new StockList();

    public static void main(String[] args) {

        StockItem temp = new StockItem("bread", 0.86, 100);
        stockList.addStock(temp);

        temp = new StockItem("cake", 1.10, 7);
        stockList.addStock(temp);

        temp = new StockItem("car", 11.20, 2);
        stockList.addStock(temp);

        temp = new StockItem("toy", 50, 200);
        stockList.addStock(temp);

        temp = new StockItem("toy", 48, 7);
        stockList.addStock(temp);

        temp = new StockItem("pipi", 72.95, 7);
        stockList.addStock(temp);

        temp = new StockItem("apple", 1.05, 7);
        stockList.addStock(temp);

        System.out.println(stockList);

//        for(String s : stockList.Items().keySet()) {
//            System.out.println(s);
//        }

        Basket timsBasket = new Basket("Tim");
        sellItem(timsBasket, "car", 1);
        System.out.println(timsBasket);

        sellItem(timsBasket, "car", 1);
        System.out.println(timsBasket);

        if(sellItem(timsBasket, "car", 1) != 1) {
            System.out.println("There are no more cars in stock");
        }
        sellItem(timsBasket, "spanner", 5);
//        System.out.println(timsBasket);

        sellItem(timsBasket, "juice", 4);
        sellItem(timsBasket, "cup", 12);
        sellItem(timsBasket, "bread", 1);
//        System.out.println(timsBasket);

//        System.out.println(stockList);

        Basket basket = new Basket("customer");
        sellItem(basket,"cup", 100);
        sellItem(basket, "juice", 5);
        removeItem(basket, "cup", 1);
        System.out.println(basket);

        removeItem(timsBasket, "car", 1);
        removeItem(timsBasket, "cup", 9);
        removeItem(timsBasket, "car", 1);
        System.out.println("cars removed: " + removeItem(timsBasket, "car", 1)); // should not remove
        System.out.println(timsBasket);

        System.out.println("\n Display stokc list before and after checkout");
        System.out.println(basket);
        System.out.println(stockList);
        checkOut(basket);
        System.out.println(basket);
        System.out.println(stockList);

        checkOut(timsBasket);
        System.out.println(timsBasket);

//        removeItem(timsBasket, "bread", 1);

//        temp = new StockItem("pen", 1.2);
//        stockList.Items().put(temp.getName(), temp);

//        stockList.Items().get("car").adjustStock(2000);
//        System.out.println(stockList);
//
//        for(Map.Entry<String, Double> price: stockList.Pricelist().entrySet()) {
//            System.out.println(price.getKey() + " costs " + price.getValue());
//        }

    }

    public static int sellItem(Basket basket, String item, int quantity) {
        StockItem stockItem = stockList.get(item);
        if(stockItem == null) {
            System.out.println("We don't sell " + item);
            return 0;
        }
        if(stockList.reserveStock(item, quantity) != 0) {
            return  basket.addToBasket(stockItem, quantity);
        }
        return 0;
    }

    public static int removeItem(Basket basket, String item, int quantity) {
        StockItem stockItem = stockList.get(item);
        if(stockItem == null) {
            System.out.println("We don't sell " + item);
            return 0;
        }
        if(basket.removeFromBasket(stockItem, quantity) == quantity) {
            return  stockList.unreserveStock(item, quantity);
        }
        return 0;
    }

    public static void checkOut(Basket basket) {
        for(Map.Entry<StockItem, Integer> item : basket.Items().entrySet()) {
            stockList.sellStock(item.getKey().getName(), item.getValue());
        }
        basket.clearBasket();
    }
}
