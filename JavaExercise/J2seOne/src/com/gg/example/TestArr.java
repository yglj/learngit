package com.gg.example;



public class TestArr {
	public static void main(String[] args) {
		int a[][] = new int[3][] ;
		a[0] = new int[1];
		a[1] = new int[2];
		a[2] = new int[3];
		a[0][0] = 1;
		a[1][0] = 2;
		a[1][1] = 3;
		a[2][0] = 4;
		a[2][1] = 5;
		a[2][2] = 6;		

		int b[] = {1,2,3,4,5,6};
//        for (int i : b) {
//        	System.out.println(i);
//		}
    	Integer i = new Integer("24");
    	Integer ii = Integer.parseInt("34");
    	//System.out.println(ii.intValue());
    	int a1 =123;
    	int b1 =1234;
    	Integer d = 1234;
    	Integer d2 = 1234;
    //	System.out.println(a1 instanceof Integer);
    //   	System.out.println();
    	System.out.println(d == d2);
    	System.out.println(a1 == b1);
    //	d.intValue();
        
	}

	
}
