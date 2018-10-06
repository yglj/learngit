package com.gg.example;

public class TestThis {
	String str;
	int a;
	TestThis(int a){
		this();
		this.a =a;
	}
	TestThis(){
		System.out.println("构造器第一句。");
	}
	public void setA(int a){
		this.a = a;
	}
	public static void main(String [] args){
		TestThis t = new TestThis(5);
		
	}
	
}
