/**
 * 测试递归的基本流程，阶乘的例子
 * @author Administrator
 *
 */
public class TestRecursion2 {
	static int a = 0;
	/**
	 * 测试递归体，递归头
	 */
	public static void test01(){
		a++;
		System.out.println("test01:"+a);
		if(a<=10){  //递归头
			test01();
		}else{      //递归体
			System.out.println("over");
		}
	}
	/**
	 * 方法，输出一句话test02
	 */
	public static void test02(){
		System.out.println("TestRecursion.test02()");
	}
	
	/**
	 * 一个方法，计算某个数的阶乘
	 * @param n  n的阶乘
	 * @return   阶乘结果
	 */
	public static long factorial(int n){
		if(n==1){
			return 1;
		}else{
			return n*factorial(n-1);
		}
	}
	
	public static void main(String[] args) {
		test01();
		System.out.println(factorial(10));  
	}
}
