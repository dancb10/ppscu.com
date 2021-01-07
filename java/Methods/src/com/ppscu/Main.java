package com.ppscu;

public class Main {

    public static void main(String[] args) {
        boolean gameOver = true;
        int score = 500;
        int levelCompleted = 5;
        int bonus = 100;

        int highScore = calculateScore(true, 500, 5, 100);
        System.out.println("Your final score was: "+highScore);
        System.out.println("Your final score was: "+calculateScore(true, 800, 8, 1000));

        score = 10000;
        levelCompleted = 8;
        bonus = 200;
        highScore = calculateScore(gameOver, score, levelCompleted, bonus);


        int highScorePosition = calculateHighScorePosition(1500);
        displayHighScorePosition("Dan", highScorePosition);

        highScorePosition = calculateHighScorePosition(900);
        displayHighScorePosition("Tim", highScorePosition);

        highScorePosition = calculateHighScorePosition(1000);
        displayHighScorePosition("Shim", highScorePosition);
    }

    public static int calculateScore(boolean gameOver,
                                      int score,
                                      int levelCompleted,
                                      int bonus) {

        if (gameOver) {
            int finalScore = score + (levelCompleted * bonus);
            finalScore += 2000;
            return finalScore;
        }
        return -1;
    }

    public static void displayHighScorePosition(String playerName, int playerPosition) {

        System.out.println(playerName + " managed to get into position " + playerPosition + " on the hight score table");
    }

    public static int calculateHighScorePosition(int playerScore) {

//        if (playerScore >= 1000) {
//            return 1;
//        }
//        else if (playerScore >= 500) {
//            return 2;
//        }
//        else if (playerScore >= 100) {
//            return 3;
//        }
//        return 4;

        int position = 4;
        if (playerScore >= 1000) {
            position = 1;
        }
        else if (playerScore >= 500) {
            position = 2;
        }
        else if (playerScore >=100) {
            position = 3;
        }
        return position;
    }

}
