import javax.crypto.Cipher;
import javax.crypto.KeyGenerator;
import javax.crypto.SecretKey;

public class AESExample {
    public static void main(String[] args) throws Exception {
        String message = "Hello World";

        KeyGenerator keyGen = KeyGenerator.getInstance("AES");
        keyGen.init(128);

        SecretKey key = keyGen.generateKey();

        Cipher cipher = Cipher.getInstance("AES");

        cipher.init(Cipher.ENCRYPT_MODE, key);
        byte[] encrypted = cipher.doFinal(message.getBytes());

        System.out.println("Encrypted text: " + new String(encrypted));

        cipher.init(Cipher.DECRYPT_MODE, key);
        byte[] decrypted = cipher.doFinal(encrypted);

        System.out.println("Decrypted text: " + new String(decrypted));
    }
}