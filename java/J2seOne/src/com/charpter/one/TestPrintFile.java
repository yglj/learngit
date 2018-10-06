
package com.charpter.one;

import java.io.File;

public class TestPrintFile {
	public static void main(String[] args) {
		File file = new  File("F:/BaiduYunDownload/¿ı√Ï∏Û");
		printFile(file, 0);
	}
	public static void printFile(File f,int level){
		for (int i = 0; i < level; i++) {
			System.out.print("---");
		}
		System.out.println(f.getName());
		if(f.isDirectory()){
			File file [] = f.listFiles();
			for (File temp : file) {
				printFile(temp, level+1);
			}
		}
	}
	
}
