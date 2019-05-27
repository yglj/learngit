#include <stdio.h>
float average(int *a,int n){
	if(n == 1){
		return (float)a[0];
	}
	else{
		int t = (n-1)*average(a,n-1);
	//	printf("t=%d\n",t);
		return (float)(t+a[n-1])/n;
	}
}

int sum(int *a,int n){
	if(n == 0){
		return a[0];
	}
	else {
		return a[n]+sum(a,n-1);
	}
}
int main(){
	int a[9] = {1,2,3,4,5,6,7,8,9};
	int m = average(a,9);
	int n = sum(a,8);
	printf("sum=%d\n",n);
	printf("average=%d\n",m);
	return 0;
} 
