import socket


def server(port):

    MAX_BYTES = 65535

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM )
    #create a socket object of domain AF_INET and type SOCK_DGRAM
    sock.bind(('127.0.0.1', port)) #accepts address as a tuple (HOST, PORT) incase of IP_V4
    print(f'Server listening @ {sock.getsockname()}')

    with sock as s: #context manager handles sock.close() automatically since this context manager class is predefined
        try:
            while True:
                (data, address) = s.recvfrom(MAX_BYTES)
                text = data.decode()
                print(f'CLIENT @ {address} :    {text}')
        except KeyboardInterrupt:
            print('shutting down the server')



server(12345)