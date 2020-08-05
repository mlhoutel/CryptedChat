import socket
import threading
import sys
import select

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 

# checks whether sufficient arguments have been provided 
if len(sys.argv) != 3: 
    print("Correct usage: script, IP address, port number")
    exit() 

# takes the first argument from command prompt as IP address 
IP_address = str(sys.argv[1]) 

# takes second argument from command prompt as port number 
Port = int(sys.argv[2]) 

server.bind((IP_address, Port)) 
print("Binding ", IP_address,":", Port)

server.listen(10) # listen for 10 connections
clients = [] 

def clientthread(conn, addr): 
    message = "<system>Welcome to this chatroom " + addr[0] + "<system>"
    conn.send(message.encode('utf-8')) 

    while True: 
        try: 
            data = conn.recv(2048)
            if data:
                message = data.decode('utf-8','ignore')
                print("<" + addr[0] + "> " + message.rstrip())

                message_to_send = "<" + addr[0] + "> " + message 
                broadcast(message_to_send, conn) 
            else:
                print(addr[0] + " disconnected")
                remove(conn)
                break
        except: 
            continue

def broadcast(message, conn): 
    for client in clients: 
        if client!=conn: 
            try: 
                client.send(message) 
            except: 
                continue
               # remove(client) 

def remove(conn):
    if conn in clients:
        conn.close()
        clients.remove(conn)

while True: 
    conn, addr = server.accept() 
    clients.append(conn) 

    print(addr[0] + " connected")
    threading.Thread(target=clientthread, args=(conn,addr)).start()
  
conn.close() 
server.close()
