# include <iostream>
using namespace std;
float D(float x,float y)
{
	if(y==0) throw y;
	return x/y;
} 
int main()
{
 float a=10.0, b=5.0,c=0.0;
   try
   {
    cout<<D(a,b)<<endl; 
    cout<<D(b,a)<<endl; 
   cout<<D(c,b)<<endl; 
   	cout<<D(a,c)<<endl; 
   }
   catch(float)
   {
   	cout<<"·ÖÄ¸Îª0"<<endl;
   }
   
  cout<<"calulate finished"<<endl;
	return 0;
}
