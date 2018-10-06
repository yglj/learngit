package com.gg.example;

public class Student {
	int num;
	String name;
	String render;
	int age;
	Computer computer;
	public void Study(){
		System.out.println(name+"在学习");
	}
	public void sayHello(String sname){
		System.out.println(name+"对"+sname+"说你好");
		
	}
	public static void main(String [] args){
		Computer c = new Computer();
		
		Student s = null;
		s = new Student();
		s.name = "wangba";
		s.Study();
		s.sayHello("nn");
	    s.computer = c;
		s.computer .brand  = "dell";
		System.out.println(s.computer.brand);
		c.priece = 1000;
		System.out.println(s.computer.priece);
		String str = "dell";
		boolean b;
		if(b = (str == s.computer.brand)){
			 System.out.println(b);
		   }
	}
}
