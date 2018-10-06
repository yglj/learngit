package com.gg.example;
/**
 * 递归test
 * @author Administrator
 *
 */
import java.util.Scanner;;
public class TestRecursion {
	
	public static void main(String [] args){
		System.out.println("输入一个整数：");
		Scanner s = new Scanner(System.in);
		int a = s.nextInt();
		System.out.println(a+"的阶乘为："+f(a));
		s.close();
	}
	
	static long f(int n){
		if(n == 1){
			return 1;
		}
		else{
			return n*f(n-1);
		}
	}
	
	
}
