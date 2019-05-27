# include <iostream>
using namespace std;
float CheckAgeScore(int a,float s)
{
	if(s<0||s>5)throw s;
  if(a<15||a>25)throw a;	
   cout<<a<<endl;
  return s*20;
} 
int main()
{
	string name;
	int age;
	float score;
	cin>>name;
	cin>>age;
	cin>>score;
	try{
    cout<<name<<endl;
	cout<<CheckAgeScore(age,score)<<endl;
     }
	catch(float)
	{
	cout<<"fault \n";
	}
	catch(int)
	{
	cout<<"fault \n";
	}
    cout<<"true \n";
    return 0;
}

