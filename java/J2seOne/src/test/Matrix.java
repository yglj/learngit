package test;


import java.util.Arrays;



public class Matrix {
	public static void matrix(int a[][],int b[][]){
		try {
			if(a.length != b.length){
				throw new Exception();
			}
			
		} catch (Exception e) {
			// TODO: handle exception
		}
		int c[][] = new int[a.length][a.length];
		for(int i = 0; i < a.length;i++)
			for (int j = 0; j < b.length; j++) {
				c[i][j] = a[i][j]+b[i][j];
			}
		print(c);
	}
	public static void print(int c[][]){
		for(int i = 0; i <c.length;i++){
			for (int j = 0; j <c.length; j++) {
				System.out.print(c[i][j]+"\t");
			}
			System.out.println();
		}
	}
	public static void main(String[] args) {
		int a[][] = {
				{1,3},
				{2,5}
		};
		int b[][] = {
				{3,6},
				{9,3}
		};
		matrix(a, b);
		int s[] = {14,3,62,7,47,8,8};
		Arrays.sort(s);
		Arrays.fill(s,0,1,3);
		System.out.println(Arrays.binarySearch(s,42));
	    System.out.println(Arrays.toString(s));
			
	}
	static void testArrays(){
		//int a[][] ;
		int a[][] = new int[2][];
		int [] c = {0,44,55};
		a[0] = c;
		a[1] = new int[5];
		int b[][] = {
				     	{1,2},
				        {3,4,5,6,7}
				     };
		//未初始化第二维
		a[0][0] = 11;
		a[1][0] = 22;
		a[1][1] = 33;
		for (int[] i : b) {
			for (int j : i) {
				System.out.println(j);
			}
		}
		System.out.println("##########");
		System.out.println((Arrays.toString(a[1])));
		System.out.println(Arrays.toString(c));
	   // System.out.println(a[0]);
	}
}
