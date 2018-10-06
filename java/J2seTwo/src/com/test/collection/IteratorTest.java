package com.test.collection;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Iterator;
import java.util.List;
import java.util.Map;

public class IteratorTest {
	public static void main(String[] args) {
		Map<String,String> map = new HashMap<String,String>();
		map.put("1", "1");
		map.put("2", "2");
		map.put("3", "3");
		map.put("4", "4");
		map.put("5", "5");
		
		List list = new ArrayList();
		for(int i = 0 ; i<map.size() ; i++){
			System.out.println(i+":"+list.add(map.get(i+1+"") ) ); 
		}
		
		for(Iterator iter = list.iterator();iter.hasNext();){
			System.out.println(iter.next());
		}
		
	}
}
