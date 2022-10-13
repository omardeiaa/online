import socket
from _thread import *
import sys
import pickle

server = "192.168.1.11"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))

except socket.error as e:
    str(e)

s.listen(2)
print(f"Waiting For a Connection ...")

pos = [(15, 0), (100, 0)]
def handle_client(conn, player):
    conn.send(str.encode(pickle.dumps(pos[player]))) 
    reply = ""
    while True:
        try:
            data = pickle.loads(conn.recv(2048))
            pos[player] = data
            if not data:
                print("Disconnected")
                break
            else:
                if player == 1:
                    reply = pos[0]
                else:
                    reply = pos[1]

                print("Sending", reply)
                print("Receving", reply)

            conn.sendall(pickle.dumps(data))
        except:
            break
        print("Lost Connection !")
        conn.close()

currentplayer = 0
while True:
    conn, addr = s.accept()
    print(f"Connected to : {addr}")

    start_new_thread(handle_client, (conn, currentplayer))
    currentplayer += 1



