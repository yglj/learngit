# include <iostream>
using namespace std;
class Test
{
	private:
		int x,y;
	public:
	 void Init(int m,int n)
		{
			x=m;
			y=n;
		}
		void Print()
		{
			cout<<"x="<<x<<"\t"<<"y="<<y;	
		}
};
int main()
{
	Test a;
	a.Init(35,15);
	a.Print();
	return 0;
} 
