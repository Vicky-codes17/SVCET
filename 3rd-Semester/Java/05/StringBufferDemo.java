public class StringBufferDemo
{
	public static void main(String[] args) 
	{
     // To delete a character in string
		StringBuffer sb = new StringBuffer("Java Programming");  
        	System.out.println("string: " + sb);  
     // deleting the character at index 4  
        	sb = sb.deleteCharAt(4);  
        	System.out.println("After deleting: " + sb);  

     //To delete a string from the given string
      		StringBuffer sb1 = new StringBuffer("Welcome to Java Programming");
      		System.out.println("Before deletion the string is: " + sb1);
     //initialize the startIndex and endIndex values
      		int startIndex = 11;
      		int endIndex = 16;
      		System.out.println("The startIndex and endIndex values are: " + startIndex + " and " + endIndex);
      //using the delete() method
      		StringBuffer new_str = sb1.delete(startIndex, endIndex);
      		System.out.println("After deletion the remaing string is: " + new_str);
	}
}
