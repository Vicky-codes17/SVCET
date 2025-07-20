public class StringBuffer
{
  public static void main(String args[])
   {
	//To delete a character in string
	StringBuffer sb = new_StringBuffer("Java Programming");
	System.out.println("string: " +sb);

	//deleting the character at index 4
	sb = sb_deleteCharAt(4);
	System.out.println("After deleting: "+sb);

        //To delete a string from thhe given string

	StringBuffer sb1 = new_StringBuffer("Welcome to Java Programming");
	System.out.println("Before deletion the strings is: " +sb1);

	//initialize the startIndex and endIndex values
	int startIndex = 11;
	int endIndex = 16;
	System.out.println("The startIndex and endIndex values are : "+startIndex+" and "+endIndex);
	//usig the delete() method

	StringBuffer new_str = sb1.delete(startIndex,endIndex);
	System.out.println("After deletion the remaing string is: " + new_str);
   }
}