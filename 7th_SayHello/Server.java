// Server.java
import java.io.*;
import java.net.*;

public class Server {
    public static void main(String[] args) {
        try (ServerSocket serverSocket = new ServerSocket(1234)) {
            System.out.println("Server is waiting for connection...");
            Socket clientSocket = serverSocket.accept();
            System.out.println("Client connected!");

            // Create output stream to send a message to the client
            PrintWriter out = new PrintWriter(clientSocket.getOutputStream(), true);
            // Create input stream to receive a message from the client
            BufferedReader in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));

            // Send "Hello" to the client
            out.println("Hello from Server!");

            // Read "Hello" from the client
            String message = in.readLine();
            System.out.println("Client says: " + message);

            clientSocket.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
