import socket
import threading
from os import error
import string
import webbrowser

HOST = '127.0.0.1'
PORT = 8080
FORMAT = "utf8"

LOGIN = "login"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((HOST, PORT))

    print("SERVER SIDE")
    print('* Running on http://{HOST}:{PORT}')
    print("server:", HOST, PORT)
    print("Waiting for Client!!!")

except socket.error as e:
    print('socket error: {e}')
    print('socket error: %s' %(e)) 





def handleClient(conn, addr):
    while True:
        data = conn.recv(1024).decode()
        print(data)
        if not data: break
        request_line = data.split('\r\r')[0]
        print('1 ', request_line)
        request_method = request_line.split(' ')[0]
        print('2 ', request_method)
        request_url = (request_line.split(' ')[1]).strip('/')    
        print('3 ', request_method, request_url)
        length = len(request_line.split('\n'))
        print(length)
        x = request_line.split('\r\n')[length - 1]
        
        if request_method == 'GET':
            if request_url == '' or request_url == 'index.html':
                #trang chu
                url = 'index.html'
                Content_type = 'text/html'
                data = read_file(url, Content_type)
                conn.send(data)
                del data
                pass
            elif request_url == 'utils.css':
                #trang chu
                url = 'utils.css'
                Content_type = 'text/css'
                data = read_file(url, Content_type)
                conn.send(data)
                del data
                pass
            
            elif request_url == 'images/background.png':
                #trang chu
                url = 'images/background.png'
                Content_type = 'image/png'
                data = read_file(url, Content_type)
                conn.send(data)
                del data
                pass
            elif request_url == 'images/tetviet.png':
                url = 'images/tetviet.png'
                Content_type = 'image/png'
                data = read_file(url, Content_type)
                conn.send(data)
                del data
                pass
                
            elif request_url == 'images/bg.png':
                #trang chu
                url = 'images/bg.png'
                Content_type = 'image/png'
                data = read_file(url, Content_type)
                conn.send(data)
                del data
                pass
            elif request_url == 'images/LogoFIT.png':
                url = 'images/LogoFIT.png'
                Content_type = 'image/png'
                data = read_file(url, Content_type)
                conn.send(data)
                del data
                pass
            elif request_url == 'images/1.jpg':
                #trang chu
                url = 'images/1.jpg'
                Content_type = 'image/jpeg'
                data = read_file(url, Content_type)
                conn.send(data)
                del data
                pass
            
            elif request_url == 'images/2.jpg':
                #trang chu
                url = 'images/2.jpg'
                Content_type = 'image/jpeg'
                data = read_file(url, Content_type)
                conn.send(data)
                del data
                pass
            
            elif request_url == 'images/3.jpg':
                #trang chu
                url = 'images/3.jpg'
                Content_type = 'image/jpeg'
                data = read_file(url, Content_type)
                conn.send(data)
                del data
                pass
            
            elif request_url == 'images/4.jpg':
                #trang chu
                url = 'images/4.jpg'
                Content_type = 'image/jpeg'
                data = read_file(url, Content_type)
                conn.send(data)
                del data
                pass
            
            else: 
                url = '404.html'
                Content_type = 'text/html'
                data = read_file(url, Content_type)
                conn.send(data)
        
        elif request_method == 'POST':
            if request_url == 'images.html' and x == 'Username=admin&Password=123456':
                url = 'images.html'
                Content_type = 'text/html'
                data = read_file(url, Content_type)
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
    
    
def serverLogin(conn):
    client_account = conn.recv()

    
if __name__ == '__main__':
    s.listen()
    while True:
        try:
            conn, addr = s.accept()
            thread = threading.Thread(target=handleClient, args=(conn, addr))
            thread.start()
        except:
            print('Error')
