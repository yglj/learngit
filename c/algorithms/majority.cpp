# include <stdio.h>
int candidate(int *a,int n,int m){
	int i = m ;
    int c = a[m];
    int count = 1;
    while(i < n && count > 0){
    	if(a[++i] == c)	count ++;
    	else	count--;
    }
    if(i == n) return c ;
    else return candidate(a,n,i+1);
}
int majority(int *a,int n){
	int c = candidate(a,n-1,0);
	int count = 0;
	for(int i = 0; i<n ; i++){
		if (c == a[i]){
		count++;
		}
	}
	if(count > n/2) return c;
	else return NULL;
}
int main(){
	int a[8] ={2,4,1,4,4,4,6,4};
	int m = majority(a,8);
	printf("多数元素是：%d\n",m);
	return 0;
} 
