import socket

def send_ping(server_ip):
    port = 12345  # Must be the same as the server port
    
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, port))
    
    client_socket.send('Ping'.encode('utf-8'))
    print("[*] Sent: Ping")
    
    data = client_socket.recv(1024).decode('utf-8')
    print(f"[*] Received: {data}")
    
    client_socket.close()

if __name__ == "__main__":
    server_ip = input("Enter the IP address of the server: ")  # e.g., 192.168.1.2 or the external IP if on a different network
    send_ping(server_ip)