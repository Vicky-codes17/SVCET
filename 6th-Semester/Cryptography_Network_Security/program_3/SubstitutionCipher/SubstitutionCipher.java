import java.util.Scanner;

public class SubstitutionCipher {
    static String plain = "abcdefghijklmnopqrstuvwxyz";
    static String cipher   = "qwertyuiopasdfghjklzxcvbnm";

    static String encrypt(String text) {
        text = text.toLowerCase();
        String result = "";
        for (char ch : text.toCharArray()) {
            if (plain.indexOf(ch) != -1)
                result += cipher.charAt(plain.indexOf(ch));
            else
                result += ch; // Non-alphabetic characters are unchanged
        }
        return result;
    }
    static String decrypt(String text) {
        String result = "";
        for (char ch : text.toCharArray()) {
            if (cipher.indexOf(ch) != -1)
                result += plain.charAt(cipher.indexOf(ch));
            else
                result += ch; // Non-alphabetic characters are unchanged
    }
        return result;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter plain text: ");
        String text = sc.nextLine();   

        String encrypted = encrypt(text);
        System.out.println("Encrypted text: " + encrypted);
        
        System.out.println("Decrypted text: " + decrypt(encrypted));
    }
}