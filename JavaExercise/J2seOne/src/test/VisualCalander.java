package test;

import java.text.DateFormat;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.Date;
import java.util.GregorianCalendar;
import java.util.Scanner;


public class VisualCalander {
	public static void main(String[] args){
		System.out.println("请输入日期（格式：yyyy.MM.dd）：");
	    Scanner scanner = new Scanner(System.in);
		String  str = scanner.nextLine();
		try {

			DateFormat format = new SimpleDateFormat("yyyy.MM.dd");
			Date date = format.parse(str);
			Calendar calendar = new GregorianCalendar();
			calendar.setTime(date);
			calendar.set(calendar.DATE, 1);
		//	System.out.println(calendar.get(calendar.DAY_OF_WEEK));
			System.out.println("日\t一\t二\t三\t四\t五\t六");
	        for (int j =1 ;j <calendar.get(calendar.DAY_OF_WEEK); j++) {
					System.out.print("\t");
				}

			for(int i = 1 ; i<= calendar.getActualMaximum(calendar.DAY_OF_MONTH) ; i++){		
				System.out.print(i+"\t");
                int day  = calendar.get(calendar.DAY_OF_WEEK);

				if(day == calendar.SATURDAY){
					System.out.println();
				}
				calendar.add(calendar.DATE, 1);
			}
		} catch (ParseException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

	}
}
