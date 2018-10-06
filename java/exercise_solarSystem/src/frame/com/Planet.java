package frame.com;

import java.awt.Color;
import java.awt.Graphics;
import java.awt.Image;
import tool.GetImage;
/**
 * 行星类
 * @author Administrator
 *
 */
public class Planet extends Star {
	Star center;
	double longAxis,shortAxis;
	double speed,degree;
	boolean sateillate;
// 除了图片，坐标，行星沿着椭圆轨迹运行：长轴，短轴，速度，角度，绕着某个Star飞
	

	Planet(double x, double y, String imgespath) {
		super(x,y,imgespath);
	}

	Planet(double x, double y, Image image) {
		//super(x, y, image);
	}
    	
	Planet(Star center,String imagespath, double longAxis, double shortAxis, double speed) {		
		super(GetImage.getImage(imagespath));
		this.x = center.x + longAxis;
		this.y = center.y;
		this.center = center;
		this.longAxis = longAxis;
		this.shortAxis = shortAxis;
		this.speed = speed;
	}

	Planet(Star center,String imagespath, double longAxis, double shortAxis, double speed, boolean sateillate) {
		this(center, imagespath, longAxis, shortAxis, speed);
		this.sateillate = sateillate;
	}

	@Override
	void draw(Graphics g) {
		move();
		paintTrack(g);
		super.draw(g);
	}
	void move(){
		x = (center.x-center.imgWidth/2) + longAxis*Math.cos(degree);
		y = (center.y-center.imgHeight/2) + shortAxis*Math.sin(degree);
		degree += speed;
	}
	void paintTrack(Graphics g){
		if(!sateillate){
		Color c = g.getColor();
		g.setColor(Color.red);
		g.drawOval((int)(center.x-longAxis), (int)(center.y-shortAxis), (int)longAxis*2, (int)shortAxis*2);
		g.setColor(c);
		}
	}

}
