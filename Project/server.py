import socket
import threading


#Define a header size of 64 bytes because don't know the size of the message we are sending
HEADER = 64

#Pick a port to run a server on
PORT = 5050 

#Put the ipaddress of the computer that will host the server
SERVER = socket.gethostbyname(socket.gethostname)
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"

#Create a socket that will allow...
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

#Start a new thread which handles the communications
def handle_client(conn, addr):
    print("[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        msg_length = int(msg_length)
        msg = conn.recv(msg_length).decode(FORMAT)

        if msg == DISCONNECT_MESSAGE:
            connected = False

        print(f"[{addr}] {msg}")

    conn.close()



#Listens for new connections and then distributes it with threads
def start():
    server.listen()

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn,addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


print("[STARTING] server is starting")