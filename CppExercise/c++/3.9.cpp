# include <iostream>
using namespace std;
class Date
{
	private:
		int year,month,day;
	public:
		
		Date(int y,int m,int d);
		void SetDate(int y,int m, int d) ;
		void ShowDate(); 
};
Date::Date(int y,int m,int d)
{
	year=y;
	month=m;
	day=d;
}
void Date::ShowDate()
{
	cout<<year<<"."<<month<<"."<<day<<endl;
}
void Date::SetDate(int y,int m,int d)
{
	year=y;
	month=m;
	day=d;
}
int main()
{
	Date date1(2002,11,14);

//	cout<<"date1:";
	 date1.ShowDate();
/*	Date date2(2005);
	cout<<"date2:";
	 date2.ShowDate();
	Date date3(2006,12,15);
	cout<<"date3:";
     date3.ShowDate();*/ 
	
	return 0;
}
