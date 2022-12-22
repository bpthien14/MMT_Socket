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

def readRequest(conn):
    request = conn.recv(FILE_SIZE).decode()
    print(request)
    if not request: print("Didn't receive request!!")
    return request

def handleClient(conn, addr):
    while True:
        data = readRequest(conn)

        request_line = data.split('\r\r')[0]
        
        request_method = request_line.split(' ')[0]
        
        request_url = (request_line.split(' ')[1]).strip('/')    
        url_tail = request_url.split('.')[1]
        
        length = len(request_line.split('\n'))

        user = request_line.split('\r\n')[length - 1]
        
        if request_method == 'GET':
            Content_type = cont_type(url_tail)
            if url_tail != 'ico':
                data = read_file(request_url,Content_type)
                conn.send(data)
        elif request_method == 'POST':
            if request_url == 'images.html' and user == 'Username=admin&Password=123456':
                Content_type = 'text/html' 
                data = read_file(request_url, Content_type)
                conn.send(data)
            else:
                url = '401.html'
                Content_type = 'text/html'   
                data = read_file(url, Content_type)
                conn.send(data)
        else:
            url = '404.html'
            Content_type = 'text/html'   
            data = read_file(url, Content_type)
            conn.send(data)
        conn.close()   
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

def start():
    server.listen()
    while True:
        try:
            conn, addr = server.accept()
            thread = threading.Thread(target=handleClient, args=(conn, addr))
            thread.start()
        except:
            print('Error')

if __name__ == '__main__':
    start()
