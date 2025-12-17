import java.io.*;
import java.net.*;

public class Server {

    public static void main(String[] args) {
        try {
            ServerSocket server = new ServerSocket(5000);
            System.out.println("Server started. Waiting for clients...");

            while (true) {
                Socket clientSocket = server.accept(); // new client
                System.out.println("New client connected!");

                // Create a new thread for each client
                ClientHandler handler = new ClientHandler(clientSocket);
                Thread t = new Thread(handler);
                t.start(); // start thread
            }

        } catch (IOException e) {
            System.out.println("Server Error: " + e.getMessage());
        }
    }
}

// Thread class to handle each client
class ClientHandler implements Runnable {
    private Socket socket;

    public ClientHandler(Socket socket) {
        this.socket = socket;
    }

    public void run() {
        try {
            BufferedReader reader = new BufferedReader(
                    new InputStreamReader(socket.getInputStream()));
            PrintWriter writer = new PrintWriter(socket.getOutputStream(), true);

            writer.println("Connected to server!");

            String message;
            while ((message = reader.readLine()) != null) {
                System.out.println("Client says: " + message);
                writer.println("Server received: " + message);
            }

        } catch (IOException e) {
            System.out.println("Client disconnected.");
        }
    }
}