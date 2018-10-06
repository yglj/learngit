# include <iostream>
# include <string>
# include <vector>
# include <algorithm>
using namespace std;
const char X = 'X';  //全局常量 
const char O = 'O';
const char EMPTY = ' '; 
const char TIE = 'T';
const char NO_ONE = 'N';
void instructions(); //显示游戏操作指南 
char askYesNo(string question);  
int askNumber(string question, int high, int low = 0);
char humanpiece();
char opponent(char piece);
void displayBoard(const vector<char> & board);
char winner(const vector<char> & board);
bool isLegal(const vector<char> &board, int move);
int humanMove(const vector<char> & board,char human);
int computerMove(vector<char> board , char computer);
void announceWinner(char winner , char computer, char human);
int main()
{
	int move;
	const int NUM_SQUARES = 9; 
    vector<char> board(NUM_SQUARES,EMPTY); //初始化棋盘为空 
    instructions(); 
    char human = humanpiece();  //确定玩家旗子 
    char computer = opponent(human);  
    displayBoard(board);
    char turn = X; 
    while(winner(board) == NO_ONE)  //winner（）确定胜者  循环条件：无人取胜 
    {
    //	if (human == turn)
    	if (turn == human) //若人类棋子是X，先走 
    	{
    		move = humanMove(board,human); //move接收下棋位置 
    		board[move] = human; //更新棋盘 
    	}
    	else
    	{
    		move = computerMove(board,computer);
    		board[move] = computer;
    	}
    	displayBoard(board);
    	turn = opponent(turn); //换棋 ，让对手下棋 
    }
    announceWinner(winner(board),computer,human);
	return 0;
}
void instructions()
{
	cout<<"Welcome to the game!\n"; 
} 
char askYesNo(string question) //参数传入问题 
{
	char answer;
	do{
	cout<<question<<"(y/n):";
	cin>>answer;                           
    }while(answer != 'y' && answer != 'n');  // 用循环限制回答为y或n 
	return answer ;	
} 
int askNumber(string question, int high, int low )
{
	int number; //用数字代表下棋位置 
	do{
	cout<<question<<"("<<high<<"-"<<low<<"):";
	cin>>number;
    }while(number < low || number >high);	//number不能超出棋盘位置 ||或 
	return number;	
} 
char humanpiece()
{
  char go_first = askYesNo("Do you require the first move");
  if (go_first == 'y')  //询问玩家是否先走 
  {
  	return X;  
  }
  else 
  {
  return O;
  }
}
char opponent(char piece)
{
	if (piece == X)
	{
		return O;
	}
	else 
	{
		return X;
	}
}
void displayBoard(const vector<char> & board) //显示棋盘 
{
	cout<<"\n\t"<<board[0]<<"|"<<board[1]<<"|"<<board[2];
	cout<<"\n\t"<<"------";
	cout<<"\n\t"<<board[3]<<"|"<<board[4]<<"|"<<board[5];
	cout<<"\n\t"<<"------";
	cout<<"\n\t"<<board[6]<<"|"<<board[7]<<"|"<<board[8];
	cout<<"\n\n"; 
}
char winner(const vector<char> & board)
{  //用数组装入获胜条件的下棋位置 
   const int winner_row[8][3]={{0,1,2},{3,4,5},{6,7,8},{0,3,6},
                                {1,4,7},{2,5,8},{0,4,8},{2,4,6}};
   const int TOTAL_ROWS = 8 ; 
   for(int i =0; i < TOTAL_ROWS; ++i) //比较每个条件三个位置的棋子是否一样且不为空 
   {
   	if(board[winner_row[i][0]] != EMPTY && board[winner_row[i][0]]
   	== board[winner_row[i][1]] && board[winner_row[i][0]]
   	== board[winner_row[i][2]] )
   	{ return board[winner_row[i][0]]; };//若满足条件返回第一个棋子 
   }
   	if(count(board.begin(),board.end(),EMPTY) == 0)
   	{
   		return TIE ;//count()检查所有棋盘位置是否有空位 
   	}
  return NO_ONE ;	
}
inline bool isLegal( int move,const vector<char>& board)//返回布尔值 
{  
   return (board[move] == EMPTY);  //检查所选位置是否为空 返回true 
}
int humanMove(const vector<char> & board,char human)
{   // 接收下棋位置 
	int move = askNumber("\nwhere you move：",(board.size()-1));
	while(!isLegal(move, board)){ //不为空 false 时循环 
	move = askNumber("\nwhere you move：",(board.size()-1));
	}
	return move;
}
int computerMove(vector<char> board , char computer)
{  //1.若计算机能一招取胜则选择这招棋 
   unsigned	int move;  //无符号整形 
   bool found =false;  //逻辑判断 初始化为false 
   while(!found && move < board.size()){ //结束条件为found不为false  
   	 if(isLegal(move,board)){   //在所有招棋中，检查合法性 
   		board[move] = computer; //假定下棋 
   		found = winner(board) == computer;//判断棋招是否取胜 胜返回true 
   		//否则返回false  
   		board[move] = EMPTY ; //清空棋招 
   	   }
   	 if(!found){ // 
   		++move ;
   	   } 	
   }
   //2 否则，若人类能在下一步取胜，则阻止 
   if(!found){ //if(true) 为真必执行if 
   	move =0;
   	char human = opponent(computer);
   	while(!found  && move < board.size()){//结束条件：found为 true 
   	    if(isLegal(move,board)){
   	    	board[move] = human;  //找到人类下一步获胜位置 
   	    	found = winner(board) == human;
   		    board[move] = EMPTY ;
   	      }
   	    if(!found){
   		    ++move ;
   	      }
      }
   } 
   //3.否则在剩下空格选最优的方格 
   if(!found){ 
   	 move = 0;
   	 unsigned int i = 0;
     const int BEST_MOVES[] ={4,0,2,6,8,1,3,5,7};//空格优先度，中间最优，角落次优 
   	 while(!found  && i < board.size()){
           move =BEST_MOVES[i];
   	       if(isLegal(move,board))
			 {
        	   found = true ;
             } 
             ++i; 
   	   }
    }
    cout<<"computer choice move:"<<move<<endl;
	return move;
}
void announceWinner(char winner , char computer, char human)
{

	if(winner == computer)
	{
		cout<<"computer winner!\n";
	}
	else if(winner == human)
	{
		cout<<"human winner!\n";
	}
	else
	{
		cout<<"Not winner!\n";
	}
}
