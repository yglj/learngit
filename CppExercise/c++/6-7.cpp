# include <iostream>
using namespace std;
class Base
{
public:
		virtual ~Base()
{
	cout<<"destructing B "<<endl;
}	
};
class Derive:public Base
{
	public:
		virtual ~Derive()
{
	cout<<"destructing D"<<endl;
}	
};
int main()
{
	Base *b;
	b=new Derive();
	delete b;
	return 0;
}
