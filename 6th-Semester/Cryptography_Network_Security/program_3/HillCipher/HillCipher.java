import java.util.Scanner;

public class HillCipher {
    static int[][] key = {{5, 5}, {5, 5}};

    static String encrypt(String text) {
        text = text.toUpperCase();
        if (text.length() % 2 != 0) {
            text += 'X'; // Padding if odd length
        }
        String cipherText = "";

        for (int i = 0; i < text.length(); i += 2) {
            int x = text.charAt(i) - 'A';
            int y = text.charAt(i + 1) - 'A';

        int c1 = (key[0][0] * x + key[0][1] * y) % 26;
        int c2 = (key[1][0] * x + key[1][1] * y) % 26;

        cipherText += (char) (c1 + 'A');
        cipherText += (char) (c2 + 'A');
    }
    return cipherText;

}
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter plain text (UPPERCASE): ");
        String text = sc.nextLine();

        System.out.println("Encrypted Text: " + encrypt(text));
    }
}