import java.io.*;
public class ReadByteArray {
   public static void main(String [] args)throws IOException{
	   InputStream is = new FileInputStream("C:\\Users\\Administrator\\Desktop\\1.txt");
	   int n = is.available();
	   System.out.println("文件长度："+n);
	   byte b[] = new byte[100];
	   while((n = is.read(b)) != -1 ){
		   System.out.print(new String(b,0,n));
	   }
	   is.close();
   }
}
