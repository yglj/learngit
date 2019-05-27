# include <iostream>
using namespace std;
class Date
{
	int year,month,day;
	public:
		Date(int y,int m,int n)
		{
			year=y;
			month=m;
			day=n;
		}
	void Print()
	{
		cout<<year<<"."<<month<<"."<<day<<endl;
	}
};
class Vehicle 
{
	private:
	Date date;
	int price;
	public:
	  Vehicle(int m,int n,int d,int i):date(m,n,d)
		{
			price=i;
		}
		void set(int n)
		{
			 price=n;
		}
		void Print()
		{
			date.Print();
			cout<<"price="<<price<<endl;	
		}
};
class Car:public Vehicle
{
	private:
		int person;
	public:
		Car(int a,int b,int c,int d,int m):Vehicle(a,b,c,d)
		{
			person=m;
		}
		void Print()
		{
			Vehicle::Print();
			cout<<"person="<<person<<endl;	
		}
};
class Truck:public Vehicle
{
	private:
	int ton;
	public:
	 Truck(int a,int b,int c,int d,int t):Vehicle(a,b,c,d)
	  {
	  	ton=t;
	  } 
	 	void Print()
		{
			Vehicle::Print();
			cout<<"ton="<<ton<<endl;	
		}
};
int main()
{
	Vehicle a(2014,8,5,14000);
	Car b(1,2,3,4000,20);
	Truck c(0,0,0,10000,100);
	a.Print();
	b.Print();
	c.Print();
	return 0;
} 
