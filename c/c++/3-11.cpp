# include <iostream>
// # include <cstring>
using namespace std;
class Car
{
	private:
	string brand;
	string type;
	int price;
	int time;
	public:
      void setinfo(string b,string m,int p,int t)
	 {
	 	price=t;
	 	time=p;
	 	brand=b;
	 	type=m;
	 }		
	 void print()
	 {
	 	cout<<"商标："<<brand<<endl;
	 	cout<<"类型："<<type<<endl;
	 	cout<<"出厂年份："<<time<<endl;
	 	cout<<"价格："<<price<<endl;
	 }
};
int main()
{
	Car c;
	c.setinfo("Ford\0","usv\0",2007,1000000); 
	c.print();
	return 0;
} 
