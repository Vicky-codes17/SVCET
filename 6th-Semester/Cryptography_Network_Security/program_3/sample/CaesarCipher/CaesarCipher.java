import java.util.Scanner;

public class CaesarCipher {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter plain text: ");
        String text = sc.nextLine().toUpperCase();

        System.out.print("Enter key value: ");
        int key = sc.nextInt();

        String encrypted = "";
        String decrypted = "";

        for (int i = 0; i < text.length(); i++) {
            char ch = text.charAt(i);
            encrypted += (char) ((ch - 'A' + key) % 26 + 'A');
        }

        for (int i = 0; i < encrypted.length(); i++) {
            char ch = encrypted.charAt(i);
            decrypted += (char) ((ch - 'A' - key + 26) % 26 + 'A');
        }

        System.out.println("Encrypted Text: " + encrypted);
        System.out.println("Decrypted Text: " + decrypted);
    }
}
