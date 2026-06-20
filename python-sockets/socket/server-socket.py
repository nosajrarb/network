import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

with server_socket as server:
    server_socket.bind(('127.0.0.1', 3000))
    server_socket.listen()
    
    #MAIN LOOP OF THE SERVER
    while True:
        sock , client_address = server_socket.accept()
        sock.send(b'hi\n')
        print('connected to client @ ', client_address)
        print('SERVER : hi')
        buffer = b''
        while not buffer.endswith(b'\n'):
            chunk = sock.recv(5000)
            if not chunk: 
                break
            buffer += chunk
            
        print(f'CLIENT: {buffer.decode()}')
        sock.send(b'')
        sock.close()
        break