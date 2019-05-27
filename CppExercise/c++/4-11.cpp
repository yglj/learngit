# include <iostream>
# include <cstring>
using namespace std;
class Book
{
	private:
		char* name;
	char* author=new char[10];
	//	char* author[10];
		int sale;
		public:
			Book();
			Book(char*a,char* b,int n);
			void Print();
			~Book(); 
};
Book::Book()
{   sale=0; 
    name=new char[5];
    strcpy(name,"w");
	cout<<"默认创建"<<endl;
}
Book::Book(char*a,char *b,int n)
{
   name=new char[5];
	strcpy(name,a);
//	author=new char[6]; 
	strcpy(author,b);
	sale=n;
	cout<<"创建"<<endl; 
}
void Book::Print()
{
cout<<sale<<endl;	
cout<<"name="<<name<<endl;
}
Book::~Book()
{
	delete []name;
	delete []author;
	cout<<"毁灭"<<endl;
}
int main()
{
	Book b;
	Book bb("o","l",6);
	b.Print();
	bb.Print(); 
	return 0;
}
