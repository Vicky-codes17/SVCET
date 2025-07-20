public class ConstructorExample 
{
    	int id;
    	String name;
    // Constructor with no arguments
    	public ConstructorExample() 
	{
        	id = 10;
        	name = "Svcet";
        	System.out.println("Default constructor called");
    	}
    // Constructor with arguments
    	public ConstructorExample(int i, String n) 
	{
        	id = i;
        	name = n;
        	System.out.println("Parameterized constructor called");
    	}
	public void display() 
	{
        	System.out.println("Id: " + id);
        	System.out.println("Name: " + name);
    	}
    	public static void main(String[] args) 
	{
      // Creating objects using different constructors
        	ConstructorExample obj1 = new ConstructorExample();
        	obj1.display();

        	ConstructorExample obj2 = new ConstructorExample(20, "Svcet-Chittoor");
        	obj2.display();
    	}
}
