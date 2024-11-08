// FileServer.java
import java.io.*;
import java.net.*;

public class FileServer {
    public static void main(String[] args) {
        int port = 1234; // Port to listen on
        try (ServerSocket serverSocket = new ServerSocket(port)) {
            System.out.println("Server is waiting for a connection...");
            Socket socket = serverSocket.accept();
            System.out.println("Client connected!");

            // Create input stream to receive the file
            DataInputStream dis = new DataInputStream(socket.getInputStream());

            // File to save the received data
            FileOutputStream fos = new FileOutputStream("received_file.txt");
            BufferedOutputStream bos = new BufferedOutputStream(fos);

            // Read the file data from client and write it to the file
            byte[] buffer = new byte[4096];
            int bytesRead;
            while ((bytesRead = dis.read(buffer)) != -1) {
                bos.write(buffer, 0, bytesRead);
            }

            System.out.println("File received successfully!");
            bos.close();
            dis.close();
            socket.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
