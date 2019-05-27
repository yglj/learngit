
import java.io.*;
public class ReadCharArray {

	public static void main(String[] args) throws IOException{
        int n;
		Reader is = new FileReader("C:\\Users\\Administrator\\Desktop\\1.txt");
        char b[] = new char[100];
		if(is.ready()){
			while((n = is.read(b)) >  -1){
		        System.out.print(new String(b,0,n));
			}
		}
                is.close();
	}

}
