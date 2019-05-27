/*
deal player and the house two initial cards
Hide the house's card 
display player's card and house's card
deal addtional cards to players
Reveal house's first card
if house is busted 
    everyone who is not busted wins 
otherwise
    for each player
     if player isn't busted
       if players total is greater than the house's total
          player wins
       otherwise if player's total is less than house's total
          player less
       otherwise
          player pushes
Remove eneryone's cards
*/ 
# include<iostream>
# include<vector>
# include<string>
# include<algorithm>
# include<ctime>
using namespace std;
class Card{
  public:
  	//声明枚举类型 ，表示牌的花色，大小 
   enum rank {ACE = 1,TWO,THREE,FOUR,FIVE,SIX,SEVEN,EIGHT,NINE,TEN,
   JACK,QUEEN,KING};
   enum suit {CLUBS,DIAMONDS,HEARTS,SPADES};
   Card(rank r = ACE,suit s = SPADES,bool b = true):m_Rank(r),m_Suit(s),m_IsFaceUp(b){}
   int GetValue() const  //返回牌的值 ，1-11 
  	{   int value;
  		if(m_IsFaceUp)
  		{
  			value = m_Rank;
  			if(value >10)
  			{
  				value = 10;
  			}
  		}
  		return value;
  	}
   void Flip()  //翻牌，若正面朝上，翻成反面朝上 
   {
  	m_IsFaceUp = !m_IsFaceUp;
   }
   private:
   	bool m_IsFaceUp ;
    rank m_Rank;  
	suit m_Suit; 
   friend ostream &operator <<(ostream & os,const Card &aCard);
};
class Hand{  //玩家的手牌，Card的集合 
public:
	Hand()
	{  
		m_Cards.reserve(7);  //限制向量的容量 
	}
	virtual ~Hand()
	{
		Clear();
	}
	void Add(Card * pCard)   //向手牌添牌 
	{
		m_Cards.push_back(pCard);
	}
	void Clear() //清空手牌 
	{
		//遍历向量，释放在堆中的所有空间 （Card对象的内容） 
		vector<Card *>::iterator iter = m_Cards.begin() ;
		for(iter;m_Cards.end() != m_Cards.end(); ++iter)
		{
			delete *iter;  
			*iter = 0;
		}
		m_Cards.clear(); //清空向量中的指针
	}
	int GetTotal() const //返回手牌值的和 
	{
	 if(m_Cards.empty())  //先判读Cards集合手牌是不是空 
	 {
       return 0;
	 }
     if(m_Cards[0]->GetValue() == 0)
	 {  //若第一张牌的值为0，这个牌是正面朝下的（庄家的手牌），返回0 
      return 0;
	 }
	 int total =0 ; 
	 vector<Card *>::const_iterator iter = m_Cards.begin() ;
	   for(iter;iter != m_Cards.end();++iter)
		{
			total += (*iter)->GetValue() ;  //计算正面的牌值的和，把A的值默认1 
		}
       bool containsAce = false;  // 包含牌A ？ 
	 for(iter;iter != m_Cards.end();++iter)
		{
		 if((*iter)->GetValue() == Card::ACE) containsAce = true ;
		}
       if(containsAce && total<= 11)
	   {//若手牌包含A，且总值够小，让A的值为11 
		   total += 10;
	   }
      return total ;
	}
protected:
	vector<Card *> m_Cards ;  //Card指针类型的向量  存Card对象的地址 

};
class GenericPlayer: public Hand{//玩家 
   public:
   	 GenericPlayer(const string & name ="  "):m_name(name){
   	 }
   	 virtual ~GenericPlayer(){//虚析构函数 
   	 }
   	 virtual bool IsHitting() const = 0;  //指示玩家是否想要跟牌 
   	 bool IsBusted()const{   //返回玩家（牌是否大于21）出局 
   	 	return (GetTotal() > 21);
   	 }
   	 void Bust(){
   	 	cout<<m_name<<"bust!\n";
   	 }
   friend ostream & operator <<(ostream & os,const GenericPlayer & play);
   protected:
   	 string m_name;
}; 
class Deck: public Hand{   //牌堆 
   public:
    Deck(){
    	m_Cards.reserve(52);   //一副牌52张 
    	Populate();    
    	} 
	virtual ~Deck(){}
	void Populate(){  //创建一副标准的52张牌 
		Clear();  //清空手牌 
		for(int s = Card::CLUBS; s <=Card::SPADES ;s++){
			for(int r = Card::ACE; r <= Card::KING;r++){
				Add(new Card(static_cast<Card::rank>(r),static_cast<Card::suit>(s))) ;
			}//列出所有可能的牌，static_cars将int型变为Card定义的枚举型 
		}
	}
	void Shuffle(){//算法shuffle，洗牌 
		random_shuffle(m_Cards.begin(),m_Cards.end());
	}
	void Deal(Hand & aHand){//发牌 
		if(!m_Cards.empty()){    
			aHand.Add(m_Cards.back()); //向手牌对象添m_Cards（牌组）末尾处指针的副本 
			m_Cards.pop_back();//移除牌组的末尾处指针 
		}
		else{
			cout<<"Out of Cards,Unable to Deal\n";
		}
	}
	void AdditionalCards(GenericPlayer & aGenericPlayer){//跟牌 
		while(!(aGenericPlayer.IsBusted()) && aGenericPlayer.IsHitting()){
			Deal(aGenericPlayer);//若玩家没有出局且想要跟牌，发牌 
			cout<<aGenericPlayer<<endl;
			if(aGenericPlayer.IsBusted()){
				aGenericPlayer.Bust();//玩家出局，则宣布出局 
			} 
		}
	} 
};

