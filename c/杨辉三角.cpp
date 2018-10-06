# include <stdio.h>
int main(){
	int a[5][5] = {};
	int i,j=0;
	for (i=0;i<5;i++){
		a[i][0] = 1;
		for(j=0;j<5;j++){
			if(i == j){
				a[i][j] = 1;			
			}
			if(j>0 && j<i)
			a[i][j] = a[i-1][j-1] + a[i-1][j];	
			printf("%d\t",a[i][j]);    
		}
	printf("\n\n");
    }
    
	return 0;
} 
