
import java.io.*;
public class WriterAppend {

	public static void main(String[] args) throws IOException{
        BufferedWriter bw = null;
		String s ="Hello";
		bw = new BufferedWriter(new FileWriter("temp.txt"));
		bw.write(s);
		bw.newLine();
		bw.append(s+"World!");
		bw.close();
	}

}
