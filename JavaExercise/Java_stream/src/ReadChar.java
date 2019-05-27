
import java.io.*;
public class ReadChar {

	public static void main(String[] args) throws IOException{
       int b;
		Reader is = new FileReader("C:\\Users\\Administrator\\Desktop\\1.txt");

		while((b = is.read()) != -1){
		        System.out.print((char)b);
		}
                is.close();
	}

}
