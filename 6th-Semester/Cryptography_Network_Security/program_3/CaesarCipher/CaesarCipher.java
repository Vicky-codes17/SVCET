import java.util.Scanner;

public class CaesarCipher {
    static String encrypt(String text, int key) {
       String result = "";
       for(char ch : text.toCharArray()) {
            if (Character.isUpperCase(ch)) {
                result += (char) ((ch - 'A' + key) % 26 + 'A');
            } else if (Character.isLowerCase(ch)) {
                result += (char)((ch - 'a' + key) % 26 + 'a');
            } else {
                 result += ch; // Non-alphabetic characters are unchanged
            }
         }
         return result;
    }
    static String decrypt(String text, int key) {
        return encrypt(text, 26 - key);
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter plain text: ");
        String text = sc.nextLine();

        System.out.print("Enter key value: ");
        int key = sc.nextInt();

        String encrypted = encrypt(text, key);
        System.out.println("Encrypted Text: " + encrypted);

        System.out.println("Decrypted Text: " + decrypt(encrypted, key));
    }
}