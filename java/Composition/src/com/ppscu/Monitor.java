package com.ppscu;

public class Monitor {

    private String monitor;
    private String manufacturer;
    private int size;
    private Resolution nativeResolution;

    public Monitor(String monitor, String manufacturer, int size, Resolution nativeResolution) {
        this.monitor = monitor;
        this.manufacturer = manufacturer;
        this.size = size;
        this.nativeResolution = nativeResolution;
    }

    public void drawPixelAt(int x, int y, String color) {
        System.out.println("Drawing pixel at " + x + "," + y + " in color " + color);
    }

    public String getMonitor() {
        return monitor;
    }

    public String getManufacturer() {
        return manufacturer;
    }

    public int getSize() {
        return size;
    }

    public Resolution getNativeResolution() {
        return nativeResolution;
    }
}
