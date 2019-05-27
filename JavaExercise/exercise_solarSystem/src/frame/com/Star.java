package frame.com;

import java.awt.Graphics;
import java.awt.Image;
import tool.GetImage;


/**
 * –«–«¿‡
 * @author Administrator
 *
 */
public class Star {
	double imgWidth,imgHeight;
	double x,y;
    Image image;
	public Star(){	
	}
	public Star(Image img){
		this.image = img;
		this.imgWidth = image.getWidth(null);
		this.imgHeight = image.getHeight(null);
	}
	public Star(double x, double y, Image image) {
		this.x = x;
		this.y = y;
		this.image = image;
	}
	public Star(double x, double y, String imgespath) {
		this.x = x;
		this.y = y;
		this.image = GetImage.getImage(imgespath);
	}
	void draw(Graphics g){
		x = x - imgWidth/2;
		y -= imgHeight/2;
		g.drawImage(image, (int)x, (int)y, null);
	}
	
}
