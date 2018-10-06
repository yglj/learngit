package com.gg.example;

public class Test {
	public static void main(String[] args) {
//		String s = "abcdfe";
//		int i = 9 ;
//		System.out.println((s+i) instanceof String);
//		char c = 'a';
//		int a[] = {1,2,4};
//		int b[] = new int [3];
//		System.arraycopy(a,1,b,1,2);
//		System.out.println(s+c);
	   
		StringBuilder str = new StringBuilder("abcef");
		System.out.println(str.length());
		System.out.println(str.capacity());
		str.append(1).append('a').append(true);
		System.out.println(str); 
	}
}
