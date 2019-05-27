package com.test.set;

import java.util.HashMap;
import java.util.Map;
import java.util.Set;
import java.util.TreeSet;


public class mySet {
	private int size;
	private Map map = new HashMap();
	private static final Object Present = 0;
	public int size(){
		return map.size();
	}
	
	@SuppressWarnings("unchecked")
	public void add(Object obj){
		  map.put(obj,Present == null);
	}
	
	public Object get(Object obj){
		return map.get(obj);
	}
	
	public static void main(String[] args) {
		mySet m = new mySet();
		m.add(m);
		m.add(2);
		System.out.println(m.size());
	}
}
