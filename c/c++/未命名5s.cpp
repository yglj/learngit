# include<iostream>
using namespace std;
int x=5,y=10;
int &r=x;
void Print()
{
	cout<<"x="<<x<<" y="<<y<<endl;
	cout<<"r="<<r<<endl;
	cout<<"Address"<<'\t'<<&x<<'\t'<<&y<<'\t'<<&r<<endl;
}
int main()
{
	Print();
	r=y;
	y=100;
	Print();
	
	return 0;
} 
