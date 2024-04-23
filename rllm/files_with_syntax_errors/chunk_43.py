import struct
def process_socket_data(socket): 
    # continuously receive data from socket, unpack into unsigned integer and return
    # the integer
    while True:
        data = socket.recv(1024)
        if not data:
            break
        try:
            data = struct.unpack('>I', data)[0]
        except struct.error:
            print 'Error unpacking data'
            continue
        return data

def process_socket_data_2(socket):
    # continuously receive data from socket, unpack into unsigned integer and return
    # the integer
    while True:
        data = socket.recv(1024)
        if not data:
            break
        try:
            data = struct.unpack('>I', data)[0]
        except struct.error:
            print 'Error unpacking data'
            continue
        return data

def process_socket_data_3(socket):
    # continuously receive data from socket, unpack into unsigned integer and return
    # the integer
    while True:
        data = socket.recv(1024)
        if not data:
            break
        try:
            data = struct.unpack('>I', data)[0]
        except struct