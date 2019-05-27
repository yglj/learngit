package com.test.map;

import java.util.LinkedList;

import javax.imageio.ImageTypeSpecifier;

/**
 * 
 * @author Administrator
 * key - value 
 * 利用 hashcode（）提高查询效率
 * map 的底层实现   数组+链表
 */
public class MapTest {
	public static void main(String[] args) {
		mymap  m = new mymap();
		m.put("1", 1);
		m.put("2",2);
		m.put("1",111);
		System.out.println(m.get("1"));
	}
}
class mymap{                        //利用hashcode（）实现
	@SuppressWarnings("rawtypes")
	private LinkedList array[] = new LinkedList[100];
	public void put(Object key , Object value){
		int h = key.hashCode() % array.length;
		Kv  kv = new Kv(key, value);
		if(array[h] == null){
			LinkedList list = new LinkedList();
			array[h] = list;
			list.add(kv);

		}else{
			LinkedList list = array[h];
			for (int i = 0 ; i< array[h].size() ;i++) {
				if(((Kv)array[h].get(i)).key.equals(key)){
					((Kv)list.get(i)).value = value;
					
				}
			}
		}
	}
	public Object get(Object key){
		int h = key.hashCode() % array.length;
			LinkedList list = array[h];
			for (int i = 0 ; i< array[h].size() ;i++) {
				Kv k = (Kv) list.get(i);
				if(k.key.equals(key)){
					return k.value;
				}
			}
		return null;
	}

}
class mymap0{                        //根据键找值
	Kv array[] = new Kv[100];
	private int size;
	public void put(Object key , Object value){
		for (int i = 0; i<size ; i++) {   //解决键值重复问题
			if(array[i].key.equals(key)){
				array[i].value = value;
				return ;
			}
		}
		array[size++] = new Kv(key,value);
	}
	public Object get(Object key){
		for (Kv i : array) {
			if(i.key.equals(key)){
				return i.value;
			}
		}
		return null;
	}
	public boolean containsKey(Object key){
		for (int i = 0; i<size ; i++) {
			if(array[i].equals(key)){
				return true;
			}
		}
		return false;
	}
}
class Kv{
	Object key;
	Object value;
	public Kv(Object key, Object value) {
		this.key = key;
		this.value  = value;
		// TODO Auto-generated constructor stub
	}
}