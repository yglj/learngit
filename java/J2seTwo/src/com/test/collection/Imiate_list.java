package com.test.collection;



public class Imiate_list {
	private Object[] elementDate;
	private int size ;
	
	public Imiate_list(){
		this(3);
	}
	public Imiate_list(int capacity){
		elementDate = new Object[capacity];
	}
	
	public int size(){
		return size;
	}
	
	public void add(Object obj){
		elementDate[size++] = obj;
		ensureCapacity();
	}
	
	public void add(int index , Object obj){
		size++;
		RangeCheck(index);
		ensureCapacity();
		for (int i = size ; i >= index; i--) {
			elementDate[i+1] = elementDate[i];
		}
//		for (int i = index ; i <=size; i++) {
//		elementDate[i+1] = elementDate[i];
//	}
		elementDate[index] = obj;
	}
	public Object set(int index,Object obj){
		RangeCheck(index);
		Object old = elementDate[index];
		elementDate[index] = obj;
		return old;
	}
	
	public void get(int index){
		RangeCheck(index);
		System.out.println(elementDate[index]);;
	}

	public boolean remove(int index){
		RangeCheck(index);
		for (int i = index; i <= size; i++) {
			elementDate[i] = elementDate[i + 1];
		}
		size--;
		return true;
	}
	
	public boolean remove(Object obj){
		for (int i = 0; i < elementDate.length; i++) {
			if (obj.equals(elementDate[i])) {
				remove(i);
				break;
			}
		}
		return true;
	}
	private void RangeCheck(int index)  {
		if(index >= size){
			try {
				throw new Exception("bundary");
			} catch (Exception e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}
	}
	
	private void ensureCapacity(){
		if (size >= elementDate.length) {
			Object new_arr[] = new Object[2*elementDate.length +1];
			System.arraycopy(elementDate, 0, new_arr, 0,elementDate.length);
			elementDate = new_arr;
		}
	}
	public void capacity(){
		System.out.println("capacity:"+elementDate.length);
	}
	
	
	public static void main(String[] args){
		System.out.println("begin:");
		Imiate_list mylist = new Imiate_list();
		mylist.add('a');
		mylist.add(2);
		mylist.add(1,"bb");
		mylist.capacity();
		mylist.add(true);
		for (int i=0 ; i<mylist.size() ; i++) {
			mylist.get(i);
		}

		System.out.println("size:"+mylist.size());
		System.out.println("------------------");
		System.out.println("three element:");
		System.out.println("now was replaced thired element is "+mylist.set(2, 'B'));
		mylist.get(2);
		System.out.println("------------------");
		System.out.println("now delete frist element "+mylist.remove(0));
		System.out.println("size:"+mylist.size());
		mylist.remove(true);
		for (int i=0 ; i<mylist.size() ; i++) {
			mylist.get(i);
		}
		System.out.println("size:"+mylist.size());
	}
}
