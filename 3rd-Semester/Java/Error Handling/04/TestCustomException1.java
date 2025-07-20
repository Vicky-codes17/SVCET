class AgeException extends Exception {
    AgeException(String s) {
      super(s);
    }
  }
  
  class TestCustomException1 {
    static void validate(int age) throws AgeException {
      if (age < 18)
        throw new AgeException("not valid");
      else
        System.out.println("welcome to vote");
    }
  
    public static void main(String args[]) {
      try {
        validate(19);
      } catch (Exception m) {
        System.out.println("Exception occurred: " + m);
      }
      System.out.println("rest of the code...");
    }
  }