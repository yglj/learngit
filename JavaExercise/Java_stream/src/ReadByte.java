import java.io.*;
public class ReadByte {
	 public static void main(String [] args)throws IOException{
     InputStream is = new FileInputStream("C:\\Users\\Administrator\\Desktop\\1.txt");
     System.out.println("文件长度："+(is.available()) );
       int b = is.read();
       System.out.print(" "+b);
     while((b = is.read()) != -1){
    	 b = is.read();
    	 System.out.print(" "+b); 	 
     }
     is.close();
  }
}