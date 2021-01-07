package com.ppscu;

import java.util.*;

public class Main {

    private static List<Album> albums = new ArrayList<Album>();
    public static void main(String[] args) {

        Album album = new Album("Stormbringer", "Deep Purple");
        album.addSong("Stormbrinder", 4.6);
        album.addSong("You can't do it right", 4.22);
        album.addSong("The stuff", 5.1);
        album.addSong("Test song", 6.);
        albums.add(album);

        album = new Album("For these about to rock", "AC/DC");
        album.addSong("Yoo", 3.2);
        album.addSong("My stuff", 7.22);
        album.addSong("Flick", 5.2);
        album.addSong("Yoo22", 3.22);
        albums.add(album);

        List<Song> playlist = new Vector<Song>();
        albums.get(0).addToPlayList("You can't do it right", playlist);
        albums.get(0).addToPlayList("The stuff", playlist);
        albums.get(0).addToPlayList("Test song", playlist);
        albums.get(0).addToPlayList("Test song does not exist", playlist); // does not exist
        albums.get(0).addToPlayList(1, playlist);
        albums.get(1).addToPlayList("Flick", playlist);
        albums.get(1).addToPlayList("My stuff", playlist);
        albums.get(1).addToPlayList(1, playlist);
        play(playlist);
    }

    private static void play(List<Song> playList) {
        Scanner scanner = new Scanner(System.in);
        boolean quit = false;
        boolean forward = true;
        ListIterator<Song> listIterator = playList.listIterator();
        if(playList.size() == 0) {
            System.out.println("No songs in playlist");
        } else {
            System.out.println("Now playing: " + listIterator.next().toString());
            printMenu();
        }

        while(!quit) {
            int action = scanner.nextInt();
            scanner.nextLine();

            switch (action) {
                case 0:
                    System.out.println("Playlist complete.");
                    quit=true;
                    break;
                case 1:
                    if(!forward) {
                        if(listIterator.hasNext()) {
                            listIterator.next();
                        }
                        forward = true;
                    }
                    if(listIterator.hasNext()) {
                        System.out.println("Now playing: " + listIterator.next().toString());
                    } else {
                        System.out.println("We have reached the end of the playlist");
                        forward = false;
                    }
                    break;
                case 2:
                    if(forward) {
                        if(listIterator.hasPrevious()) {
                            listIterator.previous();
                        }
                        forward = false;
                    }
                    if(listIterator.hasPrevious()) {
                        System.out.println("Now playing: " +listIterator.previous().toString());
                    } else {
                        System.out.println("We have reached the start of the playlist");
                        forward = true;
                    }
                    break;
                case 3:
                    if(forward) {
                        if (listIterator.hasPrevious()) {
                            System.out.println("Now replaying: " + listIterator.previous().toString());
                            forward = false;
                        } else {
                            System.out.println("We are at the start of the list");
                        }
                    } else {
                        if(listIterator.hasNext()) {
                            System.out.println("Now replaying " + listIterator.next().toString());
                            forward = true;
                        } else {
                            System.out.println("We have reached the end of the list");
                        }
                    }
                    break;
                case 4:
                    printList(playList);
                    break;
                case 5:
                    printMenu();
                    break;
                case 6:
                    if(playList.size() > 0) {
                        listIterator.remove();
                        if(listIterator.hasNext()) {
                            System.out.println("Now playing: " + listIterator.next());
                        } else if(listIterator.hasPrevious()) {
                            System.out.println("Now playing: " + listIterator.previous());
                        }
                    }
                    break;
            }
        }
    }

    private static void printMenu() {
        System.out.println("Available actions:\npress");
        System.out.println("0 - to quit\n" +
                "1 - to play next song\n" +
                "2 - to play previous song\n" +
                "3 - to replay the current song\n" +
                "4 - list songs in the playlist\n" +
                "5 - print available actions\n" +
                "6 - delete current song from playlist");
    }

    private static void printList(List<Song> playList) {
        Iterator<Song> iterator = playList.iterator();
        System.out.println("===============================================");
        while(iterator.hasNext()) {
            System.out.println(iterator.next());
        }
        System.out.println("===============================================");
    }
}
