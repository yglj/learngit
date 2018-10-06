package com.test.collection;

import java.lang.reflect.Field;
import java.util.*;

@SuppressWarnings({"rawtypes","unused","unchecked"})
public class collection {
	public static void main(String[] args) {
		run();
	}
	public static void run() {
		List list = new LinkedList<>();
		Collection c ;
		Map  map = new HashMap<>();
		map.put("1","a");
		
		
	}
	
	public static void testA_Field(){
		A a = new A();
		Field[] field = a.getClass().getDeclaredFields();
		for (Field f : field) {   //从a实例中拿到A类的非私有属性 对象
			try {
				A aa = new A();
				System.out.println(f.getInt(aa));  //get INt类型属性的值，param：对象
			} catch (IllegalArgumentException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			} catch (IllegalAccessException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
	}
	
}

class A{
	public int a = 9;
	public String b = "9";
	public int b5 = 8;
}