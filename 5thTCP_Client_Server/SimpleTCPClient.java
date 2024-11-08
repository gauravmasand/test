import java.io.*;
import java.net.*;

public class SimpleTCPClient {
    public static void main(String[] args) {
        String hostname = "127.0.0.1";
        int port = 8080;

        try (Socket socket = new Socket(hostname, port)) {
            PrintWriter writer = new PrintWriter(socket.getOutputStream(), true);
            BufferedReader reader = new BufferedReader(new InputStreamReader(socket.getInputStream()));

            writer.println("Hello from client!"); // Send message to server
            String response = reader.readLine(); // Receive response from server
            System.out.println("Received from server: " + response);

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
