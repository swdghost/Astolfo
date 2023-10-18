
import socket

def get_ip_address():
  return socket.gethostbyname(socket.gethostname())