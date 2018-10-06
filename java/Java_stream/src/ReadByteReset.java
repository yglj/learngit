import java.io.*;
public class ReadByteReset {
	 public static void main(String [] args)throws IOException{
     BufferedInputStream is = new BufferedInputStream(new FileInputStream("C:\\Users\\Administrator\\Desktop\\1.txt"));
     System.out.println("文件长度："+(is.available()) );
     int b ;
     
     is.mark(10);
     while((b = is.read()) != -1){
    	// System.out.print(" "+b); 	     
     }
     System.out.print("\nread again:");
     is.reset();
     while((b = is.read()) != -1){
    	 System.out.print((char)b); 	     
     }
     
     is.reset();
     is.skip(200);
     
     System.out.print("\nreset:");   
     
     while((b = is.read()) != -1){
    	 System.out.print((char)b); 	     
     }
     is.close();
  }
}