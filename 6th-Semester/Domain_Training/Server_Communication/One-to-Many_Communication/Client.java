import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.Scanner;

// Client connects to chat server with acknowledgement support
public class Client {
    private static final DateTimeFormatter dateFormat = DateTimeFormatter.ofPattern("HH:mm:ss");

    public static void main(String[] args) {
        try (Socket socket = new Socket("localhost", 8080);
             BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
             PrintWriter out = new PrintWriter(socket.getOutputStream(), true);
             Scanner scanner = new Scanner(System.in)) {

            System.out.println("[" + getTime() + "] Connected to server. Type messages; 'exit' to quit.");

            // background thread to print every server broadcast and acknowledgements
            Thread listener = new Thread(() -> {
                try {
                    String inbound;
                    while ((inbound = in.readLine()) != null) {
                        System.out.println("[" + getTime() + "] " + inbound);
                    }
                } catch (IOException e) {
                    System.out.println("[" + getTime() + "] Connection closed: " + e.getMessage());
                }
            });
            listener.setDaemon(true);
            listener.start();

            // Heartbeat thread to send acknowledgement periodically
            Thread heartbeat = new Thread(() -> {
                try {
                    while (true) {
                        Thread.sleep(10000); // Send ACK every 10 seconds
                        out.println("ACK");
                    }
                } catch (InterruptedException ignored) { }
            });
            heartbeat.setDaemon(true);
            heartbeat.start();

            String line;
            while (true) {
                System.out.print("[" + getTime() + "] You: ");
                line = scanner.nextLine();
                out.println(line);
                if ("exit".equalsIgnoreCase(line)) {
                    System.out.println("[" + getTime() + "] Disconnected from server.");
                    break;
                }
            }
        } catch (IOException e) {
            System.out.println("[" + getTime() + "] Client error: " + e.getMessage());
        }
    }

    private static String getTime() {
        return LocalDateTime.now().format(dateFormat);
    }
}