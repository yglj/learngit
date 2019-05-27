
public class Majority {
	public static void main(String[] args) {
		int A[] = {4,9,9,9,9,6};
		int B[] = {9,4,9,7,9,6};
		majority(A);
		majority(B);

		
	}
	public static void majority(int A[]){
		int n = A.length-1;
		int c = candidate(A,0,n);
		int count = 0;
		for(int j =0 ; j<n ;j++){
			if(A[j] == c){
				count++;
			}
		}
		if(count > (n+1)/2){
			System.out.println("多数为；"+c);
		}
		else{
			System.out.println("没有多数");
		}
	
	}
	
	public static int candidate(int A[],int m,int n){
		int j= m;
		int c= A[m];
		int count = 1;
		while (j<n && count >0){
			j++;
			if (A[j] == c ){
				count++;
			}
			else{
				count--;
			}
		}
		if(j == n){
			return c;
		}
		else{
			return candidate(A,j+1,n);
		}
	}
	
}