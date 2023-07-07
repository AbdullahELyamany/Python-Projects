
"""
 Chatroom Server Written in Python. He makes sure that the client and server can send messages back and forth.
 
 (list_msg.py) In This File, Messages are displayed


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


def start():
    connection = connect()
    while True:
        msg = connection.recv(1024).decode(FORMAT)
        print(msg)
        

start()

