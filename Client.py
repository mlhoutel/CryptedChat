import socket
import select 
import sys   

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
if len(sys.argv) != 3: 
    print("Correct usage: script, IP address, port number")
    exit() 
    
IP_address = str(sys.argv[1]) 
Port = int(sys.argv[2]) 
server.connect((IP_address, Port)) 
print("Connected:",IP_address, Port)

while True:
    sockets_list = [sys.stdin, server] 
    read_sockets, write_socket, error_socket = select.select(sockets_list,[],[]) 

    for socks in read_sockets: 
        if socks == server: 
            data = socks.recv(2048)
            if data:
                message = data.decode('utf-8','ignore')
                print(message)
            else:
                server.close()
                exit()
        else: 
            text = sys.stdin.readline() 
            message = text.rstrip()
            if message == 'exit':
                server.close()
                exit()
            server.sendall(message.encode('utf-8'))
            # sys.stdout.write("<You>") 
            # sys.stdout.write(message) 
            sys.stdout.flush() 
server.close() 
