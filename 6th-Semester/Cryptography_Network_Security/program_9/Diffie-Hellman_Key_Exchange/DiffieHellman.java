import java.math.BigInteger;

public class DiffieHellman {

    public static void main(String[] args) {

        BigInteger p = new BigInteger("23");
        BigInteger g = new BigInteger("5");

        BigInteger a = new BigInteger("6");
        BigInteger b = new BigInteger("15");

        BigInteger A = g.modPow(a, p);
        BigInteger B = g.modPow(b, p);

        BigInteger key1 = B.modPow(a, p);
        BigInteger key2 = A.modPow(b, p);

        System.out.println("Shared key for Alice: " + key1);
        System.out.println("Shared key for Bob: " + key2);
    }
}