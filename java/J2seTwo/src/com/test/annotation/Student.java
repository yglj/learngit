package com.test.annotation;

@myannotation01("tb_student")
public class Student {
	@SuppressWarnings("unused")
	private int i;
	@myField(name="ID",type="varchar",length=32)
	private int id;
	@myField(name="sname",type="varchar",length=10)
	private String student;
	@myField(name="age",type="int",length=3)
	private int age;
	public int getId() {
		return id;
	}
	public void setId(int id) {
		this.id = id;
	}
	public String getStudent() {
		return student;
	}
	public void setStudent(String student) {
		this.student = student;
	}
	public int getAge() {
		return age;
	}
	public void setAge(int age) {
		this.age = age;
	}
}
