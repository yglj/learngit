# include <iostream>
using namespace std;
int main()
{  int sum1=0,sum2=0;
	int *p=new int[4];
	for(int i=0;i<4;i++)
	{
		cin>>p[i];
		if(p[i]<0)
		sum1++;
		else
		sum2++;	
	} 
	delete []p;
  cout<<sum1<<" "<<sum2<<endl;
  return 0;	
} 
