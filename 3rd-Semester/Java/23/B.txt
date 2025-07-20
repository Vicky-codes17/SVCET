import mypack.*;

public class B
{
	public void display()
	{
		System.out.println("Welcome again from Class B");
	}
	public static void main(String args[])
	{
		A obj1 = new A();
		obj1.show();

		B obj2 = new B();
		obj2.display();
	}
}