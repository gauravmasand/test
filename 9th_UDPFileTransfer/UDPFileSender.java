// UDPFileSender.java
import java.io.*;
import java.net.*;

public class UDPFileSender {
    public static void main(String[] args) {
        String filePath = "sample_text_file.txt";  // Example file (can be script, text, audio, or video)
        String serverAddress = "localhost"; // Server address
        int port = 1234; // Server port
        DatagramSocket socket = null;

        try {
            socket = new DatagramSocket();
            InetAddress serverIp = InetAddress.getByName(serverAddress);

            // Read the file to be sent
            FileInputStream fis = new FileInputStream(filePath);
            BufferedInputStream bis = new BufferedInputStream(fis);

            byte[] sendData = new byte[4096];

            // Send file in chunks
            int bytesRead;
            while ((bytesRead = bis.read(sendData)) != -1) {
                DatagramPacket sendPacket = new DatagramPacket(sendData, bytesRead, serverIp, port);
                socket.send(sendPacket);
            }

            // Send an empty packet to signal the end of the file
            DatagramPacket endPacket = new DatagramPacket(new byte[0], 0, serverIp, port);
            socket.send(endPacket);

            System.out.println("File sent successfully!");
            bis.close();
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            if (socket != null && !socket.isClosed()) {
                socket.close();
            }
        }
    }
}
