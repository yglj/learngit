
import java.io.*;
public class Print {

	public static void main(String[] args) throws IOException{
       PrintStream ps = new PrintStream(new FileOutputStream("temp1.txt"));
       PrintWriter pw = new PrintWriter(new OutputStreamWriter(new FileOutputStream("temp2.txt")));
	
	 ps.print("PrintStream print \r\n");
	 ps.println("PrintStream print again");
	 ps.flush();
	 
	 pw.println("PrintWriter print");
	 pw.flush();
	 
	 ps.format("%f,%d,%s", 1.1f,2,"String");
	 System.out.format("%f,%d,%s", 1.1f,2,"String");
	 ps.close();
	 pw.close();
	}

}
