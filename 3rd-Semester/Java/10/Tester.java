class Shape
{
	public void display() 
	{
      		System.out.println("Inside shape class");
   	}
}
class Rectangle extends Shape 
{
   	public void area() 
	{
      		System.out.println("Inside Rectangle class");
   	}
}
class Cube extends Rectangle 
{
	public void volume() 
	{
      		System.out.println("Inside Cude class");
   	}
}
public class Tester 
{
   	public static void main(String[] arguments) 
	{
      		Cube cube = new Cube();
      		cube.display();
      		cube.area();
      		cube.volume();
   	}
}
