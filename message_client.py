import socket

hostname=socket.gethostname()
ser_host = socket.gethostbyname(hostname) 
port = 5003

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ser_host,port))
print(ser_host + " has joined")

while True:
    
    data = s.recv(1024)
    txt = str(data.decode())
    print("Server:-", txt)
    
    msg = input("client:- ")
    s.send(msg.encode())

    if txt == "exit":
        break
    
s.close()
    