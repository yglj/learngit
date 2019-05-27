package tool;

import java.awt.Frame;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;

import tool.constant;
/**
 * 框架结构类
 * @author Administrator
 *
 */
@SuppressWarnings("serial")
public class Myframe extends Frame {
	public void launchFrame(){  //加载窗口
		setSize(constant.Width, constant.Height);
		setLocation(100,100);
		setVisible(true);
		new PaintThread().start();  //启动重画线程
		addWindowListener(new WindowAdapter(){  //匿名类
			@Override       
			public void windowClosing(WindowEvent e) {
				System.exit(0);
			}
			
		});
	}
	
	class PaintThread extends Thread{ //内部类，刷新窗口的线程类
		public void run(){
			while(true){
				repaint();
				try {
					Thread.sleep(40);
				} catch (InterruptedException e) {
					e.printStackTrace();
				}
			}
		}
	}
}
