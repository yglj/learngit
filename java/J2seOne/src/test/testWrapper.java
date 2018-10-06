package test;

public class testWrapper {
	public static void main(String[] args) {
		Integer intege9r  = new Integer(100);
		Integer.parseInt("300");
		int i = 1;
	//  编译时装箱	int i = new Integer(1)  把整型对象变成int型
	    Integer a = new Integer(128);
	    Integer b = new Integer(128);
	// 编译时自动拆箱  int a = new Integer(2).inValue()
	    int j = 1;
	    System.out.println(i == j);
	    System.out.println(a == b); //注意在byte类型范围时仍当基本类型处理
	}
}
