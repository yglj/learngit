# include<stdio.h>
# include<iostream>
using namespace std; 
int main(){
	void lingxin(int len); 
	lingxin(5);
	return 0;
}
void lingxin(int len){
	for(int i=1 ; i<=len ; i++){
		for(int j=len-i+1; j>=1 ; j--){
			printf(" ");
		}
		for(int k=1 ; k<=i ; k++){
			printf("*");
			printf(".");
		}
		printf("\n");
	}
	for(int i=1 ; i<len ; i++){
		for(int j=1; j<=i+1 ; j++){
			printf(" ");
		}
		for(int k=i+1 ; k<=len ; k++){
			printf("*");
			printf(".");
		}
		printf("\n"); 
	}
		
}

