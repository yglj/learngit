# include <iostream>
# include <cstring>
using namespace std;
struct person
{
 char name[20];
 int age;
};
int main()
{
	  
	  person *p;
	  p=new person;
      strcpy(p->name,"wang fun");
	  p->age=23;
	  cout<<"\n"<<p->name<<" "<<endl<<p->age;
	  delete p;
	  return 0;
}
