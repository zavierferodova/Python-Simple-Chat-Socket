import socket
from threading import Thread

HOST = 'localhost'
PORT = 50001

def listen_for_messages(s: socket):
    empty_response = 0
    while True:
        response = s.recv(1024) # receive server response
        msg = response.decode()

        if msg != "":
            print(msg) # print messages
        else:
            empty_response += 1

        if empty_response > 10:
            print("Connection disconnected, press enter to continue!")
            exit(0)

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
        try:
            msg_input = input()
            if (msg_input.lower() == "/cmd exit"):
                s.close()
                exit(0)
            else:
                msg = f"{username}> {msg_input}"
                s.send(bytes(msg.encode())) # send message
        except ValueError: # I/O exception because program is exit after empty responses
            exit(0)