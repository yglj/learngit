#include <iostream>
#include <algorithm>
using namespace std;
void HeapAdjust(int A[],int size ){
    for(int i = size/2 ;i >= 0; i--){
	  int l = 2*i;
	  int r = 2*i+1;
      int tmp ;
	  while(l<=size){
		tmp = l;
		if(r<=size && A[r]>A[l]){  //左右节点比较
			tmp = r;
		}
		if(A[tmp]>A[i]){            //与父节点比较 
			swap(A[i],A[tmp]);
		}
		else break;
	  }
	}
}
/*
void MakeHeap(int A[],int size){
	int i;
	for(i = size/2 ;i >= 0; i--){   //从最后一个非叶子节点开始到根节点 
		HeapAdjust(A,size);
	}
}*/
void HeapSort(int A[], int size){
	int i;
    HeapAdjust(A,size);
	for(i = size;i >= 1;i--){
			swap(A[0],A[i]); //算法 
        	HeapAdjust(A,i-1);
	}
}
int main(){
	int a[8] = {9,4,5,2,1,7,4,6};
 	HeapSort(a,8);
	for(int i=0;i<8;i++){
		cout<<"第"<<i<<"个数:"<<a[i]<<endl;
	}
	return 0;
}

