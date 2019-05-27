# include <iostream>
using namespace std;
class Mammal
{
	public:
		virtual void Speak()=0;
};
class Dog:public Mammal
{
	void Speak()
	{
		cout<<"ÍôÍô"<<endl;
	}
};
int main()
{
	Mammal *m;
	Dog d;
	m=&d;
	m->Speak(); 
	return 0;
}
