import socket
import threading

def handle_client(client_socket, client_address):
    """
    Handle messages from a client.
    """
    print(f"Connected: {client_address}")
    while True:
        try:
            message = client_socket.recv(1024).decode("utf-8")
            if not message:
                break
            print(f"Received from {client_address}: {message}")
            # Broadcast the message to all connected clients
            broadcast(message)
        except Exception as e:
            print(f"Error: {e}")
            break
    print(f"Disconnected: {client_address}")
    client_socket.close()

def broadcast(message):
    """
    Broadcast a message to all connected clients.
    """
    for client_socket in client_sockets:
        try:
            client_socket.send(message.encode("utf-8"))
        except Exception as e:
            print(f"Error broadcasting message: {e}")

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("0.0.0.0", 5555))
server_socket.listen(5)

print("Chat server is running...")

client_sockets = []

while True:
    client_socket, client_address = server_socket.accept()
    client_sockets.append(client_socket)
    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_thread.start()
