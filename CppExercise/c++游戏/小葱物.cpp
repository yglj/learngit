/*创造一个宠物
当player不想离开游戏时
     在菜单中选择玩法 
        if the palyer wants to listen to the critter
	       Make the critter talk
		if the player wants to feed the critter
		   Make the critter eat
		if the player wants to play with the critter
		   Make the critter play 
*/
# include<iostream>
using namespace std;
class Critter
{
	private:
		int m_Hunger; //饥饿值 
		int m_Boredom; //舒适度 
		int GetMood()const   //常函数 获取心情 
		{
			return(m_Hunger+m_Boredom);
		}
		int PassTime(int time = 1) //时间推移 
		{
			m_Hunger+=time;
			m_Boredom+=time;
		}
	public:
		Critter(int hunger = 0,int boredom = 0):
		m_Hunger (hunger),m_Boredom(boredom)
        { }
		void Talk()
		{
		int mood = GetMood();
		 if	(mood>15)
		  {
			cout<<"I feel mad\n";
		  }
		 else if (mood>10)
		  {
		  	cout<<"I feel frustrated\n";
		  }
		 else if (mood>5)
		  {
		  	cout<<"I feel okay\n";
		  }
		  else
		  {
		  	cout<<"I feel happy\n";
		  }
		  PassTime();     //随时间推移饥饿，舒适度增加 
		}
		void Eat(int food = 4)
		{
		  cout<<"eat\n";   
		  m_Hunger -= food;  //改变饥饿度 
		  if(m_Hunger < 0)
		  {
		  	m_Hunger = 0;
		  }	
		  PassTime();
		}
		void Play(int fun = 4)
		{
		  cout<<"play\n";
		  m_Boredom -= fun;     
		  if(m_Boredom < 0)   //令数据不为负数 
		  {
		  	m_Boredom = 0;
		  }
		  PassTime();
		}
};
int main()
{   
    Critter c;
    c.Talk();
    cout<<"0 - Quit\n";
    cout<<"1 - Listen to your critter\n";
    cout<<"2 - Feed your c\n";
    cout<<"3 - Play with your c\n";
    int choice;
    do{
     cin>>choice;
	 switch(choice)                    //switch嵌套while中 
	   {
		case 0:                          //选择一种玩法，退出选择 
		    cout<<"Goodbye\n";
			break;
		case 1:c.Talk();
			break;
		case 2:c.Eat();
			break;
		case 3:c.Play();
			break;
		default: cout<<"illegal input\n";
      } 
    }while(choice != 0);        //当选择不是（0）退出时 循环 
	return 0;
}
 
