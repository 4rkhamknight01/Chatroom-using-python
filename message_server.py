import socket

host = ''
port = 5003

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('',port))

s.listen(1)
print("listening")
c, addr = s.accept()
print("connection from ", addr[0])

while True: 
    
    msg = input("server:- ")
    c.send(msg.encode())
    data = c.recv(1024)
    txt = str(data.decode())
    print("client:- ", txt)

    if txt == "exit":
        break

s.close()

