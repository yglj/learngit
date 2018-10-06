
public class Test3 {
	public static void test(int a,int b,int c){
		for(int i = 1; i <= a ; i++){
			if(i % b == 0){
				System.out.print(i+"\t");
			}
			if(i % (b * c) == 0){
				System.out.println();
			}
		}
	}
	public static void main(String [] args){
	/*
	 * 	int rand = 1 + (int)(Math.random()*6);
		//System.out.println(rand);
		for(int i = 1 ; i <= 9 ; i++){
			for(int j = 1 ; j <= i ; j++){
				System.out.print(i+"*"+j+"="+(i*j)+"\t");
			}
		System.out.println();
	    }
	*/
	//	test(100,7,2);
		int tatol = 0;
		while(true){
			tatol++;
			double d = 100 * Math.random();
			int i = (int) Math.round(d);
			if(i == 78){
				break;
			}
		}
		System.out.print("run times: "+tatol);
	}
}
