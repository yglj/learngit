# include <iostream>
using namespace std;
int main()
{   int f=0,z=0,i;
	int *a=new int[20];
	if(!a)
	{
		cout<<"failure\n";
		return -1;
	}
	for(i=0;i<20;i++)
	{
		
    cin>>a[i];
   // if(a[i]!=0)
    //if(a[i]<0||a[i]>0)
	{
    if(a[i]>0)	++z;
     if(a[i]<0) ++f;
    }
   }
    cout<<z<<'\t'<<f;
	delete []a;
	return 0; 

}
