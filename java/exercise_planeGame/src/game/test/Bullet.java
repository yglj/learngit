package game.test;

import java.awt.Color;
import java.awt.Graphics;
import java.awt.Rectangle;
import java.util.Random;

import tool.constant;

public class Bullet extends GameObject{
	double degree;
	public Bullet(){
		this.x = constant.Width/2;
		this.y = constant.Height/2;
		degree =  new Random().nextFloat()*Math.PI*2;
	}
	public Bullet(double x,double y,double speed){
		this();
	}
	public void draw(Graphics g){
		Color c = g.getColor();
		g.setColor(Color.red);
		g.fillOval((int)x,(int)y,8,8);
		g.setColor(c);
	}
	public void move(){
		if (x<8 || x>600-16) {
			degree = Math.PI-degree;
		}
		if (y<30 || y>600-16) {
			degree = -degree;
		}
		x = x+speed*Math.cos(degree);
		y = y+speed*Math.sin(degree);
	}
	public Rectangle getRect(){
		return new Rectangle((int)x+8,(int)y+8,8,8);
	}
}
