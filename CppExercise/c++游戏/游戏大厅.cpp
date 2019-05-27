# include <iostream>
# include <string>
using namespace std;
class Player
{ 
  private:
  	string m_Name;
  	Player *m_pNext;
  public:	  
    Player(const string & name =" "):m_Name(name),m_pNext(0)
    {}
    Player* GetNext() const  //返回一个指针类型的常函数 
    {
    	return m_pNext;
    }
    string GetName() const
    {
    	return m_Name;
    }
    void SetNext(Player *next)//传入指针对象，赋给next指针成员 
    {
    	m_pNext = next ; 
    }
};
class Lobby
{ 
  private:
  	Player *pHead;
  public:
  	Lobby():pHead(0)
  	{}
  	~Lobby()
  	{
  		clear();
  	}
  	void addPlayer()
  	{
  		string name;
  		cout<<"Enter the name:\n";
  		cin>> name;
  		Player *newplayer = new Player(name);
  		if(pHead == 0) //队列头部为空，直接插入 
  		{
  			pHead = newplayer;
  		}
  		else
  		{
  			Player * pIter = pHead;
  			while(pIter->GetNext() != 0){ //到尾节点时pIter->Getnext()指针为0
		//找到一个对象的next指针为空 ，那么这个对象是尾节点 
		//用指针pIter指向的对象的方法返回的指针作判断，不能用对象作判断 
  				pIter = pIter->GetNext();
	   //把pIter 指针指向（指针指向的对象返回的指针存有下个对象的地址）下一个对象 
  			}
  			pIter->SetNext(newplayer);
  			//把新对象的地址传给（pIter指向的对象的方法返回）末尾对象的next指针 
  		}
  		cout<<"add successful\n";
  	}
  	void removePlayer()
  	{
  		if(pHead == 0)  //头部为空？ 
  		{
  			cout<<"The list is Empty\n";
  		}
  		else        
  		{
  			Player * pTemp = pHead;  
  			pHead = pHead->GetNext(); 	  //头部指针指向下一个对象		 
  			delete pTemp;  //删除指针 
  		}
  		cout<<"delete successful\n";
  	}
  	void clear()
  	{
  		while(pHead != 0){ //一直移除，直到头部为空 
  			removePlayer();
  		}
  		cout<<"clear successful\n";
  	}
  	friend ostream& operator << (ostream &os,const Lobby &lobby);
};
//重载<<运算符函数作友元函数  
ostream& operator << (ostream &os,const Lobby &lobby)
{
	Player *pIter = lobby.pHead ;  // 
	cout<<"\nWho is in the Lobby game:\n";
	if(pIter == 0){
		os<<"empty!\n";
	} 
	else{                //遍历所有节点，输出每个节点的名字 
	  while(pIter != 0){ //到尾节点时pIter指针不为0
		os<<pIter->GetName()<<endl;
		pIter = pIter->GetNext(); 
	   }
	}
	return os; 
}
int main()
{
	Lobby lobby;
	cout<<"Lobby game\n";
	cout<<"0-Quit\n";
	cout<<"1-Add player game\n";
	cout<<"2-Remove player\n";
	cout<<"3-Clear player\n";
	int choice ;
	do
	{
	cout<<lobby;
	cout<<"\nplease choice:\n";
	cin>>choice ;
	switch (choice)
	 {
		case 0:cout<<"Goodbye!\n";
			break;
		case 1: lobby.addPlayer();
			break;
		case 2: lobby.removePlayer();
			break;
		case 3: lobby.clear();
			break;
		default: cout<<"you enter invavid input\n";
	 }
	}while (choice != 0);
	return 0;
} 
