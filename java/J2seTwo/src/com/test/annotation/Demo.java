package com.test.annotation;

import java.lang.annotation.Annotation;
import java.lang.reflect.Field;

public class Demo {

	@SuppressWarnings("unchecked")
	public static void main(String[] args) {
		try {
			Class c = Class.forName("com.test.annotation.Student");
			//获取类的注解
			Annotation[] annotation = c.getAnnotations();
			for (Annotation a : annotation) {
				System.out.println(a);
			}
			
			//获取类的指定注解
			myannotation01   aa= (myannotation01) c.getAnnotation(myannotation01.class);
			SuppressWarnings s = (SuppressWarnings) c.getAnnotation(SuppressWarnings.class);
			System.out.println(aa.value());
			
			//获取类的属性注解
			Field[]  f = c.getDeclaredFields();
			for (Field field : f) {
				myField myField =  (com.test.annotation.myField) field.getAnnotation(myField.class);
				System.out.println(myField);
			}
		} catch (ClassNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
	
}
