import socket
from threading import Thread

HOST = 'localhost'
PORT = 50001

def listen_for_messages(socket):
    while True:
        msg = socket.recv(1024).decode() # receive server response
        print(msg)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print(f'Connecting with {HOST}:{PORT} ...')
    s.connect((HOST, PORT))
    print('Connected ! \n')
    username = input('Input Username : ')
    print()

    t = Thread(target=listen_for_messages, args=(s,))
    t.daemon = True
    t.start()

    while True:
        msg_input = input()
        if (msg_input.lower() == "/cmd exit"):
            s.close()
            exit(0)
        else:
            msg = f"{username}> {msg_input}"
            s.send(bytes(msg.encode())) # send command