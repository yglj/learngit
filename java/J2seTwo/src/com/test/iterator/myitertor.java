package com.test.iterator;
/**
 *模仿arraylist实现一个内部迭代器
 */

import java.util.Iterator;



public class myitertor implements java.lang.Iterable<String>{	
	private String[] elem = {"a","b","c","d","f"};
	private int size = elem.length;
	
	public Iterator<String> iterator(){
		return new Iterator<String>(){
			private int cursor;
					public boolean hasNext(){
						return cursor < size;
					}	
					public String next(){
						return elem[cursor++];
					}
					public void remove(){
						
					}
		};   //使用匿名内部类
	}
	
	public static void main(String[] args) {
		myitertor m = new myitertor();
		Iterator<String> it = m.iterator();
		while(it.hasNext()){			
			System.out.println(it.next());
		}
		
System.out.println("********");
		for(String temp : m){		
			System.out.println(temp);
		}
	}
	
}

