package frame.com;

import java.awt.Graphics;
import java.awt.Image;
import tool.GetImage;
import tool.Myframe;
import tool.constant;
/**
 * Ì«ÑôÏµ
 * @author Administrator
 *
 */
@SuppressWarnings("serial")
public class Solar extends Myframe{
	Image bg = GetImage.getImage("images/bg.jpg");
    Star sun = new Star(constant.Width/2, constant.Height/2, "images/sun.jpg");
    Planet earth = new Planet(sun,"images/Earth.jpg",150,100,0.1);
    Planet Mars = new Planet(sun, "images/Mars.jpg", 200, 150, 0.15);
    Planet moon = new Planet(earth,"images/moon.jpg", 30,20,0.1,true);
	@Override
	public void paint(Graphics g) {		
		g.drawImage(bg, 0, 0, null);
		sun.draw(g);
		earth.draw(g);
		Mars.draw(g);
		moon.draw(g);
	}

	public static void main(String[] args) {
		Solar solar = new Solar();
		solar.launchFrame();
	}
}
