//Program to user input in Java
import java.util *;

class userinput
{
	public static void main(String args[])
	{
		scanner sc = new scanner(system.in);
		system.out.println("Enter value");
		int x = sc.nextInt();
		System.out.println("Enter value");
		int y = sc.nextInt();
		int z = x*y;
		System.out.println("The Total is " +z);
	}
}