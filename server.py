import socket
if __name__ == "__main__":
    ip = "198.168.10.1"
    port = 1234
    
    server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind((ip,port))
    server.listen(5)
    
    while True:
        client, address = server.accept()
        print("connected :",ip)
        string=client.recv(1024)
        string=string.decode("utf-8")
        string=string.upper()
        print(string)
        client.send(bytes(string,"utf-8"))
        client.close()
