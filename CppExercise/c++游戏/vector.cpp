# include <iostream>
# include <vector>
# include <string>
# include <algorithm>
# include <ctime>
# include <cstdlib>
using namespace std;
int main()
{
	vector<string> v;
	v.push_back("sword01");
	v.push_back("shield09");
	v.push_back("zone08");
	vector<string>::iterator myiter;
	vector<string>::const_iterator iter;
	myiter = v.begin();
	*(myiter+1) = "cat02";
	v.insert(v.begin(),"corrbow04");
	random_shuffle(v.begin(),v.end());//ÂÒĞò 
	sort(v.begin(),v.end());//ÉıĞòÅÅĞò 
	for(iter = v.begin();iter !=v.end();++iter)
	{
		cout<<*iter<<endl;
	} 
	iter = find(v.begin(),v.end(),"zone"); //²éÕÒ 
	if (iter!=v.end()) 
	{
		cout<<"find"<<endl;
	}
	else
	{
		cout<<"unfind"<<endl;
	}
	vector<int> s(10,1);
	s.reserve(30);  //¶¨Èİ  
	s.push_back(0);
	cout<<s.size()<<endl;
	cout<<s.capacity()<<endl;  //ÈİÁ¿ 
	 
	return 0;
} 
