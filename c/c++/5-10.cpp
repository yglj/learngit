# include <iostream>
using namespace std;
class Shape 
{
	private:
		int x,y;
	public:
	  Shape(int m,int n)
		{
			x=m;
			y=n;
		}
		void Print()
		{
			cout<<"x="<<x<<"\t"<<"y="<<y<<endl;	
		}
};
class Rect:public Shape
{
	private:
		int w,h;
	public:
		Rect(int a,int b,int c,int d):Shape(a,b)
		{
			w=c;
			h=d;
		}
};
class Circle :public Shape
{
	private:
	int r;
	public:
	  Circle(int a,int b,int c):Shape(a,b)
	  {
	  	r=c;
	  } 
};
int main()
{
	Shape a(35,15);
	Rect b(1,2,3,4);
	Circle c(0,0,1);
	a.Print();
	b.Print();
	c.Print();
	return 0;
} 
