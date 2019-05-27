# include <iostream>
# include <cstring>
using namespace std;
class Stu
{
	public:
	char *name;
	double s;
	
		Stu(char *p,double c)
		{
			s=c;
			name=new char[strlen(p)+1];
			strcpy(name,p);
		}
	friend void c(Stu &a,Stu &b);	
};
class test
{	
		int max;
		int min;
		public:
			void c(Stu &a,Stu &b)
			{
				max=a.s>b.s?a.s:b.s; 
				min=a.s<b.s?a.s:b.s;
			}
			void print()
			{
				cout<<"最高分"<<max<<endl;
				cout<<"最低分"<<min<<endl;
			}
} ;
int main()
{  
    Stu a[5]={Stu("z",78),Stu("w",80),Stu("z",92),Stu("l",65),Stu("c",50)};
    test t;
    for (int j=1;j<5;j++) 
        { 
            for (int i=0;i<5-i;i++) 
            {
            	
			 t.c(a[j],a[i]);
            }
        }
        t.print();
   	return 0;
}
