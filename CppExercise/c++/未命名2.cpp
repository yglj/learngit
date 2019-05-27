# include <iostream>
using namespace std;
int sum=5050;
int main()
{
	int arr[3],i;
	{
		for(int  i=0; i<3;i++)
		cin>>arr[i];
		
	} 
	int sum=0;
	for(i=0;i<3;i++)
    sum+=arr[i];
    for(i=0;i<3;i++)
   cout<<arr[i]<<endl;
   cout<<sum<<endl;
      ::sum+=sum;
    cout<<::sum<<endl;
	   return 0;
}
