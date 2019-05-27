# include <iostream>
using namespace std;
namespace one 
{
	const int m=200;
	int inf=10;
}
namespace two
{
	int x;
	int inf=11;
}

using namespace  one;
int main()
{
	using  two::x;
	x=-100;
	cout<<inf<<endl;
	two::inf*=2;
	cout<<two::inf<<endl;
	cout<<x<<endl;
	
	
	
	cout<<"Welcome to C++!"<<endl; 
	return 0;
} 
