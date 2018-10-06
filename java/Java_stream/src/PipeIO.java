import java.io.*;
public class PipeIO {
   public static void main(String [] args) throws IOException{
	 final  PipedOutputStream pos = new PipedOutputStream();
	 final PipedInputStream pis = new PipedInputStream(pos);
	   
	   Thread t1 = new Thread( new Runnable(){
		   
		   public void run(){
			   try{
				   pos.write("Hello!".getBytes());
			   }
			   catch(IOException ioe){
				   ioe.toString();
			   }
		   }
	   });

	   Thread t2 = new Thread( new Runnable(){
		   
		   public void run(){
			   try{
				   int c;
				   while( (c = pis.read()) != -1){
					   System.out.print((char)c);
				   }
			   }
			   catch(IOException ioe){
				   ioe.toString();
			   }
		   }
	   });
	   
	   t1.start();
	   t2.start();
	   
	   pis.close();
   }
}
