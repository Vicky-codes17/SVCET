import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.Scanner;

public class Server {
    public static void main(String[] args) {
        try (ServerSocket serverSocket = new ServerSocket(8080)) {
            System.out.println("Server started. Waiting for client...");

            try (Socket socket = serverSocket.accept();
                 BufferedReader input = new BufferedReader(new InputStreamReader(socket.getInputStream()));
                 PrintWriter output = new PrintWriter(socket.getOutputStream(), true);
                 Scanner console = new Scanner(System.in)) {

                System.out.println("Client connected! Type messages to send. Type 'exit' to close.");

                // Reader 
                Thread reader = new Thread(() -> {
                    String inbound;
                    try {
                        while ((inbound = input.readLine()) != null) {
                            System.out.println("Client: " + inbound);
                            if ("exit".equalsIgnoreCase(inbound)) {
                                System.out.println("Client requested exit. Closing server...");
                                break;
                            }
                        }
                    } catch (IOException e) {
                        System.out.println("Error reading from client: " + e.getMessage());
                    }
                });

                reader.setDaemon(true);
                reader.start();

                // Main thread handles server console input and sends to client.
                while (true) {
                    String outbound = console.nextLine();
                    output.println(outbound);

                    if ("exit".equalsIgnoreCase(outbound)) {
                        System.out.println("Server exiting...");
                        break;
                    }
                }

                // Closing try-with-resources handles cleanup.
            }
        } catch (IOException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}