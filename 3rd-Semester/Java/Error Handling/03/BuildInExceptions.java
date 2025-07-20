
class BuildInExceptions {
  public static void main(String args[]) {
    try {
      // int a = 30, b = 1;
      // int c = a / b;
      // System.out.println("Result = " + c);
      
      // int[] arr = new int[5];
      // arr[10] = 9;
      
      // File file = new File("file.txt");
      // FileReader fr = new FileReader(file);
      
      // String str = null; 
      // System.out.println(str.charAt(0));
      
      // int num = Integer.parseInt("akki");
      // System.out.println(num);
      
      String str1 = "This is like chipping "; 
      char x = str1.charAt(24); 
      System.out.println(str1);
    } 
    //  catch (ArithmeticException e) {
    //   System.out.println("Can't divide a number by 0");
    // }
    //  catch (ArrayIndexOutOfBoundsException e) {
    //   System.out.println("Array Index is Out Of Bounds");
    // }
    //  catch (FileNotFoundException e) {
    //   System.out.println("File does not exist");
    // }
    //  catch (NullPointerException e) {
    //   System.out.println("NullPointerException..");
    // }
    //  catch (NumberFormatException e) {
    //   System.out.println("Number format exception");
    // }
     catch (StringIndexOutOfBoundsException e) {
      System.out.println("StringIndexOutOfBoundsException");
    }
    System.out.println("Out of the try-catch block");
  }
}