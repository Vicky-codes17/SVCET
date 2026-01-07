import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.List;
import java.util.concurrent.CopyOnWriteArrayList;

// Simple one-to-many chat server with acknowledgements and status tracking
public class Server {
    private static final List<ClientHandler> clients = new CopyOnWriteArrayList<>();
    private static int clientCounter = 0;
    private static final DateTimeFormatter dateFormat = DateTimeFormatter.ofPattern("HH:mm:ss");

    public static void main(String[] args) {
        try (ServerSocket server = new ServerSocket(8080)) {
            server.setReuseAddress(true);
            System.out.println("[" + getTime() + "] Server started on port 8080");

            while (true) {
                Socket client = server.accept();
                String name = "Client " + (++clientCounter);
                ClientHandler handler = new ClientHandler(client, name);
                clients.add(handler);
                System.out.println("[" + getTime() + "] " + name + " connected");
                broadcast(name + " connected", handler, true);
                new Thread(handler).start();
            }
        } catch (IOException e) {
            System.out.println("Server error: " + e.getMessage());
        }
    }

    private static void broadcast(String message, ClientHandler source, boolean isSystemMessage) {
        for (ClientHandler client : clients) {
            client.send(message);
        }
        String displayMessage = isSystemMessage ? "[" + getTime() + "] [SYSTEM] " + message : "[" + getTime() + "] " + message;
        System.out.println(displayMessage);
    }

    private static String getTime() {
        return LocalDateTime.now().format(dateFormat);
    }

    private static class ClientHandler implements Runnable {
        private final Socket socket;
        private final String name;
        private PrintWriter out;
        private volatile boolean isAlive = true;
        private long lastMessageTime = System.currentTimeMillis();
        private static final long TIMEOUT = 30000; // 30 seconds

        ClientHandler(Socket socket, String name) {
            this.socket = socket;
            this.name = name;
        }

        public String getName() {
            return name;
        }

        public boolean isAlive() {
            return isAlive;
        }

        @Override
        public void run() {
            try (BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
                 PrintWriter writer = new PrintWriter(socket.getOutputStream(), true)) {

                this.out = writer;
                String line;
                while ((line = in.readLine()) != null && isAlive) {
                    lastMessageTime = System.currentTimeMillis();
                    
                    if ("exit".equalsIgnoreCase(line)) {
                        break;
                    }

                    if ("ACK".equalsIgnoreCase(line)) {
                        System.out.println("[" + getTime() + "] " + name + " - Acknowledgement received");
                        continue;
                    }

                    // Broadcast the message
                    broadcast(name + ": " + line, this, false);
                    
                    // Send acknowledgement back to client
                    out.println("[SERVER ACK] Message received: " + line);
                }
            } catch (IOException e) {
                System.out.println("[" + getTime() + "] " + name + " error: " + e.getMessage());
            } finally {
                isAlive = false;
                clients.remove(this);
                broadcast(name + " disconnected", this, true);
                try {
                    socket.close();
                } catch (IOException ignored) { }
                System.out.println("[" + getTime() + "] " + name + " offline");
            }
        }

        void send(String message) {
            if (out != null && isAlive) {
                out.println(message);
            }
        }
    }
}