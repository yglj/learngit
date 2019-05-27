package one.game.com;

import java.awt.*;
/**
 * 游戏窗口类
 * @author Administrator
 *
 */

@SuppressWarnings("serial")
public class frame0 extends Myframe {
	Image imge = GetImage.getImage("src/sun.jpg");
	private double x = 100,y = 100;
	private double degree = 3.14/3;
	@Override
	public void paint(Graphics g) {
		System.out.println("paint!");
		g.drawImage(imge, (int)x, (int)y, null);
		x = 100 + 100*Math.cos(degree);  //椭圆轨迹
		y = 200 + 50*Math.sin(degree);
		degree +=0.1;
//		private double speed = 10;
//		if(speed >0){  //任意角度飞行
//			speed -= 0.01;
//		}
//		else{
//			speed =0;
//		}
//		x += speed*Math.cos(degree);
//		y += speed*Math.sin(degree);
//		if(x < 0 || x > 500 -30){
//			degree = Math.PI - degree;
//			degree = -degree;
//		}
//		if(y < 30 || y > 500 -30){
//			degree = -degree;
//		}
//		Font font = new Font("正楷",Font.BOLD, 30); //画笔基本操作
//		g.setFont(font);
//		g.drawLine(100, 100, 200, 200);
//		g.drawRect(100, 100, 200, 200);
//        g.drawOval(100, 100, 200, 200);
//		g.drawString("(x,y)", 200, 200);
//		Color color = g.getColor();
//		g.setColor(Color.green);
//		g.fillRect(100, 100, 20, 20);
//		g.setColor(color);
//		g.fillOval(200, 200, 20, 20);

// 	private boolean left,up ; //上下移动
//		if (left) {
//			x -= 10;
//		} else {
//			x += 10;
//		}
//		if (x > 500 - 30) {
//			left = true;
//		}
//		if (x < 0) {
//			left = false;
//		}
//		if (y < 0) {
//			up = false;
//		}
//		if (up) {
//			y -= 10;
//		} else {
//			y += 10;
//		}
//		if (y > 500 - 30) {
//			up = true;
//		}
//		if (y < 30) {
//			up = false;
//		}
	}

	public static void main(String[] args) {
		frame0 w = new frame0();
		w.launchFrame();
	}
}

