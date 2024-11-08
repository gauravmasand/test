// Client.java
import java.io.*;
import java.net.*;

public class Client {
    public static void main(String[] args) {
        try (Socket socket = new Socket("localhost", 1234)) {
            System.out.println("Connected to server!");

            // Create output stream to send a message to the server
            PrintWriter out = new PrintWriter(socket.getOutputStream(), true);
            // Create input stream to receive a message from the server
            BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));

            // Read "Hello" from the server
            String message = in.readLine();
            System.out.println("Server says: " + message);

            // Send "Hello" to the server
            out.println("Hello from Client!");

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
