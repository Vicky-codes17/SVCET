import javax.crypto.Cipher;
import javax.crypto.KeyGenerator;
import javax.crypto.SecretKey;

public class BlowfishExample {

    public static void main(String[] args) throws Exception {

        String text = "Hello World";

        KeyGenerator keyGen = KeyGenerator.getInstance("Blowfish");
        SecretKey secretKey = keyGen.generateKey();

        Cipher cipher = Cipher.getInstance("Blowfish");

        cipher.init(Cipher.ENCRYPT_MODE, secretKey);
        byte[] encrypted = cipher.doFinal(text.getBytes());

        System.out.println("Encrypted text: " + new String(encrypted));
    }
}
