// UDPFileReceiver.java
import java.io.*;
import java.net.*;

public class UDPFileReceiver {
    public static void main(String[] args) {
        int port = 1234; // Port to listen on
        DatagramSocket socket = null;
        byte[] receiveData = new byte[4096];

        try {
            socket = new DatagramSocket(port);
            System.out.println("Server is waiting for file...");

            // Create a file output stream to save the received file
            FileOutputStream fos = new FileOutputStream("received_file");
            BufferedOutputStream bos = new BufferedOutputStream(fos);

            // DatagramPacket to receive data
            DatagramPacket packet = new DatagramPacket(receiveData, receiveData.length);

            while (true) {
                socket.receive(packet);  // Receive the data
                byte[] data = packet.getData();
                int length = packet.getLength();

                if (length == 0) {
                    break; // End of file
                }

                // Write received data to file
                bos.write(data, 0, length);
            }

            System.out.println("File received successfully!");
            bos.close();
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            if (socket != null && !socket.isClosed()) {
                socket.close();
            }
        }
    }
}
