# include <iostream>
using namespace std;
int &S(const int &a,int&b)
{
	b+=a;
	return b;
}
int main()
{   int x=500,y=1000,z=0;
 cout<<x<<'\t'<<y<<'\t'<<z<<endl;
 z=S(x,y);
  cout<<x<<'\t'<<y<<'\t'<<z<<endl;
 S(x,y)=200;
  
   cout<<x<<'\t'<<y<<'\t'<<z<<endl;

  return 0;	
} 
