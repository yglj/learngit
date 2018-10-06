
import java.io.*;
public class FileCharIO {

	public static void main(String[] args) throws IOException{
         
		File file = new File("FileCharIO.java");
		FileReader fr = new FileReader(file);
		FileWriter fw = new FileWriter("FileCharIO(1).java");
		
		char b[] = new char[100];
		int count = 0;
		while((count = fr.read(b,0,100)) != -1)
            fw.write(b,0,count);
		
		fr.close();
		fw.flush();
		fw.close();
	}

}
