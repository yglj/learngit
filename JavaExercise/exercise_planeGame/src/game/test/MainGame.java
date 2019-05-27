package game.test;

import java.awt.Color;
import java.awt.Graphics;
import java.awt.Image;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;
import java.util.ArrayList;
import java.util.Date;

import tool.GetImage;
import tool.Myframe;
import tool.constant;

@SuppressWarnings("serial")
public class MainGame extends Myframe{
	Image bg = GetImage.getImage("res/bg.jpg");
	Plant plant = new Plant("res/plane.png",constant.Width/4,constant.Height/2);
	ArrayList<Bullet> bulletsList = new ArrayList<>();
	boolean live = true;
	Explode explode;
	long livetime;
	long endtime;
	long starttime =new Date().getTime() ;
	public void paint(Graphics g){
		//g.drawImage(bg,0,0,null);
		printInfo("Time:"+(float)livetime/10+"s",20, 60, g,Color.yellow, 30);
		if(live){
			plant.draw(g);
		    endtime = new Date().getTime();
		    livetime = ((endtime-starttime)/100);
		}
		else{
			printInfo("Game over",150, 300, g,Color.GRAY, 50);
			switch ((int)livetime/100) {
			case 0:	
				printInfo("111",200, 400, g,Color.BLUE, 50);
				break;
			case 1:
				printInfo("233",200, 400, g,Color.BLUE, 50);
				break;
			case 2:
				printInfo("666",200, 400, g,Color.BLUE, 50);
				break;
			default:
				break;
			}
		}
		for (int i=0;i<bulletsList.size();i++) {
			Bullet bullet = (Bullet)bulletsList.get(i);
			bullet.draw(g);
			bullet.move();
			if(plant.getRect().intersects(bullet.getRect())){  //Åö×²¼ì²â
				live = false;
				if(explode == null){
				explode = new Explode(plant.x,plant.y);
				}
				explode.draw(g);
				break;
			}
		}
	}
	@Override
	public void launchFrame() {
		for (int i = 0; i <= 50; i++) {
			Bullet bullet = new Bullet();
			bulletsList.add(bullet);
		}
		super.launchFrame();
		addKeyListener(new GetKeyBoard());
	}
	class GetKeyBoard extends KeyAdapter{   //Get¼üÅÌ°´¼üÏûÏ¢Àà
	    public void keyPressed(KeyEvent key) {
	    	plant.direction(key);
	    	plant.move();	    	
	    }
	    public void keyReleased(KeyEvent key) {
	    	plant.direction_F(key);
	    	plant.move();
	    }	
	}
	public static void main(String[] args) {
		MainGame m = new MainGame();
		m.launchFrame();
	}
}
