#include <stdio.h>
int sum(int *a, int low ,int high){
	int mid = 0;
	if(low == high) return a[high];
	else{
		mid = (low + high) / 2;
		return sum(a,low,mid)+sum(a,mid+1,high);
	}
}  
int main(){
	int a[9] = {1,2,3,4,5,6,7,8,9};
	int result = sum(a,0,8);
	printf("sum=%d\n",result);
	return 0;
}
