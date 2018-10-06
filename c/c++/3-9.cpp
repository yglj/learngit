# include <iostream>
using namespace std;
class box
{
	int width,high,length;
	public:
		box(int w,int h,int l)
		{
			width=w;
			high=h;
			length=l;
		}
		int bulk();
};
int box::bulk()
{
	return width*high*length;
}
int main()
{
	box v(2,5,6);
	cout<<v.bulk();
	return 0;
}
