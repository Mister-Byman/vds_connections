import socket

def monitor_port(port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', port))
    server_socket.listen(5)
    print(f"Listening for incoming connections on port {port}...")
    
    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Incoming connection from {client_address}")
        client_socket.close()

if __name__ == '__main__':
    monitor_port(900)
