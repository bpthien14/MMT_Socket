import socket
import threading
from os import error
import webbrowser

HOST = '127.0.0.1'
PORT = 8080
FORMAT = "utf8"
FILE_SIZE =1024

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    server.bind((HOST, PORT))
    print('* Running on http://127.0.0.1:8080')
    print("Waiting for Client!!!")

except socket.error as e:
    print('socket error: {e}')
    print('socket error: %s' %(e))
    
def start():
    server.listen()
    while True:
        try:
            client, addr = server.accept()
            thread = threading.Thread(target=handleClient, args=(client, addr))
            thread.start()
        except:
            print('Error')

def readRequest(client):
    request = client.recv(FILE_SIZE).decode()
    print(request)
    if not request: print("Didn't receive request!!")
    return request

def html():
  return 'text/html'

def txt():
  return 'text/plain'

def jpg():
  return 'image/jpeg'
def png():
  return 'image/png'
def css():
  return 'text/css'

def cont_type(x):
    switcher = {
        'html': html(),
        'txt': txt(),
        'jpg': jpg(),
        'jpeg': jpg(),
        'css': css()
    }
    return switcher.get(x, "nothing")
def handleClient(client, addr):
    while True:
        data = readRequest(client)

        request_line = data.split('\r\r')[0]
        
        method = request_line.split(' ')[0]
        
        url = (request_line.split(' ')[1]).strip('/')    
        
        length = len(request_line.split('\n'))

        user = request_line.split('\r\n')[length - 1]
        
        if method == 'GET':
            if url == '' or url == 'index.html':
                #trang chu
                Content_type = 'text/html'
                data = read_file(url, Content_type)
                client.send(data)
                del data
                pass
            elif url == 'utils.css':
                #trang chu
                Content_type = 'text/css'
                data = read_file(url, Content_type)
                client.send(data)
                del data
                pass
            
            elif url == 'images/background.png':
                #trang chu
                Content_type = 'image/png'
                data = read_file(url, Content_type)
                client.send(data)
                del data
                pass
            elif url == 'images/tetviet.png':
                Content_type = 'image/png'
                data = read_file(url, Content_type)
                client.send(data)
                del data
                pass
                
            elif url == 'images/bg.png':
                #trang chu
                Content_type = 'image/png'
                data = read_file(url, Content_type)
                client.send(data)
                del data
                pass
            elif url == 'images/LogoFIT.png':
                Content_type = 'image/png'
                data = read_file(url, Content_type)
                client.send(data)
                del data
                pass
            elif url == 'images/1.jpg':
                #trang chu
                Content_type = 'image/jpeg'
                data = read_file(url, Content_type)
                client.send(data)
                del data
                pass
            
            elif url == 'images/2.jpg':
                #trang chu
                Content_type = 'image/jpeg'
                data = read_file(url, Content_type)
                client.send(data)
                del data
                pass
            
            elif url == 'images/3.jpg':
                #trang chu
                Content_type = 'image/jpeg'
                data = read_file(url, Content_type)
                client.send(data)
                del data
                pass
            
            elif url == 'images/4.jpg':
                #trang chu
                Content_type = 'image/jpeg'
                data = read_file(url, Content_type)
                client.send(data)
                del data
                pass
            elif url == 'favicon.io':   
                Content_type = 'image/jpeg'
                data = read_file(url, Content_type)
                client.send(data)
                del data
                pass
            else: 
                Content_type = 'text/html'
                data = read_file(url, Content_type)
                client.send(data)
        
        elif method == 'POST':
            if url == 'images.html' and user == 'Username=admin&Password=123456':
                Content_type = 'text/html'
                data = read_file(url, Content_type)
                client.send(data)

            else:
                Content_type = 'text/html'   
                data = read_file(url, Content_type)
                client.send(data)
            
        else:
            url = '404.html'
            Content_type = 'text/html'   
            data = read_file(url, Content_type)
            client.send(data)
            
        client.close()   
        break

def read_file(filename, Content_type):
    f = open(filename, 'rb')
    fdata = reponse_header(Content_type)
    fdata += f.read()
    return fdata

def reponse_header(Content_type):
    mess_head = 'HTTP/1.1 200 \n'
    mess_head += f'Content-type: {Content_type}'
    mess_head += '\r\n\r\n'
    mess_head = mess_head.encode()
    return mess_head


if __name__ == '__main__':
    start()
