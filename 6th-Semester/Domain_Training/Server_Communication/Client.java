import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;
import java.util.Scanner;

public class Client {
    public static void main(String[] args) {
        try (Socket socket = new Socket("localhost", 8080);
             BufferedReader input = new BufferedReader(new InputStreamReader(socket.getInputStream()));
             PrintWriter output = new PrintWriter(socket.getOutputStream(), true);
             Scanner scanner = new Scanner(System.in)) {

            System.out.println("Connected to server.");

            System.out.println("Type messages to send. Type 'exit' to close.");

                // Reader 
                Thread reader = new Thread(() -> {
                    String inbound;
                    try {
                        while ((inbound = input.readLine()) != null) {
                            System.out.println("Server: " + inbound);
                            if ("exit".equalsIgnoreCase(inbound)) {
                                System.out.println("Server requested exit. Closing client...");
                                break;
                            }
                        }
                    } catch (IOException e) {
                        System.out.println("Error reading from server: " + e.getMessage());
                    }
                });

                reader.setDaemon(true);
                reader.start();

                // Input Values
                while (true) {
                    String outbound = scanner.nextLine();
                    output.println(outbound);

                    if ("exit".equalsIgnoreCase(outbound)) {
                        System.out.println("Connection closed.");
                        break;
                    }
                }
        } catch (IOException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}