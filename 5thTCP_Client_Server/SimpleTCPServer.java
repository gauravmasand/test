import java.io.*;
import java.net.*;

public class SimpleTCPServer {
    public static void main(String[] args) {
        int port = 8080;

        try (ServerSocket serverSocket = new ServerSocket(port)) {
            System.out.println("TCP Server is running on port " + port);
            Socket socket = serverSocket.accept(); // Wait for a client to connect

            BufferedReader reader = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            PrintWriter writer = new PrintWriter(socket.getOutputStream(), true);

            String message = reader.readLine(); // Read message from client
            System.out.println("Received from client: " + message);

            writer.println("Hello from server!"); // Send response to client

            socket.close(); // Close the socket connection
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
