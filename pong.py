import socket

def start_server():
    host = '0.0.0.0'  # Listen on all available interfaces
    port = 12345  # Choose an appropriate port
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    
    print(f"[*] Listening on {host}:{port}")
    
    client_socket, addr = server_socket.accept()
    print(f"[*] Accepted connection from {addr[0]}:{addr[1]}")
    
    data = client_socket.recv(1024).decode('utf-8')
    print(f"[*] Received: {data}")
    
    if data.lower() == 'ping':
        client_socket.send('Pong'.encode('utf-8'))
        print("[*] Sent: Pong")
    
    client_socket.close()
    server_socket.close()

if __name__ == "__main__":
    start_server()
