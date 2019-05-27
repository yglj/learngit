package game.test;

import java.awt.Image;
import java.awt.Rectangle;

public class GameObject {
	Image img;
	double x,y;
	double speed = 3;
	int imgWidth,imgHeight;
	public Rectangle getRect(){
		return new Rectangle((int)x+imgWidth,(int)y+imgHeight,imgWidth,imgHeight);
	}
}
