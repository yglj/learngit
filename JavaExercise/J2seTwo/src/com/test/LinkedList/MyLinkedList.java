package com.test.LinkedList;


public class MyLinkedList {
	private Node first ;
	private Node last ;
	private int size;
	
	public int size(){
		return size;
	}
	
	public void add(Object obj){
		Node n = new Node();
		n.data = obj;
		if(first == null){
			first = n;
			last = first;
		}
		else{
			last.next = n;
			n.previous = last;
			last = n;
		}
		size++;
	}
	
	public void add(int index,Object obj){ //不考虑插入first
		rangeCheck(index);
		Node n = node(index);
		Node p = new Node();
		p.data = obj;
		if(index == 0){
			n.previous = p;
			first = p;
			p.next = n;
		}
		else{
			Node up = n.previous;
			up.next = p;
			p.previous = up;
			n.previous = p;
			p.next = n;
			System.out.println("error:"+n.data);
		}
		size++;
	}
	
	public Object get(int index){
		rangeCheck(index);
		Node n = node(index);
		//System.out.println(n);
		return n.data;
	}
	
	public void remove(int index){
		rangeCheck(index);
		Node n = node(index);
		if(index == 0){
			if(first == last){
				first = null;
				last =null;
			}
			first = first.next;
			first.previous = null;
		}
		else if(index == size-1){
			if(first == last){
				first = null;
				last =null;
			}
			last.previous = last;
			last.next = null;
		}
		else{
			n.previous.next = n.next;
			n.next.previous = n.previous;
			n.next = null;
			n.previous = null;	
		}
		size--;
	}
	
	private Node node(int index){ //遍历节点
		rangeCheck(index);
		if(first != null){
			Node n = first;
			while(index > 0){
				n = n.next;  //改正 n = first.next
				index--;
			}
			return n;
		}
		return null;
	}
	
	private void rangeCheck(int index){
		if(index < 0 || index > size){
			try{
				throw new Exception("越界！");
			}catch(Exception e){
				e.printStackTrace();
			}
		}
	}
	
	class Node{
		Node previous;
		Object data ;
		Node next;
		public Node getPrevious() {
			return previous;
		}
		public void setPrevious(Node previous) {
			this.previous = previous;
		}
		public Object getData() {
			return data;
		}
		public void setData(Object data) {
			this.data = data;
		}
		public Node getNext() {
			return next;
		}
		public void setNext(Node next) {
			this.next = next;
		}	
	}
	public static void main(String[] args) {
		MyLinkedList m = new MyLinkedList();
		m.add("1");
		m.add("3");
		System.out.println("size:"+m.size());
		for (int i = 0; i < m.size(); i++) {
			System.out.println(m.get(i));
		}
		m.add(1,"2");
		m.add(0,"-3");
		
		System.out.println("size:"+m.size());
		for (int i = 0; i < m.size(); i++) {
			System.out.println(i+": "+m.get(i));
		}
		
		System.out.println("----------------");
		m.remove(2);//remove(begin) remove(end)
		System.out.println("size:"+m.size());
		for (int i = 0; i < m.size(); i++) {
			System.out.println(i+": "+m.get(i));
		}
		
	}
}