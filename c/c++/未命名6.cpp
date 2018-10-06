# include<iostream>
using namespace std;
/*void Swap(int m,int n)   //传值 
{
	int t;
	t=n;
	n=m;
	m=t;
}
int main()
{
	 int a=5,b=10;
	 cout<<a<<'\t'<<b<<endl;
	 Swap(a,b);
	 cout<<a<<'\t'<<b<<endl; 
	return 0;
} */
/*void Swap(int &m,int &n)  //引用 
{
	int t;
	t=n;
	n=m;
	m=t;
}
int main()
{
	 int a=5,b=10;
	 cout<<a<<'\t'<<b<<endl;
	 Swap(a,b);
	 cout<<a<<'\t'<<b<<endl; 
	return 0;
} */
void Swap(int *m,int *n)  //指针 
{
	int t;
	t=*n;
	*n=*m;
	*m=t;
}
int main()
{
	 int a=5,b=10;
	 cout<<a<<'\t'<<b<<endl;
	 Swap(&a,&b);
	 cout<<a<<'\t'<<b<<endl; 
	return 0;
} 
