import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1", 5555))
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print(f"Connction from {address} has been established")
    clientsocket.send(bytes("Welcome to the server", "utf-8"))
    clientsocket.send(bytes("", "utf-8"))
    
    
    

