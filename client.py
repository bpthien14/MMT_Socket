import socket
import time

HOST = "127.0.0.1"
SERVER_PORT = 8080
FORMAT = "utf8"

LOGIN = "login"

def sendList(client, list):
    for item in list:
        client.sendall(item.encode(FORMAT))
        client.recv(1024)
    
    msg = "end"
    client.send(msg.encode(FORMAT))

def clientLogin(client):
    account = []
    username = input("Username: ")
    password = input("Password: ")   
    #check valid
    account.append(username)
    account.append(password)
    sendList(client, account)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("Client side")
try:
    client.connect((HOST, SERVER_PORT))
    print("Client address: ", client.getsockname())
    
    
    list = ["nam", "123"]
    msg = None
    while(msg != "x"):
        msg = input("talk: ")
        client.sendall(msg.encode(FORMAT))
        if(msg == LOGIN):
            client.recv(1024)
            clientLogin(client)
            
    
except:
    print("404 not found")

client.close()

