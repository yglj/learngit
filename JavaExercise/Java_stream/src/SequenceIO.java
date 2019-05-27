import java.io.*;
public class SequenceIO {
    public static void main(String [] args)throws IOException{
    	
    FileInputStream f1 = new  FileInputStream("C:\\Users\\Administrator\\Desktop\\1.txt");
    FileInputStream f2 = new  FileInputStream("temp.txt");
    SequenceInputStream sis = new SequenceInputStream(f1,f2);
    int c;
    while((c = sis.read()) != -1){
    	System.out.print((char)c);
    }
    System.out.println();
    f1.close();
    f2.close();
    sis.close();
    
    }
}
