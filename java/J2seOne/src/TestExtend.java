class Anmial{
	int foot;
	public void sleep(){
		System.out.println("睡觉");
	}
	public void eat(){
		System.out.println("吃饭");
	}
}
class Dog extends Anmial{  //继承
	public void brak(){
		System.out.println("汪汪....");
	}
}
class Cat extends Anmial{
	public void eat(){ 
		super.eat();  //调用父类被覆盖的方法
		System.out.println("sisissi..."); //重写
	}
	public void say(){
		System.out.println("喵喵喵...");
	}
}
public class TestExtend {
	public static void main(String [] args){
		Cat c = new Cat();
		c.eat();  //子类自己的方法
		c.say(); //子类重写的方法
	}

}
