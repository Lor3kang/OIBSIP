import socket
import threading

def receive_messages():
    """
    Receive messages from the server.
    """
    while True:
        try:
            message = client_socket.recv(1024).decode("utf-8")
            print(message)
        except Exception as e:
            print(f"Error receiving message: {e}")
            break

def send_message():
    """
    Send messages to the server.
    """
    while True:
        try:
            message = input()
            client_socket.send(message.encode("utf-8"))
        except Exception as e:
            print(f"Error sending message: {e}")
            break

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("localhost", 5555))

receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

send_thread = threading.Thread(target=send_message)
send_thread.start()
