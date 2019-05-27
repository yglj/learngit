# include<iostream>
using namespace std;
double Gt(float x,float y)
{
	return x>y?x:y;
}
int main()
{   
  int i=23,j=45,result;
  double d;
  d=i;
  result=Gt(i,j);
  cout<<d<<endl;
  cout<<result<<endl;
  
	
	return 0;
}
