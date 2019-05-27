package test;



import org.omg.CORBA.PUBLIC_MEMBER;

import com.gg.example.TestThis;

import test.Computer.Boardkey;
import test.Computer.Cpu;

public class TestInner {
	public static void main(String[] args) {

		Computer c = new Computer();  //非静态内部类必须先创建外部类，再用外部类对象来创建
		Computer.Cpu c1 = c.new Cpu ();
		Computer.Cpu c2 = new Computer().new Cpu();

		Boardkey  b = new Boardkey(); //静态可直接创建
		Computer.Boardkey bb= new Computer.Boardkey();
		b.f();
		bb.f();
		c2.f();
	}
//	public static void function(new WindowAdapter(){
//		void fun(){
//		System.out.println("功能测试");}
//	}){System.out.println("功能测试");}
  


}



class Computer{
	private int price =1000;
	static String brand = "dell";
	static void work(){
		System.out.println("开机");
	}
	void close(){
		System.out.println("end");
	}
	class Cpu{  //非静态类不能有静态成员，可调用静态方法，属性，非静态方法属性
		int price;
		void f(){
			work();
			close();
			System.out.println(Computer.brand);  //静态属性
			System.out.println(Computer.this.price);
			System.out.println("cpu");
		}
	}
	static class Boardkey{  //静态类只能调用静态方法，属性
		static int price;
		void f(){
			price =120;
			System.out.println("静态内部类 "+brand);
		}
	}
}