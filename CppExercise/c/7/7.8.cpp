# include <stdio.h>
int main()
{
	void hanoi (int n,char one ,char two,char there);
	int m; 
	printf("input the  number of dislike\n:");
	scanf("%d",&m);
	printf("The step to move %d dislikes£º\n",m);
	hanoi(m,'A','B','C');
	
	
} 
void hanoi(int n,char one,char two, char there)
{void move(char x,char y);
if(n==1)
move(one,there);
else
{hanoi(n-1,one,there,two);
move(one,there);
hanoi(n-1,two,one,there);
}

}
void move(char x,char y)
{printf("%c->%c\n",x,y);
} 