class Player: public GenericPlayer{ //人类玩家 
   public:
   	Player(const string & name ):GenericPlayer(name){
   	}
   	virtual ~Player(){  
   	}
   	bool IsHitting() const{   //向玩家询问是否跟牌 
   		char response;
   		cout<<"do you want hit?(y/n):";
   		cin>>response ;
   		return (response == 'y' || response == 'Y');
   	}
   	void Win()const{  //宣布结果 
   		cout<<m_name<<" win!\n"; 
   	}
   	void Lose()const{
   		cout<<m_name<<" loses!\n"; 
   	}
   	void Push()const{
   		cout<<m_name<<" pushes!\n"; 
   	}
};
class House: public GenericPlayer{  //庄家 
    public:
    	House(const string & name = "House"){
    	}
    	~House(){
    	}
    	bool IsHitting()const{
    		return (GetTotal() <= 16);  //判断返回点数是否小于等于16，表示庄家跟牌 
    	}
    	void FlipFirstCard(){   
    		if(!(m_Cards.empty())){
    			m_Cards[0]->Flip();  //翻转庄家的第一张牌 
    		}
    		else{
    			cout<<"the cards is empty!\n";
    		}
    	}
};
class Game {
	Deck m_Deck;
	House m_House;
	vector<Player> m_Players;  //创造一个玩家类型的向量 
    public: 
    Game(const vector<string> names){
    	vector<string>::const_iterator pName; // 遍历一个名字向量来实例化Player对象 
    	for(pName = names.begin(); pName < names.end(); ++pName){
    	m_Players.push_back(Player(*pName));
		}
		srand(static_cast<unsigned int>(time(0)));
		m_Deck.Populate(); //生成牌堆 
		m_Deck.Shuffle();  //洗牌 
    }
    ~Game(){}
    void Play(){  //向玩家发两张牌 
    	vector<Player>::iterator pPlayer ;
    	for(int i = 0; i < 2 ; ++i){
    		for(pPlayer = m_Players.begin(); pPlayer < m_Players.end(); ++pPlayer){
    			m_Deck.Deal(*pPlayer);
    		}
    		m_Deck.Deal(m_House);
    	}
    	m_House.FlipFirstCard();  //隐藏庄家的第一张牌 
    	for(pPlayer = m_Players.begin(); pPlayer < m_Players.end(); ++pPlayer){
    			cout<<*pPlayer<<endl;
    		}
    	cout<<m_House<<endl;     //显示每个玩家手牌 
    	for(pPlayer = m_Players.begin(); pPlayer < m_Players.end(); ++pPlayer){
    			m_Deck.AdditionalCards(*pPlayer);
    		}//对跟牌的玩家加一张牌 
    	m_House.FlipFirstCard(); //翻开庄家的第一张牌 
    	m_Deck.AdditionalCards(m_House);//庄家跟牌 
    	
    	if(m_House.IsBusted()){ //庄家出局 
    		for(pPlayer =m_Players.begin(); pPlayer <m_Players.end(); ++pPlayer){
    			if(!pPlayer->IsBusted()){ //每个没出局的玩家获胜 
    				pPlayer->Win();
    			}
    		}
    	}
    	else{ //比较没出局的玩家与庄家的手牌，三种结果 
    		for(pPlayer =m_Players.begin(); pPlayer <m_Players.end(); ++pPlayer){
    			if(!pPlayer->IsBusted()){
    			   if(pPlayer->GetTotal() > m_House.GetTotal()){
    			   	pPlayer->Win();
    			   }
    			   else if(pPlayer->GetTotal() < m_House.GetTotal()){
    			   	pPlayer->Lose();
    			   }
    			   else{
    			   	pPlayer->Push(); 
    			   }
    			}
		    }
    	}
    	for(pPlayer =m_Players.begin(); pPlayer <m_Players.end(); ++pPlayer){
              pPlayer->Clear();
    	}
		m_House.Clear();    	
    } 
};
//重载<<，让标准输出流输出Card，GenericPlayer对象 
ostream &operator <<(ostream & os,const Card &aCard)
{
   const string Rank[] = {"0","A","2","3","4","5","6","7","8","9","10","J","Q","K"};
   const string Suit[] = {"梅花","方块","红心","黑桃"};
   if(aCard.m_IsFaceUp){ //是正面输出牌，反面输出xx 
   	os<<Rank[aCard.m_Suit]<<Suit[aCard.m_Rank]<<endl;
   }
   else{
   	os<<"xx\n";
   }
   return os; 	
}
ostream &operator <<(ostream & os,const GenericPlayer & p)
{
	os<<p.m_name<<":\t"; //名字 
	vector<Card *>::const_iterator pCard;
	if(!p.m_Cards.empty()){   //玩家的牌 
		for(pCard = p.m_Cards.begin(); pCard <p.m_Cards.end();++pCard){
			os<<*(*pCard)<<"\t";
		}
	}
	if(p.GetTotal() != 0){  //点数 
		os<<p.GetTotal()<<endl;
	}
	else{
		os<<"empty\n";
	}
	return os;
}
int  main()
{   
    cout<<"weclome blackjack\n";
    int playernum ;
    while(playernum > 7 || playernum < 1) //输入玩家数 
    {
    	cout<<"输入玩家数（1-7）：";
		cin>>playernum;
    }
    vector<string> names ;
    string name;
    for(int i = 1 ; i < playernum ; i++)  //玩家名装入向量 
    {
    	cout<<"请输入第"<<i<<"个的玩家名字:";
    	cin>>name;
		names.push_back(name); 
    }
    Game game(names);
    char again = 'y';   //游戏主循环 
    while(again != 'n')
    {
    	game.Play();
    	cout<<"请选择是否继续游戏（y/n）：";
    	cin>>again;
    }
	return 0;
}
