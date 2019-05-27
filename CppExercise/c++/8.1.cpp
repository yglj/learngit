# include <iostream>
using namespace std;
template <typename T>T Max(T a,T b)
{
	return a>b?a:b;
}
template <typename T>T Abs(T a)
{
	return a>0?a:-a;
} 
int main()
{
	int a=-5,b=11,c;
	float z=3.14f,x=7.2f,v;
	c=Max(a,b);
	cout<<c<<endl;
	cout<<Abs(a)<<endl;
	cout<<Max(z,x)<<endl;
    cout<<Abs(z)<<endl;
	return 0;
}
