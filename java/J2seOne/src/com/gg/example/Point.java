package com.gg.example;

public class Point {
	double x,y,z;
	public Point(double x, double y, double z){
		this.x = x;
		this.y = y;
		this.z = z;
	}
	public void setx(double x){
		this.x = x;
	}
	public void sety(double y){
		this.y = y;
	}
	public void setz(double z){
		this.z = z;
	}
	public double distance(Point p){
		return Math.sqrt((x - p.x)*(x - p.x)+(y - p.y)*(y - p.y)+(z - p.z)*(z - p.z));
	}
	public static void main(String [] args){
		Point p = new Point(2,3,5);
		p.setz(10);
		System.out.println(p.x+" "+p.y+" "+p.z);
		System.out.println(p.distance( new Point(2,3,5)));
	}
}
