#!/usr/bin/env python3


def serverIpInput(ServerIp):

    # Lets catch the 1st argument as server ip
    if (len(ServerIp) > 1):
        return ServerIp
    else:
        print("\n\n Run like \n python3 client.py < serverip address > \n\n")
        exit(1)

def connectSocketSending(ServerIp):
    print(ServerIp+"\n\n")
    import socket

    # Now we can create socket object
    s = socket.socket()

    # Lets choose one port and connect to that port
    PORT = 9898

    # Lets connect to that port where server may be running
    s.connect((ServerIp,PORT))

    return s

def sendFiletoServer(s):
    # We can send file sample.txt
    file = open("sample.txt", "rb")
    SendData = file.read(1024)

    while SendData:
        # Now we can receive data from server
        print("\n\n########################## Below message is received from server ############################# \n\n", s.recv(1024).decode("utf-8"))
        # Now send the content of sample.txt to server
        s.send(SendData)
        SendData = file.read(1024)

    # Close the connection from client side
    s.close()

def clientSide(ServerIp):
    ServerIp = serverIpInput(ServerIp)
    s = connectSocketSending(ServerIp)
    sendFiletoServer(s)



# Server Code

def connectSocketListen(port = 9898):
    # Importing socket library
    import socket

    # Now we can create socket object
    s = socket.socket()

    # Let choose one port and start listening on that port
    PORT = port
    print("\n Server is listening on port :", PORT, "\n")

    # Now we need to bind to the above port at server side
    s.bind(('', PORT))

    # Now we will put server into listening mode
    s.listen(10)
    return s

def recvFile():
    # Open one recv.txt file in write mode
    file = open("recv.txt", "wb")
    print("\n Copied file name will be recv.txt at server side\n")
    return file

def serverListen(s,file):
    # Now we don't know when client contact server so, server will be listening continously
    while True:
        # Now we can establish connection with client
        conn, addr = s.accept()

        # Send a hello message to client
        msg = "\n\n|-----------------------|\n Hi Client[IP address: "+ addr[0] + "], \n**Welcome to Server** \n -Server\n|------------------------------------|\n\n\n "
        conn.send(msg.encode())

        # Receive any data from client side
        RecvData = conn.recv(1024)
        while RecvData:
            file.write(RecvData)
            RecvData = conn.recv(1024)

        # Close the file open at server side once copy is completed
        file.close()
        print("\n File has been copied successfully \n")

        # Close connection with client
        conn.close()
        print("\n Server closed the connection \n")

        # Come out from the infinite while loop as the file has been copied from client
        break

def serverSide():
    s = connectSocketListen(9898)
    file = recvFile()
    serverListen(s, file)