package game.test;

import java.awt.Graphics;
import java.awt.event.KeyEvent;

import tool.GetImage;

public class Plant extends GameObject{
	boolean left,right,up,down; //Ïò°Ë·½ÒÆ¶¯
	public Plant() {
	}
	Plant(String imgpath, double x, double y) {
		super();
		img = GetImage.getImage(imgpath);
		this.x = x;
		this.y = y;
		imgWidth = img.getWidth(null);
		imgHeight = img.getHeight(null);
		}
	public void move(){
		if(left){
			x -= 10;
		}
		if(right){
			x += 10;
		}
		if(up){
			y -= 10;
		}
		if(down){
			y += 10;
		}
	}
	public void direction(KeyEvent key){
    	switch (key.getKeyCode()) {
		case KeyEvent.VK_LEFT:
			left = true;
			break;
		case KeyEvent.VK_RIGHT:
			right = true;
			break;
		case KeyEvent.VK_UP:
			up = true;
			break;
		case KeyEvent.VK_DOWN:
			down = true;
			break;
		default:
			break;
		}
	}
	public void direction_F(KeyEvent key){
    	switch (key.getKeyCode()) {
		case KeyEvent.VK_LEFT:
			left = false;
			break;
		case KeyEvent.VK_RIGHT:
			right = false;
			break;
		case KeyEvent.VK_UP:
			up = false;
			break;
		case KeyEvent.VK_DOWN:
			down = false;
			break;
		default:
			break;
		}
	}
	public void draw(Graphics g){
		g.drawImage(img,(int)x,(int)y,null);
	}
}
