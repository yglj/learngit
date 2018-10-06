
import java.util.Scanner;

/**
 * 小游戏综合练习：猜单词
 * @author Administrator
 *
 */
public class guess {
	//属性
	private int len;
	private char[] letter = new char[26];
	private char[] word;
	private int[] position = new int[26];
	private boolean flag = false;
	private int count = 0;
	char[] input;
	int score;
	public guess(int len) {  //生成26个字母
		this.len = len;
		word = new char[len];
		input = new char[len];
		score = len*100;
		for(int i=0 ; i<letter.length ; i++){
			letter[i] =(char)('a'+i);
		}
		// TODO Auto-generated constructor stub
	}
	public void setWord(){ //生成随机单词
		int index = 0;
		for(int i=0 ; i<len ; i++){
			do{
				index = (int) (Math.random()*26);
				if(position[index] == 1 ){
					//System.out.println(position[index]+"--"+index);
					flag = true;
				}
				else{
					flag = false;
				}
				word[i] = letter[index];
				position[index] = 1;
			}while(flag);
		}
		System.out.println(word);
	}
	public int check(char[] input){
		count = 0;
		for (int i = 0; i < len; i++) {
			if(word[i] == input[i]){
				count++;
			}
			else{
				score-=10;
			}
		}
		return count;
	}
	public void game(){
		int sum = 0;
		System.out.println("开始");
		Scanner s = new Scanner(System.in);
		while(true){
			sum++;
			setWord();
			do{		
				System.out.println("请输入"+len+"个字符：");
				input = s.next().toLowerCase().toCharArray();
			}while(input.length < len || input.length >5);
			check(input);
			System.out.println("猜对"+count+"个"+",猜错"+(len-count)+"个。");
			System.out.println("得分："+score+",一共猜了"+sum+"次。");
			System.out.println("是否继续（y/n）：");
			if(s.next().equals("n")){
				break;
			}
		}
	}
	
	public static void main(String[] args){
		guess g = new guess(5);
		g.game();
		
	}
}
