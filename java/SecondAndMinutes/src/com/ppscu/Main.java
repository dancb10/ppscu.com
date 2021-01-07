package com.ppscu;

public class Main {

    private static final String INVALID_VALUE_MESSAGE = "Invalid value";
    public static void main(String[] args) {

        String duration = getDurationString(65, 45);
        System.out.println(duration);
        duration = getDurationString(60);
        System.out.println(duration);
    }

    private static String getDurationString(int minutes, int seconds) {
        if ((minutes < 0) || (seconds < 0) || (seconds > 59)) {
            return INVALID_VALUE_MESSAGE;
        }

        int calculatedHours = minutes / 60;
        int remainingMinutes = minutes % 60;

        String hoursString = calculatedHours + "h";
        if (calculatedHours < 10) {
            hoursString = "0" + hoursString;
        }

        String minutesString = remainingMinutes + "m";
        if (remainingMinutes < 10) {
            minutesString = "0" + minutesString;
        }

        String secondsString = seconds + "s";
        if (seconds < 10) {
            secondsString = "0" + secondsString;
        }

        return hoursString + " " + minutesString + " " + secondsString;
    }

    private static String getDurationString(int seconds) {
        if (seconds < 0) {
            return  INVALID_VALUE_MESSAGE;
        }

        int calculatedMinutes = seconds / 60;
        int calculatedSeconds = seconds % 60;

        return getDurationString(calculatedMinutes, calculatedSeconds);
    }
}
