class Example
{
	public static void main(String args[])
	{
      		try
		{
         		//int arr[]=new int[7];
         		//arr[4]=30/0;  //arr[10]=30/0;
			String str = null;  
			System.out.println("Length of the string:"+str.length());
      			System.out.println("Last Statement of try block");
      	}
      	catch(ArithmeticException e)
	{
         	System.out.println("You should not divide a number by zero");
      	}
      	catch(ArrayIndexOutOfBoundsException e)
	{
        	System.out.println("Accessing array elements outside of the limit");
      	}
      	catch(Exception e)
	{
         	System.out.println("Some Other Exception");
      	}
      	System.out.println("Out of the try-catch block");
   	}
}
