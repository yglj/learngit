# include <iostream>
using namespace std;
class Sample
{
	private:
		int x;
		int&rx;
		const float pi;
		public:
			Sample(int x1):rx(x1),pi(3.14)
			{
				x=x1;
			}
			void Print()
			{
				cout<<"x="<<x<<" rx="<<rx<<" pi="<<pi;
			}
};
int main()
{
	Sample a(10);
	a.Print();
	
	return 1;
} 
