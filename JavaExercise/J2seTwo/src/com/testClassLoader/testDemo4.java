package com.testClassLoader;

public class testDemo4 {
	public static void main(String[] args) throws ClassNotFoundException {
		FilesystemClassLoader loader = new FilesystemClassLoader("D:\\es");
		Class<?> c = loader.loadClass("com.testClassLoader.A");
		Class<?> c2 = loader.loadClass("com.testClassLoader.A");
		System.out.println(c);
		System.out.println(c.hashCode());
		System.out.println(c2.getClassLoader());
		System.out.println(c2.hashCode());
		//同一类加载器，同一个类名加载的类，被JVM认为是同一个类
		FilesystemClassLoader loader2 = new FilesystemClassLoader("D:\\es\\新建文件夹\\partice\\bin\\com\\testClassLoader");
		Class<?> c4 = loader2.loadClass("com.testClassLoader.A");
		System.out.println(c4.getClassLoader());
		System.out.println(c4.hashCode());
		//不同类加载器，加载的同一类名，被JVM认为是不同的类
		Class<?>  s = loader2.loadClass("java.lang.String");
		System.out.println(s);
		System.out.println(s.hashCode());
	}
	/*
	public static void main(String[] args) {
		System.out.println("classloader");
	}*/
}
