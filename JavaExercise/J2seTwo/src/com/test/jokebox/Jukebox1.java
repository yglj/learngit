package com.test.jokebox;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.util.ArrayList;

public class Jukebox1 {
	ArrayList<String> songs = new ArrayList<String>();
	public static void main(String[] args){
		Jukebox1 box = new Jukebox1();
		box.go();
	}
	public void go(){
		getSongs();
		System.out.println(songs);
	}
	
	void getSongs(){
		BufferedReader b = null;
		try{
			File f = new File("C:/Users/Administrator/Desktop/SongList.txt");
			b = new BufferedReader(new FileReader(f));
			String line = null;
			while((line = b.readLine()) != null){
				addSongs(line);
			}
			b.close();
		}
		catch(Exception e){
			e.printStackTrace();
		}

	}
	
	void addSongs(String line){
		String[] tokens = line.split("/");
		songs.add(tokens[0]);
	}
	
	
}
