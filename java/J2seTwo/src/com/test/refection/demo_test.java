package com.test.refection;

import java.lang.reflect.Constructor;
import java.lang.reflect.Field;
import java.lang.reflect.Method;

public class demo_test {
	@SuppressWarnings("unused")
	public static void main(String[] args) {
		try {
			String path = "com.test.refection.WW";
			Class<?> w = Class.forName(path);
			System.out.println(w.getName());
			System.out.println(w.getSimpleName());
			
			WW w1 = (WW)w.newInstance();			
			Constructor<?> c = w.getConstructor();
			System.out.println(w1.toString());
			WW w2 = (WW)c.newInstance();
			System.out.println(w2.toString());
			
			Method method  = w.getMethod("setA", int.class);
			method.invoke(w2, 4);
			System.out.println(method);
			
			Field [] fields = w.getDeclaredFields();
			
			System.out.println(fields.length);
			Field field = w.getDeclaredField("a");
			field.setAccessible(true); //不做安全性检查
			field.set(w1, 6);
			
			System.out.println(field.get(w1));
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
}
