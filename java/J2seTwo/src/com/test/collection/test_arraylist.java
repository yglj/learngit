package com.test.collection;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Vector;

public class test_arraylist {
	@SuppressWarnings({ "unchecked", "rawtypes" })
	public static void main(String[] args) {
		List list = new ArrayList();
		list.add(123);  //param：Object instance 基本类型会自动装箱
		list.size();
		list.isEmpty();
		List list2 =  new LinkedList();
		list.set(0, list2);
		list.add(0, 'a');
//		String s1 = "a";
//		String s2 = "a";
		String s1 = new String("b");
		String s2 = new String("b");
		System.out.println("s1==s2: "+(s1 == s2));
		System.out.println(s1.equals(s2));
		System.out.println("##");
		System.out.println("a"=="a");
		System.out.println("s1: "+s1.hashCode()+"---s2: "+s2.hashCode());
	}
}
class A2{
	public static int aaa;
	public void run(){
		Vector<?> v = new  Vector<>();
	}
}