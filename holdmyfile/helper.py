import socket
import urllib2

def netcat(hostname, port, content):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((hostname, port))
    s.sendall(content)
    s.shutdown(socket.SHUT_WR)
    response = ''
    while 1:
        data = s.recv(1024)
        if data == "":
            break
        data = repr(data)
        response = response + data

    s.close()
    response = response[:-3][1:]
    return response

def retrive_from_file(file_path):
    decoded_content = ''
    file = open(file_path,'r')
    for character in file:
        decoded_content = decoded_content + character
    return decoded_content

def retrive_from_url(file_url):
    encoded_content = urllib2.urlopen(file_url).read()
    return encoded_content
