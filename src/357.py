import socket
def create_TCP_connections(): # create 10,000 TCP connections to example.com on port 80
    for i in range(10000):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect(('www.example.com', 80))
            s.close()
        except:
            pass

create_TCP_connections()