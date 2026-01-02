import java.util.Scanner;

public class SubstitutionCipher {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        String key    = "QWERTYUIOPASDFGHJKLZXCVBNM";

        System.out.print("Enter plain text: ");
        String plainText = sc.nextLine().toUpperCase();

        String encrypted = "";
        String decrypted = "";

        for (int i = 0; i < plainText.length(); i++) {
            encrypted += key.charAt(normal.indexOf(plainText.charAt(i)));
        }

        for (int i = 0; i < encrypted.length(); i++) {
            decrypted += normal.charAt(key.indexOf(encrypted.charAt(i)));
        }

        System.out.println("Encrypted Text: " + encrypted);
        System.out.println("Decrypted Text: " + decrypted);
    }
}
