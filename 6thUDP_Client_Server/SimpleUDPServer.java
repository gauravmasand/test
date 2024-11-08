import java.net.*;
import java.io.*;
public class SimpleUDPServer {
    public static void main(String[] args) {
        int port = 8080;
        byte[] buffer = new byte[1024];

        try (DatagramSocket socket = new DatagramSocket(port)) {
            System.out.println("UDP Server is running on port " + port);

            DatagramPacket packet = new DatagramPacket(buffer, buffer.length);
            socket.receive(packet); // Wait for a client packet

            String message = new String(packet.getData(), 0, packet.getLength());
            System.out.println("Received from client: " + message);

            String response = "Hello from server!";
            byte[] responseBytes = response.getBytes();
            DatagramPacket responsePacket = new DatagramPacket(
                    responseBytes, responseBytes.length, packet.getAddress(), packet.getPort()
            );
            socket.send(responsePacket); // Send response to client

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
