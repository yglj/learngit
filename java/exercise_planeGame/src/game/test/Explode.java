package game.test;

import java.awt.Graphics;
import java.awt.Image;
import java.util.ArrayList;

import tool.GetImage;

public class Explode {
	double x,y;
	static ArrayList<Image> explode = new ArrayList<>();
	public Explode(double x,double y) {
		for (int i = 1; i < 17; i++) {
			explode.add(GetImage.getImage("explode/e"+i+".gif"));
		}
		this.x = x;
		this.y = y;
	}
	public void draw(Graphics g) {
		for (int i = 0; i < 16; i++) {
			g.drawImage(explode.get(i), (int)x, (int)y, null);
		}
	}
}
