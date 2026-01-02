import java.util.Scanner;

public class HillCipher {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int[][] key = {{3, 3}, {2, 5}};

        System.out.print("Enter plain text (2 letters): ");
        String text = sc.nextLine().toUpperCase();

        int[] msg = new int[2];
        for (int i = 0; i < 2; i++) {
            msg[i] = text.charAt(i) - 'A';
        }

        int[] cipher = new int[2];
        for (int i = 0; i < 2; i++) {
            cipher[i] = 0;
            for (int j = 0; j < 2; j++) {
                cipher[i] += key[i][j] * msg[j];
            }
            cipher[i] %= 26;
        }

        System.out.println("Encrypted Text:");
        for (int i = 0; i < 2; i++) {
            System.out.print((char) (cipher[i] + 'A'));
        }
    }
}
