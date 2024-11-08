// FileClient.java
import java.io.*;
import java.net.*;

public class FileClient {
    public static void main(String[] args) {
        String filePath = "file_to_send.txt"; // Path of the file to send
        String serverAddress = "localhost"; // Server address
        int port = 1234; // Server port

        try (Socket socket = new Socket(serverAddress, port)) {
            System.out.println("Connected to server!");

            // Create output stream to send the file
            FileInputStream fis = new FileInputStream(filePath);
            BufferedInputStream bis = new BufferedInputStream(fis);
            DataOutputStream dos = new DataOutputStream(socket.getOutputStream());

            // Read the file data and send it to the server
            byte[] buffer = new byte[4096];
            int bytesRead;
            while ((bytesRead = bis.read(buffer)) != -1) {
                dos.write(buffer, 0, bytesRead);
            }

            System.out.println("File sent successfully!");
            bis.close();
            dos.close();
            socket.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
