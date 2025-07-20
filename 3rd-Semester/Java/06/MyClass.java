public class MyClass 
{
    // Method to display a message
    	public void displayMessage() 
	{
        	System.out.println("Hello from a method!");
    	}

    // Method to calculate the sum of two numbers
    	public int calculateSum(int a, int b) 
	{
        	return a + b;
    	}
    	public static void main(String[] args) 
	{
     // Create an object of the MyClass
        	MyClass obj = new MyClass();
      // Calling methods using object
        	obj.displayMessage();
        	int num1 = 10, num2 = 20;
        	int sum = obj.calculateSum(num1, num2);
        	System.out.println("Sum of " + num1 + " and " + num2 + " is: " + sum);
    	}
}
