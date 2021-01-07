package com.ppscu;

public class Main {

    public static void main(String[] args) {
        // ArrayList<Teams> teams;
        // Collections.sort(teams);

        League<Team<FootballPlayer>> footballLeague = new League<>("AFL");

        Team<FootballPlayer> adelaideCrows = new Team<>("Adelaide Crows");
        Team<FootballPlayer> melbourne = new Team<>("Melbourne");
        Team<FootballPlayer> hawthorn = new Team<>("Howthorn");
        Team<FootballPlayer> fremantle = new Team<>("Fremantle");

        hawthorn.matchResult(fremantle, 1, 0);
        hawthorn.matchResult(adelaideCrows, 3,8 );
        adelaideCrows.matchResult(fremantle, 2, 1);

        footballLeague.add(adelaideCrows);
        footballLeague.add(melbourne);
        footballLeague.add(hawthorn);
        footballLeague.add(fremantle);

        footballLeague.showLeagueTable();

        League<Team<BaseballPlayer>> baseballLeague = new League<>("BSE");
        Team<BaseballPlayer> baseballTeam = new Team<>("Chicago Cubs");
        Team<BaseballPlayer> baseballTeam1 = new Team<>("My baseball");

        baseballTeam.matchResult(baseballTeam1, 2, 1);
        baseballTeam1.matchResult(baseballTeam1, 2,2);

        baseballLeague.add(baseballTeam);
        baseballLeague.add(baseballTeam1);
        baseballLeague.showLeagueTable();

    }
}
