# include <iostream>
using namespace std;
float checkAgecore(int age ,float s)
{
	if(age<15||age>25) throw age;
	if(s<0||s>5) throw age;
	else s*=20;
	return s;
}
int main()
{   int age=20;
  float  s=4;
	string name="l"; 
  cout<<name<<endl;
   cout<<age<<endl;
  try
  {
  	cout<<checkAgecore( age , s)<<endl;
  }
  catch(float b)
  {
  	 cout<<"flaut "<<endl;
  }
    catch(int a)
  {
  	 cout<<"flaut "<<endl;
  }
  

  return 0;	
} 
