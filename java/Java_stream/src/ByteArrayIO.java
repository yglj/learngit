
import java.io.*;
public class ByteArrayIO {
@SuppressWarnings("resource")
public static void main(String[] args)throws IOException {
	String s="这是一个String";
	ByteArrayOutputStream bao=new ByteArrayOutputStream();
	bao.write(s.getBytes());
	System.out.println(bao.toString());
	bao.close();
	FileInputStream fin=new FileInputStream("C:\\Users\\Administrator\\Desktop\\1.txt");
	bao.close();
	int c=0;
	while((c=fin.read())!=-1){
		bao.write(c);
		
		
	}
	System.out.println("长度"+bao.size());
	System.out.println(bao.toString());
	bao.close();

	byte buf[]=s.getBytes("GBK");
	ByteArrayInputStream bai=new ByteArrayInputStream(buf);
	byte t[]=new byte[100];
	while((c=bai.read(t))>-1){
		System.out.println(new String(t,0,c));
		
	}
	bai.close();
}
}