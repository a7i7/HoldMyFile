import socket
import urllib2
import time

RECEIVE_CHUNK_LENGTH = 1024

def netcat(hostname, port, content):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((hostname, port))
    s.sendall(content)
    s.shutdown(socket.SHUT_WR)
    response = ''
    while 1:
        data = s.recv(RECEIVE_CHUNK_LENGTH)
        if data == "":
            break
        data = repr(data)
        response = response + data
    s.close()
    response = response[:-3][1:]
    return response

def convert_to_two_bytes(character):
    res = ''
    ascii_value = ord(character)
    first_part = chr(ord('a')+ascii_value/16)
    second_part = chr(ord('a')+ascii_value%16)
    return first_part+second_part

def convert_back_from_two_bytes(two_bytes):
    first_part = ord(two_bytes[0])-ord('a')
    second_part = ord(two_bytes[1])-ord('a')
    return 16*first_part+second_part

def retrive_from_file(file_path):
    decoded_content = ''
    file = open(file_path,'rb')
    while True:
        c = file.read(1)
        if not c:
            break
        decoded_content = decoded_content + convert_to_two_bytes(c)
    return decoded_content

def retrive_from_url(file_url):
    encoded_content = urllib2.urlopen(file_url).read()
    return encoded_content