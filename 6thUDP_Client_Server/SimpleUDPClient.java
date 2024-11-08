import java.net.*;
import java.io.*;
public class SimpleUDPClient {
    public static void main(String[] args) {
        String hostname = "127.0.0.1";
        int port = 8080;
        String message = "Hello from client!";

        try (DatagramSocket socket = new DatagramSocket()) {
            byte[] buffer = message.getBytes();
            InetAddress address = InetAddress.getByName(hostname);

            DatagramPacket packet = new DatagramPacket(buffer, buffer.length, address, port);
            socket.send(packet); // Send packet to server

            byte[] responseBuffer = new byte[1024];
            DatagramPacket responsePacket = new DatagramPacket(responseBuffer, responseBuffer.length);
            socket.receive(responsePacket); // Receive response from server

            String response = new String(responsePacket.getData(), 0, responsePacket.getLength());
            System.out.println("Received from server: " + response);

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
