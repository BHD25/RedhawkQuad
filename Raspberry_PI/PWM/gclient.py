import socket
import sys

HOST = '192.168.0.100'
PORT = 1000

s = socket.socket()
s.connect((HOST, PORT))

while 1:
	msg = raw_input("Command To Send: ")
	if msg == "stop":
		s.close()
		sys.exit(0)
	s.send(msg)
