package test;

import java.util.Calendar;
import java.util.Date;
import java.util.GregorianCalendar;

public class TestDate {
	public static void main(String[] args) {
		Date date = new Date(1369971105691L);
		long l = System.currentTimeMillis();
		System.out.println(l);
		System.out.println(date.toString());
		Calendar calendar = new GregorianCalendar();
         calendar.set(Calendar.DATE,1);

	}
	
    @Deprecated
	public static  void function(int a){
		System.out.println(" ");
	}
}
