package tool;
import java.awt.Image;
import java.awt.image.BufferedImage;
import java.net.URL;

import javax.imageio.ImageIO;
/**
 * 加载图片工具类
 * @author Administrator
 *
 */
public class GetImage {
	public static Image getImage(String path){
		URL url = GetImage.class.getClassLoader().getResource(path);
		BufferedImage b = null;
		try {
			b = ImageIO.read(url);
		} catch (Exception e) {
			e.printStackTrace();
		}
		return b;
	}
}
