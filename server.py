import socket
from threading import Thread

HOST = 'localhost'
PORT = 5001

client_connections = set()
max_conn = 100

def remove_connection(conn: socket):
    client_connections.remove(conn)

def broadcast_message(msg: str):
    for client_connection in client_connections:
        client_connection.send(msg.encode())

def listen_for_client(conn: socket):
    while True:
        try:
            bytes_data = conn.recv(1024) # receive data
            msg = bytes_data.decode()
            if msg != "":
                broadcast_message(msg)
        except Exception as e:
            remove_connection(conn)
            break

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(max_conn)
    print(f'Socket listen on {HOST}:{PORT}')
    print('Waiting clients connection ...')

    while True: 
        try:
            conn, addr = s.accept() # accept client connection
            print(f'Connected by {addr}')
            client_connections.add(conn)
            t = Thread(target=listen_for_client, args=(conn,))
            t.daemon = True
            t.start()
        except KeyboardInterrupt:
            print("\nDisconnected by user!")
            s.close()
            exit()
