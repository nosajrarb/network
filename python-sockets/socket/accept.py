import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    server_address = (('127.0.0.1', 3000))
    s.bind(server_address)
    s.listen();
    s.setblocking(False)    #set the server in non blocking mode
    print(f'SERVER LISTENING @ {server_address}')
    try:
        while True: 
            try:     
                sock , clientAdd = s.accept()
                print(f'client @ {clientAdd}')
            except BlockingIOError: 
                pass
    except KeyboardInterrupt: 
        print('closing the server')
                             