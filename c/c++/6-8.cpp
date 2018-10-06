# include <iostream>
using namespace std;
class Shape 
{
	public:
	virtual double area()=0;
	virtual	void Print()=0;
	
};
class Rect:public Shape
{
	private:
		int w,h;
	public:
		Rect(int a,int b)
		{
			w=a;
			h=b;
		}
		double area()
		{
			return w*h;
		}
		void Print()
		{
			cout<<"area="<<area()<<endl; 
		}
};
class Circle :public Shape
{
	private:
	int r;
	public:
	  Circle(int c)
	  {
	  	r=c;
	  } 
	  	double area()
		{
			return 3.1416*r*r;
		}
		void Print()
		{
			cout<<"area="<<area()<<endl; 
		}
};
class Square:public Shape
{
	private:
	int z;
	public:
	  Square(int c)
	  {
	  	z=c;
	  } 
	  	double area()
		{
			return z*z;
		}
		void Print()
		{
			cout<<"area="<<area()<<endl; 
		}
};
class Triangle:public Shape
{
	private:
	int w,h;
	public:
	  Triangle(int a,int b)
	  {
	  	w=a;
	  	h=b;
	  } 
	  	double area()
		{
			return 0.5*w*h;
		}
		void Print()
		{
			cout<<"area="<<area()<<endl; 
		}
};
class Trapezoid:public Shape
{
	private:
	int w1,w2,h;
	public:
	  Trapezoid(int a,int b,int c)
	  {
	  	w1=a;
	  	w2=b;
	  	h=c;
	  } 
	  	double area()
		{
			return (w1+w2)*h*0.5;
		}
		void Print()
		{
			cout<<"area="<<area()<<endl; 
		}
};
int main()
{   int i;
    double sum;
	Shape *a[5];
	for(int i=0;i<5;i++)
	switch(i)
	{
	case 0:a[i]=new Rect(2,3); break;
 	case 1:a[i]=new Circle(1);break;
	case 2:a[i]=new Trapezoid(3,5,6);break;
	case 3:a[i]=new Square(4); break;
	case 4:a[i]=new Triangle(8,9);

   }
   for(int i=0;i<5;i++)
  {
	sum+=a[i]->area();
   }
	for(int i=0;i<5;i++)
	a[i]->Print();
	cout<<sum;
	return 0;
} 
