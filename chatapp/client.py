
"""
 Chatroom Server Written in Python. He makes sure that the client and server can send messages back and forth.
 
 (client.py) In This File, You write the message that is sent to the server


 Created by *Abdullah EL-Yamany*

 YouTube Channel => Linode
 Link Of Part1 => https://youtu.be/t331lKVrJ00
 Link Of Part2 => https://youtu.be/f7VYv9QpSzg
"""

import socket
import time


PORT = 1344
SERVER = "localhost"  # socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"


def connect():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    return client

def send(client, msg):
    message = msg.encode(FORMAT)
    client.send(message)


def start():
    answer = input("World You Like To Connect (yes/no)?")
    if answer.lower() != 'yes':
        return 

    connection = connect()
    while True:
        msg = input("Message (q for quit)")

        if msg == 'q':
            break
    
        send(connection, msg)

    send(connection, DISCONNECT_MESSAGE)
    time.sleep(2)
    print('DisConnected')


start()




