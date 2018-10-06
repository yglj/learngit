package test;

import com.gg.example.Tf;

public class TestObj extends Tf{

	public static void main(String [] args){
	 Object obj = new Object(); 
	 Object obj1 = new Object(); 
		System.out.println(obj.toString());
		System.out.println(obj1.toString());
		System.out.println(obj.equals(obj1));
		Tf f =new Tf();
		f.print();
	}
}
